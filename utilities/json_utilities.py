import json, os
from typing import Dict, List, Optional
from custom_exceptions.exceptions import FileExtensionError


def read_json_data_from_file(json_file_path: str) -> Dict[str, str]:
    """
    Read the json data from the file

    Parameters:
        json_file_path (str): File path

    Returns:
        json_data (dict): json data from the specified file

    Raises:
        FileExistsError: If the file doesn't exist in the specified file path
    """
    if not(os.path.exists(json_file_path)):
        raise FileNotFoundError(f"File doesn't exists in the given path")
        #raise FileExistsError(f"File doesn't exist in {json_file_path}")
    elif ".json" not in json_file_path:
        raise FileExtensionError(f"Incorrect file extension in the {json_file_path}")
    else:
        file_content = open(json_file_path, 'r')
        json_data = json.load(file_content)
        file_content.close()
        return json_data
        # with open(json_file_path, 'r') as file_content:
        #     json_data = json.load(file_content)
        # return json_data


def compare_jsons(actual_json: Dict[str, str], expected_json: Dict[str, str],
                  skip_fields: Optional[List[str]] = None) -> bool:
    """
    Compare the actual and the expected json

    Parameters:
        actual_json (dict): Actual json data
        expected_json (dict): Expected json data
        skip_fields (list): Fields which needs to be skipped

    Returns:
        Bool: Status of the compared json data

    Raises:
        KeyError: If key from actual json not found in expected json
    """
    if skip_fields:
        for key, value in actual_json.items():
            try:
                if key not in skip_fields:
                    if value != expected_json[key]:
                        return False
            except KeyError:
                raise KeyError(f"{key} not found in {expected_json}")
        return True
    else:
        return actual_json == expected_json
