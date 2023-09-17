from barcode import EAN13
from barcode.writer import ImageWriter
import random
import qrcode

#Gerador de código de barras
#codigo_barra = EAN13(str(random.randint(0o00000000001, 999999999999)), writer=ImageWriter())
#codigo_barra.save("codigo_barra")

codigos_sites = {
    "Youtube": str(random.randint(0o000000000001, 9999999999999)),
    "Instagram": str(random.randint(0o000000000001, 9999999999999)),
    "LinkedIn": str(random.randint(0o000000000001, 9999999999999)),
    "GitHub": str(random.randint(0o000000000001, 9999999999999)),
}

for site in codigos_sites:
    codigo = codigos_sites[site]
    codigo_barra = EAN13(codigo, writer=ImageWriter())
    codigo_barra.save(f"codigo_barra_{site}")

#Gerador de QR Code
#imagem_qrcode = qrcode.make("https://github.com/")
#imagem_qrcode.save("qrcode_github.png")

links_sites = {
    "Youtube": "https://www.youtube.com",
    "Instagram": "https://www.instagram.com",
    "LinkedIn": "https://www.linkedin.com",
    "GitHub": "https://github.com",
}

for site in links_sites:
    link = links_sites[site]
    imagem_qrcode = qrcode.make(link)
    imagem_qrcode.save(f"qrcode_{site}.png")