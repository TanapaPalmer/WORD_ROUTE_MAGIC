from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hi/<string:name>')
def hi(name):
    return render_template("index.html", name=name)

@app.route('/<string:any_word>')
def any_word(any_word):
    return render_template("index.html", any_word=any_word)

@app.route('/<string:anything>/<int:num>')
def repeat(anything,num):
    content = anything * num
    return render_template("index.html", content=content, anything=anything, num=num)

if __name__=="__main__":
    app.run(debug=True)