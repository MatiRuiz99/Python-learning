import fitz

doc = fitz.open("nombre.pdf")

with open("contenido_extraido.txt", "w", encoding="utf-8") as archivo_txt:
    for i, pagina in enumerate(doc):
        texto = pagina.get_text()
        archivo_txt.write(f"\n--- pagina {i + 1} ---\n")
        archivo_txt.write(texto + "\n")

doc.close()
print("guardado a txt")