import img2pdf
import os

# Configuration
input_folder = "images_input"
output_pdf = "resultat.pdf"

# Lister les images valides
images = [
    os.path.join(input_folder, f) 
    for f in os.listdir(input_folder) 
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

# Trier par ordre alphabétique
images.sort()

if images:
    # Générer le PDF
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(images))
    
    print(f"PDF créé : {output_pdf}")
else:
    print("Aucune image")
