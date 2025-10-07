
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
  tmpltr = current_app.config["templater"]
  mnst = dl.get_monster(name)
  if not mnst:
    abort(404)
  
  class BlockPageObj (object):
    pass
  bpobj = BlockPageObj()
  bpobj.title=mnst.name
  with open('templater/templates/html/css/statblock.css') as f:
    bpobj.statblock_style = f.read()
  with open('templater/templates/html/css/statblock_page.css') as f:
    bpobj.page_style = f.read()
    
  bpobj.monsters = []
  bpobj.monsters.append(mnst)
  html = tmpltr.make(bpobj, "statblock_page")
  
  return html
