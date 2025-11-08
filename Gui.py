from tkinter.ttk import Label

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
        self.How_Many_Lable = ctk.CTkEntry(
            self,
            placeholder_text="Podaj liczbę",
            font=("Ariel",12),
            width=100
        )
        self.How_Many_Lable.pack(pady=(2,2))
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
        )
        self.Accept_button.pack(pady=(15,2))

    def Gender_ComboBox_get(self):
        return self.Gender_ComboBox.get()



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

    # def secendert_Frame(self):
    #
    #
    #
    #
    #
    #     secendery_Frame.pack(expand=True,pady=10,padx=10)
    #     """++++++++++++++++++++++++++ Lable_choise +++++++++++++++++++++++++"""
    #     choise_lable = ctk.CTkLabel(
    #         secendery_Frame,
    #         text = "Wybierz płeć zbioru danych",
    #         font= ("Ariel",15,"bold")
    #     )
    #     choise_lable.pack(pady=(0,30))



if __name__ == "__main__":
    apka = App()
    apka.mainloop()