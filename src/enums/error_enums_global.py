from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_TYPE = "Error: Order data must be a dictionary."
    WRONG_STATUS_CODE = f"Received status code is not equal to expected"
    WRONG_FIELD = "There are no such fields in the object."
