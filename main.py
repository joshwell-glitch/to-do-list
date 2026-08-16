import customtkinter as ctk
from tkinter import messagebox
from settings_manager import *
from tasks_manager import *
import json
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.settings_manager = SettingsManager()
        self.tasks_manager = TasksManager()
        self.settings = self.settings_manager.load_settings()
        ctk.set_appearance_mode(self.settings["appearance"])
        ctk.set_default_color_theme(self.settings["color_theme"])
        self.title(APP_TITLE)
        self.geometry("400x500")
        self.resizable(False, False)
        self.iconbitmap(ICONPATH)
        self.task_id = 1

        # MAIN MENU FRAME:
        self.frame = ctk.CTkFrame(master=self,
                                  width=250,
                                  height=300)
        self.frame.place(relx=0.5,
                         rely=0.5,
                         anchor='center')
        self.frame.propagate(False)

        # MAIN MENU TITLE:
        self.title = ctk.CTkLabel(master=self.frame,
                                  text="To-Do List",
                                  font=DEFAULT_TITLE_FONT)
        self.title.place(relx=0.5,
                         rely=0.1,
                         anchor='n')

        # SETTINGS BUTTON:
        self.settings_button = ctk.CTkButton(master=self,
                                      text="Settings",
                                      font=DEFAULT_FONT,
                                      height=30,
                                      width=30,
                                      command=self.handle_settings)
        self.settings_button.place(relx=0.830,
                                   rely=0.010)

        # ADD TASK BUTTON:
        self.add_button = ctk.CTkButton(master=self.frame,
                                        text="Add Task",
                                        font=DEFAULT_FONT,
                                        command=self.open_add_task)
        self.add_button.place(relx=0.5,
                              rely=0.350,
                              anchor='center')

        # VIEW TASK BUTTON:
        self.view_button = ctk.CTkButton(master=self.frame,
                                         text="View Tasks",
                                         font=DEFAULT_FONT, 
                                         command=self.open_view_tasks)
        self.view_button.place(relx=0.5, 
                               rely=0.475, 
                               anchor='center')

        # EDIT TASK BUTTON:
        self.edit_button = ctk.CTkButton(master=self.frame, 
                                         text="Edit Task", 
                                         font=DEFAULT_FONT, 
                                         command=self.edit_tasks)
        self.edit_button.place(relx=0.5, 
                               rely=0.6,
                               anchor='center')

        # DELETE TASK BUTTON:
        self.delete_button = ctk.CTkButton(master=self.frame, 
                                         text="Delete Task", 
                                         font=DEFAULT_FONT, 
                                         command=self.delete_tasks)
        self.delete_button.place(relx=0.5, 
                               rely=0.725, 
                               anchor='center')

        #VERSION LABEL:
        self.bottom_label = ctk.CTkLabel(master=self, 
                                         text="Version 1.0", 
                                         font=DEFAULT_FONT)
        self.bottom_label.pack(anchor='sw', 
                               padx=12,
                               expand=True)

        self.info_label = ctk.CTkLabel(master=self,
                                        text="Restart the application to load changes.",
                                        font=DEFAULT_FONT)

    # ADD TASK:
    def open_add_task(self):
        self.settings_button.place_forget()
        self.frame.place_forget()

        # ADD TASK FRAME:
        self.add_task_frame = ctk.CTkFrame(master=self,
                                           height=400,
                                           width=350)
        self.add_task_frame.place(relx=0.5,
                                  rely=0.5,
                                  anchor='center')

        # ADD TASK TITLE:
        self.add_task_title = ctk.CTkLabel(master=self.add_task_frame,
                                           text='Add Task',
                                           font=DEFAULT_TITLE_FONT)
        self.add_task_title.place(relx=0.5, 
                                  rely=0.1,
                                  anchor='center')

        #NAME OF TASK ENTRY:
        self.name_of_task_entry = ctk.CTkEntry(master=self.add_task_frame,
                                               width=300,
                                               placeholder_text='Task Name...',
                                               font=DEFAULT_FONT,
                                               border_color='',
                                               fg_color="#222222")
        self.name_of_task_entry.place(relx=0.5,
                                      rely=0.225,
                                      anchor='center')

        # DESCRIPTION OF TASK:
        self.add_task_textbox = ctk.CTkTextbox(master=self.add_task_frame,
                                             font=DEFAULT_FONT,
                                             height=175,
                                             width=300,
                                             border_color='',
                                             activate_scrollbars= True)
        self.add_task_textbox.place(relx=0.5,
                                    rely=0.5,
                                    anchor='center')

        # ADD NEW TASK BUTTON:
        self.add_task_button = ctk.CTkButton(master=self.add_task_frame,
                                    text='Add Task',
                                    font=DEFAULT_FONT,
                                    command=self.add_new_task)
        self.add_task_button.place(relx=0.5,
                          rely=0.8,
                          anchor='center')

        # CLOSE ADD TASK BUTTON:
        self.close_add_task_button = ctk.CTkButton(master=self.add_task_frame,
                                    text='Cancel',
                                    font=DEFAULT_FONT,
                                    command=self.close_add_task)
        self.close_add_task_button.place(relx=0.5,
                          rely=0.9,
                          anchor='center')

    def add_new_task(self):
        task_name = self.name_of_task_entry.get()
        task_description = self.add_task_textbox.get("0.0", "end-1c")

        task = {"id": self.task_id,
                "name": task_name,
                "description": task_description,
                "completed": 0}

        self.tasks_manager.save_task(task)
        self.task_id += 1
        self.close_add_task()

    def close_add_task(self):
        self.add_task_frame.place_forget()
        self.frame.place(relx=0.5,
                         rely=0.5,
                         anchor='center')
        self.settings_button.place(relx=0.830,
                                   rely=0.010)

    # VIEW TASKS:
    def open_view_tasks(self):
        self.settings_button.place_forget()
        self.frame.place_forget()
        self.loaded_tasks = self.tasks_manager.load_task()

        # VIEW TASKS FRAME:
        self.view_tasks_frame = ctk.CTkFrame(master=self,
                                             height=400,
                                             width=350)
        self.view_tasks_frame.place(relx=0.5,
                                    rely=0.5,
                                    anchor='center')

        # VIEW TASKS TITLE:
        self.view_tasks_label = ctk.CTkLabel(master=self.view_tasks_frame,
                                             text='View Tasks',
                                             font=DEFAULT_TITLE_FONT)
        self.view_tasks_label.place(relx=0.5,
                                    rely=0.1,
                                    anchor='center')

        # VIEWS TASKS SCROLLABLE FRAME:
        self.scrollable_frame_view_task = ctk.CTkScrollableFrame(master=self.view_tasks_frame,
                                                                 label_font=DEFAULT_FONT,
                                                                 height=250,
                                                                 width=300)
        self.scrollable_frame_view_task.place(relx=0.5,
                                              rely=0.5,
                                              anchor='center')

        no_task = 0
        for task in self.loaded_tasks:
            checked_int = task["completed"]
            id_status = task["id"]
            print(f"{no_task}")
            self.label_task = ctk.CTkCheckBox(master=self.scrollable_frame_view_task,
                                              text=f"{task["name"]} : {task["description"]}",
                                              font=DEFAULT_FONT,
                                              command=lambda: self.check(no_task))
            self.label_task.pack(pady=3,
                                 anchor='w')
            no_task += 1

        #VIEW TASKS BACK BUTTON:
        self.close_view_tasks_button = ctk.CTkButton(master=self.view_tasks_frame,
                                                     text='Back',
                                                     font=DEFAULT_FONT,
                                                     command=self.close_view_tasks)
        self.close_view_tasks_button.place(relx=0.5,
                                         rely=0.925,
                                         anchor='center')

    def check(self, num):
        checked = self.loaded_tasks[0]["completed"]
        if num == self.loaded_tasks[0]["id"]:
            print(f"Task is: {self.loaded_tasks["id"]}")
            if checked != 0:
                print(f'true - variable: {checked}')
            else:
                print(f'false - variable: {checked}')
        self.tasks_manager.save_task(self.loaded_tasks)

    def close_view_tasks(self):
        self.view_tasks_frame.place_forget()
        self.frame.place(relx=0.5,
                         rely=0.5,
                         anchor='center')
        self.settings_button.place(relx=0.830,
                                   rely=0.010)

    def edit_tasks(self):
        print("Editing Task!")

    def delete_tasks(self):
        print("Deleting Tasks!")

        # HANDLE SETTINGS INPUT:.
    def handle_settings(self):
        if self.settings_button._text == 'Settings':
            self.open_settings()
        else:
            self.close_settings()

        # OPEN SETTINGS AFTER HANDLE INPUT:
    def open_settings(self):

        # SETTINGS FRAME:
        self.settings_frame = ctk.CTkFrame(master=self, 
                                           height=300, 
                                           width=250)
        self.settings_frame.place(relx=0.5, 
                                  rely=0.5, 
                                  anchor='center')
        # configures the settings_button after input.
        self.settings_button.configure(text='Main Menu')
        self.settings_button.place_configure(relx=0.800)

        self.frame.place_forget()

        # INFO:
        self.created_by = ctk.CTkLabel(master=self.settings_frame,
                                     text="Created by: Joshwell\n Created in: August 12, 2026",
                                     font=DEFAULT_FONT)
        self.created_by.place(relx=0.5, 
                            rely=0.30,
                            anchor='center')

        # SETTINGS TITLE LABEL:
        self.settings_label = ctk.CTkLabel(master=self.settings_frame, 
                                           text='Settings', 
                                           font=DEFAULT_TITLE_FONT,
                                           anchor='center')
        self.settings_label.place(relx=0.5,
                                  rely=0.150,
                                  anchor='center')

        
        # change_theme_var is a BooleanVar() from CTkinter, it is a data type for this library.
        self.change_appearance_var = ctk.BooleanVar()
        self.current_appearance = ctk.get_appearance_mode()
        if self.current_appearance == "Light":
            self.change_appearance_var.set(value=False)
        if self.current_appearance == "Dark":
            self.change_appearance_var.set(value=True)

        #DARK THEME MODE SWITCH:
        self.change_theme_switch = ctk.CTkSwitch(master=self.settings_frame, 
                                                 text='Dark Mode', 
                                                 font=DEFAULT_FONT,
                                                 command=self.edit_theme,
                                                 variable=self.change_appearance_var)
        self.change_theme_switch.place(relx=0.5, 
                                       rely=0.450, 
                                       anchor='center')

        # LABEL FOR COLOR SLIDER:
        self.change_color_label = ctk.CTkLabel(master=self.settings_frame, 
                                               text=self.settings["name_color"], 
                                               font=DEFAULT_FONT,)
        self.change_color_label.place(relx=0.5, 
                                      rely=0.550, 
                                      anchor='center')

         # COLOR CHANGER SLIDER:
        self.change_color_slider = ctk.CTkSlider(master=self.settings_frame, 
                                                 from_=0,
                                                 to=2,
                                                 command=self.change_color,
                                                 number_of_steps=2,
                                                 width=150)
        self.change_color_slider.place(relx=0.5, 
                                       rely=0.600, 
                                       anchor='center')
        self.change_color_slider.set(self.settings["number_color"])


         # DELETE ALL TASK BUTTON:
        self.delete_all_task_button = ctk.CTkButton(master=self.settings_frame,
                                          text='Delete All Tasks',
                                          font=DEFAULT_FONT,
                                          command=self.delete_all_task)
        self.delete_all_task_button.place(relx=0.5,
                                rely=0.725,
                                anchor='center')


        # DEFAULT SETTINGS BUTTON:
        self.default_settings_button = ctk.CTkButton(master=self.settings_frame,
                                          text='Default Settings',
                                          font=DEFAULT_FONT,
                                          command=self.default)
        self.default_settings_button.place(relx=0.5,
                                rely=0.850,
                                anchor='center')

        
    # EDIT APPEARANCE SWITCH FUNCTION:
    def edit_theme(self):

        if self.change_appearance_var.get() == True:
            appearance = "Dark"
        else:
            appearance = "Light"

        ctk.set_appearance_mode(appearance)

        self.settings["appearance"] = appearance
        self.settings_manager.save_settings(self.settings)


    # CHANGE COLOR SLIDER FUNCTION:
    def change_color(self, value):

        if value == 0.0:
            theme = "blue"
            color = "Blue"
            number = 0.0
            self.change_color_label.configure(text=color)

        elif value == 1.0:
            theme = "dark-blue"
            color = "Dark Blue"
            number = 1.0
            self.change_color_label.configure(text=color)

        elif value == 2.0:
            theme = "green"
            color = "Green"
            number = 2.0
            self.change_color_label.configure(text=color)

        ctk.set_default_color_theme(theme)

        self.settings["name_color"] = color
        self.settings["number_color"] = number
        self.settings["color_theme"] = theme
        self.settings_manager.save_settings(self.settings)
        try:
            self.info_label.place(relx=0.5,
                                 rely=0.9,
                                 anchor='center')
        except AttributeError:
            pass


    # CLOSE SETTINGS FUNCTION:
    def close_settings(self):

        self.frame.place(relx=0.5,
                                 rely=0.5,
                                 anchor='center')
        self.info_label.place_forget()
        self.settings_frame.place_forget()
        self.settings_button.configure(text='Settings')
        self.settings_button.place_configure(relx=0.840)


    # DEFAULT APPEARANCE AND THEME BUTTON:
    def default(self):
        self.erase = os.remove(SETTINGS_PATH)
        with open(SETTINGS_PATH, "w") as file:
            json.dump(DEFAULT_SETTINGS, file)
        ctk.set_appearance_mode(self.settings["appearance"])
        ctk.set_default_color_theme(self.settings["color_theme"])
        try:
            self.info_label.place(relx=0.5,
                                 rely=0.9,
                                 anchor='center')
        except AttributeError:
            pass


    # DELETE ALL TASKS BUTTONS:
    def delete_all_task(self):
        self.task_id = 0
        try:
            os.remove(TASKS)
        except FileNotFoundError:
            messagebox.showinfo(title=APP_TITLE,
                                message='No Tasks to Delete.')
            return
        messagebox.showinfo(title=APP_TITLE,
                            message='Successfully Deleted All Tasks.')



if __name__ == "__main__":
    app = App()
    app.mainloop()