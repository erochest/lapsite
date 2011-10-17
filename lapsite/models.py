

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Community(Base):
    __tablename__ = 'communities'

    comid = Column(Integer, primary_key=True)
    projid = Column(Integer)
    type = Column(String(1))
    name = Column(String(30))
    state = Column(String(2))
    code = Column(String(10))
    x = Column(Integer)
    y = Column(Integer)

    def __init__(self, project, type, name, state, code, x, y):
        self.projid = project.projid
        self.type = type
        self.name = name
        self.state = state
        self.code = code
        self.x = y
        self.y = y

    def __repr__(self):
        return '<%s #%s %s>' % (self.__class__.__name__, self.comid, self.name)

