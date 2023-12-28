from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker

from config.db_config import SQLALCHEMY_DATABASE_URI


class Database(object):
    """Initialize sqlite database """
    db_uri = SQLALCHEMY_DATABASE_URI
    table = ""

    def __init__(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = self.db_uri
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        self.db = SQLAlchemy(app)
        self.engine = create_engine(self.db_uri)
        self.metadata = MetaData()
        self.session = scoped_session(sessionmaker(bind=self.engine))

    def cur(self):
        return self.session

    def query(self, q):
        if (len(self.table)>0):
            q = q.replace("@table", self.table)

        return self.session.execute(q)

    def commit(self):
        self.session.commit()
