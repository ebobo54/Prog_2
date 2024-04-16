from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton, ControlTextArea
from electron import Electron
from neitron import Neitron
from proton import Proton
from docx import Document

class ParticlePropertiesCalculator(BaseWidget):
    def __init__(self):
        super().__init__('Калькулятор свойств частиц')

        self._electron_button = ControlButton('Рассчитать свойства электрона', default=self.calculate_electron_properties)
        self._neitron_button = ControlButton('Рассчитать свойства нейтрона', default=self.calculate_neitron_properties)
        self._proton_button = ControlButton('Рассчитать свойства протона', default=self.calculate_proton_properties)

        self._output_area = ControlTextArea('Результаты')

        self.formset = [('_electron_button', '_neitron_button', '_proton_button', ), '_output_area']

    def calculate_electron_properties(self):
        particle = Electron()
        specific_charge = particle.specific_charge()
        compton_wavelength = particle.calculate_compton_wavelength()
        result_text = f"Удельный заряд электрона: {specific_charge:.2e} Кл/кг\nКомптоновская длина волны: {compton_wavelength:.2e} м"
        self._output_area.value = result_text

        doc = Document()
        doc.add_paragraph(result_text)
        doc.save('proton_properties.doc')

    def calculate_neitron_properties(self):
        particle = Neitron()
        specific_charge = particle.specific_charge()
        compton_wavelength = particle.calculate_compton_wavelength()
        result_text = f"Удельный заряд электрона: {specific_charge:.2e} Кл/кг\nКомптоновская длина волны: {compton_wavelength:.2e} м"
        self._output_area.value = result_text

        doc = Document()
        doc.add_paragraph(result_text)
        doc.save('proton_properties.doc')

    def calculate_proton_properties(self):
        particle = Proton()
        specific_charge = particle.specific_charge()
        compton_wavelength = particle.calculate_compton_wavelength()
        result_text = f"Удельный заряд электрона: {specific_charge:.2e} Кл/кг\nКомптоновская длина волны: {compton_wavelength:.2e} м"
        self._output_area.value = result_text

        doc = Document()
        doc.add_paragraph(result_text)
        doc.save('proton_properties.doc')

if __name__ == "__main__":
    from pyforms import start_app
    start_app(ParticlePropertiesCalculator)

