from flask import Flask, render_template
import requests
import secrets
import json
app = Flask(__name__)

api_key = secrets.api_key
baseurl = 'https://api.nytimes.com/svc/topstories/v2/'

def make_url(section, format):
    url = baseurl
    url += section + '.' + format
    url += '?api_key=' + api_key
    return url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<usr>')
def user(usr):
    readback = json.loads(requests.get(make_url('technology', 'json')).text)
    return render_template('user.html', name = usr, topic = 'technology', my_list = readback['results'][:5])
    
@app.route('/user/<usr>/<tpc>')
def topic(usr, tpc):
    readback = json.loads(requests.get(make_url(str(tpc), 'json')).text)
    return render_template('user.html', name = usr, topic = tpc, my_list = readback['results'][:5])
    
    
if __name__ == '__main__':
    app.run(debug = True)