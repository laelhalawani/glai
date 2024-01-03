Module glai.ai.auto_ai
======================

Classes
-------

`AutoAI(name_search: Optional[str] = None, quantization_search: Optional[str] = None, keyword_search: Optional[str] = None, new_tokens: int = 1500, max_input_tokens: int = 900, model_db_dir: str = './gguf_db')`
:   Initialize the AutoAI class for super easy LLM AI generation.
    
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

    ### Methods

    `count_tokens(self, user_message_text: str, ai_message_to_be_continued: Optional[str] = None) ‑> int`
    :   Count the number of tokens in a generated message.
        
        Args:
            user_message_text: User message text.
            ai_message_to_be_continued: Optional text to prepend.
        
        Returns:
            Number of tokens in generated message.

    `generate(self, user_message_text: str, ai_message_to_be_continued: Optional[str] = None, stop_at: Optional[str] = None, include_stop_str: bool = True) ‑> glai.back_end.messages.AIMessage`
    :   Generate an AI response to a user message.
        
        Args:
            user_message_text: User message text.
            ai_message_to_be_continued: Optional text to prepend.
        
        Returns:
            Generated AIMessage object.

    `generate_from_prompt(self, prompt: str, max_tokens_if_needed: int = 2000, stop_at: str = None, include_stop_str: bool = True) ‑> str`
    :   Generate text from a prompt using the LlamaAI model.
        
        Args:
            prompt: Prompt text to generate from.
            max_tokens_if_needed: Max tokens to allow.
        
        Returns:
            Generated text string.

    `is_within_input_limit(self, user_message_text: str, ai_message_to_be_continued: Optional[str] = None) ‑> bool`
    :   Check if the generated message is within the input limit.
        
        Args:
            user_message_text: User message text.
            ai_message_to_be_continued: Optional text to prepend.
        
        Returns:
            True if within input limit, False otherwise.