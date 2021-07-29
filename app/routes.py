from flask import render_template, flash, redirect, url_for

from app import app, db
from app.forms import LoginForm, Clients
from database.models import Clients


@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.html",
        title="Home",
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/insert-data", methods=["GET", "POST"])
def insert_data():
    form = Clients()
    if form.validate_on_submit():
        client = Clients(
            name=form.name.data,
            surname=form.surname.data,
        )
        db.session.add(client)
        db.session.commit()
    return render_template("insert_data.html", title="Inserting", form=form)
