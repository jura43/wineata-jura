from flask import Flask
from flask_babel import Babel, gettext


def create_app():
    app = Flask(__name__)
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    babel = Babel(app)
    
    @babel.localeselector
    def get_locale():
        return 'en'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app