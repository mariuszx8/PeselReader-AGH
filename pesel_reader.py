import re
import datetime  # Data i czas
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def pesel_check(x):  # Sprawdzanie poprawności numeru pesel
    if len(str(x)) == 11:  # Sprawdzenie ilości cyfr
        if re.match('[0-9]{11}$', x):  # Sprawdzanie numeru wyrażeniem regularnym, czy składa się z samych cyfr
            suma = int(x[0]) + (3 * int(x[1])) + (7 * int(x[2])) + (9 * int(x[3])) + int(x[4]) + (3 * int(x[5])) + (
                7 * int(x[6])) + (9 * int(x[7])) + int(x[8]) + (3 * int(x[9])) + int(x[10])
            if suma % 10 != 0:  # Sprawdzenie cyfry kontrolnej (jeśli ostatnia cyfra sumy to 0, numer PESEL ma poprawną cyfrę kontrolną)
                return 0
            else:
                return x  # Jeśli numer pesel jest poprawny zwraca jego wartość, jeśli błędny to zwraca 0
        else:
            return 0
    else:
        return 0


def pesel_plec(x):  # Odczyt płci
    if (int(x[9])) % 2 == 0:  # Dziesiąta cyfra odpowiada za płeć (0,2,4,6,8 kobieta; 1,3,5,7,9 mężczyzna)
        return 'K'
    else:
        return 'M'


def pesel_data(x):  # Odczyt daty urodzenia
    d = str(x[4]) + str(x[5])  # Dzień urodzenia (5. i 6. cyfra)
    r = 0
    if x[2] == '8' or x[2] == '9':  # Odczyt stulecia roku urodzenia
        r = "18"
    if x[2] == '0' or x[2] == '1':
        r = "19"
    if x[2] == '2' or x[2] == '3':
        r = "20"
    r = str(r) + str(x[0]) + str(x[1])  # Doklejenie roku z 1. i 2. cyfry do stulecia
    if int(x[2]) % 2 == 0:  # Odczyt miesiąca urodzenia
        tmp = '0'
    else:
        tmp = '1'
    m = str(tmp) + str(x[3])
    u = str(r) + "." + str(m) + "." + str(d)  # Połączenie pełnej daty urodzenia
    return u


def date_check(data):  # Sprawdzanie poprawności daty urodzenia
    try:
        d = datetime.datetime.strptime(data, '%Y.%m.%d')  # Jeśli zostanie zwrócony ValueError znaczy, że data jest niepoprawna
        today = datetime.date.today().strftime('%Y.%m.%d')  # Pobranie dzisiejszej daty, w odpowiednim formacie
        if d < datetime.datetime.strptime(today, '%Y.%m.%d'):  # Sprawdzenie czy data urodzenia jest starsza niż dzisiejsza data
            return 1
        else:
            return 0
    except ValueError:
        return 0  # Funkcja zwraca 0 dla niepoprawnej daty


def sortowanie_babelkowe(lista):  # Sortowanie dat urodzenia (algorytm bubblesort)
    n = len(lista)
    while n > 1:
        zamiana = False
        for i in range(0, n - 1):
            if (lista[i]) > (lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]  # Zamiana wartości
                zamiana = True
        n -= 1
        if not zamiana:
            break
    return lista


def zmiana_daty(lista):  # Funkcja do zmiany formatu daty z RRRR.MM.DD na DD.MM.RRRR (wydaje się być bardziej czytelny)
    for i in range(len(lista)):
        element = lista[i].split(" ")
        data = element[0].split(".")
        r = data[0]
        m = data[1]
        d = data[2]
        lista[i] = str(d) + "." + str(m) + "." + str(r) + " " + str(element[1]) + " " + str(element[2])


def back():  # Funkcja która wraca z okna wyświetlania danych do początkowego okna wczytywania danych
    show_data_frame.forget()  # Zamyka ramkę z danymi
    load_data_frame.pack(fill='both', expand=1)  # Otwiera początkową ramkę [Expand - czy ramka ma zmieniać rozmiar przy zmianie rozmiaru okna, Fill - W których kierunkach może zmieniać rozmiar]


def showlist(lista):  # Funkcja wyświetlająca listę z odczytanymi danymi
    save_btn.config(command=lambda: saveresult(lista))  # Podpięcie funkcji zapisującej do przycisku Zapisz (funkcja lambda, żeby przycisk wywoływał funkcję z argumentem)
    listbox.delete('0', 'end')  # Wyczyszczenie listy przed wyświetleniem
    headers = ["Data urodz", "PESEL", "Płeć"]  # Nagłówki kolumn listy
    row_format = "{:<11}  {:^12}  {:^1}"  # Format wyglądu poszczególnych kolumn (< wyrównanie do lewej, ^ wyśrodkowanie, liczba to szerokość kolumny)
    listbox.insert(0, row_format.format(*headers))  # Wstawienie nagłówków do listy  * do użycia zmiennej liczby argumentów .format("Data urodz", "PESEL", "Płeć"))
    for i in lista:
        items = i.split(" ")
        listbox.insert('end', row_format.format(*items))  # Wstawienie elementu do listboxa
    show_data_frame.pack(fill='both', expand=1)  # Wyświetlenie ramki w odczytanymi danymi
    load_data_frame.forget()  # Zamknięcie ramki z wczytywaniem danych


def saveresult(lista):  # Zapis wyniku działania programu do pliku
    if len(lista) != 0:  # Sprawdzenie czy są odczytane wartości
        filepath = filedialog.asksaveasfilename(filetypes=[("Plik tekstowy", "*.txt")], defaultextension="*.txt",
                                                initialfile="wyniki_PESEL")  # Okienko wyboru lokalizacji zapisu, typ pliku tekstowy, domyślna nazwa
        if filepath != '':  # Sprawdzenie czy wybrano lokalizację zapisu
            save = open(filepath, 'w')  # Stworzenie pliku wyjściowego
            save.write("DD.MM.RRRR Numer PESEL Płeć" + '\n')
            for i in lista:
                save.write(str(i) + '\n')  # Zapis danych linijka po linijce
            save.close()
            effect = messagebox.askyesno("Powrót", "Czy chcesz wrócić do przeglądu danych?")  # Wyświetlenie okienka z zapytaniem (tak/nie)
            if not effect:
                back()  # Jeśli wybrano nie, powrót do ekranu początkowego wczytywania danych


def msg(msg_title, message):  # Wyświetlenie okienka z podaną informacją
    messagebox.showinfo(msg_title, message)


def error(error_msg):  # Wyświetlenie komunikatu błędu
    messagebox.showerror('Wystąpił błąd', error_msg)


def readfile():  # Wczytywanie pliku i przetwarzanie danych
    filepath = filedialog.askopenfilename(filetypes=[("Plik tekstowy", "*.txt")])  # Okienko wyboru pliku wejściowego
    lista = []
    if filepath != '':
        file = 0
        try:
            try:
                file = open(filepath, 'r')  # Odczyt pliku wejściowego
                for line in file.readlines():
                    x = line.strip()  # Pobranie danych z każdej linii, usunięcie znaków na początku i na końcu (w tym znaku \n)
                    if pesel_check(x) != 0 and date_check(pesel_data(x)) != 0:  # Sprawdzenie czy pesel jest poprawny i czy data urodzenia w nim zawarta jest poprawna
                        lista.append(str(pesel_data(x)) + " " + str(x) + " " + str(pesel_plec(x)))  # Odczyt poszczególnych danych i dodanie ich do listy (na koniec)
                sortowanie_babelkowe(lista)  # Sortowanie listy wg daty urodzenia (od najstarszej do najmłodszej) lista.sort() też działa
                zmiana_daty(lista)  # Zmiana formatu daty
            finally:
                if file:
                    file.close()  # Zamknięcie pliku wejściowego
        except Exception as exception:
            error("Wystąpił błąd podczas wczytywania danych: " + str(exception))  # Przechwycenie ewentualnych błędów i wyświetlenie komunikatu

        if len(lista) != 0:
            showlist(lista)  # Wyświetlenie list, jęsli udało się odczytać dane
        else:  # Jeśli nie odczytano danych wyświetla komunikat o możliwej złej zawartości pliku wejściowego
            messagebox.showwarning('Uwaga', 'Dane nie zostały przetworzone.\nSprawdź zawartość wybranego pliku')


# Stworzenie interfejsu graficznego
root = tk.Tk()
root.title("Odczyt danych PESEL")  # Tytuł okna programu
root.geometry("300x300")  # Wymiary domyślne okna
root['background'] = '#e8e8e8'  # Tło okna programu
load_data_frame = tk.Frame(root)  # Stworzenie poszczególnych ramek, z ekranem wczytywania i prezentacji danych
show_data_frame = tk.Frame(root)

load_data_frame.columnconfigure(0, weight=1)  # Ustalenie kolum i wierszy siatki grid
load_data_frame.columnconfigure(1, weight=1)
load_data_frame.columnconfigure(2, weight=1)
load_data_frame.rowconfigure(0, weight=1)
load_data_frame.rowconfigure(1, weight=1)
load_data_frame.rowconfigure(2, weight=1)

title = tk.Label(load_data_frame, text='Odczyt danych PESEL')  # Nagłówek z tytułem programu
title.config(font=('Arial', 14))  # Właściwości czcionki
title.grid(row=0, column=1, sticky=tk.NS)  # Wstawienie elementu do odpowiedniego wiersza  i kolumny, opcja sticky opisuje jak umiejscowić element (NS rozciąga na całą wysokość i środkuje pionowo)

info = tk.Label(load_data_frame, text='Wybierz plik tekstowy z danymi')
info.config(font=('Arial', 11))
info.grid(row=1, column=1, sticky=tk.N)  # N - Góra wyśrodkowana

button = tk.Button(load_data_frame, command=readfile, text='Otwórz', bg='#0277BD', fg='white', activebackground='#0288D1', borderwidth=0, font=('Calibra', 11, 'bold'))  # Przycisk wczytujący ścieżkę do pliku
button.grid(row=1, column=1, ipadx=8, ipady=4)  # ipadx i ipady to marginesy wewnętrzne

show_data_frame.columnconfigure(0, weight=1)
show_data_frame.columnconfigure(1, weight=1)
show_data_frame.columnconfigure(2, weight=1)
show_data_frame.rowconfigure(0, weight=1)
show_data_frame.rowconfigure(1, weight=1)
show_data_frame.rowconfigure(2, weight=1)

listbox = tk.Listbox(show_data_frame, width=40, height=10, font=('Arial', 10))  # Lista do wyświetlania danych
listbox.grid(row=0, column=0, columnspan=3, sticky=tk.EW, padx=15, pady=5)  # EW - rozciąga element w poziomie i środkuje w pionie

scrollbar = tk.Scrollbar(show_data_frame, orient='vertical', command=listbox.yview)  # Pasek do przewijania listy ,przesuwać zawartość Listbox gdy przesuwany jest Scrollbar
scrollbar.grid(row=0, column=2, sticky='nse')  # NSE - połączenie NS i E czyli wyrównania do prawej strony
listbox.config(yscrollcommand=scrollbar.set)    # Połączenie scrollbara z listą  ,przesuwać zawartość Scrollbar gdy element w Listbox jest przesuwany

save_btn = tk.Button(show_data_frame, text='Zapisz', bg='#50b472', fg='white', activebackground='#95d1a9', borderwidth=0, font=('Calibra', 11, 'bold'))  # Przycisk zapisu danych
save_btn.grid(row=1, column=1, ipadx=4, ipady=2)

back_btn = tk.Button(show_data_frame, command=back, bg='white', fg='black', activebackground='#D3D3D3', text='Powrót', borderwidth=0, font=('Calibra', 10))
back_btn.grid(row=2, column=1, ipadx=5, ipady=2)

load_data_frame.pack(fill='both', expand=1)  # Expand - czy ramka ma zmieniać rozmiar przy zmianie rozmiaru okna, Fill - W których kierunkach może zmieniać rozmiar
root.mainloop()  # Mainloop - wyświetla okno i czeka na akcję użytkownika
