from pydantic import BaseModel
from typing import List, Optional

class Project(BaseModel):
    name: str
    description: str
    tech_stack: List[str]

class Resume(BaseModel):
    name: str
    education: str
    skills: List[str]
    projects: List[Project]
    target_position: Optional[str] = None
