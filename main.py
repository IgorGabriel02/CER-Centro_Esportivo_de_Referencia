from flask import Flask , render_template 
from forms import userR_form

# CREATE ROUTES HUB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CERadmin_server1'


#FORMS 


# FLASK ROUTES



@app.route('/register')
def index4():
    Rform = userR_form()
    return render_template('index4.html' , form=Rform ) 


# START FLASK

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)