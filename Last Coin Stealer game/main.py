import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from random import randint
import Global
import time


class MenuScreen(Screen):

    def update(self, player):
        Global.PLAYER = player

    def exitapp(self):
        App.get_running_app().stop()


class FirstScreen(Screen):

    ded_p1 = ObjectProperty()
    p1 = ObjectProperty()
    p2 = ObjectProperty()
    ded_p2 = ObjectProperty()
    slot = ObjectProperty()
    coin = ObjectProperty()
    instruct = ObjectProperty()

    def clearP2(self):
        self.ded_p2.text = ''

    def random_coins(self):
       # print(t.text)
        self.coin.text = str(randint(2,9))
        self.p1.disabled = False
        self.p2.disabled = True
        self.ded_p2.text = ''
        self.ded_p1.text = ''
        Global.CHANCE = ''
        if Global.PLAYER == 'Player 2':
            self.slot.text = 'Player II'
        else:
            self.slot.text = 'DescrierX'

    def ded_coin(self):
        global coin_left
        coin_left = int(self.coin.text)

        if self.ded_p1.text != '':
            deduct = self.ded_p1.text
            Global.CHANCE = 'Player 1'
        elif self.ded_p2.text != '':
            deduct = self.ded_p2.text
            Global.CHANCE = 'Player 2'
        else:
            self.instruct.text = 'pick something appropriate'
            deduct = '0'

        if int(deduct) == 0:
            self.instruct.text = 'U have to pick something..'
        elif not self.ispowerof2(int(deduct)):
            self.instruct.text = 'No. of coins entered is not a power of 2.Please enter again..'
            self.ded_p2.text = ''
        elif int(deduct) > int(coin_left):
            self.instruct.text = 'Aweee...you cant pick more than what is left!'
            self.ded_p2.text = ''
        else:
            coin_left = coin_left - int(deduct)
            if Global.PLAYER == 'Player 2':
                self.p1.disabled = not self.p1.disabled
                self.p2.disabled = not self.p2.disabled
                self.ded_p2.text = ''
            else:
                if coin_left > 1:
                    Global.CHANCE = 'Player 2'
                    if coin_left % 3 == '2':
                        print('in 2')
                        self.ded_p2.text = '2'
                    elif coin_left % 3 == 1:
                        print('in 4')
                        self.ded_p2.text = '4'
                    else:
                        self.ded_p2.text = '2'
                    coin_left = coin_left - int(self.ded_p2.text)
                else:
                    Global.CHANCE = 'Player 1'
                self.p2.disabled = True
                self.p1.disabled = False
            self.ded_p1.text = ''
            self.instruct.text = ''
        self.coin.text = str(coin_left)

        if coin_left < 2:
            #time.sleep(1)
            self.manager.current = 'end_screen'

    def ispowerof2(self,n: int) -> int:
        while (n % 2 != 1):
            if n == 2:
                break
            n = n // 2
        if int(n) == 2:
            return 1
        else:
            return 0


class HelpScreen(Screen):

    help = ObjectProperty()

    def helpgame(self):
        self.help.text = Global.HELP



class EndScreen(Screen):
    win_note = ObjectProperty()

    def exitapp(self):
        App.get_running_app().stop()

    def winner(self):
        if Global.PLAYER == 'Computer' and Global.CHANCE == 'Player 2':
            Global.CHANCE = 'DescrierX'
        self.win_note.text = '{} is the Winnner !!!'.format(Global.CHANCE)


class CoinsGameApp(App):

    def build(self):
        return Builder.load_file('coinsgame.kv')


if __name__ == '__main__':
    CoinsGameApp().run()
