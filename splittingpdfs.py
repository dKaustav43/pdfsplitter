import os
from PyPDF2 import PdfWriter, PdfReader

input_pdf_path = input("Enter the path of the pdf file here:")

#file_name = "sample.pdf"

if not os.path.isfile(input_pdf_path):
    print(f"The file {input_pdf_path} does not exist.")
else:
    inputpdf = PdfReader(open(input_pdf_path, "rb"))

    writer = PdfWriter()

    # for i in range(min(6,len(inputpdf.pages))):
    for i in range(100,200):
        writer.add_page(inputpdf.pages[i])

    # Write to a single merged PDF
    with open("merged.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Created '{"merged.pdf"}'")
