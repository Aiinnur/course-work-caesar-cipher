import customtkinter as CTk
import tkinter
from PIL import Image
import algorithm


CTk.set_appearance_mode("dark")

class App(CTk.CTk): #Класс с элементами графического интерфейса
    def __init__(self): #Функция автоматического вызова класса
        super().__init__()

        self.geometry("560x470")
        self.title("Caesar's Cipher")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("image.png"), size=(400, 175)) #Создание логотипа
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0,padx=70)

        self.main_frame = CTk.CTkFrame(master=self, fg_color="transparent")  # Создание фрейма
        self.main_frame.grid(row=1, column=0, padx=(20, 20),
                                 sticky="nsew")  # Закрепили фрейм на окне

        self.entry = CTk.CTkEntry(master=self.main_frame, width=400, placeholder_text="Enter your message")
        self.entry.grid(row=0, column=0, padx=(0, 20), pady=(0, 20))
        self.entry.bind("<Button-3>", self.show_context_menu)

        self.models_logo = CTk.CTkLabel(master=self.main_frame, text="Выберите режим:")
        self.models_logo.grid(row=1, column=0, sticky="w")

        self.radio_var_1 = tkinter.IntVar(value=0) #Создание радиокнопок для выбора режима
        self.radio_button_1 = CTk.CTkRadioButton(master=self.main_frame, variable=self.radio_var_1, text="Шифровка",
                                                           value=0)
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.radio_button_2 = CTk.CTkRadioButton(master=self.main_frame, variable=self.radio_var_1, text="Дешифровка",
                                                           value=1)
        self.radio_button_2.grid(row=1, column=0, pady=10, padx=20, sticky="e")

        self.models_logo = CTk.CTkLabel(master=self.main_frame, text="Выберите язык:")
        self.models_logo.grid(row=2, column=0, sticky="w")

        self.radio_var_2 = tkinter.IntVar(value=0) #Создание радиокнопок для выбора языка
        self.radio_button_1 = CTk.CTkRadioButton(master=self.main_frame, variable=self.radio_var_2, text="Русский",
                                                 value=0)
        self.radio_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.radio_button_2 = CTk.CTkRadioButton(master=self.main_frame, variable=self.radio_var_2, text="Английский",
                                                 value=1)
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="e")


        self.btn_generate = CTk.CTkButton(master=self.main_frame, text="Generate", width=100,  # Добавление кнопки генерации
                                          command=self.result)
        self.btn_generate.grid(row=3, column=0, pady=10)

        self.text_field = CTk.CTkEntry(master=self.main_frame, width=400) #Поле для вывода полученного текста
        self.text_field.grid(row=4, column=0, pady=10)
        self.text_field.bind("<Button-3>", self.show_context_menu)

        self.appearance_mode_option_menu = CTk.CTkOptionMenu(master=self.main_frame, #Виджет для изменения цвета
                                                             values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=5, column=0, pady=30)

        self.appearance_mode_option_menu.set("Dark")

    def show_context_menu(self, event):
        context_menu = tkinter.Menu(self, tearoff=0)
        context_menu.add_command(label="Copy", command=self.copy_text)
        context_menu.add_command(label="Paste", command=self.paste_text)
        context_menu.tk_popup(event.x_root, event.y_root)

    def copy_text(self):
        selected_text = self.entry.selection_get()
        self.clipboard_clear()
        self.clipboard_append(selected_text)

    def paste_text(self):
        clipboard_text = self.clipboard_get()
        self.entry.insert("insert", clipboard_text)

    def change_appearance_mode_event(self, new_appearance_mode): #Функция, меняющая цвет фона
        CTk.set_appearance_mode(new_appearance_mode)

    def get_data(self): #Функция, получающая значения радиокнопок
        variables = []
        variables.append(self.radio_var_1.get())
        variables.append(self.radio_var_2.get())
        return variables

    def result(self): #Функция вывода на окно
        self.text_field.delete(0, "end")
        self.text_field.insert(0, algorithm.caesar(text = self.entry.get(), variables=self.get_data()))


if __name__ == "__main__": #Если скрипт запустится, то выполнится
    app = App()
    app.mainloop()


