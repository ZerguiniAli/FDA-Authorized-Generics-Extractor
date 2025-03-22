```md
# 📝 FDA Authorized Generics PDF Extractor

This project provides a Python script to **extract data from an FDA Authorized Generics PDF document** and convert it into a structured **JSON file**.

## 📌 Features
- ✅ **Extracts tables** from FDA’s Authorized Generics PDF.
- ✅ **Cleans and formats text**, removing unnecessary line breaks.
- ✅ **Outputs structured JSON** with proper formatting.
- ✅ **Automates data processing** for research, analysis, and database storage.

## 📂 Project Structure
```
📁 FDA-Authorized-Generics-Extractor
│── 📄 ag-listing-8-1-2025.pdf  # Input FDA PDF file
│── 📄 extract_to_json.py       # Python script to extract data
│── 📄 ag-listing.json          # Output JSON file
│── 📄 README.md                # Project documentation
```

---

## 🔧 Requirements
Ensure you have the following installed before running the script:

### **🛠 Required Software**
- Python **3.x**

### **📦 Required Libraries**
Install dependencies using `pip`:
```sh
pip install pdfplumber
```

---

## 🚀 Usage
### **1️⃣ Place the PDF File**
Make sure the **FDA Authorized Generics PDF** is in the same directory as the script.

### **2️⃣ Run the Script**
Execute the Python script to extract the data:
```sh
python extract_to_json.py
```

### **3️⃣ View the Output**
The extracted data will be saved as a JSON file (`ag-listing.json`) in the project directory.

---

## 📜 How It Works
1. **Opens the PDF** and scans each page.
2. **Extracts tables** containing drug information.
3. **Cleans text** by removing unwanted line breaks (`\n`).
4. **Formats data** into a structured JSON file.
5. **Saves the output** in `ag-listing.json`.

---

## 📂 JSON Output Format
The output JSON file will contain structured data like this:

```json
[
  {
    "id": 1,
    "Proprietary Name": "ABSORICA",
    "Dosage Form": "Capsules",
    "Strength": "40 mg",
    "NDA Applicant Name": "Sun Pharmaceutical Industries, Inc.",
    "Date Authorized Generic Entered the Market": "12/2020"
  },
  {
    "id": 2,
    "Proprietary Name": "ACANYA",
    "Dosage Form": "Gel",
    "Strength": "1.2% / 2.5%",
    "NDA Applicant Name": "Bausch Health Americas, Inc.",
    "Date Authorized Generic Entered the Market": "07/2018"
  }
]
```

---

## 🏆 Why Use This Script?
This script automates the process of extracting **Authorized Generics** data from **FDA PDFs**, making it useful for:
- 📊 **Pharmaceutical Market Analysis**
- 🔬 **Research & Drug Studies**
- 💾 **Database Management**
- 🏥 **Medical & Healthcare Industry Applications**

---

## 🔄 Future Enhancements
🔹 **Improve table extraction for complex layouts**  
🔹 **Add support for additional PDF formats**  
🔹 **Enhance error handling for missing/incorrect data**  

---

## 🤝 Contributions
Feel free to **fork** this repository, improve the script, and submit a **pull request**! 🚀  
For questions, reach out via **GitHub Issues**.

---

**⭐ If you find this project useful, please star the repository!** 🌟
```
