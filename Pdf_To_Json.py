import pdfplumber
import json

# Path to the input PDF file
pdf_path = "ag-listing-8-1-2025.pdf"
# Path to save the output JSON file
json_path = "ag-listing.json"

data_list = []

# Open and read the PDF file
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        # Extract table from the current page
        table = page.extract_table()
        if table:
            for i, row in enumerate(table[1:], start=1):  # Skip the header row
                if len(row) >= 5:  # Ensure the row has enough columns
                    entry = {
                        "id": row[0],
                        "Proprietary Name": row[1].replace("\n", " ").strip(),  # Clean newlines
                        "Dosage Form": row[2].replace("\n", " ").strip(),
                        "Strength": row[3].replace("\n", " ").strip(),
                        "NDA Applicant Name": row[4].replace("\n", " ").strip(),
                        "Date Authorized Generic Entered the Market": row[5].replace("\n", " ").strip()
                    }
                    data_list.append(entry)

# Save the extracted data as a JSON file
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

print(f"JSON file saved at: {json_path}")
