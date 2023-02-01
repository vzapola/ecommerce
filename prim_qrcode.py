import qrcode

img = qrcode.make("https://www.google.com.br")
type(img)
img.save("primeiro_qrcode.png")