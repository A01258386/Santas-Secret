#Santa's Secret
from flask import Flask, render_template, request
import random

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])


def santas_secret():
    transcript = ""
    friends = ['Amanda', 'Alex A', 'Alex H', 'Gokce','Steven','Yi']
    random.shuffle(friends)
    
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        transcript = random.choice(friends)
    # print('Now I will tell you who is your secret friend!')
    return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
    app.run(debug=True,threaded=True)