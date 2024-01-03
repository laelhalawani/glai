from __future__ import annotations

from typing import Optional
from ..back_end import AIMessages, AIMessage, LlamaAI, ModelData, ModelDB, DEFAULT_LOCAL_GGUF_DIR

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
        model_db_dir: Directory to store model data in. Default DEFAULT_LOCAL_GGUF_DIR.

    Attributes:
        ai_db: ModelDB object. - represents the database of models, has useful functions for searching and importing models.
        model_data: ModelData object. - represents the data of the model, has useful functions for creating, downloading and loading the model data and gguf.
        ai: LlamaAI object. - represents the LlamaAI model, a wrapper for llama llm and tokenizer models quantized to gguf format. Has methods for adjusting generation and for generating.
        msgs: AIMessages object. - represents the AIMessages a collection of AIMessage objects, has useful functions for adding and editing messages and can be printed to string.
        
    """
    def __init__(self, 
                 name_search: Optional[str] = None,
                 quantization_search: Optional[str] = None,
                 keyword_search: Optional[str] = None,
                 new_tokens: int = 1500,
                 max_input_tokens: int = 900,
                 model_db_dir:str = DEFAULT_LOCAL_GGUF_DIR) -> None:

        self.ai_db = ModelDB(model_db_dir=model_db_dir, copy_examples=True)
        self.model_data: ModelData = self.ai_db.find_model(
            name_search, quantization_search, keyword_search
        )
        self.model_data.download_gguf()
        self.ai = LlamaAI(
            self.model_data.gguf_file_path, new_tokens, max_input_tokens
        )
        print(f"Using model: {self.model_data}")
        self.msgs: AIMessages = AIMessages(
            self.model_data.user_tags, self.model_data.ai_tags
        )

    def generate_from_prompt(
        self, 
        prompt: str,
        max_tokens_if_needed: int = 2000,
        stop_at:str = None,
        include_stop_str:bool = True
    ) -> str:
        """
        Generate text from a prompt using the LlamaAI model.

        Args:
            prompt: Prompt text to generate from.
            max_tokens_if_needed: Max tokens to allow.

        Returns:
            Generated text string.
        """
        return self.ai.infer(
            prompt, only_string=True, max_tokens_if_needed=max_tokens_if_needed, stop_at_str=stop_at, include_stop_str=include_stop_str
        )

    def generate(
        self,
        user_message_text: str,
        ai_message_to_be_continued: Optional[str] = None,
        stop_at:Optional[str] = None,
        include_stop_str:bool = True
    ) -> AIMessage:
        """
        Generate an AI response to a user message.

        Args:
            user_message_text: User message text.
            ai_message_to_be_continued: Optional text to prepend.
            stop_at: Optional string to stop generation at.
            include_stop_str: Whether to include the stop string in the generated message.

        Returns:
            Generated AIMessage object.
        """
        generation_messages = AIMessages(user_tags=self.model_data.user_tags, ai_tags=self.model_data.ai_tags)
        generation_messages.reset_messages()
        generation_messages.add_user_message(user_message_text)


        if ai_message_to_be_continued is not None:
            generation_messages.add_message(
                ai_message_to_be_continued, 
                self.msgs.ai_tag_open, 
                ""
            )
        print(f"Promt: {generation_messages.text()}")
        
        generated = self.generate_from_prompt(generation_messages.text(), stop_at=stop_at, include_stop_str=include_stop_str)

        if ai_message_to_be_continued is not None:
            generation_messages.edit_last_message(
                ai_message_to_be_continued + generated,
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
        user_message_text: str,
        ai_message_to_be_continued: Optional[str] = None
    ) -> int:
        """
        Count the number of tokens in a generated message.

        Args:
            user_message_text: User message text.
            ai_message_to_be_continued: Optional text to prepend.

        Returns:
            Number of tokens in generated message.
        """
        generation_messages = AIMessages()
        generation_messages.reset_messages()
        generation_messages.add_user_message(user_message_text)

        if ai_message_to_be_continued is not None:
            generation_messages.add_message(
                ai_message_to_be_continued, 
                self.msgs.ai_tag_open, 
                ""
            )
        return self.ai.count_tokens(generation_messages.text())
    
    def is_within_input_limit(
        self,
        user_message_text: str,
        ai_message_to_be_continued: Optional[str] = None
        ) -> bool:
        """
        Check if the generated message is within the input limit.

        Args:
            user_message_text: User message text.
            ai_message_to_be_continued: Optional text to prepend.

        Returns:
            True if within input limit, False otherwise.
        """
        return self.ai.is_within_input_limit(self.count_tokens(user_message_text, ai_message_to_be_continued))