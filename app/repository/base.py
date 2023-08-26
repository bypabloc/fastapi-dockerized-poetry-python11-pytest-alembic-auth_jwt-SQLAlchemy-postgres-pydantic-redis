from pydantic import BaseModel

from app.db.main import Base as DBBase


class RepositoryBase:
    """
    Base repository
    """
    model: DBBase
    schema: BaseModel
    database: DBBase

    def __init__(self, database):
        """
        Constructor
        """
        self.database = database

    def create(self):
        """
        Create a new user
        """
        raise NotImplementedError

    def update(self):
        """
        Update a user
        """
        raise NotImplementedError

    def delete(self):
        """
        Delete a user
        """
        raise NotImplementedError

    def get(self):
        """
        Get a user
        """
        raise NotImplementedError

    def get_all(self):
        """
        Get all users
        """
        raise NotImplementedError
