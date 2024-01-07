from glai.ai import AutoAI, EasyAI



# IMPORT REPO EXAMPLE
def import_repo_example():
    print(f"----> EXAMPLE: Importing models from repo...")
    #input()
    easy_ai = EasyAI()
    easy_ai.load_model_db('./gguf_db', False)
    easy_ai.import_from_repo(
        hf_repo_url="https://huggingface.co/TheBloke/SOLAR-10.7B-Instruct-v1.0-GGUF",
        user_tags=["[INST]", "[/INST]"],
        ai_tags=["", ""],
        description="We introduce SOLAR-10.7B, an advanced large language model (LLM) with 10.7 billion parameters, demonstrating superior performance in various natural language processing (NLP) tasks. It's compact, yet remarkably powerful, and demonstrates unparalleled state-of-the-art performance in models with parameters under 30B.",
        keywords=["10.7B", "upstage","isntruct", "solar"],
        replace_existing=False,
    )
    easy_ai.model_db.show_db_info()

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

#Run examples
# import_repo_example() 
# auto_ai_quick_example()
# easy_ai_step_by_step_example()
# easy_ai_all_in_one_example()
# auto_ai_from_dict_one_line_example()
# easy_ai_from_dict_one_line_example()
# easy_ai_get_from_url_example()

