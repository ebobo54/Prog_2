import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

class lab_12(BaseWidget):

    def __init__(self):
        super().__init__('Элементарные частицы')

        self._electron =ControlText =ControlText('Електрон')
        self._neitron =ControlText =ControlText('Нейтроны')
        self._proton =ControlText =ControlText('Протоны')


    # from pyforms import start_app

if __name__ =="__main__": pyforms.start_app(lab_12)