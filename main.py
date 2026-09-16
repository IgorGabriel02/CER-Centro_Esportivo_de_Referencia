from werkzeug.security import generate_password_hash , check_password_hash
from flask import Flask , render_template  , request , flash , get_flashed_messages , redirect , url_for
from forms import userR_form , UserL_form
from models import db , user




# CREATE ROUTES HUB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CERadmin_server1'



# SQALCHEMY CODES 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CERbase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# FLASK ROUTES AND FUNCTIONS

messages = get_flashed_messages


@app.route('/register' , methods=['POST' , 'GET'])
def register():
    form = userR_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            password_hash = generate_password_hash(form.password.data.strip())
            try:
                new_user = user(
                    name=form.name.data.strip(),
                    email=form.email.data.strip(),
                    senha=password_hash )
                
                db.session.add(new_user)
                db.session.commit()
                flash('usuário cadastrado!')
            except Exception as e:
                print(e)
                flash('erro ao cadastrar o usuário.')

                
        else:
            
            flash('alguma informação está em falta.')
    return render_template('index4.html' , form=form ) 
    

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    form = UserL_form()
    if request.method == 'POST':
        if form.validate_on_submit(): 

            username = user.query.filter_by(name=form.user_input.data).first()
            if username and check_password_hash(username.senha , form.user_password.data ) :

                return redirect(url_for('index5'))
            else:
                flash('senha ou usuário incorreto.')
                print('erro ao cadastrar usuário.')
    return render_template('index3.html' , form=form)


            
@app.route('/feed' , methods=['GET' , 'POST'])
def index5():
    return render_template('index5.html')


# HOST FLASK

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)