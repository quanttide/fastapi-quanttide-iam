"""
用户领域模型
"""
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class BaseUser(BaseModel):
    """
    用户
    """
    id: UUID
    created_at: datetime


class AnonymousUser(BaseUser):
    """
    匿名用户
    """
    pass


class RegisteredUser(BaseUser):
    """
    注册用户
    """

    updated_at: datetime


class DeactivatedUser(BaseUser):
    """
    注销用户
    """
    deleted_at: datetime
