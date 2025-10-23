#%%
import os
from PyPDF2 import PdfWriter, PdfReader, PdfMerger
#%%
file_name = "sample.pdf"
#%%
if not os.path.isfile(file_name):
    print(f"The file {file_name} does not exist.")
else:
    inputpdf = PdfReader(open(file_name, "rb"))

    for i in range(0, 6):
        writer = PdfWriter()
        writer.add_page(inputpdf.pages[i])
        with open("%s-page%s.pdf" % (file_name, i), "wb") as output_pdf1:
            writer.write(output_pdf1)

    # Merge the split PDF files
    merge_pdf = PdfMerger()

    for i in range(0, 6):
        merge_pdf.append(open("%s-page%s.pdf" % (file_name, i), "rb"))

    with open("merged_%s" % file_name, "wb") as output_pdf1:
        merge_pdf.write(output_pdf1)

# %%
