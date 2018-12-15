from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
import json
import requests


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    #def on_enter(self):

    def search_location(self):
        global urlresults
        print("1")
        search_temp = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=04000e5990ae9f47fcde912d52a0890b"
        search_url = search_temp.format(self.search_input.text)
        urlresults = (requests.get(search_url)).json()
        print(urlresults)
        if int(urlresults['cod']) == 404:
            self.search_results.item_strings = ['Non Existent']
        else:
            self.found_location(urlresults)

    def found_location(self, data):
        print('123')
        #self.search_result.item_strings = []
        city = [data['name'], data['sys']['country']]
        data['main']['temp'] = data['main']['temp'] - 273
        data['main']['temp_min'] = data['main']['temp_min'] - 273
        data['main']['temp_max'] = data['main']['temp_max'] - 273
        climate = [(k,str(v)) for k,v in data['main'].items()]
        print(climate)
        print(city)
        city.extend(climate)
        self.search_results.item_strings = [str(i) for i in city]
        #if self.search_results.item_strings[0]!='Non Existent' :

        print(self.search_results.item_strings)


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()