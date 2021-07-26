import os
from flask import Flask
from .models import db as models_db
from .app_service import db as service_db
from .routes import bp

def create_app(config=None):
    app = Flask(__name__)
    app.config.update(config)
    setup_app(app)
    return app

def setup_app(app):
    
    @app.before_first_request
    def create_tables():
        models_db.create_all()
        service_db.create_all()
    models_db.init_app(app)
    service_db.init_app(app)
    
    app.register_blueprint(bp, url_prefix='')
