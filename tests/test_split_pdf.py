import pytest
from PyPDF2 import PdfReader
from splittingpdf.splittingpdfs import split_pdf

def test_split_pdf(tmp_path):
    # tmp_path - temporary directory created by pytest, unique to each function
    sample = "sample_files/sample.pdf"
    output = tmp_path/"out.pdf"

    result_path = split_pdf(sample,output,1,3)

    reader = PdfReader(result_path)

    assert output.exists()
    assert len(reader.pages) == 3

def test_invalid_range(tmp_path):
    sample = "sample_files/sample.pdf"
    output = tmp_path/"out.pdf"

    with pytest.raises(ValueError):
        split_pdf(sample,output,600,700) #out of range
    

def test_file_notfound(tmp_path):
    output = tmp_path/"out.pdf"

    with pytest.raises(FileNotFoundError):
        split_pdf("missing_file.pdf",output,1,3)




