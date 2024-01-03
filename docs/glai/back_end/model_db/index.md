Module glai.back_end.model_db
=============================

Sub-modules
-----------
* glai.back_end.model_db.db
* glai.back_end.model_db.db_settings
* glai.back_end.model_db.model_data

Classes
-------

`ModelDB(model_db_dir: Optional[str] = None, copy_examples=True)`
:   

    ### Methods

    `add_model_by_json(self, json_file_path: str) ‑> None`
    :

    `add_model_by_url(self, url: str) ‑> None`
    :

    `add_model_data(self, model_data: glai.back_end.model_db.model_data.ModelData, save_model=True) ‑> None`
    :

    `find_model(self, name_query: Optional[str] = None, quantization_query: Optional[str] = None, keywords_query: Optional[str] = None) ‑> Optional[glai.back_end.model_db.model_data.ModelData]`
    :

    `find_models(self, name_query: Optional[str] = None, quantization_query: Optional[str] = None, keywords_query: Optional[str] = None, treshold: float = 0.5) ‑> Optional[None]`
    :

    `get_model_by_url(self, url: str) ‑> Optional[glai.back_end.model_db.model_data.ModelData]`
    :

    `import_models_from_repo(self, hf_repo_url: str, user_tags: Optional[list[str]] = None, ai_tags: Optional[list[str]] = None, keywords: Optional[list[str]] = None, description: Optional[str] = None, replace_existing: bool = False)`
    :

    `list_available_models(self) ‑> list[str]`
    :

    `list_models_quantizations(self, model_name: str) ‑> list[str]`
    :

    `load_models(self) ‑> None`
    :

    `load_models_data_from_repo(self, hf_repo_url: str, user_tags: Optional[list[str]] = None, ai_tags: Optional[list[str]] = None, keywords: Optional[list[str]] = None, description: Optional[str] = None)`
    :

    `save_all_models(self) ‑> None`
    :

    `set_model_db_dir(self, model_db_dir: str) ‑> None`
    :

    `show_db_info(self) ‑> None`
    :

`ModelData(gguf_url: str, db_dir: str, user_tags: Union[dict, list, set] = ('', ''), ai_tags: Union[dict, list, set] = ('', ''), description: Optional[str] = None, keywords: Optional[None] = None)`
:   

    ### Static methods

    `from_dict(model_data: dict) ‑> glai.back_end.model_db.model_data.ModelData`
    :

    `from_file(gguf_file_path: str, save_dir: Optional[str] = None, user_tags: Union[dict, list, set] = ('[INST]', '[/INST]'), ai_tags: Union[dict, list, set] = ('', ''), description: Optional[str] = None, keywords: Optional[None] = None) ‑> glai.back_end.model_db.model_data.ModelData`
    :

    `from_json(json_file_path: str) ‑> glai.back_end.model_db.model_data.ModelData`
    :

    `from_url(url: str, save_dir: str, user_tags: Union[dict, list, set] = ('[INST]', '[/INST]'), ai_tags: Union[dict, list, set] = ('', ''), description: Optional[str] = None, keywords: Optional[None] = None) ‑> glai.back_end.model_db.model_data.ModelData`
    :

    ### Methods

    `download_gguf(self, force_redownload: bool = False) ‑> str`
    :

    `get_ai_tag_close(self) ‑> str`
    :

    `get_ai_tag_open(self) ‑> str`
    :

    `get_ai_tags(self) ‑> list[str]`
    :

    `get_user_tag_close(self) ‑> str`
    :

    `get_user_tag_open(self) ‑> str`
    :

    `get_user_tags(self) ‑> list[str]`
    :

    `has_json(self) ‑> bool`
    :   Checks if the model is in the db.

    `is_downloaded(self) ‑> bool`
    :   Checks if the model file is downloaded.

    `json_path(self) ‑> str`
    :

    `model_path(self) ‑> str`
    :

    `save_json(self, replace_existing: bool = True) ‑> str`
    :

    `set_ai_tags(self, ai_tags: Union[dict, set[str], list[str], tuple[str]]) ‑> None`
    :

    `set_save_dir(self, save_dir: str) ‑> None`
    :

    `set_tags(self, ai_tags: Union[dict, set[str], list[str], tuple[str], ForwardRef(None)], user_tags: Union[dict, set[str], list[str], tuple[str], ForwardRef(None)]) ‑> None`
    :

    `set_user_tags(self, user_tags: Union[dict, set[str], list[str], tuple[str]]) ‑> None`
    :

    `to_dict(self)`
    :