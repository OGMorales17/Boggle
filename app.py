from flask import Flask, request, render_template, session, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdfgkjtjkkg45yfdb'

boggle_game = Boggle()


@app.route('/')
def home_page():
    """Show board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get('highscore', 0)
    numplays = session.get('numplays', 0)

    return render_template('/index.html', board=board, highscore=highscore, numplays=numplays)


@app.route('/check-word')
def check_word():
    """Check if word in dictionary."""

    word = request.args['word']
    board = session['board']
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})


@app.route('/post-score', methods=['POST'])
def post_score():
    """Recive score, update numplays, update hight score if appropiate."""

    score = request.json['score']
    highscore = session.get('highscore', 0)
    numplays = session.get('numplays', 0)

    session['numplays'] = numplay + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokenRecord=score > highscore)
