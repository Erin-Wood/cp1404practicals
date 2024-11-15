from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    pass


class BoxLayoutDemoApp(App):
    def build(self):
        return MyBoxLayout()

    def handle_greet(self):
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


if __name__ == '__main__':
    BoxLayoutDemoApp().run()
