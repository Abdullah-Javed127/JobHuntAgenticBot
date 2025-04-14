from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import routes and register them with the app
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
