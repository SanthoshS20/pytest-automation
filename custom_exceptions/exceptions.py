class CustomException(Exception):
    pass

class FileExtensionError(CustomException):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
