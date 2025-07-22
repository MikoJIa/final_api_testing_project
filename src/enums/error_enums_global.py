from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_TYPE = "Error: Order data must be a dictionary."
    WRONG_STATUS_CODE = f"Received status code is not equal to expected"
    WRONG_FIELD = "There are no such fields in the object."
    WRONG_STATUS_CODE_404 = "The status of the code does not match the expected one."
