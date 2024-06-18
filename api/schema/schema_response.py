from pydantic import BaseModel
from typing import Dict, Union

class Response(BaseModel):
    status_code: int = 200
    message: str = "success"
    body: Dict[str, Union[str, float]] = {}