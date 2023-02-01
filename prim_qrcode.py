import qrcode
pqrcode = qrcode.make("https://www.google.com.br")
type(pqrcode)
pqrcode.save("primeiro_qrcode.jpg")
