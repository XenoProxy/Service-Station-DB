from flask import render_template, flash, redirect, url_for

from app import app, db
from app import forms
from database import models


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
    auto_form = forms.Auto()
    client_form = forms.Clients()
    if client_form.validate_on_submit():
        client = models.Clients(
            name=client_form.name.data,
            surname=client_form.surname.data,
        )
        db.session.add(client)
        db.session.commit()
    if auto_form.validate_on_submit():
        auto = models.Auto(
            vin=auto_form.vin.data,
            number=auto_form.number.data,
            brand=auto_form.brand.data,
            model=auto_form.model.data,
            make=auto_form.make.data,
        )
        db.session.add(auto)
        db.session.commit()
    return render_template("insert_data.html", title="Inserting", form=client_form)
