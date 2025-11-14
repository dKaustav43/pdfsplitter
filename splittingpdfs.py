import os
from PyPDF2 import PdfWriter, PdfReader
from utilities import *
input_pdf_path = input("Enter the path of the pdf file here:")
output_pdf_path = input("Enter the path where you would like to store the spliced pdf:")

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
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Created '{output_pdf_path}'")
