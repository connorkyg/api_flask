import psycopg2
from psycopg2 import pool
from flask import current_app, g


class Database:
    def __init__(self):
        self._conn_pool = None

    def init_app(self, app):
        conf = app.config.get_namespace('DB_')
        self._conn_pool = pool.SimpleConnectionPool(
            conf.min_conn, conf.max_conn, **conf.params)

    def get_conn(self):
        if self._conn_pool is None:
            raise RuntimeError('database not initialized')
        return self._conn_pool.getconn()

    def return_conn(self, conn):
        self._conn_pool.putconn(conn)

    def close_conn_pool(self):
        if self._conn_pool is not None:
            self._conn_pool.closeall()


def get_db():
    if 'db' not in g:
        g.db = Database().get_conn()
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        Database().return_conn(db)


def init_app(app):
    db = Database()
    db.init_app(app)
    app.teardown_appcontext(close_db)
