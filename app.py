from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
var=eval(input('enter your val: '))
def home():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

