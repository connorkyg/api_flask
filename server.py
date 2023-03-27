from app.init import create_app
from db.pool import init_db
from gunicorn.app.base import BaseApplication
from gunicorn import util


class FlaskApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/database_name'
    init_db(app)

    options = {
        'bind': '0.0.0.0:5000',
        'workers': 2,
        'threads': 4
    }

    FlaskApplication(app, options).run()
