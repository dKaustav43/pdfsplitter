import os
from PyPDF2 import PdfWriter, PdfReader, PdfMerger

file_name = "sample.pdf"

if not os.path.isfile(file_name):
    print(f"The file {file_name} does not exist.")
else:
    inputpdf = PdfReader(open(file_name, "rb"))

    writer = PdfWriter()

    # for i in range(min(6,len(inputpdf.pages))):
    for i in range(100,200):
        writer.add_page(inputpdf.pages[i])

    # Write to a single merged PDF
    with open("merged.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Created '{"merged.pdf"}'")
