from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

from sqlalchemy.orm import declarative_base


Base = declarative_base()


@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
