from PIL import Image  # Python Imaging Library
import numpy as np

def rysuj_paski_w_obrazie(obraz, grub): # rysuje pionowy pas grubości grub po lewej stronie oraz po prawej stronie
    tab_obraz = np.asarray(obraz).astype(np.uint8) # wczytanie tablicy obrazu i zamiana na int
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w-grub, w):
            tab_obraz[i][j] = 0
    tab = tab_obraz.astype(bool) # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)

def rysuj_pola_w_obrazie(obraz, grub): # rysuje pionowy pas grubości grub po lewej stronie oraz po prawej stronie
    tab_obraz = np.asarray(obraz).astype(np.uint8) # wczytanie tablicy obrazu i zamiana na int
    h, w = tab_obraz.shape
    for i in range(w):
        for j in range(grub):
            tab_obraz[j][i] = 0
        for j in range(h-grub, h):
            tab_obraz[j][i] = 0
    tab = tab_obraz.astype(bool) # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)

inicjaly = Image.open("bs.bmp")
my_inicjaly = Image.open("my_inicjaly.bmp")

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy", t_inicjaly.shape)



def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)  # wczytanie tablicy obrazu i zamiana na int
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w - grub, w):
            tab_obraz[i][j] = 0
    for i in range(w):
        for j in range(grub):
            tab_obraz[j][i] = 0
        for j in range(h-grub, h):
            tab_obraz[j][i] = 0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

#rysuj_paski_w_obrazie(inicjaly, 10).show()
#rysuj_pola_w_obrazie(inicjaly, 10).show()
#rysuj_ramke_w_obrazie(inicjaly, 10).show()

def rysuj_ramki(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    koef = min(int(w / (2*grub)), int(h / (2*grub)))
    print(koef)
    for i in range(0, koef):
        print(i)
        if(i % 2 == 0):
            tab[grub*i:(h - grub*i), grub*i:(w - grub*i)] = 0
        else:
            tab[grub*i:(h - grub*i), grub*i:(w - grub*i)] = 1

        print(i , "-", grub * i, ":", (h - grub)*i, " do ", grub*i, ":", (w - grub)*i)

    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

#rysuj_ramki(250, 150, 15).show()

def rysuj_pasy_poziome(w, h, grub):  # w, h   -  rozmiar obrazu
    t = (h, w)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)
    # jaki bedzie efekt, gdy np.ones zamienimy na np.zeros?
    ile = int(h/grub)  # liczba pasów  o grubości grub
    for k in range(ile):  # uwaga k = 0,1,2..   bez ile
        for g in range(grub):
            i = k * grub + g  # i - indeks wiersza, j - indeks kolumny
            for j in range(w):
                tab[i, j] = k % 2  # reszta z dzielenia przez dwa
    tab = tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
    return Image.fromarray(tab)  # tworzy obraz

#rysuj_pasy_poziome(100, 180, 20).show()

def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    print(ile)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)

#rysuj_pasy_pionowe(180, 160, 12).show()

def rysuj_wlasne(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    kwadrat_wys = (h // grub) - 1 # wysokość pojedynczego kwadratu
    kwadrat_szer = (w // grub) - 1  # szerokość pojedynczego kwadratu
    koef = grub + 1
    print(koef)

    for i in range(koef):
        start_x = i * kwadrat_szer
        tab[0:h, start_x:start_x+grub] = 1

    for i in range(koef):
        start_y = i * kwadrat_wys
        tab[start_y:start_y+grub, 0:w] = 1

    tab = tab * 255
    return Image.fromarray(tab)

#rysuj_wlasne(250, 200, 5).show()

#tab = (10, 10)
#tab = np.zeros(tab, np.uint8)
#tab[0:9, 0:2] = 1
#print(tab)

def wstaw_obraz(w, h, m, n, obraz): # w,h rozmiary nowego obrazu, m<=w,  n<=h (m,n miejsce wstawienia obrazu )
    tab_obraz = np.asarray(obraz).astype(np.int_)
    h0, w0 = tab_obraz.shape
    t = (h, w)  # rozmiar tablicy nowego obrazu
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    n_k = min(h, n + h0) # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
    m_k = min(w, m + w0) # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
    n_p = max(0, n) # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w górę), to przycinamy
    m_p = max(0, m) # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w lewo), to przycinamy
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab[i][j] = tab_obraz[i - n][j - m]
    tab = tab.astype(bool) # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)

#wstaw_obraz(200, 100, -20, 20, inicjaly).show()

def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_bazowy = np.asarray(obraz_bazowy).astype(np.int_)
    tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.int_)

    h0, w0 = tab_bazowy.shape
    h1, w1 = tab_wstawiany.shape
    n_k = min(h0, n + h1)
    m_k = min(w0, m + w1)
    n_p = max(0, n)
    m_p = max(0, m)

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_bazowy[i][j] = tab_wstawiany[i - n][j - m]

    tab = tab_bazowy.astype(bool)
    return Image.fromarray(tab)

#wstaw_obraz_w_obraz(inicjaly, my_inicjaly, -35, 22).show()




tab = Image.open("tablica.txt")
tab.show()