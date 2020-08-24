import click
from flask import abort, Flask, _app_ctx_stack, jsonify, json, request, render_template
from flask_cors import CORS
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import HTTPException

from app import models
from app.models import Answer, Case
from app.database import SessionLocal, engine
from app.queens import ChessBoard

app = Flask(__name__)
CORS(app)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)


@app.cli.command('initdb')
def initdb():
    models.Base.metadata.create_all(bind=engine)


@app.cli.command("generate-chessboard")
@click.argument("dimension")
def generate_chessboard(dimension):
    board = ChessBoard(int(dimension), True)
    board.n_queens()


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    data = dict(
        message=e.description,
    )
    return jsonify(data), e.code


@app.route('/')
def index():
    print(__name__)
    return render_template('chessboard.html')


@app.route('/cases')
def get_cases():
    cases = app.session.query(Case).all()
    return json.dumps([row.to_dict() for row in cases])


@app.route('/cases/<dimension>/answer')
def get_answer(dimension):
    case = app.session.query(Case).filter_by(dimension=dimension).first()
    if case is None:
        return abort(404, description="Case not found")

    page = (request.args.get('page'), '1')[request.args.get('page') is None]
    if not page.isnumeric():
        return abort(400, description="Not a valid value for page")

    limit = 1
    page = int(page)

    answers = app.session.query(Answer).filter_by(dimension=dimension).limit(limit).offset(limit * (page - 1))

    data = {
        'total': app.session.query(Answer).filter_by(dimension=dimension).count(),
        'data': list()
    }
    for answer in answers:
        data['data'].append({
            'dimension': answer.dimension,
            'solution': answer.solution,
        })
    return json.dumps(data)


if __name__ == "__main__":
    from os import environ

    debug = (environ.get("DEBUG") == 'true')
    port = int(environ.get("PORT", 5000))
    host = environ.get("HOST", '127.0.0.1')

    app.run(debug=debug, port=port, host=host)
