from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# funkcja dodatkowa

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


im = Image.open('im.png')
# print("tryb", im.mode)
# print("format", im.format)
# print("rozmiar", im.size)
#w, h = im.size

#im.show()

mix011 = Image.open('pliki_do_testu/mix011.png')
mix012 = Image.open('pliki_do_testu/mix012.png')
mix19 = Image.open('pliki_do_testu/mix19.png')
mix29 = Image.open('pliki_do_testu/mix29.png')
mix110 = Image.open('pliki_do_testu/mix110.png')
mix111 = Image.open('pliki_do_testu/mix111.png')
mix210 = Image.open('pliki_do_testu/mix210.png')
mix211 = Image.open('pliki_do_testu/mix211.png')
mix212 = Image.open('pliki_do_testu/mix212.png')
mix310 = Image.open('pliki_do_testu/mix310.png')
obraz1 = Image.open('pliki_do_testu/obraz1.jpg')
obraz2 = Image.open('pliki_do_testu/obraz2.jpg')
obraz3 = Image.open('pliki_do_testu/obraz3.jpg')
obraz4 = Image.open('pliki_do_testu/obraz4.jpg')
obraz5 = Image.open('pliki_do_testu/obraz5.jpg')
obraz6 = Image.open('pliki_do_testu/obraz6.jpg')
obraz7 = Image.open('pliki_do_testu/obraz7.jpg')
obraz8 = Image.open('pliki_do_testu/obraz8.jpg')
obraz9 = Image.open('pliki_do_testu/obraz9.jpg')
obraz10 = Image.open('pliki_do_testu/obraz10.jpg')
obraz11 = Image.open('pliki_do_testu/obraz11.jpg')
obraz12 = Image.open('pliki_do_testu/obraz12.jpg')




# Zadanie 1

def szary(w, h):
    # Tworzymy pustą tablicę o wymiarach w x h
    tablica = np.zeros((h, w), dtype=np.uint8)

    # Wypełniamy tablicę zgodnie ze wzorem
    for i in range(h):
        for j in range(w):
            tablica[i, j] = (-3 * i + j) % 256

    return tablica

w, h = obraz11.size

obraz_szary = Image.fromarray(szary(w, h), mode='L')

# obraz11.show()
# obraz_szary.show()

r, g, b = obraz11.split()

mix = Image.merge("RGB", (r, obraz_szary, b))
mix.save("mix.png", "png")

# Zadanie 2


T = np.array(im)
# print("typ danych tablicy obrazu: ", T.dtype)
# print("rozmiar elementu tablicy obrazu: ", T.itemsize)
# print("rozmiar tablicy obrazu: ", T.shape)

t_r = T[:, :, 0]
# print("typ danych tablicy kanału r: ", t_r.dtype)
# print("rozmiar elemntu tablicy kanału r: ",t_r.itemsize)
# print("rozmiar tablicy kanału r: ",t_r.shape)
im_r = Image.fromarray(t_r)
# print("tryb kanału r: ", im_r.mode)

t_g = T[:, :, 1]
im_g = Image.fromarray(t_g)

t_b = T[:, :, 2]
im_b = Image.fromarray(t_b)

# b)
im1 = Image.merge('RGB', (im_r, im_g, im_b))
im1.save("im1.png", "png")

diff = ImageChops.difference(im, im1)
# diff.show()
# c)
# plt.figure(figsize=(7, 9))
# plt.subplot(3, 1, 1)
# plt.imshow(im)
# plt.axis('off')
# plt.subplot(3, 1, 2)
# plt.imshow(im1)
# plt.axis('off')
# plt.subplot(3, 1, 3)
# plt.imshow(diff)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.03, hspace=0.03)
# plt.savefig('fig1.png')
# plt.show()

# Zadanie 3

obraz_zad7 = Image.open("im_roznica.png")


def roznica_w_miejscach(ob1, ob2):
    differ = ImageChops.difference(ob1, ob2)

    kolor_array = np.array(differ)

    kolor_array[(kolor_array != [0, 0, 0]).any(axis=2)] = [255, 0, 0]

    nowyObraz = Image.fromarray(kolor_array)
    nowyObraz.show()

def czy_identyczne(ob1, ob2):

    if ob1.mode == ob2.mode and ob1.format == ob2.format and ob1.size == ob2.size:
        tab1 = np.array(ob1)
        tab2 = np.array(ob2)

        if np.array_equal(tab1, tab2):
            print("Tablicy obrazów są identyczne")
        else:
            print("Tablicy obrazów nie są identyczne")
            return roznica_w_miejscach(ob1, ob2)

        difference = ImageChops.difference(ob1, ob2)

        np_diff = np.array(diff)
        mean_diff = np.mean(np_diff)

        if mean_diff == 0:
            print("Obrazy są identyczne.")
        else:
            print(f"Obrazy nie są identyczne. Średnia różnic: {mean_diff}")
            return roznica_w_miejscach(ob1, ob2)

    else:
        return roznica_w_miejscach(ob1, ob2)

#czy_identyczne(im, obraz_zad7)


# Zadanie 4

# s_ob9 = stat.Stat(obraz9)
# print(s_ob9.stddev)

# Zadanie 5

# im_g_ob10 = Image.fromarray((np.array(obraz10))[:, :, 1])
# im_g_ob10.show()
# #r1, g1, b1 = obraz10.split()
#
# def rysuj_histogram(obraz):
#     hist = obraz.histogram()
#     plt.title("histogram kanału zielonego ")
#     # plt.bar(range(768), hist)
#     #plt.bar(range(256), hist[:256], color='r', alpha=0.5)
#     plt.bar(range(256), hist[:256], color='g', alpha=0.4)
#     #plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
#     print(hist[110])
#
#     plt.savefig("hist.png")
#
# rysuj_histogram(im_g_ob10)

# Zadanie 6

r, g, b = im.split()
im2 = Image.merge('RGB', (b, g, r))

# a)
im2.save("im2.jpg", "JPEG")
im2.save("im2.png", "PNG")

# b)

im2_jpg = Image.open("im2.jpg")
im2_png = Image.open("im2.png")

difference = ImageChops.difference(im2_jpg, im2_png)

# c)
# plt.figure(figsize=(7, 8))
# plt.subplot(3, 1, 1)
# plt.imshow(im2_jpg)
# plt.axis('off')
# plt.subplot(3, 1, 2)
# plt.imshow(im2_png)
# plt.axis('off')
# plt.subplot(3, 1, 3)
# plt.imshow(difference)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.03, hspace=0.03)
# plt.savefig('fig2.png')
# plt.show()

# JPEG stosuje kompresję stratną, co prowadzi do utraty jakości. Tracimy część informacji o kolorach i detalach obrazu.
# JPEG próbuje zmniejszyć rozmiar pliku, usuwając mniej istotne informacje. Format PNG stosuje kompresję bezstratną,
# więc wynikowy obraz w formacie PNG powinien być identyczny z oryginałem, ale obraz JPEG będzie zawierał drobne różnice.


# Zadanie 7

obraz = obraz9
r, g, b = obraz.split()

#mix = negatyw(Image.merge("RGB", (b, g, r)))
mix = mix19

if(obraz.size == mix.size):
    print("taki sam rozmiar")

    if ImageChops.difference(obraz, mix).getbbox() is None:
        print("Obraz mix powstał od obrazu obraz")
    if ImageChops.difference(obraz, negatyw(mix)).getbbox() is None:
        print("Obraz mix powstał od obrazu obraz, jest negatywem")
    s1 = stat.Stat(obraz)
    s2 = stat.Stat(mix)
    s3 = stat.Stat(negatyw(mix))

    kanaly = ["r", "g", "b"]

    for kanal1, i in enumerate(s1.mean[0:(len(s1.mean)-2)]):
        for kanal2, j in enumerate(s2.mean):
            if(i == j and kanal1 != kanal2):
                print("kanal1 - ", kanaly[kanal1], "kanal2 - ", kanaly[kanal2])
                print("zmiana kolejności kanałów")

    for kanal1, i in enumerate(s1.mean[0:(len(s1.mean)-2)]):
        for kanal2, j in enumerate(s3.mean):
            if(i == j and kanal1 != kanal2):
                print("kanal1 - ", kanaly[kanal1], "kanal2 - ", kanaly[kanal2])
                print("zmiana kolejności kanałów oraz negatyw")

else:
    print("Obraz mix nie powstał od obrazu obraz")

obraz9.show()
mix19.show()
negatyw(mix19).show()

ImageChops.difference(obraz9, negatyw(mix19)).show()