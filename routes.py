from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/table')
def table():
    return render_template('table.html', values=get_list())

@app.route('/json')
def json():
        return jsonify(results=get_list())

def get_list():
    list = [
            {'id' : 1, 'param' : 'foo', 'val' : 2, 'state' : 'running'},
            {'id' : 2, 'param' : 'bar', 'val' : 5, 'state' : 'stopped'}
           ]
    return list


if __name__ == '__main__':
    app.run(debug=True)
