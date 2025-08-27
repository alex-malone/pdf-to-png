# pip install pdf2image pillow
# brew install poppler
# Converts each separate PDF page to a PNG file

import os
from pdf2image import convert_from_path

def pdf_to_png(pdf_path, output_folder="output_images", dpi=300):
    # Make sure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Convert PDF to images
    pages = convert_from_path(pdf_path, dpi=dpi)

    # Save each page
    for i, page in enumerate(pages, start=1):
        filename = os.path.join(output_folder, f"page_{i}.png")
        page.save(filename, "PNG")
        print(f"Saved {filename}")

    print("\n✅ Conversion complete!")

if __name__ == "__main__":
    # Change this to your PDF file path
    pdf_file = "input.pdf"
    
    pdf_to_png(pdf_file)
