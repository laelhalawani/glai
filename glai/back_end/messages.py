
from typing import Optional, Union, Any
from util_helper.file_handler import save_json_file, load_json_file

class AIMessage:
    """
    Represents a message in an AI system.

    Attributes:
        content (str): The content of the message.
        tag_open (str): The opening tag for the message.
        tag_close (str): The closing tag for the message.
    """

    def __init__(self, content:str, tag_open:str, tag_close:str):
        self.content = content
        self.tag_open = tag_open
        self.tag_close = tag_close

    def __str__(self) -> str:
        return f"{self.tag_open}{self.content}{self.tag_close}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def edit(self, new_content, new_tag_open=None, new_tag_close=None):
        """
        Edits the content of the message.

        Args:
            new_content (str): The new content for the message.
        """
        self.content = new_content
        if new_tag_open is not None:
            self.tag_open = new_tag_open
        if new_tag_close is not None:
            self.tag_close = new_tag_close
    
    def text(self):
        """
        Returns the text representation of the message.

        Returns:
            str: The text representation of the message.
        """
        return self.__str__()
    
    def get_tags(self) -> tuple:
        """
        Returns the tags of the message.

        Returns:
            tuple: The tags of the message.
        """
        return (self.tag_open, self.tag_close)
    
    def to_dict(self) -> dict:
        """
        Returns the message as a dictionary.

        Returns:
            dict: The message as a dictionary.
        """
        return {
            "content": self.content,
            "tag_open": self.tag_open,
            "tag_close": self.tag_close,
        }
    
    @staticmethod 
    def from_dict(message_dict:dict) -> "AIMessage":
        """
        Creates a new AIMessage from a dictionary.

        Args:
            message_dict (dict): The dictionary to create the AIMessage from.

        Returns:
            AIMessage: The created AIMessage.
        """
        return AIMessage(message_dict["content"], message_dict["tag_open"], message_dict["tag_close"])
    


class AIMessages:
    """
    Represents a collection of messages in an AI system.
    Properties:
        user_tag_open (str): The opening tag for user messages.
        user_tag_close (str): The closing tag for user messages.
        ai_tag_open (str): The opening tag for AI messages.
        ai_tag_close (str): The closing tag for AI messages.
        system_tag_open (str): The opening tag for system messages.
        system_tag_close (str): The closing tag for system messages.
        messages (dict): The messages in the collection: {id: AIMessage}.
        _message_id_generator (int): The id generator for the messages.

    Args:
        messages (Union[AIMessages, AIMessage, str, list]): The messages to add to the collection.
        user_tags (tuple): The tags to use for user messages.
        ai_tags (tuple): The tags to use for AI messages.
        system_tags (tuple): The tags to use for system messages.
    """

    def __init__(self,user_tags:Union[tuple[str], list[str], dict]=("[INST]", "[/INST]"), ai_tags:Union[tuple[str], list[str], dict]=("", ""), system_tags:Optional[Union[tuple[str], list[str], dict]]=None):
        if isinstance(user_tags, dict):
            if "open" in user_tags and "close" in user_tags:
                self.user_tag_open = user_tags["open"]
                self.user_tag_close = user_tags["close"]
            else:
                raise ValueError(f"Invalid user tags: {user_tags}, for dict tags both 'open' and 'close' keys must be present.")
        elif isinstance(user_tags, set) or isinstance(user_tags, list) or isinstance(user_tags, tuple):
            self.user_tag_open = user_tags[0]
            self.user_tag_close = user_tags[1]
        else:
            raise TypeError(f"Invalid type for user tags: {type(user_tags)}, must be dict, set or list.")
        
        if isinstance(ai_tags, dict):
            if "open" in ai_tags and "close" in ai_tags:
                self.ai_tag_open = ai_tags["open"]
                self.ai_tag_close = ai_tags["close"]
            else:
                raise ValueError(f"Invalid user tags: {ai_tags}, for dict tags both 'open' and 'close' keys must be present.")
        elif isinstance(ai_tags, set) or isinstance(ai_tags, list) or isinstance(ai_tags, tuple):
            self.ai_tag_open = ai_tags[0]
            self.ai_tag_close = ai_tags[1]
        else:
            raise TypeError(f"Invalid type for user tags: {type(ai_tags)}, must be dict, set or list.")
        
        if system_tags is not None:
            if isinstance(system_tags, dict):
                if "open" in system_tags and "close" in system_tags:
                    self.system_tag_open = system_tags["open"]
                    self.system_tag_close = system_tags["close"]
                else:
                    raise ValueError(f"Invalid system tags: {system_tags}, for dict tags both 'open' and 'close' keys must be present.")
            elif isinstance(system_tags, set) or isinstance(system_tags, list) or isinstance(system_tags, tuple):
                self.system_tag_open = system_tags[0]
                self.system_tag_close = system_tags[1]
            else:
                raise TypeError(f"Invalid type for system tags: {type(system_tags)}, must be dict, set or list.")
        else:
            self.system_tag_open = None
            self.system_tag_close = None
        self.messages = {}
        self._message_id_generator = 0
    
    def user_tags(self) -> tuple[str]:
        """
        Returns the user tags.

        Returns:
            tuple[str]: The user tags.
        """
        return (self.user_tag_open, self.user_tag_close)
    
    def ai_tags(self) -> tuple[str]:
        """
        Returns the AI tags.

        Returns:
            tuple[str]: The AI tags.
        """
        return (self.ai_tag_open, self.ai_tag_close)

    def system_tags(self) -> Union[tuple[str], None]:
        """
        Returns the system tags.

        Returns:
            tuple[str]: The system tags.
        """
        if self.system_tag_open is not None and self.system_tag_close is not None:
            return (self.system_tag_open, self.system_tag_close)
        else:
            return None
    
    def load_messages(self, messages:Union[Any, AIMessage, str, list[Union[dict, AIMessage]]]) -> None:
        if messages is not None:
            if isinstance(messages, AIMessages):
                self.messages = messages.messages
            elif isinstance(messages, AIMessage):
                self.messages = [messages]
            elif isinstance(messages, str):
                self.messages = [AIMessage(messages, self.user_tag_open, self.user_tag_close)]
            elif isinstance(messages, list):
                if all([isinstance(message, AIMessage) for message in messages]):
                    self.messages = messages
                elif all(isinstance(message, str) for message in messages):
                    self.messages = [AIMessage(message, tag_open=self.user_tag_open, tag_close=self.user_tag_close) for message in messages]
                elif all(isinstance(message, dict) for message in messages):
                    self.messages = [AIMessage.from_dict(message_dict) for message_dict in messages]
                else:
                    raise TypeError("If passing list as messages it must be a list of AIMessage or str")
            else:
                raise TypeError("messages must be a list of AIMessage or str")
    
    def to_dict(self) -> dict:
        """
        Returns the messages as a dictionary.

        Returns:
            dict: The messages as a dictionary.
        """
        return {
            "user_tag_open": self.user_tag_open,
            "user_tag_close": self.user_tag_close,
            "ai_tag_open": self.ai_tag_open,
            "ai_tag_close": self.ai_tag_close,
            "system_tag_open": self.system_tag_open,
            "system_tag_close": self.system_tag_close,
            "messages": [message.to_dict() for message in self.messages]
        }
    
    @staticmethod
    def from_dict(messages_dict:dict) -> "AIMessages":
        """
        Creates a new AIMessages from a dictionary.

        Args:
            messages_dict (dict): The dictionary to create the AIMessages from.

        Returns:
            AIMessages: The created AIMessages.
        """
        ai_msgs = AIMessages()
        ai_msgs.user_tag_open = messages_dict["user_tag_open"]
        ai_msgs.user_tag_close = messages_dict["user_tag_close"]
        ai_msgs.ai_tag_open = messages_dict["ai_tag_open"]
        ai_msgs.ai_tag_close = messages_dict["ai_tag_close"]
        ai_msgs.system_tag_open = messages_dict["system_tag_open"] if "system_tag_open" in messages_dict else None
        ai_msgs.system_tag_close = messages_dict["system_tag_close"] if "system_tag_close" in messages_dict else None
        ai_msgs.load_messages(messages_dict["messages"])
        return ai_msgs
    
    def _generate_message_id(self) -> int:
        """
        Generates a unique message ID.
        Iters the message ID generator.

        Returns:
            int: The generated message ID.
        """
        self._message_id_generator += 1
        id = self._message_id_generator
        return id
    
    def add_message(self, message:Union[str, AIMessage], tag_open:str, tag_close:str) -> AIMessage:
        """
        Adds a new message to the messages dictionary.
        Iters the message ID generator.

        Parameters:
        - message (str|AIMessage): The content of the message or the message object
        - tag_open (str): The opening tag for the message, set to None if message is AIMessage
        - tag_close (str): The closing tag for the message, set to None if message is AIMessage

        Returns:
        AIMessage
        """
        if isinstance(message, str):
            message = AIMessage(message, tag_open, tag_close)
        self.messages[self._generate_message_id()] = message
        return self.messages[self._message_id_generator]

    def _insert_message(self, message:AIMessage, message_id:int) -> AIMessage:
        """
        Inserts a new message to the messages dictionary.
        Iters the message ID generator.

        Parameters:
        - message (AIMessage): The message object
        - message_id (int): The id to insert the message at

        Returns:
        AIMessage
        """
        self._message_id_generator += 1 if len(self.messages) > 0 else 0
        updated_messages = {}
        for id, msg in self.messages.items():
            if id < message_id:
                updated_messages[id] = msg
            else:
                updated_messages[id+1] = msg
        updated_messages[message_id] = message
        self.messages = updated_messages

    def add_user_message(self, message: Union[str, AIMessage]) -> AIMessage:
        """
        Adds a user message to the message list.
        Uses add_message() with the user tags.
        Automatically iters the message ID generator.

        Parameters:
            message (str): The message to be added.

        Returns:
            AIMessage
        """
        return self.add_message(message, self.user_tag_open, self.user_tag_close)

    def add_ai_message(self, message:Union[str, AIMessage]) -> AIMessage:
        """
        Adds a ai message to the message list.
        Uses add_message() with the ai tags.
        Automatically iters the message ID generator.

        Parameters:
            message (str): The message to be added.

        Returns:
            AIMessage
        """
        return self.add_message(message, self.ai_tag_open, self.ai_tag_close)
    
    def set_system_message(self, message:Union[str, AIMessage]) -> AIMessage:
        """
        Adds a system message to the message list.
        Uses add_message() with the system tags.
        Automatically iters the message ID generator.

        Parameters:
            message (str): The message to be added.

        Returns:
            AIMessage
        """
        if not self.has_system_tags():
            print("System tags are not set, this model does not support system messages.")
        else:
            if isinstance(message, str):
                message = AIMessage(message, self.system_tag_open, self.system_tag_close)    
            return self._insert_message(message, 0)

    def reset_messages(self) -> None:
        self.messages = {}
        self._message_id_generator = 0

    def __str__(self) -> str:
        return "".join([str(message) for message in self.messages.values()])

    def __repr__(self) -> str:
        return self.__str__()
    
    def text(self):
        return self.__str__()
    
    def get_last_message(self) -> AIMessage:
        """
        Returns the last message in the collection.

        Returns:
            AIMessage: The last message in the collection.
        """
        return self.messages[self._message_id_generator]
    
    def edit_last_message(self, new_content:str, tag_open:str=None, tag_close:str=None) -> None:
        """
        Updates the content of the last message in the collection.

        Parameters:
            new_content (str): The new content for the message.
            tag_open (str): Optional. The new opening tag for the message.
            tag_close (str): Optional. The new closing tag for the message.

        Returns:
            None
        """
        self.get_last_message().edit(new_content, tag_open, tag_close)
    
    def edit_message(self, message_id:int, new_content:str, tag_open:str=None, tag_close:str=None) -> None:
        """
        Updates the content of a message in the collection.

        Parameters:
            message_id (int): The id of the message to edit.
            new_content (str): The new content for the message.
            tag_open (str): The new opening tag for the message.
            tag_close (str): The new closing tag for the message.

        Returns:
            None
        """
        self.messages[message_id].edit(new_content, tag_open, tag_close)

    def edit_system_message(self, new_content:str) -> None:
        if self.system_tags() is None:
            raise ValueError("System tags are not set, this model does not support system messages.")
        else:
            if self.messages[0].tag_open == self.system_tag_open and self.messages[0].tag_close == self.system_tag_close:
                self.edit_message(0, new_content)
            else:
                print("Warning: System message not found, adding system message to the start of the message list.")
                self.set_system_message(new_content)

    def has_system_tags(self) -> bool:
        """
        Returns whether the model supports system messages.

        Returns:
            bool: Whether the model supports system messages.
        """
        return self.system_tags() is not None
    
    def save_json(self, file_path:str) -> None:
        """
        Saves the messages as a json file.

        Parameters:
            file_path (str): The path to save the json file to.

        Returns:
            None
        """
        save_json_file(self.to_dict(), file_path)
    
    @staticmethod
    def from_json(file_path:str) -> "AIMessages":
        """
        Creates a new AIMessages from a json file.

        Args:
            file_path (str): The path to the json file.

        Returns:
            AIMessages: The created AIMessages.
        """
        return AIMessages.from_dict(load_json_file(file_path))
    
    @staticmethod
    def create_single_message(message:str, tag_open:str="", tag_close:str="") ->AIMessage:
        """
        Creates a single AIMessage.

        Args:
            message (str): The content of the message.
            tag_open (str): The opening tag for the message.
            tag_close (str): The closing tag for the message.

        Returns:
            AIMessage: The created AIMessage.
        """
        return AIMessage(message, tag_open, tag_close)
    
