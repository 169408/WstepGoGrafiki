from PIL import Image
import numpy as np

# Skrypt nauczyciela
def rysuj_ramke_szare(w, h, grub, kolor_ramki, kolor): #kolor od 0 do 255
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki  # wypełnienie tablicy szarym kolorem o wartości kolor_ramki
    tab[grub:h-grub, grub:w-grub] = kolor  # wypełnienie podtablicy kolorem o wartości kolor
    return Image.fromarray(tab)


im_ramka = rysuj_ramke_szare(120, 60, 8, 100, 200)
#im_ramka.show()

def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)

#obraz3 = rysuj_ramki_kolorowe(200, [20,120,220], 6, 7, -6)
#obraz3.show()

def rysuj_po_skosie_szare(h,w, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)

#rysuj_po_skosie_szare(100, 300, 3, 4).show()

# Koniec


# LAB

def rysuj_ramki_szare(w, h, grub, kolor_ramki, kolor_tla):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    koef = min(int(w / (2*grub)), int(h / (2*grub)))

    for i in range(0, koef):

        if(i % 2 == 0):
            tab[grub*i:(h - grub*i), grub*i:(w - grub*i)] = kolor_ramki
            if(kolor_ramki + 13 < 255):
                kolor_ramki += 13
        else:
            tab[grub*i:(h - grub*i), grub*i:(w - grub*i)] = kolor_tla
            if (kolor_tla + 13 < 255):
                kolor_tla += 13

    return Image.fromarray(tab)

#rysuj_ramki_szare(300, 200, 5, 70, 160).show()

def rysuj_pasy_pionowe_szare(w, h, grub, kolor_ramki):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    print(ile)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = kolor_ramki
        kolor_ramki = (kolor_ramki + 10) % 256

    return Image.fromarray(tab)

#rysuj_pasy_pionowe_szare(180, 160, 12, 70).show()

def negatyw(obraz):
    print(obraz.mode)
    if(obraz.mode == "1"):
        tab = np.asarray(obraz).astype(np.uint8)
        tab = tab * 255
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg)
    elif(obraz.mode == "L"):
        tab = np.asarray(obraz).astype(np.uint8)
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg)
    elif(obraz.mode == "RGB"):
        tab = np.asarray(obraz).astype(np.uint8)
        h, w, kolor = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                if(kolor == 3):
                    tab_neg[i, j] = [255 - tab[i, j][kolor-3], 255 - tab[i, j][kolor-2], 255 - tab[i, j][kolor-1]]
                if(kolor == 4):
                    tab_neg[i, j] = [255 - tab[i, j][kolor - 4], 255 - tab[i, j][kolor - 3], 255 - tab[i, j][kolor - 2], tab[i, j][kolor - 1]]
        return Image.fromarray(tab_neg)

gwiazdka = Image.open("gwiazdka.bmp")

#(gwiazdka).show()
#rysuj_ramki_kolorowe(200, [20,120,200], 0, 0, -13).show()
#negatyw(rysuj_ramki_kolorowe(200, [20,120,200], 0, 0, -13)).show()
#negatyw(negatyw(rysuj_ramki_kolorowe(200, [20,120,200], 0, 0, -13))).show()

#rysuj_po_skosie_szare(100, 300, 10, 5).show()
#negatyw(rysuj_po_skosie_szare(100, 300, 10, 5)).show()

def koloruj_w_paski(obraz, grub, kolor):
    if (obraz.mode == "1"):
        obraz_rgb = obraz.convert("RGB")
        tab = np.asarray(obraz_rgb).astype(np.uint8)

        h, w, color = tab.shape
        tab_kolorowa = tab.copy()
        counter = 0
        for i in range(h):
            koloruje = False
            if(counter == grub):
                counter = 0
                kolor = [(kolor[0] + 15) % 256, (kolor[1] + 55) % 256, (kolor[2] + 33) % 256]
            for j in range(w):
                if(tab_kolorowa[i, j][0] == 0):
                    tab_kolorowa[i, j] = kolor
                    koloruje = True
            if(koloruje):
                counter += 1
        return Image.fromarray(tab_kolorowa)

koloruj_w_paski(gwiazdka, 5, [10, 20, 355]).show()



# inicjaly_wlasne = Image.open("inicjaly_wlasne.bmp")
#
# inicjaly_wlasne = inicjaly_wlasne.convert("1")
#
# koloruj_w_paski(inicjaly_wlasne, 5, [200, 20, 105]).show()

# Koniec