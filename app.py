from flask import Flask, render_template
from sl import busstops


app = Flask(__name__)


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 501

@app.route('/')
def welcome():
    svar=busstops()


    return render_template('index.html',title="A timetable close to you!",svar=svar )




if __name__ == '__main__':
    app.run(debug=False)
