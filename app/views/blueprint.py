from flask import Blueprint, render_template,request
from app.endpoints.square import get 

blueprint_bp = Blueprint('blueprint', __name__)

@blueprint_bp.route('/')
def index():
    # method
    # path
    # headers
    # query_parameters
    # payload
    return render_template('index.html')

@blueprint_bp.route('/hey')
def hey():
    say_good_deed = "congratulation be brave"
    return render_template("index.html")

@blueprint_bp.route('/square', methods=['GET','POST'])
def square():
    if request.method == 'POST':
        n = int(request.form['square'])
        result = get(n)
        return {'result' : result}
    return render_template("square.html")
