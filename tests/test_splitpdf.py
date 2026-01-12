import pytest
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from splittingpdfs import check_input_pdfpath, read_pdf,write_to_newpdf,output_split_pdf


###### Testing the check_input_pdfpath function #####
#have a look at Pytest documentation on examples of suite of Tests. 
#Other testing frameworks like gtests could be useful as well. Check most popular testing framework for pytests. 

input_pdf_path = "tests/data/git_intro.pdf"
incorrect_pdf_path = "tests/data/gut_intro.pdf"

def test_pass_check_input_pdfpath(sample_path=input_pdf_path):
    
    path = check_input_pdfpath(sample_path)

    assert path.exists()
    assert isinstance(path, Path)


def test_incorrect_input_pdfpath(sample_path = incorrect_pdf_path):
    
    with pytest.raises(FileNotFoundError):
        check_input_pdfpath(sample_path)
    
###### Testing the Reader function #####
def test_pass_read_pdf(input_path:str=input_pdf_path):

    reader = read_pdf(input_path)
    num_pages = len(reader.pages)

    assert isinstance(reader,PdfReader)
    assert num_pages > 0

##### Testing the Writer function #####
def test_pass_write_to_newpdf_2(input_path:str=input_pdf_path):
    reader = PdfReader(input_path)
    start_page = 1
    end_page = 3

    writer = write_to_newpdf(reader, start_page, end_page)
    assert isinstance(writer, PdfWriter)
    assert len(writer.pages) == end_page - start_page + 1


def test_invalid_input_raiseseror(input_path:str=input_pdf_path):
    reader = PdfReader(input_path)
    start_page = -1
    end_page = 100

    with pytest.raises(ValueError):
        write_to_newpdf(reader,start_page,end_page)

###### Testing the output split pdf function #####
def test_output_split_pdf(tmp_path):
    
    writer = PdfWriter()
    writer.add_blank_page(width=72,height=72)

    output_pdf_path = tmp_path/"output_splitpdf.pdf"

    result = output_split_pdf(writer,str(output_pdf_path))

    assert result == str(output_pdf_path)
    assert output_pdf_path.exists()
    assert output_pdf_path.stat().st_size > 0





    

    


