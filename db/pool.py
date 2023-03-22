from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from . import db

def init_db(app):
    db_uri = app.config['DATABASE_URI']
    pool_size = app.config.get('DATABASE_POOL_SIZE', 5)
    engine = create_engine(db_uri, pool_size=pool_size)
    db.init_app(app)
    app.db_session = scoped_session(sessionmaker(bind=engine))
    # DB 초기화 및 연결 관리
