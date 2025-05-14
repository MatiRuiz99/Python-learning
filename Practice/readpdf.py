import fitz

doc = fitz.open("CV Matias Ruiz.pdf")

for pagina in doc:
    texto = pagina.get_text()
    print (texto)

doc.close()