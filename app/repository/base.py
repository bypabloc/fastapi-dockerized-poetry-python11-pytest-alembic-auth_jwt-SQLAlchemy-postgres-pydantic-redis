from pydantic import BaseModel


class RepositoryBase:
    """
    Base repository
    """
    schema: BaseModel

    def __init__(self, database):
        """
        Constructor
        """
        self.database = database
