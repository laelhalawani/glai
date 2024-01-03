Module glai.back_end.model_db.model_data
========================================

Classes
-------

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