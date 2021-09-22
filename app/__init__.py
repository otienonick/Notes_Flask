from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager




db = SQLAlchemy()
DB_NAME = 'database.dt'
    
    


def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'jjkkjvbbvkvgvdvkddvchvjhjdsdd8894y439879'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #initialize database
    db.init_app(app)




    from .views import views
    app.register_blueprint(views,url_prefix = '/')

    from .auth import auth
    app.register_blueprint(auth,url_prefix = '/')

    from  .models import User,Note  

    create_database(app)
    # create an instance of the class LoginManager
    login_manager = LoginManager()
    # if a user is not logged in where should he be redirected to.
    login_manager.login_view = 'auth.login'
    # tell the login_manager which app we are using.
    login_manager.init_app(app)
# use path module to determine whether path to our database exists

# tell flask how we how we load a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# create database
def create_database(app):
  
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print('created database!')
