from flask import *
from flask_cors import *

from api.gamesession import session
from util.error_advice import advice

app = Flask(__name__)

# routes and error handle routes
app.register_blueprint(session)

app.register_blueprint(advice)


if __name__ == '__main__':
    CORS(app)  # lets other programs consume app
    app.debug = True
    app.run()