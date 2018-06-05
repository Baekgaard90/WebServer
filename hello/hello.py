from flask import Flask
from flask import request

app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!"

@app.route("/")
def test():
    d = request.args

    output_string = str(d)
    try:
        output_string += ".\n\nThe device is: " + d['device'] + "\nThe latitude is: " + d['lat'] + "\nThe longitude is: " + d['lon']
    except KeyError:
        pass

    return output_string
