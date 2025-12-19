from pydantic import BaseModel
from typing import Dict

class FileCreate(BaseModel):
    file_metadata: Dict
