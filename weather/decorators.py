from flask import render_template

def city404(func):
    def wrapper():
        try:
            return func()
        except KeyError:
            return render_template('error.html')
    return wrapper