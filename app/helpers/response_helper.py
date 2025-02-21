from typing import Union, Optional
from flask import jsonify, Response
from pydantic import BaseModel
from enum import Enum
from http import HTTPStatus


class StatusEnum(str, Enum):
    SUCCESS = "success"
    ERROR = "error"

class AppResponse(BaseModel):
    status: StatusEnum
    message: Union[str, dict, None]
    data: Optional[Union[dict, list]] = None
    http_status_code: int

def success(message: Optional[str], data: Optional[Union[dict, list]], http_status_code: int = HTTPStatus.OK) -> tuple[Response, int]:
    response = AppResponse(
        status=StatusEnum.SUCCESS,
        message=message,
        data=data,
        http_status_code=http_status_code
    )
    return jsonify(response.model_dump()), http_status_code

def error(message: Union[str, dict], http_status_code: int) -> tuple[Response, int]:
    response = AppResponse(
        status=StatusEnum.ERROR,
        message=message,
        data=None,
        http_status_code=http_status_code
    )
    return jsonify(response.model_dump()), http_status_code