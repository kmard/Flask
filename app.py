import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/about')
def about_view():
    return flask.render_template('about.html')

@app.route('/welcome')
def welcome_view():
    welcome = 'WELCOM'
    number = '777'
    num_weeks = '8'
    return flask.render_template('welcome.html',
                                 welcome=welcome,
                                 number=number,
                                 num_weeks=num_weeks,)

@app.route('/third')
def third_view():
    return 'This is third page'


if __name__ == '__main__':
    app.run(debug=True)


