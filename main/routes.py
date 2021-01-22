from main import app
from flask import render_template, request, redirect, url_for
from main.models import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/home/')
def home():
    if request.method == 'POST':
        user = User.query.filter_by(exp=request.form['exp']).first()
        if user is None:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('status'))
    return render_template('home.html')


@app.route('/status/')
def status():
    user = User.query.filter_by(exp=int(request.args.get('exp'))).first()
    if user is None:
        return redirect(url_for('home'))
    else:
        return '''
            <html>
            <head>
                <title>Status</title>
            </head>
            <body>
                <h3>ESTATUS</h3>
                <h5>''' + user.tramite + '''</h5>
                <p>''' + str(user.exp) + '''</p>
                <p>''' + user.nombre + '''</p>
            </body>
            </html>'''


@app.route('/new')
def create():
    return 'create new'


@app.route('/edit')
def update():
    return 'update-upgrade'


@app.route('/delete')
def eliminate():
    return 'Deleting'
