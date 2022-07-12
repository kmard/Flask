import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/first')
def first_view():
    return 'This is first page'

@app.route('/second')
def second_view():
    return 'This is second page'

@app.route('/third')
def third_view():
    return 'This is third page'


if __name__ == '__main__':
    app.run(debug=True)


