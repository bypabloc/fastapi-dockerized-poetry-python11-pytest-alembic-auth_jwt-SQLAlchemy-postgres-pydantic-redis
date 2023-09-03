# app/models/status.py


class Status(Base):
    __tablename__ = 'statuses'

    name = Column(String, nullable=False)
    color_code = Column(String, nullable=False)
    display_order = Column(Integer, nullable=False)