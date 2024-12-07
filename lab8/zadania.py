from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
import numpy as np

# funkcje pomocnicze

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


# LAB 8

im = Image.open("image.png")
print("tryb obrazu", im.mode)
print("format obrazu", im.format)
print("rozmiar", im.size)

#im2 = im.copy()
#ImageFilter.FIND_EDGES.filterargs = ((3, 3), 1, 0, (-1, -1, -1, -1, 8, -1, -1, -1, -1))
#im2.filter(ImageFilter.FIND_EDGES).show()



# def filtruj(obraz, kernel, scale):
#     obraz_copy = obraz.copy()
#     tablica_obrazu = np.array(obraz_copy).astype(np.int32).copy()
#
#     print(tablica_obrazu.size)
#     h, w, kolor = tablica_obrazu.shape
#     print(w, h)
#     print(len(kernel), int(np.sqrt(len(kernel))))
#     bok = int(np.sqrt(len(kernel)))
#     print(bok)
#
#     kernel = np.array(kernel).reshape((bok, bok))
#
#     for i in range(h):
#         for j in range(w):
#             kolor_sr = [0, 0, 0]
#             d = int(bok/2)
#             for a in range(bok):
#                 for b in range(bok):
#                     #kolor_sr[0] += tablica_obrazu[i - d + a, j - d + b][0]
#                     ni = i - d + a  # Індекс рядка
#                     nj = j - d + b  # Індекс стовпця
#
#                     # Якщо індекси виходять за межі, використовується [0, 0, 0]
#                     if 0 <= ni < h and 0 <= nj < w:
#                         kolor_sr[0] += tablica_obrazu[ni, nj, 0] * kernel[a, b]
#                         kolor_sr[1] += tablica_obrazu[ni, nj, 1] * kernel[a, b]
#                         kolor_sr[2] += tablica_obrazu[ni, nj, 2] * kernel[a, b]
#                     else:
#                         kolor_sr[0] += 0 * kernel[a, b]
#                         kolor_sr[1] += 0 * kernel[a, b]
#                         kolor_sr[2] += 0 * kernel[a, b]
#
#             # kolor_sr[0] = ((kolor_sr[0] // bok**2) // scale) % 256
#             # kolor_sr[1] = ((kolor_sr[1] // bok**2) // scale) % 256
#             # kolor_sr[2] = ((kolor_sr[2] // bok**2) // scale) % 256
#             kolor_sr[0] = (kolor_sr[0] // scale) % 256
#             kolor_sr[1] = (kolor_sr[1] // scale) % 256
#             kolor_sr[2] = (kolor_sr[2] // scale) % 256
#             tablica_obrazu[i, j, 0] = kolor_sr[0]
#             tablica_obrazu[i, j, 1] = kolor_sr[1]
#             tablica_obrazu[i, j, 2] = kolor_sr[2]
#
#     tablica_obrazu = np.clip(tablica_obrazu, 0, 255).astype(np.uint8)
#
#     return Image.fromarray(tablica_obrazu)

# def filtruj(obraz, kernel, scale=1):
#     obraz_copy = obraz.copy()
#     tablica_obrazu = np.array(obraz_copy).astype(np.float32)
#
#     h, w, kolor = tablica_obrazu.shape
#
#
#     bok = int(np.sqrt(len(kernel)))
#     kernel = np.array(kernel).reshape((bok, bok))
#     print(kernel)
#
#     tablica_result = np.zeros_like(tablica_obrazu, dtype=np.float32)
#
#     d = bok // 2
#
#     for i in range(h):
#         for j in range(w):
#             kolor_sr = [0, 0, 0]
#
#             for a in range(bok):
#                 for b in range(bok):
#                     ni = i - d + a
#                     nj = j - d + b
#
#                     if 0 <= ni < h and 0 <= nj < w:
#                         kolor_sr[0] += tablica_obrazu[ni, nj, 0] * kernel[a, b]
#                         kolor_sr[1] += tablica_obrazu[ni, nj, 1] * kernel[a, b]
#                         kolor_sr[2] += tablica_obrazu[ni, nj, 2] * kernel[a, b]
#                     else:
#                         kolor_sr[0] += 255 * kernel[a, b]
#                         kolor_sr[1] += 255 * kernel[a, b]
#                         kolor_sr[2] += 255 * kernel[a, b]
#
#             tablica_result[i, j, 0] = kolor_sr[0]
#             tablica_result[i, j, 1] = kolor_sr[1]
#             tablica_result[i, j, 2] = kolor_sr[2]
#
#     tablica_result = (tablica_result / scale).clip(0, 255).astype(np.uint8)
#
#     return Image.fromarray(tablica_result)

def filtruj(obraz, kernel, scale=1):
    obraz_copy = obraz.copy()
    tablica_obrazu = np.array(obraz_copy).astype(np.float32)

    h, w, kolor = tablica_obrazu.shape

    bok = int(np.sqrt(len(kernel)))
    kernel = np.array(kernel).reshape((bok, bok))

    d = bok // 2

    padded_image = np.pad(
        tablica_obrazu,
        ((d, d), (d, d), (0, 0)),
        mode='edge'
    )

    tablica_result = np.zeros_like(tablica_obrazu, dtype=np.float32)

    for i in range(h):
        for j in range(w):
            kolor_sr = [0, 0, 0]

            for a in range(bok):
                for b in range(bok):
                    ni = i + a
                    nj = j + b

                    kolor_sr[0] += padded_image[ni, nj, 0] * kernel[a, b]
                    kolor_sr[1] += padded_image[ni, nj, 1] * kernel[a, b]
                    kolor_sr[2] += padded_image[ni, nj, 2] * kernel[a, b]

            tablica_result[i, j, 0] = kolor_sr[0]
            tablica_result[i, j, 1] = kolor_sr[1]
            tablica_result[i, j, 2] = kolor_sr[2]

    tablica_result = (tablica_result / scale).clip(0, 255).astype(np.uint8)

    return Image.fromarray(tablica_result)



# kernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
#
# przefiltrowany_obraz = filtruj(im, kernel, 1)
# przefiltrowany_obraz.show()


# Zadanie 2

# a)

obraz_blur = im.filter(ImageFilter.BLUR)

# b)

print(ImageFilter.BLUR.filterargs)
kernel = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
#przefiltrowany_obraz = filtruj(im, kernel, 16)
#przefiltrowany_obraz.show()


# c)

# fig, axes = plt.subplots(1, 4, figsize=(15, 5))
# axes[0].imshow(im)
# axes[0].set_title("Obraz wejściowy")
# axes[1].imshow(obraz_blur)
# axes[1].set_title("Filtr BLUR")
# axes[2].imshow(przefiltrowany_obraz)
# axes[2].set_title("Funkcja filtr")
# axes[3].imshow(ImageChops.difference(obraz_blur, przefiltrowany_obraz))
# axes[3].set_title("Porównanie różnicowe")
#
# for ax in axes:
#     ax.axis("off")
#
# plt.tight_layout()
# plt.savefig("fig1.png")
# plt.show()
#

# d)
# statystyki(ImageChops.difference(obraz_blur, przefiltrowany_obraz))


# Zadanie 3

im3 = im.copy()
im3 = im3.convert("L")

# a)

obraz_emboss = im3.filter(ImageFilter.EMBOSS)

# b)

# print(ImageFilter.EMBOSS.filterargs)
# kernel1 = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
# kernel2 = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
#
# ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, kernel1)
# sobel1 = im.filter(ImageFilter.EMBOSS)
# ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, kernel2)
# sobel2 = im.filter(ImageFilter.EMBOSS)
# ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, 0, 0, 0, 1, 0, 0, 0, 0))

# c)

# fig, axes = plt.subplots(1, 4, figsize=(15, 5))
# axes[0].imshow(im3, cmap="gray")
# axes[0].set_title("Obraz wejściowy w trybie 'L'")
# axes[1].imshow(obraz_emboss, cmap="gray")
# axes[1].set_title("Filtr EMBOSS")
# axes[2].imshow(sobel1)
# axes[2].set_title("Funkcja filtr SOBEL1")
# axes[3].imshow(sobel2)
# axes[3].set_title("Funkcja filtr SOBEL2")
#
# for ax in axes:
#     ax.axis("off")
#
# plt.tight_layout()
# plt.savefig("fig2.png")
# plt.show()

# Zadanie 4

# im4 = im.copy()
#
# obraz_detail = im4.filter(ImageFilter.DETAIL)
# obraz_edge_enhance_more = im4.filter(ImageFilter.EDGE_ENHANCE_MORE)
# obraz_sharpen = im4.filter(ImageFilter.SHARPEN)
# obraz_smooth_more = im4.filter(ImageFilter.SMOOTH_MORE)
#
#
# fig, axes = plt.subplots(4, 2, figsize=(9, 13))
# axes[0, 0].imshow(obraz_detail)
# axes[0, 0].set_title("DETAIL")
# axes[0, 0].axis("off")
# axes[0, 1].imshow(ImageChops.difference(obraz_detail, im4))
# axes[0, 1].set_title("Difference DETAIL vs oryginal")
# axes[0, 1].axis("off")
#
# axes[1, 0].imshow(obraz_edge_enhance_more)
# axes[1, 0].set_title("EDGE_ENHANCE_MORE")
# axes[1, 0].axis("off")
# axes[1, 1].imshow(ImageChops.difference(obraz_edge_enhance_more, im4))
# axes[1, 1].set_title("Difference EDGE_ENHANCE_MORE vs oryginal")
# axes[1, 1].axis("off")
#
# axes[2, 0].imshow(obraz_sharpen)
# axes[2, 0].set_title("SMOOTH_MORE")
# axes[2, 0].axis("off")
# axes[2, 1].imshow(ImageChops.difference(obraz_sharpen, im4))
# axes[2, 1].set_title("Difference SMOOTH_MORE vs oryginal")
# axes[2, 1].axis("off")
#
# axes[3, 0].imshow(obraz_smooth_more)
# axes[3, 0].set_title("SHARPEN")
# axes[3, 0].axis("off")
# axes[3, 1].imshow(ImageChops.difference(obraz_smooth_more, im4))
# axes[3, 1].set_title("Difference SHARPEN vs oryginal")
# axes[3, 1].axis("off")
#
# plt.subplots_adjust(hspace=0.6, wspace=0.2)
# plt.tight_layout()
# plt.savefig("fig3.png")
# plt.show()

# Zadanie 5

im5 = im.copy()


# filtered_images = {
#     "GaussianBlur (radius=4.5)": im5.filter(ImageFilter.GaussianBlur(radius=4.5)),
#     "UnsharpMask (radius=1, percent=150, threshold=3)": im5.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3)),
#     "MedianFilter (size=5)": im5.filter(ImageFilter.MedianFilter(size=5)),
#     "MinFilter (size=3)": im5.filter(ImageFilter.MinFilter(size=3)),
#     "MaxFilter (size=3)": im5.filter(ImageFilter.MaxFilter(size=3)),
# }

filters = {
    "GaussianBlur": {"args": "(radius=4.5)", "image": im5.filter(ImageFilter.GaussianBlur(radius=4.5))},
    "UnsharpMask": {"args": "(radius=1, percent=150, threshold=3)",
                    "image": im5.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))},
    "MedianFilter": {"args": "(size=5)", "image": im5.filter(ImageFilter.MedianFilter(size=5))},
    "MinFilter": {"args": "(size=3)", "image": im5.filter(ImageFilter.MinFilter(size=3))},
    "MaxFilter": {"args": "(size=3)", "image": im5.filter(ImageFilter.MaxFilter(size=3))},
}

# Create figure with subplots (2 rows, 5 columns)
fig, axes = plt.subplots(2, 5, figsize=(21, 9))
axes = axes.flatten()  # Flatten to easily index

# Iterate over the filtered images to display them
for idx, (filter_name, filter_data) in enumerate(filters.items()):
    filtered_image = filter_data["image"]
    args = filter_data["args"]

    # Original image and filtered image difference
    difference = ImageChops.difference(im, filtered_image)

    # Display filtered image
    axes[idx].imshow(filtered_image)
    axes[idx].set_title(f"{filter_name}\nArgs: {filter_data['args']}")  # Title with args
    axes[idx].axis("off")  # Hide axis

    # Display difference image
    axes[idx + 5].imshow(difference, cmap="gray")  # Show difference in grayscale
    axes[idx + 5].set_title(f"Oryginal vs {filter_name}")
    axes[idx + 5].axis("off")  # Hide axis

plt.tight_layout()
plt.savefig("fig4.png")
plt.show()

