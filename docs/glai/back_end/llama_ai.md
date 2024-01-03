Module glai.back_end.llama_ai
=============================

Classes
-------

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