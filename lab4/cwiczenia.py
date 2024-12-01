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

# Zadanie 1

im = Image.open('im.png')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
w, h = im.size
#im.show()

# Zadanie 2

# a)
# tablica obrazu
T = np.array(im)
print("typ danych tablicy obrazu: ", T.dtype)
print("rozmiar elementu tablicy obrazu: ", T.itemsize)
print("rozmiar tablicy obrazu: ", T.shape)

t_r = T[:, :, 0]
print("typ danych tablicy kanału r: ", t_r.dtype)
print("rozmiar elemntu tablicy kanału r: ",t_r.itemsize)
print("rozmiar tablicy kanału r: ",t_r.shape)
im_r = Image.fromarray(t_r)
print("tryb kanału r: ", im_r.mode)



t_g = T[:, :, 1]
im_g = Image.fromarray(t_g)

t_b = T[:, :, 2]
im_b = Image.fromarray(t_b)


# b)
im1 = Image.merge('RGB', (im_r, im_g, im_b))

diff = ImageChops.difference(im, im1)

# c)
# plt.figure(figsize=(3, 5))
# plt.subplot(3, 1, 1)
# plt.imshow(im)
# plt.axis('off')
# plt.subplot(3, 1, 2)
# plt.imshow(im1)
# plt.axis('off')
# plt.subplot(3, 1, 3)
# plt.imshow(diff)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig1.png')



# Zadanie 3
r, g, b = im.split()
im2 = Image.merge('RGB', (b, g, r))
#im2.show()

# a)
im2.save("zad3a_im2.jpg", "JPEG")
im2.save("zad3a_im2.png", "PNG")

# b)

im2_jpg = Image.open("zad3a_im2.jpg")
im2_png = Image.open("zad3a_im2.png")

diff_zad3 = ImageChops.difference(im2_jpg, im2_png)

# c)
# plt.figure(figsize=(3, 4))
# plt.subplot(3, 1, 1)
# plt.imshow(im2_jpg)
# plt.axis('off')
# plt.subplot(3, 1, 2)
# plt.imshow(im2_png)
# plt.axis('off')
# plt.subplot(3, 1, 3)
# plt.imshow(diff_zad3)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.03, hspace=0.03)
# plt.savefig('fig2.png')

# JPEG stosuje kompresję stratną, co prowadzi do utraty jakości. Tracimy część informacji o kolorach i detalach obrazu.
# JPEG próbuje zmniejszyć rozmiar pliku, usuwając mniej istotne informacje. Format PNG stosuje kompresję bezstratną,
# więc wynikowy obraz w formacie PNG powinien być identyczny z oryginałem, ale obraz JPEG będzie zawierał drobne różnice.

# Zadanie 4

obraz = im
r, g, b = obraz.split()

mix = negatyw(Image.merge("RGB", (b, g, r)))
#obraz.show()
#mix.show()

obraz2 = Image.open("beksinski.png")

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

# Zadanie 5

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

h, w, kolor = np.array(im).shape
print(w, h)

im3 = rysuj_pasy_pionowe_szare(w, h, 26, 15)

#im3.show()

# a)
obraz1_zad5 = Image.merge("RGB", (im3, g, b))
obraz2_zad5 = Image.merge("RGB", (r, im3, b))
obraz3_zad5 = Image.merge("RGB", (r, g, im3))

# b)

# plt.figure(figsize=(6, 10))
# plt.subplot(3, 1, 1)
# plt.imshow(obraz1_zad5)
# plt.axis('off')
# plt.subplot(3, 1, 2)
# plt.imshow(obraz2_zad5)
# plt.axis('off')
# plt.subplot(3, 1, 3)
# plt.imshow(obraz3_zad5)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.03, hspace=0.03)
# plt.savefig('fig4.png')

# Zadanie 6

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

#statystyki(im)

plt.figure().clear()

hist_g = g.histogram()
print(hist_g[1])

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    # plt.bar(range(768), hist)
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    #plt.show()

rysuj_histogram_RGB(im)

# Zadanie 7

obraz_zad7 = Image.open("im_roznica.png")


def highlight_differences(img1, img2):
    # Obraz różnicowy
    differ = ImageChops.difference(img1, img2)
    differ.show()

    kolor_array = np.array(differ)

    kolor_array[(kolor_array != [0, 0, 0]).any(axis=2)] = [255, 0, 0]

    nowyObraz = Image.fromarray(kolor_array)
    nowyObraz.show()
    # Wzmocnienie różnic
    # enhancer = ImageEnhance.Brightness(diff)
    # diff_enhanced = enhancer.enhance(10)  # Wzmocnij różnice
    #
    # # Wyświetlenie wyników
    # diff_enhanced.show()

if im.mode == obraz_zad7.mode and im.format == obraz_zad7.format and im.size == obraz_zad7.size:
    tab1 = np.array(im)
    tab2 = np.array(obraz_zad7)

    if np.array_equal(tab1, tab2):
        ident = True
        print("Obrazy są identyczne")
    else:
        print("Obrazy nie są identyczne")
        ident = False
        highlight_differences(im, obraz_zad7)

    if ident:
        difference = ImageChops.difference(im, obraz_zad7)

        np_diff = np.array(diff)
        mean_diff = np.mean(np_diff)

        if mean_diff == 0:
            print("Obrazy są identyczne.")
        else:
            print(f"Obrazy nie są identyczne. Średnia różnic: {mean_diff}")
            highlight_differences(im, obraz_zad7)

else:
    highlight_differences(im, obraz_zad7)

    # print(tab1)
    # print(tab2)


# Zadanie 8

beksinski = Image.open("beksinski1.png")
print("tryb", beksinski.mode)
print("format", beksinski.format)
print("rozmiar", beksinski.size)

r, b, g = beksinski.split() # nie działa, bo tryb jest RGBA Dlatego, kiedy próbujesz przypisać wynik do tylko trzech zmiennych (r, g, b), pojawia się błąd.