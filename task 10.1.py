from PIL import Image
img = Image.open("открытки/бабаевский шоколад.jpg")
img_cropped = img.crop((950, 350, 1900, 1400))
img_cropped.save("открытки/собака с шоколадом.jpg")