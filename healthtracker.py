from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainLayout(BoxLayout):

    def predict_steps(self):
        try:
            age = int(self.ids.age_input.text)
            weight = float(self.ids.weight_input.text)

            # Basic Health Logic
            if age < 18:
                base_steps = 12000
            elif age < 40:
                base_steps = 10000
            elif age < 60:
                base_steps = 8000
            else:
                base_steps = 6000

            # Adjust based on weight
            if weight > 90:
                base_steps += 2000
            elif weight > 75:
                base_steps += 1000

            self.ids.result_label.text = (
                f"Recommended Steps: {base_steps} steps/day\n"
                f"Target: Maintain Normal Health ✅"
            )

        except:
            self.ids.result_label.text = "Please enter valid numbers ❗"


class HealthTrackerApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    HealthTrackerApp().run()