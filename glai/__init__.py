from .ai import AutoAI, EasyAI
from .back_end import LlamaAI, AIMessages, ModelDB, ModelData
__version__ = "0.0.14"

__all__ = ['AutoAI', 'EasyAI', 'LlamaAI', 'ModelDB', 'AIMessages', 'ModelData']
print(f"""
glai
GGUF LLAMA AI - Package for simplified text generation with Llama models quantized to GGUF format is loaded.
Provides high level APIs for loading models and generating text completions.
For more information please check README.md file or visit https://github.com/laelhalawani/glai 
Detailed API documentation can be found here: https://laelhalawani.github.io/glai/
""")
