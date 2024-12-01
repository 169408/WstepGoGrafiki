from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#im = Image.open('baby_yoda.jpg')
#print("tryb obrazu", im.mode)
#print("rozmiar", im.size)
#im.show()

def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def pobierz_kolor_pixela(obraz, m, n):  # m, n współrzędne punktu na obrazie
    w, h = obraz.size
    if m < w and n < h:
        kolor = obraz.getpixel((m, n))
    return kolor


#print(pobierz_kolor_pixela(im, 260, 200))

def wstaw_pixel_w_punkt(obraz, m, n, kolor):  # m, n współrzędne punktu na obrazie, kolor -  dane pixela do wstawienia
    w, h = obraz.size
    if m < w and n < h:
        obraz.putpixel((m, n), kolor)
    return obraz

def wstaw_pixel_w_zakresie(obraz, m, n, kolor, w_z, h_z):  # w miejscu m,n wstawia prostokąt o bokach w_z, h_z
    w, h = obraz.size
    print(w, h)
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            # if(i + m >= 0 and j + n >= 0):
                obraz.putpixel((i + m, j + n), kolor)
    return obraz

#im1 = im.copy()
#wstaw_pixel_w_zakresie(im1, 200, -120, (255, 255, 0), 100, 200).show()

#wstaw_pixel_w_zakresie(obraz1, 100, 120, (255, 255, 0), 100, 100).show()

def rozjasnij_obraz_w_zakresie(obraz, m, n, a, b, c, w_z, h_z):  # w miejscu m,n "rozjaśnia" prostokat o wymiaraxh w_z, h_z
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            p = obraz.getpixel((i + m, j + n))
            obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1

#im2 = obraz.copy()
#rozjasnij_obraz_w_zakresie(im2, 500, -150, -50, 50, -40, 100, 200).show()

def skopiuj_obraz_w_zakresie(obraz, m, n, m1, n1, w_z, h_z):  # kopiuje prostokat o wymiarach w_z, h_z z miejsca m,n i wstawia w miejscu m1,n1
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i+m < w and j+n < h:
            p = obraz.getpixel((i + m, j + n))
            if i + m1 < w and j + n1 < h:
                obraz1.putpixel((i + m1, j + n1), p)
    return obraz1


#im3 = obraz.copy()
#skopiuj_obraz_w_zakresie(im3, 70, 50, 328, 30, 50, 50).show()

def rozjasnij_obraz_z_maska(obraz, maska, m, n, a, b, c):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = maska.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1

#im4 = obraz.copy()
#maska = Image.open('gwiazdka.bmp')
#rozjasnij_obraz_z_maska(im4, maska, 410, -10, 10, -100, 150).show()

def dodaj_szum(obraz, n, kolor1, kolor2):  # dodawanie szumu typu salt and pepper
    w, h = obraz.size
    x, y = np.random.randint(0, w, n), np.random.randint(0, h,
                                                         n)  # powtarza n razy losowanie z zakresu 0,w i z zakresu 0,h
    for (i, j) in zip(x, y):  # zip robi pary z list x,y
        obraz.putpixel((i, j), (kolor1 if np.random.rand() < 0.5 else kolor2))  # salt-and-pepper
    return obraz

# im5 = obraz.copy()
# dodaj_szum(im5, 40000, (255,255,0), (0,0,255)).show()

def zastosuj_funkcje(image, func):
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = func(pixele[i, j])

def przestaw_kolory(pixel):
    return (pixel[1], pixel[2], pixel[0])

def filtr_liniowy(image, a, b): # a, b liczby całkowite
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0]* a + b, pixele[i, j][1]* a + b, pixele[i, j][2]* a + b)

# im8 = im.copy()
# im8 = im8.point(lambda i: i + 100)

def efekt_plakatu(im, wsp):
    return im.point(lambda i: i > wsp and 255)  # jeżeli nieprawda, że i > wsp wstaw 0 a w przeciwnym przypadku wstaw 255


# LAB

# Zadanie 1
obraz = Image.open("im.png")
inicjaly = Image.open("inicjaly_wlasne.bmp")

obraz1 = obraz.copy()

# Zadanie 2

# a)

# def wstaw_inicjaly(obraz, obraz_wstawiany, m, n, kolor):
#     tab_bazowy = np.array(obraz)
#     tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.int_)
#
#     h0, w0, color = tab_bazowy.shape
#     h1, w1 = tab_wstawiany.shape
#     n_k = min(h0, h1+n)
#     m_k = min(w0, w1+m)
#     n_p = max(0, n)
#     m_p = max(0, m)
#
#     tab_wynnik = tab_bazowy
#     for i in range(n_p, n_k):
#         for j in range(m_p, m_k):
#             if(tab_wstawiany[i - n, j - m] == 0):
#                 tab_wynnik[i, j] = kolor
#             else:
#                 tab_wynnik[i, j] = (255, 255, 255)
#
#     return Image.fromarray(tab_wynnik)

# def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
#     # Kopia obrazu, aby nie modyfikować oryginału
#     obraz_copy = obraz.copy()
#
#     # Rozmiary obrazów
#     w0, h0 = obraz.size
#     w1, h1 = inicjaly.size
#
#     # Ograniczenie zakresów iteracji
#     n_k = min(h0, n + h1)  # Górny limit w pionie
#     m_k = min(w0, m + w1)  # Górny limit w poziomie
#     n_p = max(0, n)  # Dolny limit w pionie
#     m_p = max(0, m)  # Dolny limit w poziomie
#
#     # Iteracja po pikselach obrazu głównego
#     for i in range(n_p, n_k):
#         for j in range(m_p, m_k):
#             # Współrzędne dla obrazu inicjałów
#             i_inicjaly = i - n
#             j_inicjaly = j - m
#
#             # Pobranie piksela z inicjałów
#             if 0 <= i_inicjaly < h1 and 0 <= j_inicjaly < w1:
#                 pix = inicjaly.getpixel((j_inicjaly, i_inicjaly))
#
#                 # Jeśli piksel jest czarny, zamieniamy na kolor
#                 if pix == 0:  # Czarny piksel
#                     obraz_copy.putpixel((j, i), kolor)
#                 else:
#                     obraz_copy.putpixel((j, i), (255, 255, 255))  # Inne piksele na biało
#
#     return obraz_copy


def wstaw_inicjaly(obraz, obraz_wstawiany, m, n, kolor):
    obraz_copy = obraz.copy()
    obraz_wstawiany_copy = obraz_wstawiany.copy()

    w0, h0 = obraz_copy.size
    w1, h1 = obraz_wstawiany.size

    n_k = min(h0, h1+n)
    m_k = min(w0, w1+m)
    n_p = max(0, n)
    m_p = max(0, m)

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            if(obraz_wstawiany_copy.getpixel((j - m, i - n)) == 0): # [i - n, j - m]
                obraz_copy.putpixel((j, i), kolor)
            # else:
                # nie zrosumiałem czy muszą zostać się białe pikseli
                # obraz_copy.putpixel((j, i), (255, 255, 255))

    return obraz_copy

w_ob, h_ob = obraz1.size
w_in, h_in = inicjaly.size
#wstaw_inicjaly(obraz1, inicjaly, w_ob - w_in, h_ob - h_in, (255, 0, 0)).save("obraz1.png", "PNG")

# b)

def wstaw_inicjaly_maska(obraz, inicjaly, m, n):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (255 - p[0], 255 - p[1], 255 - p[2]))
    return obraz1

wstaw_inicjaly_maska(obraz1, inicjaly, (w_ob // 2 - w_in // 2), (h_ob // 2 - h_in // 2)).save("obraz2.png", "PNG")

# Zadanie 3

def wstaw_inicjaly_load(obraz, obraz_wstawiany, m, n, kolor):
    obraz_copy = obraz.copy()
    obraz_wstawiany_copy = obraz_wstawiany.copy()

    pix_bazowy = obraz_copy.load()
    pix_wstawiany = obraz_wstawiany_copy.load()

    w0, h0 = obraz_copy.size
    w1, h1 = obraz_wstawiany.size

    n_k = min(h0, h1 + n)
    m_k = min(w0, w1 + m)
    n_p = max(0, n)
    m_p = max(0, m)


    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            in_y = i - n
            in_x = j - m

            # Jeśli piksel inicjałów jest czarny (0), ustawiamy kolor inicjałów
            if pix_wstawiany[in_x, in_y] == 0:
                pix_bazowy[j, i] = kolor
            # else:  # Jeśli nie, ustawiamy biały piksel
                # pix_bazowy[j, i] = (255, 255, 255)

    return obraz_copy


w_ob, h_ob = obraz1.size
w_in, h_in = inicjaly.size
wstaw_inicjaly_load(obraz1, inicjaly, w_ob - w_in, h_ob - h_in, (255, 0, 0)).save("obraz3.png", "PNG")

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n):
    obraz1 = obraz.copy()
    inicjaly1 = inicjaly.copy()
    pix_baz = obraz1.load()
    pix_ini = inicjaly1.load()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if pix_ini[i, j] == 0:
                p = pix_baz[i + m, j + n]
                pix_baz[i + m, j + n] = ((255 - p[0]), (255 - p[1]), (255 - p[2])) #(x, y, z)
    return obraz1


wstaw_inicjaly_maska_load(obraz1, inicjaly, (w_ob // 2 - w_in // 2), (h_ob // 2 - h_in // 2)).save("obraz4.png", "PNG")


obraz1 = Image.open("obraz1.png")
obraz2 = Image.open("obraz2.png")
obraz3 = Image.open("obraz3.png")
obraz4 = Image.open("obraz4.png")

# Tworzenie figury i osi
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Ustawianie tytułów i wyświetlanie obrazów
axes[0, 0].imshow(obraz1)
axes[0, 0].set_title("Wstaw inicjały")
axes[0, 0].axis("off")

axes[0, 1].imshow(obraz2)
axes[0, 1].set_title("Wstaw inicjały maska")
axes[0, 1].axis("off")

axes[1, 0].imshow(obraz3)
axes[1, 0].set_title("Wstaw inicjały load")
axes[1, 0].axis("off")

axes[1, 1].imshow(obraz4)
axes[1, 1].set_title("Wstaw inicjały maska load")
axes[1, 1].axis("off")

# Zapis figury
plt.tight_layout()
plt.savefig("fig1.png")
# plt.show()

# Zadanie 4

# a)
def kontrast(obraz, wsp_kontrastu):
    wsp_kontrastu = wsp_kontrastu % 100
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return obraz.point(lambda i: int(128 + (i - 128) * mn))

# Tworzenie obrazów z różnymi wartościami współczynnika kontrastu
obraz_oryginalny = obraz.copy()
obraz_kontrast1 = kontrast(obraz_oryginalny, 12)
obraz_kontrast2 = kontrast(obraz_oryginalny, 44)
obraz_kontrast3 = kontrast(obraz_oryginalny, 92)

# Tworzenie diagramu
fig, axes = plt.subplots(1, 4, figsize=(18, 7))

# Wyświetlanie obrazów
axes[0].imshow(obraz_oryginalny)
axes[0].set_title("Oryginalny")
axes[0].axis("off")

axes[1].imshow(obraz_kontrast1)
axes[1].set_title("Kontrast 12")
axes[1].axis("off")

axes[2].imshow(obraz_kontrast2)
axes[2].set_title("Kontrast 44")
axes[2].axis("off")

axes[3].imshow(obraz_kontrast3)
axes[3].set_title("Kontrast 92")
axes[3].axis("off")

# Zapis diagramu
plt.tight_layout()
plt.savefig("fig2.png")
#plt.show()

# Funkcja kontrast modyfikuje obraz, wzmacniając różnice między jasnymi a
# ciemnymi pikselami. Jej działanie zależy od wartości parametru wsp_kontrastu.
# Oto szczegółowa analiza efektów uzyskanych dla różnych wartości współczynnika:

# Wzrost wartości wsp_kontrastu prowadzi do zwiększenia różnic tonalnych w obrazie.
# Niskie wartości kontrastu (np. 12) subtelnie poprawiają jakość obrazu, zachowując jego naturalność.
# Średnie wartości kontrastu (np. 44) podkreślają szczegóły, zwiększając wyrazistość obrazu.
# Wysokie wartości kontrastu (np. 92) dramatycznie zmieniają obraz, ale mogą powodować utratę detali w średnich tonach.


# b)

def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * (np.log(1 + i / 255)))

obraz_oryginalny = obraz.copy()
obraz_transf = transformacja_logarytmiczna(obraz.copy())
obraz_filtr_liniowy = obraz.copy()
filtr_liniowy(obraz_filtr_liniowy, 2, 100)

plt.figure(figsize=(7, 10))
plt.subplot(3, 1, 1)
plt.imshow(obraz_oryginalny)
plt.title("Obraz oryginalny")
plt.axis('off')
plt.subplot(3, 1, 2)
plt.imshow(obraz_oryginalny)
plt.title("Transformacja logarytmiczna")
plt.axis('off')
plt.subplot(3, 1, 3)
plt.imshow(obraz_filtr_liniowy)
plt.title("Filtr liniowy, a = 2, b = 100")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.14)
plt.savefig('fig3.png')

# plt.show()


# Oryginalny obraz:
#
# Zawiera oryginalne piksele bez modyfikacji.
# Rozkład jasności i kolorów jest naturalny, zgodny z danymi źródłowymi.
# Transformacja logarytmiczna:
#
# Zwiększa widoczność szczegółów w ciemniejszych partiach obrazu.
# Działa lepiej przy dużej dynamice obrazu (np. obrazy o dużym kontraście między ciemnymi a jasnymi obszarami).
# Kolory w jaśniejszych obszarach są mniej wyraźne, gdyż logarytm spłaszcza jasne wartości.
# Filtr liniowy (a=2, b=100):
#
# Jasność obrazu została znacznie zwiększona przez dodanie stałej b = 100.
# Kontrast został podwojony przez wartość a = 2.
# Obraz ma tendencję do "przepalania" pikseli, szczególnie tam, gdzie wartości są bliskie 255. Wynikiem są jasne, nienaturalnie wyglądające obszary.

# c)

def transformacja_gamma(obraz, gamma):
    if(gamma <= 0.0):
        gamma = 0.001
    elif(gamma > 100.0):
        gamma = 100.0

    return obraz.point(lambda i: ((i/255) ** (1/gamma)) * 255)

# Tworzenie obrazów z różnymi wartościami współczynnika kontrastu
obraz_oryginalny = obraz.copy()
obraz_gamma1 = transformacja_gamma(obraz_oryginalny, 9.4)
obraz_gamma2 = transformacja_gamma(obraz_oryginalny, 50.9)
obraz_gamma3 = transformacja_gamma(obraz_oryginalny, 94)

# Tworzenie diagramu
fig, axes = plt.subplots(1, 4, figsize=(18, 7))

# Wyświetlanie obrazów
axes[0].imshow(obraz_oryginalny)
axes[0].set_title("Oryginalny")
axes[0].axis("off")

axes[1].imshow(obraz_gamma1)
axes[1].set_title("Gamma 9.4")
axes[1].axis("off")

axes[2].imshow(obraz_gamma2)
axes[2].set_title("Gamma 50.9")
axes[2].axis("off")

axes[3].imshow(obraz_gamma3)
axes[3].set_title("Gamma 94")
axes[3].axis("off")

# Zapis diagramu
plt.tight_layout()
plt.savefig("fig4.png")
#plt.show()
#
# Transformacja gamma działa nieliniowo, co pozwala modyfikować sposób, w jaki jasność jest rozkładana w obrazie:
#
# Niskie wartości gamma (<1) podkreślają ciemniejsze partie obrazu.
# Średnie wartości gamma (1-40) utrzymują równowagę między ciemnymi a jasnymi partiami, co poprawia ogólną widoczność szczegółów, ale już nie tak widocznie.
# Wysokie wartości gamma (>40) powodują dominację jasnych partii obrazu, co może prowadzić do utraty szczegółów w jasnych obszarach.

# Zadanie 5

# a)

T = np.array(obraz, dtype='uint8')
T += 100
#print(T)
#print("------------------------------------------------------------")
obraz_wynik = Image.fromarray(T, "RGB")
#obraz_wynik.show()
#print(np.asarray(obraz.point(lambda i: i + 100)))
#obraz.point(lambda i: i + 100).show()

# ponieważ te dwie metody przetwarzają piksele obrazu w różny sposób.
#
# z użyciem np.array i +=
# W tej metodzie obraz jest najpierw konwertowany na tablicę NumPy
# Następnie, przy użyciu +=, dodawana jest wartość 100 do każdego piksela w tablicy
# Może wystąpić przekroczenie zakresu (np. jeśli wartość pikseli przekroczy 255, wtedy
# nastąpi "wrap-around", pixel % 256).
#
# z użyciem obraz.point() i lambda
# Funkcja obraz.point(lambda i: i + 100) działa na każdym pikselu indywidualnie,
# ale w tym przypadku jest używana na każdym kanale obrazu osobno.
# Wartości pikseli, które przekraczają 255, mogą zostać obcięte do 255 (klipping),
# co może skutkować utratą informacji o szczegółach obrazu.
#
# czyli przy pracy na tablice, wartość piksela jest pixel % 256, a przy pracy
# na samym obrazie za pomocą point(), wartość piksela jest obcięta do 255, z tego powodu obrazy mają różny wygląd

# b)

def działaj_na_tablicy(obraz):
    T = np.array(obraz, dtype='uint8')
    w, h, kolor = T.shape
    print(w, h)

    for i in range(w):
        for j in range(h):
            if(T[i, j][0] > 255 - 100 or T[i, j][1] > 255 - 100 or T[i, j][2] > 255 - 100):
                T[i, j][0] = min(T[i, j][0], 255 - 100)
                T[i, j][1] = min(T[i, j][1], 255 - 100)
                T[i, j][2] = min(T[i, j][2], 255 - 100)

            T[i, j] += 100

    return Image.fromarray(T)



działaj_na_tablicy(obraz).show()