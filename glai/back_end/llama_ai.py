from llama_cpp import Llama, LlamaTokenizer
from ..helpers.text_preprocessor import remove_list_formatting, remove_non_letters

#This class is compatible with any llama architecture encoder-decoder model (except MOE models)
class LlamaAI:
    def __init__(self, model_path:str, max_tokens:int, max_input_tokens:int) -> None:
        """
        
        """
        self.model_path = model_path
        self.max_tokens = max_tokens
        self.max_input_tokens = max_input_tokens
        self.llm = None
        self.tokenizer = None
        self._loaded = False
        self.load()
        
    @staticmethod
    def from_dict(settings_dict: dict) -> None:
        """
        Create a LlamaAI object from a dictionary containing:
        - model: The path to the model to be used.
        - tokens: The maximum number of tokens to be used.
        - input_tokens: The maximum number of input tokens to be used.

        """

        model_path = settings_dict["model"]
        max_tokens = settings_dict["tokens"]
        max_input_tokens = settings_dict["input_tokens"]
        lai = LlamaAI(model_path, max_tokens, max_input_tokens)
        lai.load()
        return lai
    
    def load(self) -> None:
        """
        Load the model and tokenizer using the model_path, max_tokens, and max_input_tokens attributes.
        """
        print(f"Loading model from {self.model_path}...")
        self.llm = Llama(model_path=self.model_path, verbose=False, n_ctx=self.max_tokens)
        self.tokenizer = LlamaTokenizer(self.llm)
        self._loaded = True

    def try_fixing_format(self, text: str, only_letters: bool = False, rem_list_formatting: bool = False) -> str:
        """
        Fixes the format of the given text by removing extra newlines and non-letter characters if specified.

        Args:
            text (str): The text to be fixed.
            only_letters (bool, optional): If True, only letters will be kept. Defaults to False.

        Returns:
            str: The fixed text.
        """
        print("Trying to fix formatting... this might have some undersired effects")
        changes = False
        if "\n\n" in text:
            #split text in that place
            core_info = text.split("\n\n")[1:]
            text = " ".join(core_info)
            changes = True
        if "\n" in text:
            text = text.replace("\n", " ")
            changes = True
        if only_letters:
            text = remove_non_letters(text)
            changes = True
        if rem_list_formatting:
            text = remove_list_formatting(text)
        if changes:
            print("The text has been sucessfully modified.")
        return text

    def _check_loaded(self)->None:
        if not self._loaded:
            try:
                self.load()
                raise Warning("Model not loaded, trying a default reload...")
            except:
                raise Exception("Model not loaded! Please provide model settings when creating the class or use load_model method after creation.")
        
    def _adjust_max_tokens(self, new_max_tokens:int) -> None:
        self.max_tokens = new_max_tokens
        self._loaded = False
   
    def _adjust_max_input_tokens(self, new_max_input_tokens:int) -> None:
        if new_max_input_tokens < self.max_tokens:
            raise Exception("The new maximum input tokens must be greater than the current maximum tokens.")
        self.max_input_tokens = new_max_input_tokens

    def adjust_tokens(self, new_max_tokens:int, new_max_input_tokens:int) -> None:
        """
        Adjust the maximum number of tokens for the current llm.

        Args:
            new_max_tokens (int): The new maximum number of tokens.
            new_max_input_tokens (int): The new maximum number of input tokens.

        Returns:
            None
        """
        self._adjust_max_tokens(new_max_tokens)
        self._adjust_max_input_tokens(new_max_input_tokens)
        self.load()

    def tokenize(self, text: str) -> list:
        """
        Create and return tokens for the given text.

        Parameters:
            text (str): The input text.

        Returns:
            list: A list of tokens.
        """
        ts = self.tokenizer.encode(text)
        return ts
    
    def untokenize(self, tokens: list) -> str:
        """
        Decode tokens into a string.

        Args:
            tokens (list): The list of tokens to decode.

        Returns:
            str: The decoded string.
        """
        return self.tokenizer.decode(tokens)
    
    def count_tokens(self, text: str) -> int:
        """
        Converts string and counts and returns the number of tokens.

        Parameters:
            text (str): The text to count tokens in.

        Returns:
            int: The number of tokens in the text.
        """
        return len(self.tokenize(text))    
    
    def is_within_input_limit(self, text: str) -> bool:
        """
        Check if the length of the given text is within the maximum allowed input tokens for the current llm.

        Args:
            text (str): The text to be checked.

        Returns:
            bool: True if the length of the text is within the maximum allowed input tokens, False otherwise.
        """
        return self.count_tokens(text) <= self.max_input_tokens
    
    def infer(self,text:str, only_string: bool = False, max_tokens_if_needed=-1, stop_at_str=None, include_stop_str=True) -> str:
        """
        Infer the completion for the given text.

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
        """
        text = str(text) 
        self._check_loaded()
        adjusted = False
        if not self.is_within_input_limit(text):
            if not max_tokens_if_needed:
                raise Exception("Text is too long!")
            else:
                print("Text is too long. Adjusting model...")
                current_max_tokens = self.max_tokens
                current_max_input_tokens = self.max_input_tokens
                input_to_total_ratio = current_max_input_tokens / current_max_tokens

                desired_prompt_len = self.count_tokens(text)
                if not any([max_tokens_if_needed > 0, desired_prompt_len - current_max_input_tokens <= max_tokens_if_needed]):
                    raise Exception("Text is too long and the model cannot be adjusted to fit it!")
                desired_input_len = int(desired_prompt_len * input_to_total_ratio)
                print(f"Adjusting model to {desired_input_len} input tokens and {desired_prompt_len} tokens.""")
                self.adjust_tokens(desired_input_len, desired_prompt_len)
                adjusted = True
                
        stop_at = None if any([stop_at_str is None, stop_at_str == ""]) else stop_at_str
        output = self.llm(text, max_tokens=self.max_tokens, stop=stop_at)
        if only_string:
            output = self._text_from_inference_obj(output)
            if include_stop_str:
                output += stop_at_str if stop_at_str is not None else ""
        if adjusted:
            print(f"Adjusting model back to {current_max_tokens} tokens and {current_max_input_tokens} input tokens.")
            self.adjust_tokens(current_max_tokens, current_max_input_tokens)
        return output
    
    def _text_from_inference_obj(self, answer_dict: dict) -> str:
        #print(f"Checking answer: {ans}")
        if 'choices' in answer_dict and 'text' in answer_dict['choices'][0]:
            #print(f"Detected answer: {ans['choices'][0]['text']}")
            extracted_answ = answer_dict['choices'][0]['text']
        return extracted_answ
