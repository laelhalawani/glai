Module glai.back_end.model_db.db
================================

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