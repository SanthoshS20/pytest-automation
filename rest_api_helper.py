from utilities.api_utils import make_api_call
from utilities.json_utilities import read_json_data_from_file
import constants

request_schema = read_json_data_from_file(constants.request_schema_file_path)


def get_user(user_id: int) -> dict:
    """
    Get the user data

    Parameters:
        user_id (int): id of the user

    Returns:
        get_user_api_response (dict): Response of the get_user API
    """
    url = constants.BASE_URL + request_schema["get_user"]["endpoint"] + user_id
    get_user_api_response = make_api_call(url=url, query_params={})
    return get_user_api_response


def create_new_user() -> dict:
    """
    Create a new user

    Returns:
        create_post_api_response (dict): Response of the create_user API
    """
    url = constants.BASE_URL + request_schema["create_new_user"]["endpoint"]
    create_post_api_response = make_api_call(url=url, method='POST', query_params={},
                                             request_body=request_schema["create_new_user"]["body"])
    return create_post_api_response
