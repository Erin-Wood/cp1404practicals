from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("convertmileskm.kv")

MILES_TO_KM = 1.60934


class ConvertLayout(BoxLayout):
    pass


class ConvertMilesKmApp(App):
    km_output = StringProperty("0.0 km")

    def build(self):
        print("Building the app...")
        return ConvertLayout()

    def update_km_output(self, miles, MILES_TO=None):
        print(f"Updating km output with miles={miles}")  # Debug statement
        if MILES_TO is None:
            MILES_TO = MILES_TO_KM

        try:
            miles = float(miles)
            km = miles * MILES_TO
            self.km_output = f"{km:.2f} km"
        except ValueError:
            print("Invalid input for miles; setting km_output to 0.0 km")
            self.km_output = "0.0 km"

    def increase_miles(self):
        miles = self.get_miles_input() + 1
        print(f"Increasing miles to {miles}")
        self.set_miles_input(miles)
        self.update_km_output(miles)

    def decrease_miles(self):
        miles = self.get_miles_input() - 1
        print(f"Decreasing miles to {miles}")
        self.set_miles_input(miles)
        self.update_km_output(miles)

    def get_miles_input(self):
        try:
            return float(self.root.ids.miles_input.text)
        except ValueError:
            print("Invalid input; assuming 0.0 miles")
            return 0.0

    def set_miles_input(self, miles):
        self.root.ids.miles_input.text = str(int(miles))

    def on_miles_input(self, *args):
        self.update_km_output(self.root.ids.miles_input.text)


if __name__ == '__main__':
    ConvertMilesKmApp().run()
