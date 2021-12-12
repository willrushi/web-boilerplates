from flask import Flask

from blueprints.routes import routes

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

# change this!
app.secret_key = "965caf956f95a7928345abafcb9f156"

app.register_blueprint(routes)


if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')