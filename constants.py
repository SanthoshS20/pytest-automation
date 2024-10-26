import pathlib, os

base_path = pathlib.Path(__file__).parent.resolve()
#base_path = os.path.dirname(os.path.abspath(__file__))

request_schema_file_path = f"{base_path}/data/request_schema.json"
response_schema_file_path = f"{base_path}/data/response_schema.json"

BASE_URL = ""

