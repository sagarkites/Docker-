from flask import Flask
app = Flask(__name__)

@app.route('/')
def sagar():
    return 'Welcome this is sagar currently testing Docker'

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')

