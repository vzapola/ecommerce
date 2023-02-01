import qrcode
primeiro_qrcode = qrcode.make("https://www.google.com.br")
type(primeiro_qrcode)
img.save("primeiro_qrcode.jpg")
