from .ai import AutoAI, EasyAI
from .back_end import LlamaAI, AIMessages, ModelDB, ModelData
__version__ = "0.0.1a"

__all__ = ['AutoAI', 'EasyAI', 'LlamaAI', 'ModelDB', 'AIMessages', 'ModelData']
print(f"""
glai - GGUF LLAMA AI - Package for simplified text generation with Llama models quantized to GGUF format is loaded.

Provides high level APIs for loading models and generating text completions.

High Level API Classes:

AutoAI:
- Automatically searches for and loads a model based on name/quantization/keyword. 
- Handles downloading model data, loading it to memory, and configuring message formatting.
- Use generate() method to get completions by providing a user message.

EasyAI:
- Allows manually configuring model data source - from file, URL, or ModelDB search.
- Handles downloading model data, loading it to memory, and configuring message formatting.
- Use generate() method to get completions by providing a user message.

ModelDB (used by AutoAI and EasyAI)):
- Manages database of model data files. via ModelData class objects.
- Useful for searching for models and retrieving model metadata.
- Can import models from HuggingFace repo URLs or import and download models from .gguf urls on huggingface.

ModelData (used by ModelDB):
- Represents metadata and info about a specific model.
- Used by ModelDB to track and load models.
- Can be initialized from URL, file, or ModelDB search.
- Used by ModelDB to download model gguf file 

For more information, see check the repo for the README.md file, 
and the examples.py file for more examples of usage.
""")
