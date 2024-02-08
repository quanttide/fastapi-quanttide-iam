"""
用户ORM模型
"""
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import registry

from base.orm import CreatedAt, Id, UpdatedAt


user_mapper_registry = registry()


@user_mapper_registry.mapped
class BaseUserORM:
    """
    基类
    """
    __abstract__ = True

    id: Mapped[Id]
    created_at: Mapped[CreatedAt]


@user_mapper_registry.mapped
class AnonymousUserORM(BaseUserORM):
    """
    匿名用户
    """
    __tablename__ = 'anonymous_user'


@user_mapper_registry.mapped
class RegisteredUserORM(BaseUserORM):
    """
    注册用户
    """
    __tablename__ = 'registered_user'
    updated_at: Mapped[UpdatedAt]


@user_mapper_registry.mapped
class DeactivatedUserORM(BaseUserORM):
    """
    注销用户
    """
    __tablename__ = 'deactivated_user'
