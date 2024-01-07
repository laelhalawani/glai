# glai
GGUF LLAMA AI - Package for simplified text generation with Llama models quantized to GGUF format

Provides high level APIs for loading models and generating text completions.
It will find (if needed download) and load the right model for inference with as little as one line of code.

## Installation
To install the package use pip
```
pip install glai
```
## Usage:
You can use one of the two high level classes provided with the package for to easily develop with ai applications.

### Import package
```python
from glai import AutoAI, EasyAI 
#it's enough to use one of these, probaly EasyAI will be better except some most basic cases
```
### AutoAI - automatic model loading and inference
`AutoAI` - the easies way out there to use llama models, can generate completions with one line of code, minimal configuration required, uses a library of preconfigured models
```python
ai = AutoAI(name_search="Mistral")
ai.generate("Hello") 
```
### EasyAI - straightforward manual model configuration 
`EasyAI` - a straightforward high level class allowing to easily use llama models from verified models database (50+ name_x_quantization versions) or import and save dozens of models at once with huggingface gguf repo links, **abstracts away everything related to handling the model configuration, managing model files, downloading, loading the model and tokenizer, message formatting, inference and everything else.** If the model files aren't downloaded it will grab them on the fly before loading the model. By default all models are saved to `gguf_modeldb` package repo and are accessible globally from any project. 
You can also provide a specific dir and import only selected models copying their ggufs or downloading them later.
```python
easy = EasyAI()
easy.load_model_db() 
easy.find_model_data(name_search="Mistral")
easy.load_ai(max_total_tokens=100)
generated_message = easy.generate("Hello")
```
## Generations are wrapped in an intuitive AIMessage object
The outputs of generations are passed via `AIMessage` data objects,
keeping information on ai/user/system tags (i.e. `[INST], [/INST]`) depending on the type of the message
and the message content.
They can be easily parsed to strings, or just the content be accessed using the attribute `content`
```python
print(generated_message) #prints message with tags
print(generated_message.content) #prints just the inner text
```

### ModelDB - search models and show db info
On the back end searching for model data, adding new model data, downloading ggufs, handling files is done by `ModelDB` from `gguf_modeldb` package. It's methods can be access via `.model_db` attribute on both `AutoAI` and `EasyAI` classes.
```python
from glai import EasyAI()

eai = EasyAI()
eai.load_model_db()
eai.model_db.show_db_info() #prints information on all available models
```
### Import Models from Repo
Some of the `ModelDB` functionality is wrapped into high level methods on `EasyAI` and to a lesser extent `AutoAI`. One example is ability to import `ModelData` and automatically create respective `json` configuration files for all ggufs in a given repo. It works by loading the repo site, analysing links and creating entries for links ending with `.gguf`. Currently compatible only with huggingface repos, but if you know other sources please create an issue and I will look into enabling those.
Importing the model from link still requires to manually provide the correct tags the model was fined tuned with (if any). Usually they are specified in the repo as 'assistant' and 'user', and ocassionally 'system'.
If there's no specific tag need for a given model input an empty string.
Below an example on how to import all solar quantized models (they're already included in the db, so it's just for demonstration)
```python

easy_ai = EasyAI()
easy_ai.load_model_db('./gguf_db', False) #creates a new model db dir and doesn't copy included verified models
easy_ai.import_from_repo(
    hf_repo_url="https://huggingface.co/TheBloke/SOLAR-10.7B-Instruct-v1.0-GGUF",
    user_tags=["[INST]", "[/INST]"],
    ai_tags=["", ""],
    description="We introduce SOLAR-10.7B, an advanced large language model (LLM) with 10.7 billion parameters, demonstrating superior performance in various natural language processing (NLP) tasks. It's compact, yet remarkably powerful, and demonstrates unparalleled state-of-the-art performance in models with parameters under 30B.",
    keywords=["10.7B", "upstage","isntruct", "solar"],
    replace_existing=False,
)
easy_ai.model_db.show_db_info()
```
### AutoAI Quick Example
AutoAI generate with all arguments.
```python
from glai import AutoAI

auto_ai = AutoAI("zephyr", "q2_k", max_total_tokens=100)
auto_ai.generate(
    user_message_text="Output just 'hi' in single quotes with no other prose. Do not include any additional information nor comments.",
    ai_message_to_be_continued= "'",
    stop_at="'",
    include_stop_str=True
)
```
### EasyAI Step By Step Example
Step by step generation with EasyAI:

```python
from glai import EasyAI

easy_ai = EasyAI()
easy_ai.load_model_db('./gguf_db')
easy_ai.find_model_data("zephyr", "q2_k")
easy_ai.load_ai()
easy_ai.generate(
    "Output a list of 3 strings. The first string should be `hi`, the second string should be `there`, and the third string should be `!`.",
    "['",
    "']"
)
```
### EasyAI one line configuration.
You can use `.configure` method to setup all the necessary configuration steppes at once.

```python
from glai import EasyAI

easy_ai = EasyAI()
easy_ai.configure(
    model_db_dir="./gguf_db",
    name_search="zephyr",
    quantization_search="q2_k",
    max_total_tokens=100
)
easy_ai.generate(
    "Output a python list of 3 unique cat names.", 
    "['", 
    "']"
)
```
### AutoAI config from dict 
You can also pass a config dict to either model
```python
from glai import AutoAI

conf = {
  "model_db_dir": "./gguf_db",
  "name_search": "zephyr",
  "quantization_search": "q2_k",
  "keyword_search": None,
  "max_total_tokens": 300 
}

AutoAI(**conf).generate(
  "Please output only the provided message as python list.\nMessage:`This string`.",
  "['", 
  "]", 
  True
)
```
### EasyAI config from dict
You can also pass a config dict to either model

```python
from glai import EasyAI

conf = {
  "model_db_dir": "./gguf_db",
  "name_search": "zephyr",
  "quantization_search": "q2_k",
  "keyword_search": None,
  "max_total_tokens": 300,
}

EasyAI(**conf).generate(
  "Please output only the provided message as python list.\nMessage:`This string`.",
  "['",
  "']",
  True  
)
```
### EasyAI from URL Example
Get a model from a URL and generate:

```python
from glai.back_end.model_db.db import ModelDB
from glai.ai import EasyAI

eai = EasyAI()
eai.load_model_db('./gguf_db', False)
eai.model_data_from_url(
    url="https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/blob/main/mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf",
    user_tags=("[INST]", "[/INST]"),
    ai_tags=("", ""),
    description="The Mixtral-8x7B Large Language Model (LLM) is a pretrained generative Sparse Mixture of Experts. The Mistral-8x7B outperforms Llama 2 70B on most benchmarks we tested.",
    keywords=["mixtral", "8x7b", "instruct", "v0.1", "MoE"],
    save=True,
)
eai.load_ai(max_total_tokens=300)
eai.generate(
    user_message="Write a short joke that's actually super funny hilarious best joke.",
    ai_response_content_tbc="",
    stop_at=None,
    include_stop_str=True,
)
```
Detailed API documentation can be found here: https://laelhalawani.github.io/glai/

# Model Summary
The project uses `gguf_modeldb` package on the back end.
gguf_modeldb comes prepacked with over 50 preconfigured, ready to download and deploy model x quantization versions from verified links on huggingface, with configured formatting data allowing you to download 
and get all model data in one line of code, then just pass it to llama-cpp-python or gguf_llama instance
for much smoother inference. Below is the summary of the available models. 

**Number of models:** 56

## Available Models:

### dolphin-2_6-phi-2:
- **Quantizations:** ['Q2_K', 'Q3_K_L', 'Q3_K_M', 'Q3_K_S', 'Q4_0', 'Q4_K_M', 'Q4_K_S', 'Q5_0', 'Q5_K_M', 'Q5_K_S', 'Q6_K', 'Q8_0']
- **Keywords:** ['dolphin', 'phi2', 'uncensored', '2.7B']
- **Description:** Dolphin 2.6 phi 2 GGUF, samll 2.7B model based on Microsoft Phi2 architecture

---

### mistral-7b-instruct-v0.2:
- **Quantizations:** ['Q2_K', 'Q3_K_L', 'Q3_K_M', 'Q3_K_S', 'Q4_0', 'Q4_K_M', 'Q4_K_S', 'Q5_0', 'Q5_K_M', 'Q5_K_S', 'Q6_K', 'Q8_0']
- **Keywords:** ['Mistral', '7B', 'INST', 'v0.2', 'default', 'instruct', 'uncensored', 'open-source', 'apache']
- **Description:** The Mistral-7B-Instruct-v0.2 Large Language Model (LLM) is an improved instruct fine-tuned version of Mistral-7B-Instruct-v0.1.

---

### mixtral-8x7b-instruct-v0.1:
- **Quantizations:** ['Q2_K', 'Q3_K_M', 'Q4_0', 'Q4_K_M', 'Q5_0', 'Q5_K_M', 'Q6_K', 'Q8_0']
- **Keywords:** ['mixtral', '8x7b', 'instruct', 'v0.1', 'MoE']
- **Description:** The Mixtral-8x7B Large Language Model (LLM) is a pretrained generative Sparse Mixture of Experts. The Mistral-8x7B outperforms Llama 2 70B on most benchmarks we tested.

---

### solar-10.7b-instruct-v1.0:
- **Quantizations:** ['Q2_K', 'Q3_K_L', 'Q3_K_M', 'Q3_K_S', 'Q4_0', 'Q4_K_M', 'Q4_K_S', 'Q5_0', 'Q5_K_M', 'Q5_K_S', 'Q6_K', 'Q8_0']
- **Keywords:** ['10.7B', 'upstage', 'instruct', 'solar']
- **Description:** We introduce SOLAR-10.7B, an advanced large language model (LLM) with 10.7 billion parameters, demonstrating superior performance in various natural language processing (NLP) tasks. It's compact, yet remarkably powerful, and demonstrates unparalleled state-of-the-art performance in models with parameters under 30B.

---

### stablelm-zephyr-3b:
- **Quantizations:** ['Q2_K', 'Q3_K_L', 'Q3_K_M', 'Q3_K_S', 'Q4_0', 'Q4_K_M', 'Q4_K_S', 'Q5_0', 'Q5_K_M', 'Q5_K_S', 'Q6_K', 'Q8_0']
- **Keywords:** ['zephyr', '3b', 'instruct', 'non-commercial', 'research']
- **Description:** StableLM Zephyr 3B is a 3 billion parameter instruction tuned inspired by HugginFaceH4's Zephyr 7B training pipeline. This model was trained on a mix of publicly available datasets, synthetic datasets using Direct Preference Optimization (DPO). Evaluation for this model is based on MT Bench and Alpaca Benchmark.

---

# Contributions
All contributions are welcome, please feel encouraged to send your PRs on develop branch.