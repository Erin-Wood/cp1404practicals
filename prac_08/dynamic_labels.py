from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Build


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define the list of names
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        return Builder.load_file("dynamic_labels.kv")

    def on_start(self):
        main_layout = self.root.ids.main
        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)


if __name__ == "__main__":
    DynamicLabelsApp().run()
