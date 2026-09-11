from flask import Flask , render_template , request


# CREATE ROUTES HUB

app = Flask(__name__)

# FLASK ROUTES



@app.route('/registeR_form')
def index4():
    return render_template('index4.html')



# START FLASK

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)