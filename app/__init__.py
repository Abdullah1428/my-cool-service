from flask import Flask
from app.routes.users import users_blueprint
from app.utils.logger import configure_logging

def create_app():
    app = Flask(__name__)
    
    configure_logging(app)
    
    app.register_blueprint(users_blueprint, url_prefix='/api')
    
    return app
