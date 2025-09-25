import ui


class WelcomeView (ui.View):
  
  def did_load(self):
    self.welcome_lbl = self['welcome_lbl']
    
  def init(self, user):
    self.welcome_lbl.text = f"Welcome to Dragon's Share, {user}!"
  
  @staticmethod
  def load_view(user):
    v = ui.load_view()
    v.init(user)
    return v

