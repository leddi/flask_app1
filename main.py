from pyfiglet import Figlet
import os
from flask import Flask

# the all-important app variable:
app = Flask(__name__)

font = Figlet(font="small")

@app.route('/')
def main():
    # get the message from the environmental variable $MESSAGE
    # or fall back to the string "no message specified"
    message = os.getenv("MESSAGE", "www.0x2019.de")

    # render plain text nicely in HTML
    html_text = font.renderText(message)\
            .replace(" ","&nbsp;")\
            .replace(">","&gt;")\
            .replace("<","&lt;")\
            .replace("\n","<br>")

    # use a monospace font so everything lines up as expected
    return "<html><body style='font-family: mono;'>" + html_text + "</body></html>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)
