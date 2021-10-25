from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_moment import Moment
from Sakha.config import DevelopmentConfig, ProductionConfig, TestingConfig




db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
migrate = Migrate(db)
moment = Moment()
login_manager = LoginManager()
login_manager.login_view='usersbp.login'
login_manager.login_message = 'You should login to access the requested page'
login_manager.login_message_category = 'info'




def create_app(Prod=ProductionConfig, Test=TestingConfig, Dev = DevelopmentConfig):
    app = Flask(__name__)

    if app.config['ENV'] == "production":
        app.config.from_object(Prod)
    elif app.config['ENV'] == "testing":
        app.config.from_object(Test)
    else:
        app.config.from_object(Dev)


    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)

    # Register BluePrint
    from Sakha.mainbp.routes import mainbp
    from Sakha.usersbp.routes import usersbp
    from Sakha.postsbp.routes import postsbp
    from Sakha.errorsbp.handlers import handlers
    app.register_blueprint(mainbp)
    app.register_blueprint(usersbp)
    app.register_blueprint(postsbp)
    app.register_blueprint(handlers)

    return app