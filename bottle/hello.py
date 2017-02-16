from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return "{'hello': 'world'}"

@app.route('/hello/<name>')
def greet(name='Stranger'):
    return "{'hello': '" + name  + "'}"

run(app, host='localhost', port=8080)
