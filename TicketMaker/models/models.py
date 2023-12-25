from pydantic import BaseModel, HttpUrl, validator
from typing import List, Optional, Dict
from datetime import datetime


class User(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: HttpUrl
    html_url: HttpUrl
    type: str
    site_admin: bool


class Label(BaseModel):
    id: int
    node_id: str
    url: HttpUrl
    name: str
    description: Optional[str] = None
    color: str
    default: bool


class Milestone(BaseModel):
    url: HttpUrl
    html_url: HttpUrl
    labels_url: HttpUrl
    id: int
    node_id: str
    number: int
    title: str
    description: Optional[str] = None
    creator: User
    open_issues: int
    closed_issues: int
    state: str
    created_at: datetime
    updated_at: datetime
    due_on: Optional[datetime]
    closed_at: Optional[datetime]


class Issue(BaseModel):
    id: int
    node_id: str
    url: HttpUrl
    repository_url: HttpUrl
    labels_url: HttpUrl
    comments_url: HttpUrl
    events_url: HttpUrl
    html_url: HttpUrl
    number: int
    state: str
    title: str
    body: Optional[str] = None
    user: User
    labels: List[Label]
    assignee: Optional[User]
    assignees: List[User]
    milestone: Optional[Milestone]
    locked: bool
    active_lock_reason: Optional[str]
    comments: int
    created_at: datetime
    updated_at: datetime
    closed_at: Optional[datetime]
    author_association: str
    pull_request: Optional[Dict] = None  # Handling a validation error

    @validator('pull_request', pre=True, always=True)
    def default_pull_request(cls, v):
        return v or {}


class Message(BaseModel):
    title: str
    body: Optional[str] = None
    labels: List[Label]
    created_by: str
    created_at: datetime
