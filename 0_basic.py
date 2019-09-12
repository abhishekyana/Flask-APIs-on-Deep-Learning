# Code to run at server(Local Machine)
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World, This message is from Flask"
if __name__ == '__main__':
    app.run(debug=True)
"""
# Output:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with fsevents reloader
* Debugger is active!
* Debugger PIN: 123-456-789 # Yours will be different.
"""
