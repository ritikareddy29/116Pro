# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Steven" # write your name
    age = "5" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Charlie" # write your name
    age = "38" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Emma" # write your name
    age = "35" # write your age

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Michael" # write your name
    age = "5" # write your age

    return render_template('friend.html' , name = name , age = age)


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
