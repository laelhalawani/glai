Module glai.back_end
====================

Sub-modules
-----------
* glai.back_end.llama_ai
* glai.back_end.messages
* glai.back_end.model_db

Classes
-------

`AIMessage(content: str, tag_open: str, tag_close: str)`
:   Represents a message in an AI system.
    
    Attributes:
        content (str): The content of the message.
        tag_open (str): The opening tag for the message.
        tag_close (str): The closing tag for the message.

    ### Static methods

    `from_dict(message_dict: dict) ‑> glai.back_end.messages.AIMessage`
    :   Creates a new AIMessage from a dictionary.
        
        Args:
            message_dict (dict): The dictionary to create the AIMessage from.
        
        Returns:
            AIMessage: The created AIMessage.

    ### Methods

    `edit(self, new_content, new_tag_open=None, new_tag_close=None)`
    :   Edits the content of the message.
        
        Args:
            new_content (str): The new content for the message.

    `get_tags(self) ‑> tuple`
    :   Returns the tags of the message.
        
        Returns:
            tuple: The tags of the message.

    `text(self)`
    :   Returns the text representation of the message.
        
        Returns:
            str: The text representation of the message.

    `to_dict(self) ‑> dict`
    :   Returns the message as a dictionary.
        
        Returns:
            dict: The message as a dictionary.

`AIMessages(user_tags: Union[tuple[str], list[str], dict] = ('[INST]', '[/INST]'), ai_tags: Union[tuple[str], list[str], dict] = ('', ''))`
:   Represents a collection of messages in an AI system.
    Properties:
        user_tag_open (str): The opening tag for user messages.
        user_tag_close (str): The closing tag for user messages.
        ai_tag_open (str): The opening tag for AI messages.
        ai_tag_close (str): The closing tag for AI messages.
        messages (dict): The messages in the collection: {id: AIMessage}.
        _message_id_generator (int): The id generator for the messages.
    
    Args:
        messages (Union[AIMessages, AIMessage, str, list]): The messages to add to the collection.
        user_tags (tuple): The tags to use for user messages.
        ai_tags (tuple): The tags to use for AI messages.

    ### Static methods

    `from_dict(messages_dict: dict) ‑> glai.back_end.messages.AIMessages`
    :   Creates a new AIMessages from a dictionary.
        
        Args:
            messages_dict (dict): The dictionary to create the AIMessages from.
        
        Returns:
            AIMessages: The created AIMessages.

    `from_json(file_path: str) ‑> glai.back_end.messages.AIMessages`
    :   Creates a new AIMessages from a json file.
        
        Args:
            file_path (str): The path to the json file.
        
        Returns:
            AIMessages: The created AIMessages.

    ### Methods

    `add_ai_message(self, message: str) ‑> glai.back_end.messages.AIMessage`
    :   Adds a ai message to the message list.
        Uses add_message() with the ai tags.
        Automatically iters the message ID generator.
        
        Parameters:
            message (str): The message to be added.
        
        Returns:
            AIMessage

    `add_message(self, message: str, tag_open: str, tag_close: str) ‑> glai.back_end.messages.AIMessage`
    :   Adds a new message to the messages dictionary.
        Iters the message ID generator.
        
        Parameters:
        - message (str): The content of the message.
        - tag_open (str): The opening tag for the message.
        - tag_close (str): The closing tag for the message.
        
        Returns:
        AIMessage

    `add_user_message(self, message: str) ‑> glai.back_end.messages.AIMessage`
    :   Adds a user message to the message list.
        Uses add_message() with the user tags.
        Automatically iters the message ID generator.
        
        Parameters:
            message (str): The message to be added.
        
        Returns:
            AIMessage

    `ai_tags(self) ‑> tuple[str]`
    :   Returns the AI tags.
        
        Returns:
            tuple[str]: The AI tags.

    `edit_last_message(self, new_content: str, tag_open: str = None, tag_close: str = None) ‑> None`
    :   Updates the content of the last message in the collection.
        
        Parameters:
            new_content (str): The new content for the message.
            tag_open (str): Optional. The new opening tag for the message.
            tag_close (str): Optional. The new closing tag for the message.
        
        Returns:
            None

    `edit_message(self, message_id: int, new_content: str, tag_open: str = None, tag_close: str = None) ‑> None`
    :   Updates the content of a message in the collection.
        
        Parameters:
            message_id (int): The id of the message to edit.
            new_content (str): The new content for the message.
            tag_open (str): The new opening tag for the message.
            tag_close (str): The new closing tag for the message.
        
        Returns:
            None

    `get_last_message(self) ‑> glai.back_end.messages.AIMessage`
    :   Returns the last message in the collection.
        
        Returns:
            AIMessage: The last message in the collection.

    `load_messages(self, messages: Union[Any, glai.back_end.messages.AIMessage, str, list[Union[dict, glai.back_end.messages.AIMessage]]]) ‑> None`
    :

    `reset_messages(self) ‑> None`
    :

    `save_json(self, file_path: str) ‑> None`
    :   Saves the messages as a json file.
        
        Parameters:
            file_path (str): The path to save the json file to.
        
        Returns:
            None

    `text(self)`
    :

    `to_dict(self) ‑> dict`
    :   Returns the messages as a dictionary.
        
        Returns:
            dict: The messages as a dictionary.

    `user_tags(self) ‑> tuple[str]`
    :   Returns the user tags.
        
        Returns:
            tuple[str]: The user tags.

`LlamaAI(model_path: str, max_tokens: int, max_input_tokens: int)`
:   

    ### Static methods

    `from_dict(settings_dict: dict) ‑> None`
    :   Create a LlamaAI object from a dictionary containing:
        - model: The path to the model to be used.
        - tokens: The maximum number of tokens to be used.
        - input_tokens: The maximum number of input tokens to be used.

    ### Methods

    `adjust_tokens(self, new_max_tokens: int, new_max_input_tokens: int) ‑> None`
    :   Adjust the maximum number of tokens for the current llm.
        
        Args:
            new_max_tokens (int): The new maximum number of tokens.
            new_max_input_tokens (int): The new maximum number of input tokens.
        
        Returns:
            None

    `count_tokens(self, text: str) ‑> int`
    :   Converts string and counts and returns the number of tokens.
        
        Parameters:
            text (str): The text to count tokens in.
        
        Returns:
            int: The number of tokens in the text.

    `infer(self, text: str, only_string: bool = False, max_tokens_if_needed=-1, stop_at_str=None, include_stop_str=True) ‑> str`
    :   Infer the completion for the given text.
        
        Args:
            text (str): The input text to generate completion for.
            only_string (bool, optional): Whether to return the completion as a string only. 
                If True, the completion will be returned as a single string. 
                If False, the completion will be returned as a list of OpenAI compatible completion dictionary objects.
                Defaults to False.
            max_tokens_if_needed (int, optional): The maximum number of tokens to use if the text is too long, allows for adaptive memory allocation. Defaults to -1.
            stop_at_str (str, optional): The string to stop at. Defaults to None. If None but model has defined EOS token, EOS token will be used. 
            include_stop_str (bool): Whether to include the stop string in the output. Defaults to True. 
        Returns:
            str OR list: The completion.

    `is_within_input_limit(self, text: str) ‑> bool`
    :   Check if the length of the given text is within the maximum allowed input tokens for the current llm.
        
        Args:
            text (str): The text to be checked.
        
        Returns:
            bool: True if the length of the text is within the maximum allowed input tokens, False otherwise.

    `load(self) ‑> None`
    :   Load the model and tokenizer using the model_path, max_tokens, and max_input_tokens attributes.

    `tokenize(self, text: str) ‑> list`
    :   Create and return tokens for the given text.
        
        Parameters:
            text (str): The input text.
        
        Returns:
            list: A list of tokens.

    `try_fixing_format(self, text: str, only_letters: bool = False, rem_list_formatting: bool = False) ‑> str`
    :   Fixes the format of the given text by removing extra newlines and non-letter characters if specified.
        
        Args:
            text (str): The text to be fixed.
            only_letters (bool, optional): If True, only letters will be kept. Defaults to False.
        
        Returns:
            str: The fixed text.

    `untokenize(self, tokens: list) ‑> str`
    :   Decode tokens into a string.
        
        Args:
            tokens (list): The list of tokens to decode.
        
        Returns:
            str: The decoded string.

`ModelDB(model_db_dir: Optional[str] = None, copy_examples=True)`
:   

    ### Methods

    `add_model_by_json(self, json_file_path: str) ‑> None`
    :

    `add_model_by_url(self, url: str) ‑> None`
    :

    `add_model_data(self, model_data: glai.back_end.model_db.model_data.ModelData, save_model=True) ‑> None`
    :

    `find_model(self, name_query: Optional[str] = None, quantization_query: Optional[str] = None, keywords_query: Optional[str] = None) ‑> Optional[glai.back_end.model_db.model_data.ModelData]`
    :

    `find_models(self, name_query: Optional[str] = None, quantization_query: Optional[str] = None, keywords_query: Optional[str] = None, treshold: float = 0.5) ‑> Optional[None]`
    :

    `get_model_by_url(self, url: str) ‑> Optional[glai.back_end.model_db.model_data.ModelData]`
    :

    `import_models_from_repo(self, hf_repo_url: str, user_tags: Optional[list[str]] = None, ai_tags: Optional[list[str]] = None, keywords: Optional[list[str]] = None, description: Optional[str] = None, replace_existing: bool = False)`
    :

    `list_available_models(self) ‑> list[str]`
    :

    `list_models_quantizations(self, model_name: str) ‑> list[str]`
    :

    `load_models(self) ‑> None`
    :

    `load_models_data_from_repo(self, hf_repo_url: str, user_tags: Optional[list[str]] = None, ai_tags: Optional[list[str]] = None, keywords: Optional[list[str]] = None, description: Optional[str] = None)`
    :

    `save_all_models(self) ‑> None`
    :

    `set_model_db_dir(self, model_db_dir: str) ‑> None`
    :

    `show_db_info(self) ‑> None`
    :

`ModelData(gguf_url: str, db_dir: str, user_tags: Union[dict, list, set] = ('', ''), ai_tags: Union[dict, list, set] = ('', ''), description: Optional[str] = None, keywords: Optional[None] = None)`
:   

    ### Static methods

    `from_dict(model_data: dict) ‑> glai.back_end.model_db.model_data.ModelData`
    :

    `from_file(gguf_file_path: str, save_dir: Optional[str] = None, user_tags: Union[dict, list, set] = ('[INST]', '[/INST]'), ai_tags: Union[dict, list, set] = ('', ''), description: Optional[str] = None, keywords: Optional[None] = None) ‑> glai.back_end.model_db.model_data.ModelData`
    :

    `from_json(json_file_path: str) ‑> glai.back_end.model_db.model_data.ModelData`
    :

    `from_url(url: str, save_dir: str, user_tags: Union[dict, list, set] = ('[INST]', '[/INST]'), ai_tags: Union[dict, list, set] = ('', ''), description: Optional[str] = None, keywords: Optional[None] = None) ‑> glai.back_end.model_db.model_data.ModelData`
    :

    ### Methods

    `download_gguf(self, force_redownload: bool = False) ‑> str`
    :

    `get_ai_tag_close(self) ‑> str`
    :

    `get_ai_tag_open(self) ‑> str`
    :

    `get_ai_tags(self) ‑> list[str]`
    :

    `get_user_tag_close(self) ‑> str`
    :

    `get_user_tag_open(self) ‑> str`
    :

    `get_user_tags(self) ‑> list[str]`
    :

    `has_json(self) ‑> bool`
    :   Checks if the model is in the db.

    `is_downloaded(self) ‑> bool`
    :   Checks if the model file is downloaded.

    `json_path(self) ‑> str`
    :

    `model_path(self) ‑> str`
    :

    `save_json(self, replace_existing: bool = True) ‑> str`
    :

    `set_ai_tags(self, ai_tags: Union[dict, set[str], list[str], tuple[str]]) ‑> None`
    :

    `set_save_dir(self, save_dir: str) ‑> None`
    :

    `set_tags(self, ai_tags: Union[dict, set[str], list[str], tuple[str], ForwardRef(None)], user_tags: Union[dict, set[str], list[str], tuple[str], ForwardRef(None)]) ‑> None`
    :

    `set_user_tags(self, user_tags: Union[dict, set[str], list[str], tuple[str]]) ‑> None`
    :

    `to_dict(self)`
    :