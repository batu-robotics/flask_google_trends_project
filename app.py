from flask import Flask,render_template

app = Flask(__name__)

sports_list="Football, Rugby & Tennis"

@app.route('/')
def home():  # put application's code here
    return render_template('main.html',sports=sports_list)

@app.route('/time_series_analytics')
def time_series_analytics():  # put application's code here
    return render_template('home.html',sports=sports_list)

@app.route('/map_analytics')
def map_analytics():  # put application's code here
    return render_template('map.html',sports=sports_list)

@app.route('/football')
def football():  # put application's code here
    return render_template('football.html',sports=sports_list)

@app.route('/rugby')
def rugby():  # put application's code here
    return render_template('rugby.html',sports=sports_list)

@app.route('/tennis')
def tennis():  # put application's code here
    return render_template('tennis.html',sports=sports_list)

if __name__ == '__main__':
    app.run()
