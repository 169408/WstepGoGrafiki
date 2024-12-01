from PIL import Image
import math

# LAB 7 kod

im = Image.open('baby_yoda.jpg')
# print("tryb obrazu", im.mode)
# print("rozmiar", im.size)

def rysuj_kwadrat_kolor(obraz, m, n, k, kolor): # m,n - srodek kwadratu, k - długość boku kwadratu, liczba nieparzysta
    obraz1 = obraz.copy()
    pix1 = obraz1.load()
    d = int(k/2)
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = kolor
    return obraz1

im1 = im.copy()
#rysuj_kwadrat_kolor(im, 100, 100, 25, (200,0,0)).show()


def rysuj_kwadrat_srednia(obraz, m, n, k):  # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] += pixel[0]
            temp[1] += pixel[1]
            temp[2] += pixel[2]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (int(temp[0] / k ** 2), int(temp[1] / k ** 2), int(temp[2] / k ** 2))
    return obraz1


im2 = im.copy()
#rysuj_kwadrat_srednia(im2, 60, 170, 25).show()

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def rysuj_kolo(obraz, m_s, n_s, r, kolor):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w, h):
        if (i-m_s)**2+(j-n_s)**2 < r**2: # wzór na koło o środku (m_s, n_s) i promieniu r
            obraz1.putpixel((i,j), kolor)
    return obraz1

im3 = im.copy()
im4 = rysuj_kolo(im3, 50, 100, 60, (200,0,0))
#im4.show()

def odbij_lewa_strone_na_prawo(im):
    img = im.copy()
    w, h = im.size
    w1 = int(w / 2)
    px = img.load()
    for i in range(w1, w):
        for j in range(h):
            px[i, j] = px[w -1- i, j]
    return img

def odbij_prawa_strone_na_lewo(im):
    img = im.copy()
    w, h = im.size
    w1 = int(w / 2)
    px = img.load()
    for i in range(0, w1):
        for j in range(h):
            px[i, j] = px[w -1- i, j]
    return img

#odbij_lewa_strone_na_prawo(im).show()
#odbij_prawa_strone_na_lewo(im).show()

def odbij_w_pionie(im):
    px0 = im.load()
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px0[w - 1- i, j]
    return img

def odbij_w_pioziomie(im):
    px0 = im.load()
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px0[i, h - 1 - j]
    return img

#odbij_w_pioziomie(im).show()


# ----------------------------
# Zadania
# ----------------------------

image = Image.open("my_img.png")

# Zadanie 1

# 1.1
def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = max(pixel[0], temp[0])
            temp[1] = max(pixel[1], temp[1])
            temp[2] = max(pixel[2], temp[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

image1 = image.copy()
rysuj_kwadrat_max(rysuj_kwadrat_max(rysuj_kwadrat_max(image1, 310, 240, 44), 20, 80, 25), 562, 155, 15).save("obraz1.png")

# 1.2
def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = min(pixel[0], temp[0])
            temp[1] = min(pixel[1], temp[1])
            temp[2] = min(pixel[2], temp[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1


rysuj_kwadrat_min(rysuj_kwadrat_min(rysuj_kwadrat_min(image1, 310, 240, 44), 20, 80, 25), 562, 155, 15).save("obraz2.png")

# Zadanie 2


def rysuj_kolo_obrazu(obraz, m_s, n_s, r, m_copy, n_copy):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):

            if i ** 2 + j ** 2 < r ** 2:
                m_wst, n_wst = m_copy + i, n_copy + j
                m_baz, n_baz = m_s + i, n_s + j

                # Sprawdzanie, czy współrzędne mieszczą się w granicach obrazu
                if 0 <= m_wst < w and 0 <= n_wst < h and 0 <= m_baz < w and 0 <= n_baz < h:
                    obraz1.putpixel((m_baz, n_baz), obraz.getpixel((m_wst, n_wst)))

    return obraz1

image2 = image.copy()
#rysuj_kolo_obrazu(image2, 230, 215, 5, 534, 160).show()
#rysuj_kolo_obrazu(image2, 285, 170, 28, 499, 94).save("obraz3.png")

rysuj_kolo_obrazu(rysuj_kolo_obrazu(rysuj_kolo_obrazu(rysuj_kolo_obrazu(rysuj_kolo_obrazu(rysuj_kolo_obrazu(rysuj_kolo_obrazu(image2, 495, 5, 28, 499, 94), 445, 55, 28, 499, 94), 405, 105, 28, 499, 94), 375, 155, 28, 499, 94), 335, 105, 28, 499, 94), 295, 55, 28, 499, 94), 255, 5, 28, 499, 94).save("obraz4.png")

image3 = image.copy()
def odbij_w_pionie2(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img

#odbij_w_pionie(image3).show()
#odbij_w_pionie2(image3).show()

