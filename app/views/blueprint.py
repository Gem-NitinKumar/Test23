from flask import Blueprint, render_template,request

bluprint_bp = Blueprint('blueprint', __name__)

@bluprint_bp.route('/')
def index():
    return render_template('index.html')

@bluprint_bp.route('/hey')
def hey():
    say_good_deed = "congratulation be brave"
    return render_template("index.html")

@bluprint_bp.route('/square', methods=['GET','POST'])
def square():
    if request.method == 'POST':
        n = int(request.form['square'])
        n = n*n
        req = str(n)
        return req
    return render_template("square.html")
