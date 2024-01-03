from setuptools import setup, find_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name="glai",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'llama-cpp-python>=0.2.26',
        'requests>=2.31.0',
        'beautifulsoup4>=4.9.3',
    ],
    package_data={'glai': ['back_end/model_db/gguf_models/*.json']},
    include_package_data=True,
    author="Łael Al-Halawani",
    author_email="laelhalawani@gmail.com",
    description="A for easy deployment of quantized llama models on cpu",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "License :: Free for non-commercial use",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: C++",
        "Programming Language :: Python :: 3.1",
        "Topic :: Text Processing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['llama', 'ai', 'artificial intelligence', 'natural language processing', 'nlp', 'quantization', 'cpu', 'deployment', 'inference', 'model', 'models', 'model database', 'model repo', 'model repository', 'model library', 'model libraries',
              'gguf', 'llm cpu', 'llm']
)