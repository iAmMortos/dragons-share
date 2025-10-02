# An entrypoint for app development from PC
import secretpals
import signal
import sys
from secretpals.db import init_db

DO_INIT = False

def signal_handler(sig, frame):
  print('Shutting down gracefully...')
  sys.exit(0)
  
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

app = secretpals.create_app()
with app.app_context():
  if DO_INIT:
    init_db()

def launch_background_app():
  app.run(debug=True, port=5001, host='localhost')

if __name__ == '__main__':
  launch_background_app()
