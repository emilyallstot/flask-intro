from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            !Hi! This is the home page." 
            <a href='/hello'>Click me!</a>
        </body>
    </html>

    """

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet", method="POST">
                <label>What's your name? <input type="text" name="person"></label>
                <input type="submit">
                
                <br>
                <br>

                <label>Select your compliment: 
                <input type="radio" name="AWESOMENESS" value="awesome">Awesome
                <input type="radio" name="AWESOMENESS" value="terrific">Terrific
                <input type="radio" name="AWESOMENESS" value="fantastic">Fantastic
                <input type="radio" name="AWESOMENESS" value="neato">Neato
                <input type="radio" name="AWESOMENESS" value="fantabulous">Fantabulous
                <input type="radio" name="AWESOMENESS" value="wowza">Wowza
                <input type="radio" name="AWESOMENESS" value="oh-so-not-meh">Oh-so-not-meh
                <input type="radio" name="AWESOMENESS" value="brilliant">Brilliant
                <input type="radio" name="AWESOMENESS" value="ducky">Ducky
                <input type="radio" name="AWESOMENESS" value="coolio">Coolio
                <input type="radio" name="AWESOMENESS" value="incredible">Incredible
                <input type="radio" name="AWESOMENESS" value="wonderful">Wonderful
                <input type="radio" name="AWESOMENESS" value="smashing">Smashing
                <input type="radio" name="AWESOMENESS" value="lovely">Lovely
                </label>
            </form>
        </body>
    </html>

    """

@app.route('/greet', methods=['post'])
def greet_person():
    player = request.args.get("person")
    compliment = request.args.get("AWESOMENESS")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
