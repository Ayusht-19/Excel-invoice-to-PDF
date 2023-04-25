import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoices nr.{invoice_nr}",ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath,sheet_name="Sheet 1")

    col = df.columns
    col = [item.replace("_", " ").title() for item in col]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=col[0], border=1)
    pdf.cell(w=60, h=8, txt=col[1], border=1)
    pdf.cell(w=40, h=8, txt=col[2], border=1)
    pdf.cell(w=30, h=8, txt=col[3], border=1)
    pdf.cell(w=30, h=8, txt=col[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)

        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=60, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=30, h=8, txt=f"The total amount is {total_sum} Rupees" , ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=30, h=8, txt=f"AT Company")

    pdf.output(f"PDFs/{filename}.pdf")