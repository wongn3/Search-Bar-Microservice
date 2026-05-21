# the flask application itself (acting as the bridge between translating 
# our python microservice to our webpage, for web testing.)
# Flask Installation: run "python -m pip install flask" (in case you don't have flask yet)

from flask import Flask, render_template, request
import subprocess   # this built-in feature let flask to run our Resulter.py (microservice) simaltaniusly (as a seperate program)

# set up the flask on web
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template("index.html")

# when user submits the search form, flask will access the given user-input from the html form, and it'll write said input into request.txt.
# in short, this is the user-input + update request.txt section.
@app.route('/search', methods=["POST"])     # matching the calls http call as established in the search web page (index)
def searching():
    user_search = request.form["search"] # (access input from the html form)

    with open("request.txt", "w") as f: # (write it into request)
        f.write(user_search)

    # run the microservice now, directly here.
    # after comparison of user-input search and available matches in the database.txt...
    # ...the result will be written in the respnose.txt...
    subprocess.run(["python", "Resulter.py"])

    # ...once result is in the response.txt, the program read it...
    with open("response.txt", "r") as f:
        result = f.read().strip()

    # ...if no matches, send user to the dusty-pg.html page...
    if (result == "No matches found"):
        return render_template("dusty-pg.html")
    else:
        return render_template(result)     # ...otherwise it works, redirect user to the content page that matches their search.

# for running the Flask server
if __name__ == "__main__":
    app.run(debug=True)

# ====================================================================================
# Execution Order: 
#   > since this flask is just a bridgeway that connects the Resulter.py (microservice) with the web (html)
#     set up in the templates folder, there's no need to switch between terminal for running.
#   > So just run the flaskServer.py, paste the http link in the browser, and begin testing!
#       > available searches can be found in the database.txt
#           > (search title on left, link on right.)

# P.S. DO NOT TOUCH THE DATABASE! (unless adding content options)