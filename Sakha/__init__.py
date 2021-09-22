from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from Sakha.config import Config




app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message = 'You should login to access the requested page'
login_manager.login_message_category = 'info'



from Sakha import routes