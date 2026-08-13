import customtkinter as ctk

ctk.set_appearance_mode("system")
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
        self.settings = ctk.CTkButton(master=self.window,
                                      text="Settings",
                                      font=("arial", 12, "bold"),
                                      height=30,
                                      width=30,
                                      command=self.open_settings)
        self.settings.place(relx=0.830,
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

    def open_settings(self):
        self.settings_frame = ctk.CTkFrame(master=self.window, height=400, width=250)
        self.settings_frame.place(relx=0.5, rely=0.5, anchor='center')

if __name__ == "__main__":
    app = App()