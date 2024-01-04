
from .messages import AIMessage, AIMessages
from .model_db import ModelDB, ModelData, MODEL_EXAMPLES_DB_DIR, DEFAULT_LOCAL_GGUF_DIR


# Making certain symbols available when the package is imported
__all__ = ['AIMessage', 'AIMessages', 'ModelDB', 'ModelData', 'MODEL_EXAMPLES_DB_DIR', 'DEFAULT_LOCAL_GGUF_DIR']
#print(f"Initializing ai package, available classes: {__all__}")
