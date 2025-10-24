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
        self.Menu()
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
    def pensja_roczna(self,ile):
        Generation = [element * 12
                      for element in range(10000)
                      if element >= 3000
                      if element % 100 == 0]
        pensja =random.choices(Generation,k=ile)
        return pensja
    def dane_osobowe(self,ile,plec,nazwa_pliku):
        """
        Metoda losuje imiona i nazwiska z pliku źródłowego i zapisuje pliki w słowniku.

        :param nazwa_pliku: Nazwa pliku w którym zapiszemy dane
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
        elif plec.lower() == "mix":
            imiona = []
            nazwiska = []
            for i in range(ile):
                case = random.choice(["m","d"])
                if case == "m":
                    imiona.append(random.choice(self.meskie))
                    nazwiska.append(random.choice(self.nazwiska_m))
                elif case == "d":
                    imiona.append(random.choice(self.damskie))
                    nazwiska.append(random.choice(self.nazwiska_d))


        wylosowane_miasta = random.choices(self.miasta, k=ile)
        pensja = self.pensja_roczna(ile)
        #print(wylosowane_miasta)

        wynik = {
            'Imiona':imiona,
            'Nazwiska': nazwiska,
            'Miasto': wylosowane_miasta,
            'Pensja roczna': pensja
        }
        df = pd.DataFrame(wynik)
        df.to_excel(nazwa_pliku, index = False,sheet_name = "Dane")
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

    def Menu(self):
        """
        Obsługa programu. Menu wyboru rodzaju danych. Do wyboru są Dane męskie, żeńskie lub mieszane określone znakami
        "m" dla mężczyzn, "d" dla kobiet, "mix" dla mieszanych. Ilość potrzebych danych jest określona w liczbach całkowitch
        Nazwa pliku jest wybierana przez użytkownika programu. Po wprowadzaniu danych na koniec jest wykonywana metoda
        dane osobowe.
        :return: plik .xlsx
        """
        print("Witam w programie do generacji danych osobowych do liku excel.")
        ile = int(input("Podaj mi liczbę potrzebnych danych: "))
        print(type(ile))
        while True:
            if type(ile) == int:
                print("Wybierz teraz jakie imiona i nazwiska potrzebujesz")
                plec = input("Męskie - m, Damskie - d, Mieszane - mix: ")
                if plec.lower() in ["m","d","mix"]:
                    nazwa_pliku = input("Dobrze, podaj mi teraz nazwę pliku pod którą mam zapisać dane: ")
                    if not nazwa_pliku.endswith(".xlsx"):
                        nazwa_pliku += ".xlsx"
                    self.dane_osobowe(ile, plec, nazwa_pliku)

                else:
                    plec = input("Nie odpowiedni wybór m - d - mix: ")
                break
            # else:
                # ile = input("Liczna musi być całkowita: ")
pass



if __name__ == "__main__":
    a = generatino_data_to_excel()

