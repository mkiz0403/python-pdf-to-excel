import pdfplumber
import pandas as pd
import openpyxl

pdf_path = "/Users/jeontaejeong/Documents/Coding/Tt/python-pdf-to-excel/pdf/2025창업지원공고문.pdf"
output_path = "/Users/jeontaejeong/Documents/Coding/Tt/python-pdf-to-excel/output/2025창업지원공고문2.xlsx"

with pdfplumber.open(pdf_path) as pdf:
    data_frames = []
    # for page_num in range(3, len(pdf.pages)):
    for page_num in range(21, len(pdf.pages)):
        page = pdf.pages[page_num]
        tables = page.extract_tables()

        for table in tables:
            df = pd.DataFrame(table [ 1: ], columns=table[0])
            data_frames.append(df)

    combined_df = pd.concat(data_frames, ignore_index=True)

    combined_df.to_excel(output_path, index=False)
    print(f"데이터가 {output_path}에 저장되었습니다.")






