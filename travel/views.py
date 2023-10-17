from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import Destination
from . import db

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))

# @mainbp.route('/login', methods=['GET', 'POST'])
# def login():
#     email = request.values.get('email')
#     passwd = request.values.get('pwd')
#     print (f"Email: {email} Password: {passwd}")
#     session['email'] = email
#     return render_template('login.html')

# @mainbp.route('/logout')
# def logout():
#     if 'email' in session:
#         session.pop('email')
#         return "User logged out"
#     else:
#         return "No User was logged in"
    



'''
updated travel/__init__.py
'''


#import flask - from the package import a module
from flask import Flask

def create_app():
    print(__name__)  #let us be curious - what is this __name__
    app = Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug = True
    #add the Blueprint
    from . import views
    app.register_blueprint(views.mainbp)
    return app