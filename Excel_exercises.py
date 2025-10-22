import functools
import random
import time
from operator import ifloordiv

import pandas as pd
from pandas import read_excel


def zmierz_czas(func,*args,**kwargs):
    start = time.perf_counter()
    wynik = func(*args,**kwargs)
    stop = time.perf_counter()
    print(f"Metoda {func.__name__} wykonna w {stop - start} s")
    return wynik
class generatino_data_to_excel:

    sciezka = "Dane_Osobowe.xlsx"

    def __init__(self):
        self.wczytaj_imiona()
    def wczytaj_imiona(self):
        try:
            df = pd.read_excel(self.sciezka)
            self.meskie = df["meskie"].dropna().values
            self.damskie = df["damskie"].dropna().values
            self.nazwiska_m = df["nazwiska_m"].dropna().values
            self.nazwiska_d = df["nazwiska_d"].dropna().values
            self.miasta = df["miasto"].dropna().values
        except Exception as e:
            print(f"Błąd odczytu pliku:{e}")
            return None
    def dane_osobowe(self,ile,plec):
        """
        Metoda losuje imiona i nazwiska z pliku źródłowego i zapisuje pliki w słowniku.

        :param ile: Liczna par do generowania
        :param plec: 'm' - męskie lub 'd' - damksie
        :return: zwrócenie Slownika z listami wylosowanych imion z nazwkisami
        """
        if plec.lower() == "m":
            imiona = random.choices(self.meskie,k=ile)
            nazwiska = random.choices(self.nazwiska_m, k=ile)
        elif plec.lower() == "d":
            imiona = random.choices(self.damskie,k=ile)
            nazwiska = random.choices(self.nazwiska_d, k=ile)
        else:
            raise ValueError ("Płeć musi być m lub d")

        wylosowane_miasta = random.choices(self.miasta, k=ile)
        #print(wylosowane_miasta)

        wynik = {
            'Imiona':imiona,
            'Nazwiska': nazwiska,
            'Miasto': wylosowane_miasta
        }
        df = pd.DataFrame(wynik)
        df.to_excel("Wynik_losowania.xlsx", index = False,sheet_name = "Dane")
        return self

    def zapis_testowy_txt(self):
        """
        Metoda do sprawdzania pobieranych danych do metod zawartych w klasie.
        separatorem będzie ';', nazwa pliku to będzie 'test'
        :return:
        """
        separator = "; "
        #Wczytaj dane z Excela
        df = pd.read_excel(self.sciezka)
        nazwa_pliku = "Test.txt"

        df.to_csv(nazwa_pliku,sep = separator, index=False, encoding='utf-8')
pass



if __name__ == "__main__":
    # start = time.perf_counter()
    # a = generatino_data_to_excel()
    # stop = time.perf_counter()
    # print(f"Pomiar czasu wynosi {stop - start}")
    # zmierz_czas(a.dane_osobowe,100,'m')
    # #a.zapis_testowy_txt()

    Test = (element
            for element in pd.read_excel("Dane_Osobowe.xlsx"))
    print(Test)
