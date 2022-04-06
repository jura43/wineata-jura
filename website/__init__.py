from flask import Flask, request, session
from flask_babelex import Babel


def create_app():
    app = Flask(__name__)
    #app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['LANGUAGES'] = { 'en' : 'English', 'hr': 'Hrvatski'}
    app.secret_key = "wineata super secret key"
    babel = Babel(app)
    
    @app.context_processor
    def inject_conf_var():
        return dict(AVAILABLE_LANGUAGES=app.config['LANGUAGES'], CURRENT_LANGUAGE=session.get('lang', request.accept_languages.best_match(app.config['LANGUAGES'].keys())))
    
    @babel.localeselector
    def get_locale():
        if request.args.get('lang'):
            session['lang'] = request.args.get('lang')
        return session.get('lang', request.accept_languages.best_match(app.config['LANGUAGES'].keys()))

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app