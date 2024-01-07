from __future__ import annotations

from typing import Optional
from ..messages import AIMessages, AIMessage
from gguf_modeldb import ModelDB, ModelData
from gguf_llama import LlamaAI

__all__ = ['AutoAI']

# CONFIG
class AutoAI:
    """
    Initialize the AutoAI class for super easy LLM AI generation.

    Searches for a model based on name/quantization/keyword. 
    Downloads model and sets up LlamaAI.

    Args:
        name_search: Name of model to search for. Optional. Default None.
        quantization_search: Quantization of model to search for. Optional. Default None.
        keyword_search: Keyword of model to search for. Optional. Default None.
        new_tokens: New token length for LlamaAI model. Default 1500.
        max_input_tokens: Max input tokens for LlamaAI model. Default 900.
        model_db_dir: Directory to store model data in. Defaults to global packages model directory.

    Attributes:
        model_db: ModelDB object. - represents the database of models, has useful functions for searching and importing models.
        model_data: ModelData object. - represents the data of the model, has useful functions for creating, downloading and loading the model data and gguf.
        ai: LlamaAI object. - represents the LlamaAI model, a wrapper for llama llm and tokenizer models quantized to gguf format. Has methods for adjusting generation and for generating.
        msgs: AIMessages object. - represents the AIMessages a collection of AIMessage objects, has useful functions for adding and editing messages and can be printed to string.
        
    """
    def __init__(self, 
                 name_search: Optional[str] = None,
                 quantization_search: Optional[str] = None,
                 keyword_search: Optional[str] = None,
                 search_only_downloaded_models:bool = False,
                 max_total_tokens: int = 1500,
                 model_db_dir:Optional[str] = None,
                 ) -> None:

        self.model_db = ModelDB(model_db_dir=model_db_dir, copy_verified_models=True)
        self.model_data: ModelData = self.model_db.find_model(
            name_search, quantization_search, keyword_search, search_only_downloaded_models
        )
        self.model_data.download_gguf()
        self.ai = LlamaAI(
            self.model_data.gguf_file_path, max_tokens=max_total_tokens
        )
        print(f"Using model: {self.model_data}")
        self.msgs: AIMessages = AIMessages(
            self.model_data.user_tags, self.model_data.ai_tags, self.model_data.system_tags
        )
    
    def generate_from_messages(self, stop_at:str = None, include_stop_str:bool = True) -> AIMessage:
        prompt = self.msgs.text()
        ai_message = self.generate_from_literal_string(prompt, stop_at=stop_at, include_stop_str=include_stop_str)
        self.msgs.add_ai_message(ai_message)
        return ai_message
    
    def generate_from_literal_string(
        self, 
        prompt: str,
        stop_at:str = None,
        include_stop_str:bool = True
    ) -> AIMessage:
        """
        Generate text from a prompt using the LlamaAI model.

        Args:
            prompt: Prompt text to generate from.

        Returns:
            Generated text string.
        """
        return self.ai.infer(
            prompt, only_string=True, stop_at_str=stop_at, include_stop_str=include_stop_str
        )

    def generate(
        self,
        user_message: str,
        ai_message_tbc: Optional[str] = None,
        stop_at:Optional[str] = None,
        include_stop_str:bool = True,
        system_message: Optional[str] = None
    ) -> AIMessage:
        """
        Generate an AI response to a user message.

        Args:
            user_message: User message text.
            ai_message_tbc: Optional text to prepend.
            stop_at: Optional string to stop generation at.
            include_stop_str: Whether to include the stop string in the generated message.
            system_message: Optional system message to include at the start, not all models support this.
            If you provide system message to a model that doesn't support it, it will be ignored.
            You can check if a model supports system messages by checking the model_data.has_system_tags() method.
        Returns:
            Generated AIMessage object.
        """
        generation_messages = AIMessages(user_tags=self.model_data.user_tags, ai_tags=self.model_data.ai_tags, system_tags=self.model_data.system_tags)
        generation_messages.reset_messages()
        if self.model_data.has_system_tags():
            if system_message is not None:
                generation_messages.set_system_message(system_message)
            else:
                print("WARNING: Model seeps to support system messages, but no system message provided.")
        generation_messages.add_user_message(user_message)


        if ai_message_tbc is not None:
            generation_messages.add_message(
                ai_message_tbc, 
                self.msgs.ai_tag_open, 
                ""
            )
        print(f"Promt: {generation_messages.text()}")
        
        generated = self.generate_from_literal_string(generation_messages.text(), stop_at=stop_at, include_stop_str=include_stop_str)

        if ai_message_tbc is not None:
            generation_messages.edit_last_message(
                ai_message_tbc + generated,
                self.msgs.ai_tag_open,
                self.msgs.ai_tag_close
            )
        else:
            generation_messages.add_ai_message(generated)

        print(f"Generated: {generation_messages.get_last_message().text()}")
        output = generation_messages.get_last_message()
        return output

    def count_tokens(
        self,
        user_message: str,
        ai_message_tbc: Optional[str] = None
    ) -> int:
        """
        Count the number of tokens in a generated message.

        Args:
            user_message: User message text.
            ai_message_tbc: Optional text to prepend.

        Returns:
            Number of tokens in generated message.
        """
        generation_messages = AIMessages()
        generation_messages.reset_messages()
        generation_messages.add_user_message(user_message)

        if ai_message_tbc is not None:
            generation_messages.add_message(
                ai_message_tbc, 
                self.msgs.ai_tag_open, 
                ""
            )
        return self.ai.count_tokens(generation_messages.text())
    
    def is_within_input_limit(
        self,
        user_message: str,
        ai_message_tbc: Optional[str] = None
        ) -> bool:
        """
        Check if the generated message is within the input limit.

        Args:
            user_message: User message text.
            ai_message_tbc: Optional text to prepend.

        Returns:
            True if within input limit, False otherwise.
        """
        return self.ai.is_within_input_limit(self.count_tokens(user_message, ai_message_tbc))