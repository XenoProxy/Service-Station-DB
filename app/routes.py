from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm
from database.connection import get_connection as conn


@app.route("/")
@app.route("/index")
def index():
    connection = conn()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("EXPLAIN `Auto`;")
            structure = cursor.fetchall()
            return render_template(
                "index.html",
                title="Home",
                structure=structure
            )


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            'Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
