

from lapsite import db


class Communities(db.Model):
    comid = db.Column(db.Integer, primary_key=True)
    projid = db.Column(db.Integer)
    type = db.Column(db.String(1))
    name = db.Column(db.String(30))
    state = db.Column(db.String(2))
    code = db.Column(db.String(10))
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)

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

