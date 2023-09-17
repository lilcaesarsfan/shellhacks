from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
#app.register_blueprint(views, url_prefix="/search")
app.secret_key = 'yessir'

if __name__ == '__main__':
    app.run(debug=True)