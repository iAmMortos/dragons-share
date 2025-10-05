
from flask import Blueprint, render_template, request, current_app, abort

main = Blueprint("main", __name__)

@main.route("/")
def index():
  query = request.args.get("q", "").lower()
  dl = current_app.config["data_loader"]
  s = dl.get_stats().replace('\n', '<br/>')
  return f'{s}'

# a simple page that says hello
@main.route('/object/<name>')
def object_detail(name):
  dl = current_app.config["data_loader"]
  return f'A page for {name}!'
