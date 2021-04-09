from flask import Flask,render_template


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/proyects')
def proyects():
    return render_template('proyects.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/social')
def social():
    return render_template('social.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


