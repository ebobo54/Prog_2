# gui.py
import dearpygui.dearpygui as dpg

class GUI:
    def __init__(self):
        self.result = None

    def calculate_button_callback(self):
        pass

    def save_to_doc(self):
        pass

    def save_to_xls(self):
        pass

    def show(self):
        with dpg.texture_registry():
            texture_id = dpg.add_texture("my_texture", "../path/to/texture.png")

        with dpg.window(label="Storage Device Selector"):
            dpg.add_text("Select Storage Device:")
            dpg.add_checkbox("HDD")
            dpg.add_checkbox("SSD")
            dpg.add_checkbox("Flash")

            dpg.add_text("Enter Data Volume (GB):")
            dpg.add_input_int("Data Volume (GB)")

            dpg.add_button("Calculate", callback=self.calculate_button_callback)

        dpg.create_context()
        dpg.create_viewport()
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
