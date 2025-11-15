
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader


def split_pdf(input_pdf_path:str, output_pdf_path:str, start:int, end:int):

    """
    Takes a PDF and extracts pages from start to end (inclusive),
    writing them into a new PDF located at the output_pdf_path.
    """

    input_path = Path(input_pdf_path)

    if not input_path.is_file():
        raise FileNotFoundError(f"Input file does not exist: {input_pdf_path}")

    reader = PdfReader(str(input_path))

    writer = PdfWriter()

    # add pages to the writer
    for i in range(start, end+1):
        writer.add_page(reader.pages[i])
    
    # validate pages
    if start < 0 or end >= len(reader.pages):
        raise ValueError("Page range is out of bounds")

    # Write to a single merged PDF
    output_path = Path(output_pdf_path)
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)
    
    return str(output_path)

def main():

    input_pdf_path = input("Enter the path of the pdf file here: ")
    output_pdf_path = input("Enter the path where you would like to store the split pdf: ")

    start = int(input("Start page index: "))
    end = int(input("End page inded: "))

    result = split_pdf(input_pdf_path, output_pdf_path, start, end)
    print(f"Created '{result}'!")


if __name__ == "__main__":
    main()