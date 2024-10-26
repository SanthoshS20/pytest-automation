from rest_api_helper import create_new_user, get_user
from constants import response_schema_file_path
from utilities.json_utilities import read_json_data_from_file, compare_jsons

response_schema_json = read_json_data_from_file(response_schema_file_path)

def test_create_user():
    create_user_response = create_new_user()
    assert create_user_response.status_code == 201, (f"Expected 201 response code but the actual response code received "
                                                     f"{create_user_response.status_code}")
    create_user_json_response = create_user_response.json()
    user_id = create_user_json_response["id"]
    get_user_response = get_user(user_id)
    assert get_user_response.status_code == 200, (f"Expected 200 response code but the actual response code received "
                                                  f"{get_user_response.status_code}")
    assert compare_jsons(get_user_response.json(), response_schema_json["new_user_response"], ["id"]), \
        f"Expected response not equal to actual response {get_user_response.json()}"