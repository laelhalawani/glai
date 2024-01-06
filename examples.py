from glai.back_end.model_db.db import ModelDB, MODEL_EXAMPLES_DB_DIR
from glai.ai import AutoAI, EasyAI



# IMPORT REPO EXAMPLE
def import_repo_example():
    print(f"----> EXAMPLE: Importing models from repo...")
    #input()
    mdb = ModelDB('./gguf_db', False)
    mdb.import_models_from_repo(
        hf_repo_url="https://huggingface.co/TheBloke/SOLAR-10.7B-Instruct-v1.0-GGUF",
        user_tags=["[INST]", "[/INST]"],
        ai_tags=["", ""],
        description="We introduce SOLAR-10.7B, an advanced large language model (LLM) with 10.7 billion parameters, demonstrating superior performance in various natural language processing (NLP) tasks. It's compact, yet remarkably powerful, and demonstrates unparalleled state-of-the-art performance in models with parameters under 30B.",
        keywords=["10.7B", "upstage","isntruct", "solar"],
        replace_existing=False,
    )
    mdb.show_db_info()

#AUTO AI QUICK EXAMPLE
def auto_ai_quick_example():
    print(f"----> EXAMPLE: AutoAI quick example...")
    #input()
    auto_ai = AutoAI("zephyr", "q2_k", max_total_tokens=50)
    auto_ai.generate(
        user_message_text="Output just 'hi' in single quotes with no other prose. Do not include any additional information nor comments.",
        ai_message_to_be_continued= "'", 
        stop_at="'",
        include_stop_str=True
        )

#EASY AI STEP BY STEP EXAMPLE
def easy_ai_step_by_step_example():
    print(f"----> EXAMPLE: EasyAI step by step example...")
    #input()
    easy_ai = EasyAI()
    easy_ai.load_model_db('./gguf_db')
    easy_ai.find_model_data("zephyr", "q2_k")
    easy_ai.load_ai()
    easy_ai.generate(
        "Output a list of 3 strings. The first string should be `hi`, the second string should be `there`, and the third string should be `!`.", 
        "['", 
        "']"
        )

#EASY AI ALL IN ONE EXAMPLE
def easy_ai_all_in_one_example():
    print(f"----> EXAMPLE: EasyAI all in one example...")
    #input()
    easy_ai = EasyAI()
    easy_ai.configure(
        model_db_dir="./gguf_db",
        name_search="zephyr",
        quantization_search="q2_k",
        max_total_tokens=50
    )
    easy_ai.generate("Output a python list of 3 unique cat names.", "['", "']")




#universal config dict for easy ai and auto ai for instantiating with existing models (doesn't support url nor gguf imports)
conf = {
    "model_db_dir": "./gguf_db",
    "name_search": "zephyr",
    "quantization_search": "q2_k",
    "keyword_search": None,
    "max_total_tokens": 50
}
#AUTO AI FROM DICT ONE LINE EXAMPLE
def auto_ai_from_dict_one_line_example():
    print(f"----> EXAMPLE: AutoAI from dict one line example...")
    #input()
    AutoAI(**conf).generate("Please output only the provided message as python list.\nMessage:`This string`.", "['", "]", True)

#EASY AI FROM DICT ONE LINE EXAMPLE
def easy_ai_from_dict_one_line_example():
    print(f"----> EXAMPLE: EasyAI from dict one line example...")
    #input()
    EasyAI(**conf).generate("Please output only the provided message as python list.\nMessage:`This string`.", "['", "]", True)

#EASY AI GET FROM GGUF URL EXAMPLE
def easy_ai_get_from_url_example():
    mdb = ModelDB('./gguf_db', False)
    mdb.show_db_info()
    #input("Press Enter to continue...")
    eai = EasyAI()
    #input("Press Enter to load model db...")
    eai.load_model_db('./gguf_db')
    #input("Press Enter to load model from url...")
    eai.model_data_from_url(
        url="https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/blob/main/mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf",
        user_tags=("[INST]", "[/INST]"),
        ai_tags=("", ""),
        description="The Mixtral-8x7B Large Language Model (LLM) is a pretrained generative Sparse Mixture of Experts. The Mistral-8x7B outperforms Llama 2 70B on most benchmarks we tested.",
        keywords=["mixtral", "8x7b", "instruct", "v0.1", "MoE"],
        save=True,
    )
    #input("Press Enter to generate...")
    eai.load_ai()
    eai.generate(
        user_message="Write a short joke that's actually super funny hilarious best joke.",
        ai_response_content_tbc="",
        stop_at=None,
        include_stop_str=True,
    )


def import_all_models_data():
    print(MODEL_EXAMPLES_DB_DIR)
    mdb = ModelDB(MODEL_EXAMPLES_DB_DIR, False)
    system_tag_open = "<|im_start|>system\n"
    system_tag_close = "<|im_end|>\n"
    user_tag_open = "<|im_start|>user\n"
    user_tag_close = system_tag_close
    ai_tag_open="<|im_start|>assistant"
    ai_tag_close=user_tag_close
    mdb.import_models_from_repo(
        hf_repo_url='https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF',
        user_tags=(user_tag_open, user_tag_close),
        ai_tags=(ai_tag_open, ai_tag_close),
        system_tags=(system_tag_open, system_tag_close),
        keywords=['dolphin', 'phi2', 'uncesored', '2.7B'],
        description="Dolphin 2.6 phi 2 GGUF",
        replace_existing=True,
    )
    system_tag_open = None
    system_tag_close = None
    user_tag_open = "[INST]"
    user_tag_close = "[/INST]"
    ai_tag_open=""
    ai_tag_close=""
    mdb.import_models_from_repo(
        hf_repo_url='https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF',
        user_tags=(user_tag_open, user_tag_close),
        ai_tags=(ai_tag_open, ai_tag_close),
        system_tags=(system_tag_open, system_tag_close),
        keywords=[
            "Mistral",
            "7B",
            "INST",
            "v0.2",
            "default",
            "instruct",
            "uncesored",
            "open-source",
            "apache"
        ],
        description="The Mistral-7B-Instruct-v0.2 Large Language Model (LLM) is an improved instruct fine-tuned version of Mistral-7B-Instruct-v0.1.",
        replace_existing=True,
    )

    system_tag_open = None
    system_tag_close = None
    user_tag_open = "[INST]"
    user_tag_close = "[/INST]"
    ai_tag_open=""
    ai_tag_close=""
    mdb.import_models_from_repo(
        hf_repo_url='https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF',
        user_tags=(user_tag_open, user_tag_close),
        ai_tags=(ai_tag_open, ai_tag_close),
        system_tags=(system_tag_open, system_tag_close),
        keywords=[
            "mixtral",
            "8x7b",
            "instruct",
            "v0.1",
            "MoE"
        ],
        description="The Mixtral-8x7B Large Language Model (LLM) is a pretrained generative Sparse Mixture of Experts. The Mistral-8x7B outperforms Llama 2 70B on most benchmarks we tested.",
        replace_existing=True,
    )

    system_tag_open = None
    system_tag_close = None
    user_tag_open = "[INST]"
    user_tag_close = "[/INST]"
    ai_tag_open=""
    ai_tag_close=""
    mdb.import_models_from_repo(
        hf_repo_url='https://huggingface.co/TheBloke/SOLAR-10.7B-Instruct-v1.0-GGUF',
        user_tags=(user_tag_open, user_tag_close),
        ai_tags=(ai_tag_open, ai_tag_close),
        system_tags=(system_tag_open, system_tag_close),
        keywords=[
            "10.7B",
            "upstage",
            "isntruct",
            "solar"
        ],
        description="We introduce SOLAR-10.7B, an advanced large language model (LLM) with 10.7 billion parameters, demonstrating superior performance in various natural language processing (NLP) tasks. It's compact, yet remarkably powerful, and demonstrates unparalleled state-of-the-art performance in models with parameters under 30B.",
        replace_existing=True,
    )

    system_tag_open = None
    system_tag_close = None
    user_tag_open = "<|user|>"
    user_tag_close = "<|endoftext|>"
    ai_tag_open="<|assistant|>"
    ai_tag_close="<|endoftext|>"
    mdb.import_models_from_repo(
        hf_repo_url='https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF',
        user_tags=(user_tag_open, user_tag_close),
        ai_tags=(ai_tag_open, ai_tag_close),
        system_tags=(system_tag_open, system_tag_close),
        keywords=[
            "zephyr",
            "3b",
            "instruct",
            "non-commercial",
            "research"
        ],
        description="StableLM Zephyr 3B is a 3 billion parameter instruction tuned inspired by HugginFaceH4's Zephyr 7B training pipeline this model was trained on a mix of publicly available datasets, synthetic datasets using Direct Preference Optimization (DPO), evaluation for this model based on MT Bench and Alpaca Benchmark",
        replace_existing=True,
    )

#Run examples
# import_repo_example() 
# auto_ai_quick_example()
# easy_ai_step_by_step_example()
# easy_ai_all_in_one_example()
# auto_ai_from_dict_one_line_example()
# easy_ai_from_dict_one_line_example()
# easy_ai_get_from_url_example()
#import_all_models_data()
