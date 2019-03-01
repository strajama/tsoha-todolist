from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.tags.models import Tag
from application.tags.forms import TagForm, EditTagForm

@app.route("/tags", methods=["GET"])
def tags_index():
    return render_template("tags/list.html", tags = Tag.query.order_by("name").limit(100).all())

@app.route("/tags/new/")
@login_required(role='admin')
def tags_form():
    return render_template("tags/new.html", form=TagForm())

@app.route("/tags/", methods=["POST"])
@login_required(role='admin')
def tags_create():
    form = TagForm(request.form)

    if not form.validate():
        return render_template("tags/new.html", form = form)

    tag = Tag(form.name.data)

    db.session().add(tag)
    db.session().commit()
  
    return redirect(url_for("tags_index"))

@app.route("/tags/edit/<tag_id>/", methods=["GET"])
@login_required(role='admin')
def tags_edit(tag_id):
    return render_template("tags/edit.html", tag_id = tag_id, form = EditTagForm(), tag=Tag.query.get(tag_id))

@app.route("/tags/edit/<tag_id>/", methods=["POST"])
@login_required(role='admin')
def tags_editor(tag_id):
    
    form = EditTagForm(request.form)
    tag = Tag.query.get(tag_id)

    if not form.validate:
        return render_template("tags/new.html", form = form)

    if form.name.data:
        if not Tag.unique_name(form.name.data):
            tag.name = form.name.data

    db.session().commit()

    return redirect(url_for("tags_edit", tag_id = tag_id))

@app.route("/tags/<tag_id>/", methods=["POST"])
@login_required(role='admin')
def tags_delete(tag_id):
    tag = Tag.query.get(tag_id)

    db.session.delete(tag)
    db.session().commit()
  
    return redirect(url_for("tags_index"))