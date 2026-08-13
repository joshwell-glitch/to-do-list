import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        # Main Window:
        self.window = ctk.CTk()
        self.window.title("To-Do List")
        self.window.geometry("400x500")
        self.window.resizable(False, False)

        # Menu Frame:
        self.frame = ctk.CTkFrame(master=self.window,
                                  width=250,
                                  height=300)
        self.frame.place(relx=0.5,
                         rely=0.5,
                         anchor='center')
        self.frame.propagate(False)

        # Menu Title Label:
        self.title = ctk.CTkLabel(master=self.frame,
                                  text="To-Do List",
                                  font=("arial", 24, "bold"))
        self.title.place(relx=0.5,
                         rely=0.1,
                         anchor='n')

        # Settings Button:
        self.settings_button = ctk.CTkButton(master=self.window,
                                      text="Settings",
                                      font=("arial", 12, "bold"),
                                      height=30,
                                      width=30,
                                      command=self.handle_settings)
        self.settings_button.place(relx=0.830,
                            rely=0.010)

        # Add task button:
        self.add_button = ctk.CTkButton(master=self.frame,
                                        text="Add Task",
                                        font=("arial", 12, "bold"),
                                        command=self.add_task)
        self.add_button.place(relx=0.5,
                              rely=0.350,
                              anchor='center')

        # View tasks button:
        self.view_button = ctk.CTkButton(master=self.frame,
                                         text="View Tasks",
                                         font=("arial", 12, "bold"), 
                                         command=self.view_tasks)
        self.view_button.place(relx=0.5, 
                               rely=0.475, 
                               anchor='center')

        # Edit task button:
        self.edit_button = ctk.CTkButton(master=self.frame, 
                                         text="Edit Task", 
                                         font=("arial", 12, "bold"), 
                                         command=self.edit_tasks)
        self.edit_button.place(relx=0.5, 
                               rely=0.6,
                               anchor='center')

        # Delete task button:
        self.delete_button = ctk.CTkButton(master=self.frame, 
                                         text="Delete Task", 
                                         font=("arial", 12, "bold"), 
                                         command=self.delete_tasks)
        self.delete_button.place(relx=0.5, 
                               rely=0.725, 
                               anchor='center')

        #Bottom label(version):
        self.bottom_label = ctk.CTkLabel(master=self.window, 
                                         text="Version 1.0", 
                                         font=("Arial", 12, "bold"))
        self.bottom_label.pack(anchor='sw', 
                               padx=12,
                               expand=True)

        self.window.mainloop()

    def add_task(self):
        print("Task Added!")

    def view_tasks(self):
        print("Viewing Tasks!")

    def edit_tasks(self):
        print("Editing Task!")

    def delete_tasks(self):
        print("Deleting Tasks!")

    # handle settings function handles the input when opening the settings.
    def handle_settings(self):
        if self.settings_button._text == 'Settings':
            self.open_settings()
        else:
            self.close_settings()

    # open settings when input is detected.
    def open_settings(self):
        # settings frame
        self.settings_frame = ctk.CTkFrame(master=self.window, 
                                           height=400, 
                                           width=250)
        self.settings_frame.place(relx=0.5, 
                                  rely=0.5, 
                                  anchor='center')
        # configures the settings_button after input.
        self.settings_button.configure(text='Main Menu')
        self.settings_button.place_configure(relx=0.800)

        # settings_label.
        self.settings_label = ctk.CTkLabel(master=self.settings_frame, 
                                           text='Settings', 
                                           font=("Arial", 24, "bold"))
        self.settings_label.place(relx=0.5, 
                                  rely=0.1, 
                                  anchor='center')

        # change_theme_var is a BooleanVar() from CTkinter, it is a data type for this library.
        self.change_theme_var = ctk.BooleanVar()
        self.current_theme = ctk.get_appearance_mode()
        if self.current_theme == "Light":
            self.change_theme_var.set(value=False)
        if self.current_theme == "Dark":
            self.change_theme_var.set(value=True)

        #change_theme_switch is a switch for dark mode.
        self.change_theme_switch = ctk.CTkSwitch(master=self.settings_frame, 
                                                 text='Dark Mode', 
                                                 font=("Arial", 12, "bold"),
                                                 command=self.edit_theme,
                                                 variable=self.change_theme_var)
        self.change_theme_switch.place(relx=0.5, 
                                       rely=0.3, 
                                       anchor='center')

        # change color depending on the slider.
        self.change_color_slider = ctk.CTkSlider(master=self.settings_frame, 
                                                 from_=0,
                                                 to=2,
                                                 command=self.change_color,
                                                 number_of_steps=2)
        self.change_color_slider.place(relx=0.5, 
                                       rely=0.9, 
                                       anchor='center')
        self.change_color_slider.set(0)

    # edit_theme function handles the input when you toggle the switch.
    def edit_theme(self):
        self.get_bool = self.change_theme_var.get()
        if self.get_bool == True:
            ctk.set_appearance_mode("Dark")
            print('dark')
        else:
            ctk.set_appearance_mode("Light")
            print('light')

    # change_color is the main function of changing the color.
    def change_color(self, value):
        print(f"The value is: {value}")
        if value == 0.0:
            ctk.set_default_color_theme("blue")
        elif value == 1.0:
            ctk.set_default_color_theme("dark-blue")
        elif value == 2.0:
            ctk.set_default_color_theme("green")

    # close_settings function closes the settings.
    def close_settings(self):
        self.settings_frame.place_forget()
        self.settings_button.configure(text='Settings')
        self.settings_button.place_configure(relx=0.840)

if __name__ == "__main__":
    app = App()