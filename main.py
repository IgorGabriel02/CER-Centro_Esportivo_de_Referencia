from werkzeug.security import generate_password_hash
from flask import Flask , render_template  , request
from forms import userR_form
from models import db , user




# CREATE ROUTES HUB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CERadmin_server1'



# SQALCHEMY CODES 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# FLASK ROUTES



@app.route('/register_template')
def index4():
    Rform = userR_form()
    return render_template('index4.html' , form=Rform ) 


# REGISTER AND LOGIN FUNCTIONS

@app.route('/register' , methods=['POST' , 'GET'])
def login():
    form = userR_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            password_hash = generate_password_hash(form.password.data)

            new_user = user(
                name=form.name.data,
                email=form.email.data,
                senha=password_hash)

            db.session.add(new_user)
            db.session.commit()
    print(form.errors)
    return render_template('index4.html', form=form)
    

# HOST FLASK

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)