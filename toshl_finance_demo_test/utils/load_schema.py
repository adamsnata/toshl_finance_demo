import json

from toshl_finance_demo_test.utils.file_path import abs_path_from_project


def load_schema(filepath):
    with (abs_path_from_project('schemas') / filepath).open() as file:
        schema = json.load(file)
        return schema
