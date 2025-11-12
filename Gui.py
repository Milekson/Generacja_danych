from tkinter.ttk import Label
import Excel_exercises
import customtkinter as ctk



class Main_Frame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        """++++++++++++++++++++++++++ Header_1 ++++++++++++++++++++++++++++++"""
        header_label = ctk.CTkLabel(
            self,
            text="Generator danych osobowych",
            font=("Arial", 20, "bold")
        )
        header_label.pack(pady=(20,10))
        """+++++++++++++ Secend_Frame_Class +++++++++++++"""
        secend_Frame = Secend_Frame(self)

class Secend_Frame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(fill="both", expand=True,padx=10,pady=10)
        """++++++++++ Choisce_Gender_Lable ++++++++++"""
        self.Generation_Lable = ctk.CTkLabel(
            self,
            text="Wybierz płeć",
            font=("Ariel",15,"bold")
        )
        self.Generation_Lable.pack(pady=(2,2))
        """+++++++++++++++ Gender_ComboBox ++++++++++++++++++"""
        self.Gender_ComboBox = ctk.CTkComboBox(
            self,
            values= ["Męskie","Damskie","Mieszane"],
            font=("Ariel",12),
            state="readonly"
        )
        self.Gender_ComboBox.pack(pady=(2,5))
        self.Gender_ComboBox.set("Wybierz")
        """++++++++++ how_many_lable ++++++++++++++"""
        self.How_Many_Lable = ctk.CTkLabel(
            self,
            text = "Podaj liczbę danych",
            font = ("Ariel",15,"bold")
        )
        self.How_Many_Lable.pack(pady=(2,2))
        """+++++++++++ How_Many_Entry ++++++++++++++"""
        self.How_Many_Entry = ctk.CTkEntry(
            self,
            placeholder_text="Podaj liczbę",
            font=("Ariel",12),
            width=100
        )
        self.How_Many_Entry.pack(pady=(2,2))
        """+++++ Name_Of_file_lable ++++++++++"""
        self.Name_Of_File_Lable = ctk.CTkLabel(
            self,
            text="Podaj nazwę pliku",
            font=("Ariel",15,"bold")
        )
        self.Name_Of_File_Lable.pack(pady=(2,2))
        """++++++++ Name_Of_File_Entry ++++++++++"""
        self.Name_Of_File_Entry = ctk.CTkEntry(
            self,
            placeholder_text=" Pod jaką nazwą zpisać plik",
            font=("Ariel",12),
            width= 170
        )
        self.Name_Of_File_Entry.pack(pady=(2,2))
        """++++++++ accept_button ++++++++++"""
        self.Accept_button = ctk.CTkButton(
            self,
            width= 80,
            text = "Generuj",
            font=("Ariel",12),
            command=self.Button_event
        )
        self.Accept_button.pack(pady=(15,2))



    def Button_event(self):
        self.selected_gender = self.Gender_ComboBox.get()
        if self.selected_gender == "Męskie":
            print(type(self.selected_gender))
            self.selected_gender="m"
            print(type(self.selected_gender))
        elif self.selected_gender =="Damskie":
            self.selected_gender="d"
        elif self.selected_gender == "Mieszane":
            self.selected_gender="mix"
        elif self.selected_gender == "Wybierz":
            print("Nie wybrałeś, dane będą mieszane")
            self.selected_gender="mix"
        how_many = int(self.How_Many_Entry.get())

        Name_File=self.Name_Of_File_Entry.get()

        Generation = Excel_exercises.generatino_data_to_excel()

        Generation.dane_osobowe(how_many,self.selected_gender,Name_File)

        




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Generator do Excela")

        self.mainFrame = Main_Frame(self)
        self.mainFrame.pack(fill="both",expand=True,padx=10,pady=10)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")




if __name__ == "__main__":
    apka = App()
    apka.mainloop()