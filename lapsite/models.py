

from sqlalchemy import BLOB, Column, Float, Integer, String, TEXT
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
        self.projid = project.projid if project is not None else None
        self.type = type
        self.name = name
        self.state = state
        self.code = code
        self.x = y
        self.y = y

    def __repr__(self):
        return '<%s #%s %s>' % (self.__class__.__name__, self.comid, self.name)


class FieldWorker(Base):
    __tablename__ = 'fieldworkers'

    fwid = Column(Integer, primary_key=True)
    projid = Column(Integer)
    code = Column(String(3))
    name = Column(String(40))

    def __init__(self, project, code, name):
        self.projid = project.projid if project is not None else None
        self.code = code
        self.name = name

    def __repr__(self):
        return '<%s %s [%s]>' % (self.__class__.__name__, self.name, self.code)


class Informant(Base):
    __tablename__ = 'informants'

    infid = Column(Integer, primary_key=True)
    projid = Column(Integer)
    comid = Column(Integer)
    informid = Column(String(10))
    oldnumber = Column(String(10))
    auxiliary = Column(String(1))
    fwid = Column(Integer)
    wsid = Column(Integer)
    yearinterviewed = Column(Integer)
    inftype = Column(String(3))
    generation = Column(String(1))
    cultivation = Column(String(1))
    sex = Column(String(1))
    age = Column(Integer)
    education = Column(String(1))
    occupation = Column(String(1))
    race = Column(String(1))
    latitude = Column(Float)
    longitude = Column(Float)

    def __init__(self, project, community, informid, oldnumber, auxiliary, fw,
                 ws, yearinterviewed, inftype, generation, cultivation, sex,
                 age, education, occupation, race, latitude, longitude):
        self.projid = project.projid if project is not None else None
        self.comid = community.comid if community is not None else None
        self.informid = informid
        self.oldnumber = oldnumber
        self.auxiliary = auxiliary
        self.fwid = fw.fwid if fw is not None else None
        self.wsid = ws.wsid if ws is not None else None
        self.yearinterviewed = yearinterviewed
        self.inftype = inftype
        self.generation = generation
        self.cultivation = cultivation
        self.sex = sex
        self.age = age
        self.education = education
        self.occupation = occupation
        self.race = race
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.informid)


class Project(Base):
    __tablename__ = 'projects'

    projid = Column(Integer, primary_key=True)
    name = Column(String(10))
    long_name = Column(String(100))

    def __init__(self, name, long_name):
        self.name = name
        self.long_name = long_name

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)


class Response(Base):
    __tablename__ = 'responses'

    responseid = Column(Integer, primary_key=True)
    projid = Column(Integer)
    item = Column(String(100))
    infid = Column(Integer)
    gramflag = Column(String(4))
    doubtflag = Column(String(4))
    commenttext = Column(BLOB)
    commentcodes = Column(String(50))
    phonetic = Column(String(255))
    simplephone = Column(String(255))
    targetid = Column(Integer)

    def __init__(self, project, item, informant, gramflag, doubtflag,
                 commenttext, commentcodes, phonetic, simplephone, target):
        self.projid = project.projid if project is not None else None
        self.item = item
        self.infid = informant.infid if informant is not None else None
        self.gramflag = gramflag
        self.doubtflag = doubtflag
        self.commenttext = commentext
        self.commentcodes = commentcodes
        self.phonetic = phonetic
        self.simplephone = simplephone
        self.targetid = target.targetid if target is not None else target

    def __repr__(self):
        return '<%s %s=%s>' % (self.__class__.__name__, self.targetid, self.item)


class Target(Base):
    __tablename__ = 'targets'

    targetid = Column(Integer, primary_key=True)
    projid = Column(Integer)
    target = Column(String(50))
    type = Column(String(1))
    page = Column(Integer)
    subpage = Column(String(1))
    item = Column(Integer)
    subitem = Column(String(1))
    notes = Column(TEXT)

    def __init__(self, project, target, type, page, subpage, item, subitem,
                 notes):
        self.projid = project.projid if project is not None else None
        self.target = target
        self.type = type
        self.page = page
        self.subpage = subpage
        self.item = item
        self.subitem = subitem
        self.notes = notes

    def __repr__(self):
        return '<%s %s, %s.%s>' % (self.__class__.__name__, self.target,
                                   self.page, self.subpage)


class WorkSheet(Base):
    __tablename__ = 'worksheets'

    wsid = Column(Integer, primary_key=True)
    projid = Column(Integer)
    code = Column(String(3))
    name = Column(String(3))

    def __init__(self, project, code, name):
        self.projid = project.projid if project is not None else None
        self.code = code
        self.name = name

    def __repr__(self):
        return '<%s %s:%s>' % (self.__class__.__name__, self.code, self.name)

