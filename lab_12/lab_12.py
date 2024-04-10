from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton, ControlTextArea
from electron import Electron
from neitron import Neitron
from proton import Proton

from report import save_to_docx, save_to_xlsx

class ParticlePropertiesCalculator(BaseWidget):
    def __init__(self):
        super().__init__('Particle Properties Calculator')

<<<<<<< HEAD
        self._electron_btn = ControlButton('Расчёт Электрон')
        self._neitron_btn = ControlButton('Расчёт Нейтрон')
        self._proton_btn = ControlButton('Расчёт Протон')

        self._output_area = ControlTextArea('результат')

        self._electron_btn.value = self._calculate_electron_properties
        self._neitron_btn.value = self._calculate_neutron_properties
        self._proton_btn.value = self._calculate_proton_properties

        self._save_docx_btn = ControlButton('Охранить .docx')
        self._save_xlsx_btn = ControlButton('Сохранить .xlsx')

        self._save_docx_btn.value = self._save_to_docx
        self._save_xlsx_btn.value = self._save_to_xlsx
=======
def calculate_button_callback(self):
        pass

    def save_to_doc(self):
        pass

    def save_to_xls(self):
        pass

        with dpg.window(label="Storage Device Selector"):
            dpg.add_text("Select Storage Device:")
            dpg.add_checkbox("HDD")
            dpg.add_checkbox("SSD")
            dpg.add_checkbox("Flash")
>>>>>>> 14c300a830963c253dc601ee14d89ffadfb5e1cb

        self.formset = [
            ('_electron_btn', '_neitron_btn', '_proton_btn'),
            '_output_area',
            ('_save_docx_btn', '_save_xlsx_btn')
        ]

    def _calculate_electron_properties(self):
        e = Electron.electron()
        specific_charge = e.specific_charge()
        compton_wavelength = e.compton_wavelength()
        self._output_area.value += f'Электрон Расчёт удельного заряда: {specific_charge}\n'
        self._output_area.value += f'комптоновской длины волны: {compton_wavelength}\n\n'

    def _calculate_neutron_properties(self):
        n = Neitron.neitron()
        specific_charge = n.specific_charge()
        compton_wavelength = n.compton_wavelength()
        self._output_area.value += f'Нейтрон Расчёт удельного заряда: {specific_charge}\n'
        self._output_area.value += f'комптоновской длины волны: {compton_wavelength}\n\n'

    def _calculate_proton_properties(self):
        p = Proton.proton()
        specific_charge = p.specific_charge()
        compton_wavelength = p.compton_wavelength()
        self._output_area.value += f'Протон Расчёт удельного заряда: {specific_charge}\n'
        self._output_area.value += f'комптоновской длины волны: {compton_wavelength}\n\n'

    def _save_to_docx(self):
        save_to_docx(self._output_area.value)

    def _save_to_xlsx(self):
        save_to_xlsx(self._output_area.value)

if __name__ == '__main__':
    from pyforms import start_app
    start_app(ParticlePropertiesCalculator)
