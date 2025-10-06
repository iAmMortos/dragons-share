
from flask import Blueprint, render_template, request, current_app, abort

main = Blueprint("main", __name__)

@main.route("/")
def index():
  query = request.args.get("q", "").lower()
  dl = current_app.config["data_loader"]
  objs = dl.monsters()
  return render_template("index.html", objects=objs, query=query)

# a simple page that says hello
@main.route('/object/<name>')
def object_detail(name):
  dl = current_app.config["data_loader"]
  obj = dl.get_monster(name)
  if not obj:
    abort(404)
  return render_template("detail.html", obj=obj)
