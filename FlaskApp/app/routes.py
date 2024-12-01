from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


# about page
@main.route("/about")
def about():
	return "<h1>Welcome to the About Page!</h1>"


# example of path parameter
@main.route("/welcome/<name>")
def welcome(name):
	return f"<h1>Hi {name.title()}, you're welcome to this Page!</h1>"


# example of integer path parameter
@main.route("/addition/<int:num>")
def addition(num):
	return f"<h1>Input is {num}, Output is {num + 10}</h1>"


# example of two integer path parameters
@main.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1, num2):
	return f"<h1>{num1} + {num2} is {num1 + num2}</h1>"