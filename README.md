# PDF Splitter

A simple Python script to split a PDF file into multiple smaller files, each containing a specified number of pages. This project uses the [PyPDF2](https://pypi.org/project/PyPDF2/) library for PDF manipulation.

## Features

- Split any PDF into smaller PDFs by page count
- Easy to use command-line interface

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/pdf-splitter.git
    cd pdf-splitter
    ```
2. Install dependencies:
    ```bash
    pip install .
    ```
    or with UV:
    ```bash
    uv sync
    ```
## Usage
Run the following command:
```bash
python splittingpdfs.py
```
Follow the prompts in your CLI to enter the path to your PDF file, a path to where the extracted pdf would be stored, start page and end page indices of the extracted pdf. 
