Module glai.ai
==============

Sub-modules
-----------
* glai.ai.auto_ai
* glai.ai.easy_ai

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

`EasyAI(**kwds)`
:   EasyAI provides a simple interface for LlamaAI based AI using quantized GGUF models
    for inference on CPU.
    
    Initialization:
    Can be intialized with no arguments, followed by following configuration methods, step by step, all in one or using a dict:
    
    Step by step call these with appropriate arguments:
    
        1. `self.load_model_db(model_db_dir: str = DEFAULT_LOCAL_GGUF_DIR)`
        2. One of the following with necessary args: `self.model_data_from_url()` or `self.model_data_from_file()` or `self.find_model_data()`
        3. `self.load_ai(max_tokens: int = 200, max_input_tokens: int = 100)`
    All in one:
    
        ```python
        self.configure(
            model_db_dir:str = DEFAULT_LOCAL_GGUF_DIR, 
            model_url: Optional[str] = None, 
            model_gguf_path: Optional[str] = None, 
            name_search: Optional[str] = None, 
            quantization_search: Optional[str] = None, 
            keyword_search: Optional[str] = None, 
            new_tokens: int = 200, 
            max_input_tokens: int = 100
            )
        ```
        
        Or with a dictionary with the following keys:
        - model_db_dir: Directory to store model data in. Defaults to DEFAULT_LOCAL_GGUF_DIR.
        - model_url: URL of model to configure with. Automatically downloads and builds as needed. (Optional)
        - name_search: Name of model to search for in the model db dir.(Optional)
        - quantization_search: Quantization of model to search for in the model db dir..(Optional)
        - keyword_search: Keyword of model to search for in the model db dir..(Optional)
        - model_gguf_path: Path to GGUF file of model to configure with.(Optional, not a recommended method, doesn't preserve download url)
        - new_tokens: Max tokens to be generated by LlamaAI model. (Defaults to 200, set to around 500-1k for regular use)
        - max_input_tokens: Max input tokens to be generated by LlamaAI model. (Defaults to 100, set to around 200-300 for regular use)
    
    Attributes:
        model_db: ModelDB for searching/loading models
        messages: AIMessages for tracking conversation 
        model_data: ModelData of selected model
        lai: LlamaAI instance for generating text
    
    Methods:
        DB:
            load_model_db: Load ModelDB from directory
        ModelData:
            find_model_data: Search model DB for ModelData
            model_data_from_url: Get ModelData from URL
            model_data_from_file: Load ModelData from file
        Load to memory:
            load_ai: Create LlamaAI instance from ModelData
        Inference:
            infer: Generate AI response to user message
    
    EasyAI handles loading models, setting up messages/LLamaAI,
    and generating responses. It provides a simple interface to using
    LLama

    ### Methods

    `configure(self, model_db_dir: str = './gguf_db', model_url: Optional[str] = None, model_gguf_path: Optional[str] = None, name_search: Optional[str] = None, quantization_search: Optional[str] = None, keyword_search: Optional[str] = None, new_tokens: int = 200, max_input_tokens: int = 100) ‑> None`
    :   Configure EasyAI with model data.
        
        Configures EasyAI with model data from given URL, GGUF file path, or model name/quantization/keyword.
        Sets model data attribute.
        
        Args:
            model_db_dir: Directory to store model data in. Defaults to DEFAULT_LOCAL_GGUF_DIR.
            max_tokens: Max tokens to be generated by LlamaAI model. (Defaults to 200, set to around 500-1k for regular use)
            max_input_tokens: Max input tokens to be generated by LlamaAI model. (Defaults to 100, set to around 200-300 for regular use)
        
            Provide at least one of these args to fetch ModelData: 
            ---
            model_url: URL of model to configure with. Automatically downloads and builds as needed. (Optional)
            name_search: Name of model to search for in the model db dir.(Optional)
            quantization_search: Quantization of model to search for in the model db dir..(Optional)
            keyword_search: Keyword of model to search for in the model db dir..(Optional)
            model_gguf_path: Path to GGUF file of model to configure with.(Optional, not a recommended method, doesn't preserve download url)
            ---
        
        Raises:
            Exception: If no model DB loaded.
            Exception: If no model data found.

    `count_tokens(self, user_message_text: str, ai_message_to_be_continued: Optional[str] = None) ‑> int`
    :   Count the number of tokens in a generated message.
        
        Args:
            user_message_text: User message text.
            ai_message_to_be_continued: Optional text to prepend.
        
        Returns:
            Number of tokens in generated message.

    `find_model_data(self, model_name: Optional[str] = None, quantization: Optional[str] = None, keyword: Optional[str] = None) ‑> glai.back_end.model_db.model_data.ModelData`
    :   Find model data in database that matches given criteria.
        
        Searches model database for model data matching the given model name, 
        quantization, and/or keyword. Any parameters left as None are not used  
        in the search.
        
        Args:
            model_name: Name of model to search for.
            quantization: Quantization of model to search for.
            keyword: Keyword of model to search for.
        
        Returns:
            ModelData object if a match is found, else None.

    `generate(self, user_message: str, ai_response_content_tbc: Optional[str] = None, stop_at: Optional[str] = None, include_stop_str: bool = True) ‑> glai.back_end.messages.AIMessage`
    :   Generate AI response to user message.
        
        Runs user message through loaded LlamaAI to generate response. Allows prepending optional 
        content to AI response. Adds messages and returns generated AIMessage.
        
        Args:
            user_message: User message text.
            ai_response_content_tbc: Optional text to prepend to AI response.
        
        Returns:
            Generated AIMessage object.
        
        Raises:
            Exception: If no AI or messages loaded yet.

    `is_within_input_limit(self, user_message_text: str, ai_message_to_be_continued: Optional[str] = None) ‑> bool`
    :   Check if the generated message is within the input limit.
        
        Args:
            user_message_text: User message text.
            ai_message_to_be_continued: Optional text to prepend.
        
        Returns:
            True if within input limit, False otherwise.

    `load_ai(self, max_tokens: int = 200, max_input_tokens: int = 100) ‑> None`
    :   Load LlamaAI model from model data.
        
        Downloads model file from model data URL if needed. Initializes LlamaAI with model and sets lai attribute.
        
        Args:
            max_tokens: Max tokens for LlamaAI model.
            max_input_tokens: Max input tokens for LlamaAI model.
        
        Raises:
            Exception: If no model data or messages loaded yet.

    `load_model_db(self, db_dir: str = './gguf_db') ‑> None`
    :   Load ModelDB from given directory.
        
        Args:
            db_dir: Directory to load ModelDB from.

    `model_data_from_file(self, gguf_file_path: str, user_tags: Tuple[str, str] = ('', ''), ai_tags: Tuple[str, str] = ('', ''), description: Optional[str] = None, keyword: Optional[str] = None, save: bool = False) ‑> None`
    :   Get model data from local GGUF file.
        
        Loads model data from the given local GGUF file path. Sets model data attribute.
        
        Args:
            gguf_file_path: Path to GGUF file.
            user_tags: User tags to assign to model data.
            ai_tags: AI tags to assign to model data.
            description: Optional description for model data.
            keyword: Optional keyword for model data.
            save: Whether to save model data JSON file.

    `model_data_from_url(self, url: str, user_tags: Tuple[str, str] = ('', ''), ai_tags: Tuple[str, str] = ('', ''), description: Optional[str] = None, keywords: Optional[str] = None, save: bool = True) ‑> None`
    :   Get model data for URL, downloading model if needed.
        
        Checks if model data already exists for the given URL. If not, downloads
        the model from the URL and creates new model data. Sets model data attribute.
        
        Args:
            url: URL of model to get data for.
            user_tags: User tags to assign if creating new model data. 
            ai_tags: AI tags to assign if creating new model data.
            description: Optional description for new model data.
            keyword: Optional keyword for new model data.
            save: Whether to save new model data JSON file.