from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    def on_login(self):
        # A verificação self.ids é adicionada aqui para garantir que os widgets estejam construídos
        if hasattr(self.ids, 'username_input') and hasattr(self.ids, 'password_input'):
            username = self.ids.username_input.text
            password = self.ids.password_input.text

            # Verifica o nome de usuário e a senha e navega para a tela do menu se forem válidos
            if username == 'admin' and password == 'admin':
                self.manager.current = 'menu'
    def sair(self, *args):
        self.manager.current = 'login'
        
class MenuWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MenuApp(App):
    def build(self):
        sm = ScreenManager()
        login_screen = LoginScreen(name='login')
        menu_screen = Screen(name='menu')
        menu_window = MenuWindow() 
        menu_screen.add_widget(menu_window)
        sm.add_widget(login_screen)
        sm.add_widget(menu_screen)
        return sm
    
    def sair(self):
        self.root.current = 'login'
    
if __name__ == '__main__':
    MenuApp().run()
