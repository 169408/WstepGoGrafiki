from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

im = Image.open('im.png')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
w_im, h_im = im.size
#im.show()

inicjaly_wlasne = Image.open('inicjaly_wlasne.bmp')
print("tryb", inicjaly_wlasne.mode)
print("format", inicjaly_wlasne.format)
print("rozmiar", inicjaly_wlasne.size)
w_in, h_in = inicjaly_wlasne.size
#inicjaly_wlasne.show()

# Zadanie 1

def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    tab_bazowy = np.array(obraz_bazowy)
    tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.int_)

    h0, w0, color = tab_bazowy.shape
    h1, w1 = tab_wstawiany.shape
    n_k = min(h0, h1+n)
    m_k = min(w0, w1+m)
    n_p = max(0, n)
    m_p = max(0, m)

    tab_wynnik = tab_bazowy
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            if(tab_wstawiany[i - n, j - m] == 0):
                tab_wynnik[i, j] = kolor

    return Image.fromarray(tab_wynnik)

#wstaw_inicjaly(im, inicjaly_wlasne, w_im - w_in, 0, (0, 255, 0)).show()
wstaw_inicjaly(im, inicjaly_wlasne, w_im - w_in, 0, (0, 255, 0)).save("obraz_inicjaly1.png")
#wstaw_inicjaly(im, inicjaly_wlasne, 0, h_im - h_in, (124, 85, 201)).show()
wstaw_inicjaly(im, inicjaly_wlasne, 0, h_im - h_in, (124, 85, 201)).save("obraz_inicjaly2.png")
#wstaw_inicjaly(im, inicjaly_wlasne, w_im - (w_in // 2), h_im // 2, (255, 0, 221)).show()
wstaw_inicjaly(im, inicjaly_wlasne, w_im - (w_in // 2), h_im // 2, (255, 0, 221)).save("obraz_inicjaly3.png")

# Zadanie 2

# a)
obraz = Image.open("im.png")
obraz.save("obraz1.jpg", "JPEG")

# b)
for i in range(1, 5):
    obraz = Image.open(f"obraz{i}.jpg")
    obraz.save(f"obraz{i+1}.jpg", "JPEG")

obraz5 = Image.open("obraz5.jpg")

# c)
def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


statystyki(obraz)
statystyki(obraz5)

obraz_hist = obraz.histogram()
obraz5_hist = obraz5.histogram()

difference_image = ImageChops.difference(obraz, obraz5)
difference_hist = difference_image.histogram()

fig, axs = plt.subplots(3, 2, figsize=(12, 10))

# Wyświetlanie `obraz.png`
axs[0, 0].imshow(obraz)
axs[0, 0].set_title("Obraz oryginalny (obraz.png)")
axs[0, 0].axis("off")

# Wyświetlanie `obraz5.jpg`
axs[0, 1].imshow(obraz5)
axs[0, 1].set_title("Obraz5.jpg")
axs[0, 1].axis("off")

# Histogramy oryginału i `obraz5.jpg`
axs[1, 0].plot(obraz_hist, color="blue")
axs[1, 0].set_title("Histogram oryginału")
axs[1, 1].plot(obraz5_hist, color="green")
axs[1, 1].set_title("Histogram obraz5.jpg")

# Wyświetlenie różnicy między obrazami
axs[2, 0].imshow(difference_image)
axs[2, 0].set_title("Różnica obrazów")
axs[2, 0].axis("off")

# Histogram różnicy
axs[2, 1].plot(difference_hist, color="red")
axs[2, 1].set_title("Histogram różnicy")

plt.tight_layout()
#plt.show()
plt.savefig("wykres1.png")

# Wczytanie obrazów `obraz4.jpg` i `obraz5.jpg`
obraz4 = Image.open("obraz4.jpg")

print("----------------------")
# d)

statystyki(obraz)
statystyki(obraz5)

obraz4_hist = obraz4.histogram()
obraz5_hist = obraz5.histogram()

difference_image = ImageChops.difference(obraz4, obraz5)
difference_hist = difference_image.histogram()

fig, axs = plt.subplots(3, 2, figsize=(12, 10))

# Wyświetlanie `obraz.png`
axs[0, 0].imshow(obraz4)
axs[0, 0].set_title("Obraz4.jpg")
axs[0, 0].axis("off")

# Wyświetlanie `obraz5.jpg`
axs[0, 1].imshow(obraz5)
axs[0, 1].set_title("Obraz5.jpg")
axs[0, 1].axis("off")

# Histogramy oryginału i `obraz5.jpg`
axs[1, 0].plot(obraz4_hist, color="blue")
axs[1, 0].set_title("Histogram obraz4.jpg")
axs[1, 1].plot(obraz5_hist, color="green")
axs[1, 1].set_title("Histogram obraz5.jpg")

# Wyświetlenie różnicy między obrazami
axs[2, 0].imshow(difference_image)
axs[2, 0].set_title("Różnica obrazów")
axs[2, 0].axis("off")

# Histogram różnicy
axs[2, 1].plot(difference_hist, color="red")
axs[2, 1].set_title("Histogram różnicy")

plt.tight_layout()
#plt.show()
plt.savefig("wykres2.png")


# Zadanie 3

def ukryj_kod(obraz, im_kod):
    t_obraz = np.asarray(obraz)
    t_kodowany = t_obraz.copy()
    h, w, d = t_obraz.shape
    t_kod = np.asarray(im_kod)
    for i in range(h):
        for j in range(w):
            if t_kod[i, j] > 0:
                k = randint(0,2)
                t_kodowany[i, j, k] = t_obraz[i, j, k] + 1
    return Image.fromarray(t_kodowany)

im_obraz = Image.open("jesien.jpg")
kod = Image.open("kod.bmp")

im_kodowany = ukryj_kod(im_obraz, kod)
im_kodowany.show()

odkodowany = ImageChops.difference(im_obraz, im_kodowany)
odkodowany.show()

# a)

def odkoduj(obraz1, obraz2):
    t_obraz1 = np.array(obraz1)
    t_obraz2 = np.array(obraz2)
    h, w, d = t_obraz1.shape
    t = (h, w)
    t_odkodowany = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if(t_obraz1[i, j][0] != t_obraz2[i, j][0] or t_obraz1[i, j][1] != t_obraz2[i, j][1] or t_obraz1[i, j][2] != t_obraz2[i, j][2]):
                t_odkodowany[i, j] = 255
    return Image.fromarray(t_odkodowany)

zakodowany1 = Image.open("zakodowany1.bmp")
odkoduj(im_obraz, zakodowany1)

odkoduj(im_obraz, im_kodowany).show()

# b)

zakodowany2 = Image.open("zakodowany2.bmp")

odkoduj(im_obraz, zakodowany2).save("kod2.bmp", "bmp")
odkoduj(im_obraz, zakodowany2).show()