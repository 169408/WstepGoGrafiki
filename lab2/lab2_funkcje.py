from PIL import Image  # Python Imaging Library
import numpy as np

inicjaly = Image.open("bs.bmp")
my_inicjaly = Image.open("my_inicjaly.bmp")

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
    Image.fromarray(tab).save("beka.bmp", "BMP")
    return Image.fromarray(tab)

#wstaw_obraz_w_obraz(inicjaly, my_inicjaly, -35, 22).show()

#bazowy = rysuj_pasy_pionowe(300, 200, 15)
#wstaw_obraz_w_obraz(bazowy, my_inicjaly, 0, 50).show()

#rysuj_ramki(80, 130, 5).show()

#ob = Image.open("obrazki/aktyw2.bmp")  # wczytywanie obrazu

#print("tryb", ob.mode)
#print("format", ob.format)
#print("rozmiar", ob.size)
#przep = np.array(ob)
#print(przep[97, 20])

#t_ob = np.asarray(ob)
#print("typ danych tablicy", t_ob.dtype)  # typ danych przechowywanych w tablicy
#print("rozmiar tablicy", t_ob.shape)  # rozmiar tablicy - warto porównac z wymiarami obrazka


#rysuj_pasy_pionowe(200, 100, 10).show()

t1 = np.loadtxt("tablica.txt", dtype=np.bool_)

print("typ danych tablicy t1:", t1.dtype)

obraz = Image.fromarray(t1)
obraz = obraz.convert('1')
obraz.show()

rysuj_ramke_w_obrazie(obraz, 40).show()
