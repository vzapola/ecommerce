import qrcode
pqrcode = qrcode.make("https://www.google.com.br")
type(pqrcode)
img.save("primeiro_qrcode.jpg")
