import numpy as np
from PIL import Image # Python Imaging Library

a = 5

b = np.append(3, 4)

print(a)
print(b)

obrazek = Image.open("rrrr.bmp")
print("tryb", obrazek.mode)
print("format", obrazek.format)
print("rozmiar", obrazek.size)

#obrazek.show()

dane_obrazka = np.asarray(obrazek)
print("----------info")
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy", dane_obrazka.shape)
print("rozmiar tablicy", dane_obrazka.size)
print("rozmiar tablicy", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)  # pokazuje ile bajtów trzeba do zapisu wartości elementu
print("pierwszy wyraz:", dane_obrazka[0][0])
print("drugi wyraz:", dane_obrazka[1][0])
print("***************************************")
print(dane_obrazka)  # mozna  zobaczyć tablicę

ob_d = Image.fromarray(dane_obrazka)  # tworzenie obrazu z tablicy dane_obrazka (typ bool)
#ob_d
ob_d.show()

print("tryb:", ob_d.mode)
print("format:", ob_d.format)
print("rozmiar:", ob_d.size)

dane_obrazka1 = dane_obrazka.astype(np.uint8)
print(dane_obrazka1)


ob_d1 = Image.fromarray(dane_obrazka1)  # tworzenie obrazu z tablicy dane_obrazka1 (typ int)
# ----- wyswietlanie informacji o obrazie -----------------------------
print("tryb:", ob_d1.mode)
print("format:", ob_d1.format)
print("rozmiar:", ob_d1.size)

ob_d1.show()
ob_d1.save("kopia.bmp")




# WAŻNE PYTANIE NA NASTEPNE ZAJECIA!!!  DLACZEGO ob_d1 widać jako obraz czarny?

# wczytywanie tablicy z pliku UWAGA! plik txt powinien zawierac same zera i jedynki oddzielane spacjami bez dodatkowych znaków jak w pliku dane.txt
# t1 = np.loadtxt("dane.txt", dtype=np.bool_)
# t2 = np.loadtxt("dane.txt", dtype=np.int_)
# t3 = np.loadtxt("dane.txt", dtype=np.uint8)
#
# # w zależnosci od tego, jakie operacje chcemy zrobić na tablicy, wybieramy jedną z powyższych postaci tablicy
# print("typ danych tablicy t1:", t1.dtype)  # typ danych przechowywanych w tablicy
# print("rozmiar tablicy t1 :", t1.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
# print("wymiar tablicy t1 :", t1.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
#
# print("typ danych tablicy t2:", t2.dtype)  # typ danych przechowywanych w tablicy
# print("rozmiar tablicy t2 :", t2.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
# print("wymiar tablicy t2 :", t2.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
#
# print("typ danych tablicy t3:", t3.dtype)  # typ danych przechowywanych w tablicy
# print("rozmiar tablicy t3 :", t3.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
# print("wymiar tablicy t3 :", t3.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
#
# print(t1)
# print(t2)
# print(t3)

