from PIL import Image  # Python Imaging Library
import numpy as np

# inicjaly = Image.open("bs.bmp")  # wczytywanie obrazu
#
# print("tryb", inicjaly.mode)
# print("format", inicjaly.format)
# print("rozmiar", inicjaly.size)
#
# t_inicjaly = np.asarray(inicjaly)
# print("typ danych tablicy", t_inicjaly.dtype)  # typ danych przechowywanych w tablicy
# print("rozmiar tablicy", t_inicjaly.shape)  # rozmiar tablicy - warto porównac z wymiarami obrazka
#
# inicjaly
# # inicjaly.show()
#

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
    for i in range(koef):
        if(i % 2 == 0):
            tab[grub:h - grub, grub:w - grub] = 0

    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

rysuj_ramki(200, 100, 20).show()
