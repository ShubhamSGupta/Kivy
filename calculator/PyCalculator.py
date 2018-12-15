import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
#from kivy.Button import Button

kivy.require('1.9.0')


class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "error"


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()

