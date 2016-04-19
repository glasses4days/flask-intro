from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Homepage</title>
      </head>
      <body>
        <p>Hi! This is the home page. Let's <a href="/hello">get started</a>!</p>
      </body>
    </html>
    """

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          You are best described as: <input type="checkbox" name="user-compliment" value="smart">smart
          <input type="checkbox" name="user-compliment" value="dope">dope
          <input type="checkbox" name="user-compliment" value="witty">witty
          <input type="checkbox" name="user-compliment" value="really, really, really good-looking">really, really, really good-looking<br>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    user_compliment = request.args.get("user-compliment")

    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s you're %s and I think you're %s!
      </body>
    </html>
    """ % (player, user_compliment, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
