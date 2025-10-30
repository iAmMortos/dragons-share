# An entrypoint for app development
import ui
import app
import sys

STARTING_PAGE = '/'

@ui.in_background
def launch_background_app():
  ds_app = app.create_app()
  
  with ds_app.app_context():
    ds_app.run(use_reloader=False, debug=True, port=5001)      

        
def show_web_browser():
  wv = ui.WebView()
  wv.right_button_items = [
    ui.ButtonItem(image=ui.Image('iob:ios7_arrow_forward_32'), action=lambda t: wv.go_forward()),
    ui.ButtonItem(image=ui.Image('iob:ios7_refresh_empty_32'), action=lambda t: wv.reload()),
    ui.ButtonItem(image=ui.Image('iob:chevron_left_24'), action=lambda t: wv.go_back())]
  wv.present(style='panel')
  wv.load_html(f'''<a href="http://127.0.0.1:5001{STARTING_PAGE}"><h1>Go to app</h1></a>
  <script>window.location.href="http://127.0.0.1:5001{STARTING_PAGE}";</script>''')


if __name__ == '__main__':
  launch_background_app()
  show_web_browser()

