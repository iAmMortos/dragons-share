import flaskr
import ui
import signal
from flask import current_app
from flaskr.db import init_db

DO_INIT = False

def signal_handler(sig, frame):
  print('Shutting down gracefully...')
  sys.exit(0)
  
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def launch_background_app():
  app = flaskr.create_app()
  with app.app_context():
    if DO_INIT:
      init_db()
    app.run(use_reloader=False, debug=True, port=5001)

if __name__ == '__main__':
  launch_background_app()
