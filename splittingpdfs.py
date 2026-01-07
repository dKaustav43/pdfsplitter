from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader

def check_input_pdfpath(input_pdf_path:str) -> Path:
    """(I/O)Checks and returns a path object from an input_pdf_path as a string input."""
    path = Path(input_pdf_path)    
    if not path.is_file():
        raise FileNotFoundError(f"Input file does not exist: {input_pdf_path}")
    
    return path
    
def read_pdf(input_pdf_path:str) -> PdfReader:
    """(Helper function)Reads the pdf file and returns an object of type PdfReader."""
    path = check_input_pdfpath(input_pdf_path)

    reader = PdfReader(str(path))
    
    return reader

def write_to_newpdf(reader:PdfReader, start_page:int, end_page:int) -> PdfWriter:
    """Uses the Reader helper function and store custom pdf pages to a PdfWriter Object"""
    
    total_pages = len(reader.pages)
    # validate pages
    if start_page < 0 or end_page >= total_pages:
        raise ValueError("Page range is out of bounds."
                         f"PDF has {total_pages} pages.")
    
    writer = PdfWriter()
    # add pages to the writer
    for i in range(start_page, end_page+1):
        writer.add_page(reader.pages[i])
    
    return writer

def output_split_pdf(writer:PdfWriter, output_pdf_path:str) -> str:
    """(I/O)Uses the write helper function and returns a pdf in output_pdf_path location."""
    # Write to a single merged PDF
    output_path = Path(output_pdf_path)
    
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)
    
    return str(output_path)

def main():

    input_pdf_path = input("Enter the path of the pdf file here: ")
    output_pdf_path = input("Enter the path where you would like to store the split pdf: ")

    start_page = int(input("Start page index: "))
    end_page = int(input("End page index: "))

    reader = read_and_validate_pdf(input_pdf_path)
    writer = write_to_newpdf(reader,start_page,end_page)

    result = output_split_pdf(writer,output_pdf_path)

    print(f"Created '{result}'!")


if __name__ == "__main__":
    main()