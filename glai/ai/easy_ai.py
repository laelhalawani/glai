from typing import Optional, Tuple, Union
from ..messages import AIMessages, AIMessage
from gguf_modeldb import ModelDB, ModelData, VERIFIED_MODELS_DB_DIR
from gguf_llama import LlamaAI

__all__ = ['EasyAI']

class EasyAI:
    """
    EasyAI provides a simple interface for LlamaAI based AI using quantized GGUF models
    for inference on CPU.
    
    Initialization:
    Can be intialized with no arguments, followed by following configuration methods, step by step, all in one or using a dict:\n
    Step by step call these with appropriate arguments:\n
        1. `self.load_model_db(model_db_dir: str = MODEL_EXAMPLES_DB_DIR)`
        2. One of the following with necessary args: `self.model_data_from_url()` or `self.model_data_from_file()` or `self.find_model_data()`
        3. `self.load_ai(max_total_tokens: int = 200)`
    All in one:\n
        ```python
        self.configure(
            model_db_dir:str = MODEL_EXAMPLES_DB_DIR, 
            model_url: Optional[str] = None, 
            model_gguf_path: Optional[str] = None, 
            name_search: Optional[str] = None, 
            quantization_search: Optional[str] = None, 
            keyword_search: Optional[str] = None, 
            max_total_tokens: int = 200, 
            )
        ```
        
        Or with a dictionary with the following keys:
        - model_db_dir: Directory to store model data in. Defaults to MODEL_EXAMPLES_DB_DIR.
        - model_url: URL of model to configure with. Automatically downloads and builds as needed. (Optional)
        - name_search: Name of model to search for in the model db dir.(Optional)
        - quantization_search: Quantization of model to search for in the model db dir..(Optional)
        - keyword_search: Keyword of model to search for in the model db dir..(Optional)
        - model_gguf_path: Path to GGUF file of model to configure with.(Optional, not a recommended method, doesn't preserve download url)
        - max_total_tokens: Max tokens to be processed by LlamaAI model. (Defaults to 200, set to around 500-1k for regular use)

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
    """
    def __init__(self, **kwds) -> None:
        self.model_db: ModelDB = None
        self.messages: Optional[AIMessages] = None
        self.model_data: Optional[ModelData] = None
        self.ai: Optional[LlamaAI] = None
        if kwds:
            self.configure(**kwds)

    def configure(self,
                  model_db_dir: Optional[str] = None,
                  model_url: Optional[str] = None,
                  model_gguf_path: Optional[str] = None,
                  name_search: Optional[str] = None,
                  quantization_search: Optional[str] = None,
                  keyword_search: Optional[str] = None,
                  search_only_downloaded: bool = False,
                  max_total_tokens: int = 200,
                                            ) -> None:
        """
        Configure EasyAI with model data.

        Configures EasyAI with model data from given URL, GGUF file path, or model name/quantization/keyword.
        Sets model data attribute.

        Args:
            model_db_dir: Directory to store model data in. If none is provided global db is used.This is preferred for most use cases.
            max_total_tokens: Max tokens to be processed (input+generation) by LlamaAI model. (Defaults to 200, set to around 500-1k for regular use)
            
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

        """
        if model_db_dir is None:
            print(f"Using provided verified models DB, files at {VERIFIED_MODELS_DB_DIR}")
        self.load_model_db(model_db_dir)
        if model_url is not None:
            self.model_data_from_url(model_url)
        elif model_gguf_path is not None:
            self.model_data_from_file(model_gguf_path)
        elif name_search is not None or quantization_search is not None or keyword_search is not None:
            self.find_model_data(name_search, quantization_search, keyword_search, search_only_downloaded)
        else:
            raise Exception("Can't find model data. Please provide a model URL, GGUF file path, or model name/quantization/keyword.")
        
        self.load_ai(max_total_tokens)
    


            
            


    def load_model_db(self, db_dir:Optional[str] = None, copy_verified_models=True) -> None:
        """
        Load ModelDB from given directory.

        Args:
            db_dir: Directory to load ModelDB from.
            copy_examples: Whether to copy example GGUF files to db_dir if db_dir is empty.
        """
        self.model_db = ModelDB(model_db_dir=db_dir, copy_verified_models=copy_verified_models)

    def import_verified_models_to_db(self, model_name_quantization_list:Optional[list[Union[list,set,tuple]]] = None) -> None:
        """
        Import verified models to new ModelDB.

        Imports verified models from global verified models DB to new ModelDB. If model_name_quantization_list is provided, only models in the list are imported.

        Args:
            model_name_quantization_list: List of tuples of model name and quantization to import. If None, all models are imported.
        """
        if self.model_db is None:
            raise Exception("No model DB loaded. Use load_model_db() first.")
        if model_name_quantization_list is not None:
            for n_q_data in model_name_quantization_list:
                name = n_q_data[0]
                quantization = n_q_data[1]
                self.model_db.import_verified_model(name, quantization, None, True)
        else:
            self.model_db.import_verified_model(None, None, None, True)
        
    def find_model_data(self,
                        model_name: Optional[str] = None,  
                        quantization: Optional[str] = None,
                        keyword: Optional[str] = None,
                        only_downloaded: bool = False) -> ModelData:
        """
        Find model data in database that matches given criteria.

        Searches model database for model data matching the given model name, 
        quantization, and/or keyword. Any parameters left as None are not used  
        in the search.

        Args:
            model_name: Name of model to search for.
            quantization: Quantization of model to search for.
            keyword: Keyword of model to search for.

        Returns:
            ModelData object if a match is found, else None.
        """
        if self.model_db is None:
            raise Exception("No model DB loaded. Use load_model_db() first.")
        model_data = self.model_db.find_model(model_name, quantization, keyword, only_downloaded)
        self.model_data = model_data
        return model_data

    def model_data_from_url(self,
                            url: str,
                            user_tags: Tuple[str, str] = ("", ""),
                            ai_tags: Tuple[str, str] = ("", ""),
                            description: Optional[str] = None,
                            keywords: Optional[str] = None,
                            save: bool = True) -> None:
        """
        Get model data for URL, downloading model if needed.

        Checks if model data already exists for the given URL. If not, downloads
        the model from the URL and creates new model data. Sets model data attribute.

        Args:
            url: URL of model to get data for.
            user_tags: User tags to assign if creating new model data. 
            ai_tags: AI tags to assign if creating new model data.
            description: Optional description for new model data.
            keyword: Optional keyword for new model data.
            save: Whether to save new model data JSON file.
        """
        if self.model_db is None:
            raise Exception("No model DB loaded. Use load_model_db() first.")
        print(f"Trying to get model data from url: {url}")
        print(f"Checking if model data already exists...")
        model_data = self.model_db.get_model_by_url(url)
        if model_data is None:
            print(f"Model data not found. Creating new model data...")
            model_data = ModelData(url, self.model_db.gguf_db_dir, user_tags, ai_tags, description, keywords)
            print(f"Created model data: {model_data}")
        else:
            print(f"Found model data: {model_data}")
        if save:
            model_data.save_json()
        self.model_data = model_data

    def model_data_from_file(self,
                             gguf_file_path: str,
                             user_tags: Tuple[str, str] = ("", ""),
                             ai_tags: Tuple[str, str] = ("", ""),
                             description: Optional[str] = None,
                             keyword: Optional[str] = None,
                             save: bool = False) -> None:
        """
        Get model data from local GGUF file.

        Loads model data from the given local GGUF file path. Sets model data attribute.

        Args:
            gguf_file_path: Path to GGUF file.
            user_tags: User tags to assign to model data.
            ai_tags: AI tags to assign to model data.
            description: Optional description for model data.
            keyword: Optional keyword for model data.
            save: Whether to save model data JSON file.
        """
        if self.model_db is None:
            raise Exception("No model DB loaded. Use load_model_db() first.")
        model_data = ModelData.from_file(gguf_file_path, self.model_db.gguf_db_dir, user_tags, ai_tags, description, keyword)
        if save:
            model_data.save_json()
        self.model_data = model_data

    def _load_messages(self) -> None:
        """
        Load AIMessages using tags from model data.

        Uses user_tags and ai_tags from loaded model data to initialize AIMessages object. 
        Sets messages attribute.

        Raises:
            Exception: If no model data loaded yet.
        """
        if self.model_data is None:
            raise Exception("No model data loaded. Use find_model_data(), get_model_data_from_url(), or get_model_data_from_file() first.")
        self.messages = AIMessages(user_tags=self.model_data.user_tags, ai_tags=self.model_data.ai_tags, system_tags=self.model_data.system_tags)

    def load_ai(self,
                max_total_tokens: int = 200,) -> None:
        """
        Load LlamaAI model from model data.

        Downloads model file from model data URL if needed. Initializes LlamaAI with model and sets lai attribute.

        Args:
            max_total_tokens: Max tokens for LlamaAI model.
        Raises:
            Exception: If no model data or messages loaded yet.
        """
        self._load_messages()
        if self.messages is None:
            raise Exception("No messages loaded. Use load_messages() first.")
        if self.model_data is None:
            raise Exception("No model data loaded. Use find_model_data(), get_model_data_from_url(), or get_model_data_from_file() first.")
        self.model_data.download_gguf()
        self.ai = LlamaAI(self.model_data.model_path(), max_tokens=max_total_tokens)
        print(f"Loaded: {self.model_data}")

    def generate(self,
              user_message: str,
              ai_message_tbc: Optional[str] = None,
              stop_at:Optional[str]=None,
              include_stop_str:bool=True,
              system_message: Optional[str] = None
              ) -> AIMessage:
        """
        Generate AI response to user message.

        Runs user message through loaded LlamaAI to generate response. Allows prepending optional 
        content to AI response. Adds messages and returns generated AIMessage.

        Args:
            user_message: User message text.
            ai_message_tbc: Optional text to prepend to AI response.
            stop_at: Optional string to stop generation at.
            include_stop_str: Whether to include stop string in generated message.
            system_message: Optional system message to include at the start, not all models support this.
            If you provide system message to a model that doesn't support it, it will be ignored.
            You can check if a model supports system messages by checking the model_data.has_system_messages()

        Returns:
            Generated AIMessage object.

        Raises:
            Exception: If no AI or messages loaded yet.
        """
        if self.ai is None:
            raise Exception("No AI loaded. Use load_ai() first.")
        if self.messages is None:
            raise Exception("No messages loaded. Use load_ai() first.")
        self.messages.reset_messages()
        if self.model_data.has_system_tags():
            if system_message is not None:
                self.messages.set_system_message(system_message)
            else:
                print("WARNING: Model supports system messages, but no system message provided.")
        self.messages.add_user_message(user_message)
        print(f"Input to model: \n{self.messages.text()}")
        generated: str = ""
        if ai_message_tbc is not None:
            generated += ai_message_tbc
            self.messages.add_message(ai_message_tbc, self.model_data.get_ai_tag_open(), "")
        if stop_at is None:
            stop_at = self.messages.ai_tag_close if any([self.messages.ai_tag_close is None, self.messages.ai_tag_close == "", self.messages.ai_tag_close != " "]) else None
            include_stop_str = False
        generated += self.ai.infer(self.messages.text(), only_string=True, stop_at_str=stop_at, include_stop_str=include_stop_str)
        if ai_message_tbc is not None:
            self.messages.edit_last_message(generated,
                                            self.model_data.get_ai_tag_open(),
                                            self.model_data.get_ai_tag_close())
        else:
            self.messages.add_ai_message(generated)
        print(f"AI message: \n{self.messages.get_last_message()}")
        return self.messages.get_last_message()

    



    def count_tokens(
        self,
        user_message_text: str,
        ai_message_tbc: Optional[str] = None
    ) -> int:
        """
        Count the number of tokens in a generated message.

        Args:
            user_message_text: User message text.
            ai_message_tbc: Optional text to prepend.

        Returns:
            Number of tokens in generated message.
        """
        generation_messages = AIMessages()
        generation_messages.reset_messages()
        generation_messages.add_user_message(user_message_text)

        if ai_message_tbc is not None:
            generation_messages.add_message(
                ai_message_tbc, 
                self.messages.ai_tag_open, 
                ""
            )

        return self.ai.count_tokens(generation_messages.text())
    
    def is_within_context(self,
        prompt: str,
        ) -> bool:
        """
        Check if the generated message is within the input limit.

        Args:
            user_message_text: User message text.
            ai_message_tbc: Optional text to prepend.

        Returns:
            True if within input limit, False otherwise.
        """
        return self.ai.is_prompt_within_limit(prompt)
    
    def import_from_repo(self, hf_repo_url: str, user_tags: Tuple[str, str] = ("", ""), ai_tags: Tuple[str, str] = ("", ""), system_tags: Optional[Tuple[str, str]] = (None, None), keywords: Optional[str] = None, description: Optional[str] = None, replace_existing: bool = False) -> None:
        """
        Imports model data from HuggingFace model repo to current model DB. 

        Args:
            hf_repo_url: URL of model to import.
            user_tags: User tags to assign to model data.
            ai_tags: AI tags to assign to model data.
            system_tags: System tags to assign to model data.
            description: Optional description for model data.
            keyword: Optional keyword for model data.
            replace_existing: Whether to replace existing model data if found.

        Raises:
            Exception: If no model DB loaded yet.
        """



        self.model_db.import_models_from_repo(
            hf_repo_url=hf_repo_url,
            user_tags=user_tags,
            ai_tags=ai_tags,
            system_tags=system_tags,
            keywords=keywords,
            description=description,
            replace_existing=replace_existing,
        )
