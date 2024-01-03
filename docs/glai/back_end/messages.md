Module glai.back_end.messages
=============================

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