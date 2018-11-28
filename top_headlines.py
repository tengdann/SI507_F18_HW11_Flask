from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/user/<usr>')
def user(usr):
    return render_template('user.html', name = usr)
    
    
if __name__ == '__main__':
    app.run(debug = True)