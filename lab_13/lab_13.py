import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from electron import Electron
from neitron import Neitron
from proton import Proton
from docx import Document

class Calculator(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.output_area = toga.MultilineTextInput(readonly=True, style=Pack(flex=1))

        electron_button = toga.Button('Рассчитать свойства электрона', on_press=self.calculate_electron, style=Pack(padding=5))
        neitron_button = toga.Button('Рассчитать свойства нейтрона', on_press=self.calculate_neitron, style=Pack(padding=5))
        proton_button = toga.Button('Рассчитать свойства протона', on_press=self.calculate_proton, style=Pack(padding=5))

        button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        button_box.add(electron_button)
        button_box.add(neitron_button)
        button_box.add(proton_button)

        main_box.add(button_box)
        main_box.add(self.output_area)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def calculate_electron(self, widget):
        particle = Electron()
        self.display_results(particle)

    def calculate_neitron(self, widget):
        particle = Neitron()
        self.display_results(particle)

    def calculate_proton(self, widget):
        particle = Proton()
        self.display_results(particle)

    def display_results(self, particle):
        specific_charge = particle.specific_charge()
        compton = particle.compton()
        result_text = f"Удельный заряд {particle.__class__.__name__}: {specific_charge:.2e} Кл/кг\nКомптоновская длина: {compton:.2e} м"
        self.output_area.value = result_text
        doc = Document()
        doc.add_paragraph(result_text)
        doc.save(f'{particle.__class__.__name__.lower()}.doc')

def main():
    return Calculator('Particle Calculator', 'org.example.particlecalculator')

if __name__ == '__main__':
    main().main_loop()
