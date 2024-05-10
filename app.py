import customtkinter as ctk
from PIL import Image


class App(ctk.CTk):
    ZONE_IDS = map(chr, range(ord("I"), ord("W") + 1))

    strength = 512
    frequency = 120
    pulse_width = 330

    def __init__(self):
        super().__init__()

        self.init_window()

        self.title_text = ctk.CTkLabel(
            self, text="JVT Virtual Touch Controller", font=("Arial", 32)
        )
        self.title_text.place(x=500, y=30, anchor="center")

        self.draw_hand_layout()
        self.draw_config_sidebar()

    def on_finger_zone_click(self, zone):
        print("button clicked", zone)

    def change_strength_value(self, value):
        self.strength = int(value)
        self.strength_value.configure(text=self.strength)

    def change_frequency_value(self, value):
        self.frequency = int(value)
        self.frequency_value.configure(text=self.frequency)

    def change_pulse_width_value(self, value):
        self.pulse_width = int(value)
        self.pulse_width_value.configure(text=self.pulse_width)

    def init_window(self):
        self.geometry("1000x800")
        self.resizable(False, False)
        self.title("JVTControl")

        self.canvas = ctk.CTkCanvas(self, width=1000, height=800)
        self.canvas.pack()

    def draw_hand_layout(self):
        self.hand_image = ctk.CTkImage(
            light_image=Image.open("res/hand.png"),
            dark_image=Image.open("res/hand.png"),
            size=(555, 740),
        )
        self.hand_image_label = ctk.CTkLabel(self, image=self.hand_image, text="")
        self.hand_image_label.place(x=20, y=60)

        finger_zones_locations = [
            (484, 333, 36),
            (450, 400, 36),
            (352, 100, 40),
            (348, 180, 44),
            (340, 270, 44),
            (235, 75, 44),
            (240, 170, 44),
            (245, 265, 44),
            (138, 105, 44),
            (150, 195, 44),
            (170, 280, 44),
            (55, 200, 32),
            (72, 270, 32),
            (95, 335, 32),
            (250, 460, 120),
        ]
        finger_zones_locations = [
            (x + 20, y + 60, z) for x, y, z in finger_zones_locations
        ]
        self.hand_zone_buttons = []

        for i, zone_id in enumerate(self.ZONE_IDS):
            self.hand_zone_buttons.append(
                ctk.CTkButton(
                    self,
                    text="",
                    command=lambda zone_id=zone_id: self.on_finger_zone_click(zone_id),
                    corner_radius=0,
                    fg_color="crimson",
                    hover_color="red",
                    border_width=2,
                    border_color="black",
                    width=finger_zones_locations[i][2],
                    height=finger_zones_locations[i][2],
                )
            )
            self.hand_zone_buttons[i].place(
                x=finger_zones_locations[i][0],
                y=finger_zones_locations[i][1],
                anchor="center",
            )

    def draw_config_sidebar(self):
        self.config_frame = ctk.CTkFrame(self, width=380, height=700)
        self.config_frame.place(x=600, y=80)

        self.config_title = ctk.CTkLabel(
            self.config_frame, text="Configuration", font=("Arial", 28)
        )
        self.config_title.place(x=190, y=30, anchor="center")

        # Strength slider
        self.strength_title = ctk.CTkLabel(
            self.config_frame, text="Strength", font=("Arial", 20)
        )
        self.strength_title.place(x=30, y=100, anchor="w")

        self.strength_slider = ctk.CTkSlider(
            self.config_frame,
            width=320,
            from_=0,
            to=1023,
            number_of_steps=1025,
            command=self.change_strength_value,
        )
        self.strength_slider.place(x=30, y=130, anchor="w")

        self.strength_value_from = ctk.CTkLabel(
            self.config_frame, text="0", font=("Arial", 20)
        )
        self.strength_value_from.place(x=30, y=155, anchor="w")

        self.strength_value_to = ctk.CTkLabel(
            self.config_frame, text="1023", font=("Arial", 20)
        )
        self.strength_value_to.place(x=350, y=155, anchor="e")

        self.strength_value = ctk.CTkLabel(
            self.config_frame, text="512", font=("Arial", 20)
        )
        self.strength_value.place(x=190, y=155, anchor="center")

        # Frequency slider
        self.frequency_title = ctk.CTkLabel(
            self.config_frame, text="Frequency", font=("Arial", 20)
        )
        self.frequency_title.place(x=30, y=200, anchor="w")

        self.frequency_slider = ctk.CTkSlider(
            self.config_frame,
            width=320,
            from_=80,
            to=150,
            number_of_steps=71,
            command=self.change_frequency_value,
        )
        self.frequency_slider.set(self.frequency)
        self.frequency_slider.place(x=30, y=230, anchor="w")

        self.frequency_value_from = ctk.CTkLabel(
            self.config_frame, text="80", font=("Arial", 20)
        )
        self.frequency_value_from.place(x=30, y=255, anchor="w")

        self.frequency_value_to = ctk.CTkLabel(
            self.config_frame, text="150", font=("Arial", 20)
        )
        self.frequency_value_to.place(x=350, y=255, anchor="e")

        self.frequency_value = ctk.CTkLabel(
            self.config_frame, text="120", font=("Arial", 20)
        )
        self.frequency_value.place(x=190, y=255, anchor="center")

        # Pulse width slider
        self.pulse_width_title = ctk.CTkLabel(
            self.config_frame, text="Pulse Width", font=("Arial", 20)
        )
        self.pulse_width_title.place(x=30, y=300, anchor="w")

        self.pulse_width_slider = ctk.CTkSlider(
            self.config_frame,
            width=320,
            from_=300,
            to=500,
            number_of_steps=201,
            command=self.change_pulse_width_value,
        )
        self.pulse_width_slider.set(self.pulse_width)
        self.pulse_width_slider.place(x=30, y=330, anchor="w")

        self.pulse_width_value_from = ctk.CTkLabel(
            self.config_frame, text="300", font=("Arial", 20)
        )
        self.pulse_width_value_from.place(x=30, y=355, anchor="w")

        self.pulse_width_value_to = ctk.CTkLabel(
            self.config_frame, text="500", font=("Arial", 20)
        )
        self.pulse_width_value_to.place(x=350, y=355, anchor="e")

        self.pulse_width_value = ctk.CTkLabel(
            self.config_frame, text="330", font=("Arial", 20)
        )
        self.pulse_width_value.place(x=190, y=355, anchor="center")

        self.clear_button = ctk.CTkButton(
            self.config_frame,
            text="Clear Stimulation",
            width=320,
            height=40,
            corner_radius=10,
            fg_color="indian red",
            hover_color="firebrick",
        )
        self.clear_button.place(x=30, y=670, anchor="sw")


app = App()
app.mainloop()
