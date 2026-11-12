import requests
from bs4 import BeautifulSoup
import os
import sys

# Configuration
OCR_URL = "http://172.16.92.245:1687/marker/upload"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FOLDER = os.path.join(BASE_DIR, "input")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")

# Ensure folders exist
if not os.path.exists(INPUT_FOLDER):
    print(f" Input folder does not exist: {INPUT_FOLDER}")
    print("Please create an 'input' folder and put your PDFs inside.")
    sys.exit(1)

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def upload_pdf(pdf_path, filename):
    """Upload PDF to OCR server and return response."""
    with open(pdf_path, "rb") as f:
        files = {"file": (filename, f, "application/pdf")}
        data = {
            "page_range": "",
            "languages": "",
            "force_ocr": "true",
            "paginate_output": "false",
            "output_format": "html"
        }
        return requests.post(OCR_URL, files=files, data=data, timeout=120)

# Get list of PDF files
pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".pdf")]

if not pdf_files:
    print(f" No PDF files found in {INPUT_FOLDER}")
    sys.exit(1)

print(f"\nProcessing {len(pdf_files)} PDFs from {INPUT_FOLDER}\n")

for filename in sorted(pdf_files):
    input_path = os.path.join(INPUT_FOLDER, filename)
    output_path = os.path.join(OUTPUT_FOLDER, filename.rsplit(".", 1)[0] + ".txt")
    
    if os.path.exists(output_path):
        print(f" Skipping (already processed): {filename}")
        continue
    
    print(f" Processing: {filename}")
    
    try:
        response = upload_pdf(input_path, filename)
        response.raise_for_status()  # Raise error if HTTP request failed
        
        html_content = response.json().get("output", "")
        text_content = BeautifulSoup(html_content, "html.parser").get_text(separator="\n", strip=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text_content)
        
        print(f" Saved: {output_path}\n")
    except requests.exceptions.RequestException as req_err:
        print(f" Request failed for {filename} - {req_err}\n")
    except Exception as e:
        print(f" Failed: {filename} - {e}\n")

print(" All PDFs processed!")
