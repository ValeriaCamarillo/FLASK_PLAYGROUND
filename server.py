from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# @app.route('/play/<int:number>')
@app.route('/play')
def green_boxes(number = 3):
    return render_template('index.html',number = 3)

@app.route('/play/<int:number>')
def num_boxes(number):
    return render_template('index.html', number = number)

@app.route('/play/<int:number>/<color>')
def repeat(number,color):
    return render_template('index.html',number = number, color = color)

if __name__ == '__main__':
    app.run(debug=True)
