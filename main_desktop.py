# An entrypoint for app development from PC
import sys
import app

def signal_handler(sig, frame):
  print('Shutting down gracefully...')
  sys.exit(0)
  
ds_app = app.create_app()

def launch_background_app():
  with ds_app.app_context():
    ds_app.run(debug=True, port=5001, host='localhost')

if __name__ == '__main__':
  launch_background_app()
