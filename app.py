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

@app.route('/people/<int:people_id>')
def people_view(people_id):
    people = {
        1:'Jonn Smith',
        2:'Eva Braun',
        3:'Philip Djonn',
        4:'Richard Gramm'
    }
    try:
      people_name = people[people_id]
    except KeyError:
        return flask.abort(404)

    return flask.render_template('people.html',people_name = people_name )


@app.route('/third')
def third_view():
    return 'This is third page'


if __name__ == '__main__':
    app.run(debug=True)


