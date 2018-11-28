from flask import Flask,render_template
import requests
from secrets import nyt_key

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

def get_stories(section = 'technology'):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendeurl = baseurl + section + '.json'
    params={'api-key':nyt_key}
    stories = requests.get(extendeurl, params).json()['results']
    res = []
    for i in range(5):
        temp = {}
        temp['title'] = stories[i]['title']
        temp['url'] = stories[i]['url']
        res.append(temp)
    return res

@app.route('/user/<nm>')
def hello_name(nm):
    res = get_stories('technology')
    head = render_template('user.html', name=nm, section='technology')
    for i in range(5):
        head += '<h3 style="text-indent:2.3em;">'
        head += '<font size="2">'
        url = res[i]['url']
        title = res[i]['title']
        head += "{}. {} ({})</font></h3>".format(i+1,title,url,url)
    return head



if __name__ == '__main__':
    app.run(debug=True)