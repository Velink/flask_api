from flask import *
from flask_cors import CORS
from werkzeug import exceptions
import smtplib, ssl


app = Flask(__name__)
CORS(app)


@app.route('/')
def welcome():
    return 'Welcome to the Video Game API!'


@app.route('/video-games', methods=['GET', 'POST'])
def vg_handler():
    if request.method == 'GET':
        return jsonify([
            {"name": "League of Legends", "ROI": 2009},
            {"name": "Tomb Raider", "ROI": 2013},
            {"name": "Skyrim", "ROI": 2011}
        ]), 200
    elif request.method == 'POST':
        data = request.json
        return f"You added a video-game! The game is called {data['name']}", 200
        wanted = input("Would you like to receive email confirmation? y/n")
        if wanted.lower() == "y":
            send_mail()


@app.route('/games/<int:game_id>')
def cat_handler(cat_id):
    pass


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Oops...{err}"}), 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"it's not you, it's us"}), 500

def send_mail():
    port = 587
    smtp_server = "smtp.gmail.com"
    message="""\
    Subject: Congratulations

    You successfully added a video game to the database.
    """
    receiver = input("Your email...")
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login("cal.vel.flask@gmail.com", "amanfromnantucket")
        server.sendmail("cal.vel.flask@gmail.com", receiver, message)


# Boilerplate code which protects users from accidentally invoking the script when they don't want to
if __name__ == '__main__':
    app.run(debug=True)
