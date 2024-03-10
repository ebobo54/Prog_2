import pyforms
from pyforms.gui.basewidget import BaseWidget
from pyforms.controls import ControlText

class lab_12(BaseWidget):

    def __init__(self):
        super().__init__('Элементарные частицы')

        self._electron = ControlText('Електрон')
        self._neutron = ControlText('Нейтрон')
        self._proton = ControlText('Протон')


if __name__ == "__main__":
    pyforms.start_app(lab_12)
