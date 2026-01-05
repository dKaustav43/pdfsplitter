
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader


def check_input_pdfpath(input_pdf_path:str):
    
    input_path = Path(input_pdf_path)    
    if not input_path.is_file():
        raise FileNotFoundError(f"Input file does not exist: {input_pdf_path}")
    
    return f"Input pdf file found at {input_path}"
    
def read_and_validate_pdf(input_pdf_path:str, start_page:int, end_page:int):
    
    input_path = check_input_pdfpath(input_pdf_path)

    reader = PdfReader(str(input_path))
    
    total_pages = len(reader.pages)

    # validate pages
    if start_page < 0 or end_page >= total_pages:
        raise ValueError("Page range is out of bounds."
                         f"PDF has {total_pages} pages.")

    return f"Pages to be extracted are starting at pg.{start_page} and ending at pg.{end_page}."

def write_to_newpdf(input_pdf_path:str, start_page:int, end_page:int):
    
    input_path = check_input_pdfpath(input_pdf_path)
    
    reader = PdfReader(input_path)
    
    writer = PdfWriter()
    # add pages to the writer
    for i in range(start_page, end_page+1):
        writer.add_page(reader.pages[i])
    
    return writer

def output_split_pdf(input_pdf_path:str, output_pdf_path:str, start_page:int,end_page:int):
    
    # Write to a single merged PDF
    output_path = Path(output_pdf_path)
    writer = write_to_newpdf(input_pdf_path, start_page,end_page)
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)
    
    return str(output_path)

# def split_pdf(input_pdf_path:str, output_pdf_path:str, start:int, end:int):

#     """
#     Takes a PDF and extracts pages from start to end (inclusive),
#     writing them into a new PDF located at the output_pdf_path.
#     """

#     input_path = Path(input_pdf_path)

#     if not input_path.is_file():
#         raise FileNotFoundError(f"Input file does not exist: {input_pdf_path}")

#     reader = PdfReader(str(input_path))
#     total_pages = len(reader.pages)

#     # validate pages
#     if start < 0 or end >= total_pages:
#         raise ValueError("Page range is out of bounds."
#                          f"PDF has {total_pages} pages.")

#     writer = PdfWriter()

#     # add pages to the writer
#     for i in range(start, end+1):
#         writer.add_page(reader.pages[i])
    
#     # Write to a single merged PDF
#     output_path = Path(output_pdf_path)
#     with open(output_path, "wb") as output_pdf:
#         writer.write(output_pdf)
    
#     return str(output_path)

def main():

    input_pdf_path = input("Enter the path of the pdf file here: ")
    check_pdf_path_msg = check_input_pdfpath(input_pdf_path)
    print(check_pdf_path_msg)
    
    output_pdf_path = input("Enter the path where you would like to store the split pdf: ")

    start_page = int(input("Start page index: "))
    end_page = int(input("End page inded: "))

    validate_page_range = read_and_validate_pdf(input_pdf_path,start_page,end_page)
    print(validate_page_range)

    result = output_split_pdf(input_pdf_path, output_pdf_path, start_page, end_page)

    print(f"Created '{result}'!")


if __name__ == "__main__":
    main()