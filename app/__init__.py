import os

from flask import Flask
from model.data_loader import DataLoader
from templater.templater import Templater

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  app.config["data_loader"] = DataLoader("Complete")
  app.config["templater"] = Templater(
    output_type='html', 
    template_dir='model/templates', 
    template_config_path='model/templates/config/template.properties',
    token_config_path='model/templates/config/token.properties')

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  from .routes import main
  app.register_blueprint(main)

  return app
