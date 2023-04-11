from pdf2docx import parse
from typing import Tuple
import docx2txt
from gtts import gTTS
import os.path


def pdf_to_doc(pdf_file_path: str, doc_file_path: str) -> Tuple[str, str]:
    """
    convert pdf file to doc file
    :param pdf_file_path: pdf file path
    :param doc_file_path: doc file path
    :return: doc file path
    """
    parse(pdf_file_path, doc_file_path)
    return doc_file_path


pdf_file_path = input("Enter pdf file path: ")

if not os.path.isfile(pdf_file_path):
    # check if file exists
    print("File not found")
    exit(1)
elif pdf_file_path.split(".")[-1] != "pdf":
    # check if file is pdf
    print("File is not pdf")
    exit(1)
else:
    doc_file_path = pdf_file_path.replace(".pdf", ".doc")
    print("Converting pdf to doc...")
    print('-'*50)

    if pdf_to_doc(pdf_file_path, doc_file_path):
        print("Doc conversion successful!\n")

    print("Converting doc to audio...\n")
    tts = gTTS(text=docx2txt.process(doc_file_path), lang="en")
    tts.save(pdf_file_path.replace(".pdf", ".mp3"))
    print("Audio conversion successful!\n")

print("Cleaning...")
os.remove(doc_file_path)
print("Done")
