from flask import render_template

def render_mainpage(notes):
    return render_template('index.html', notes=notes)