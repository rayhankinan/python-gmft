import streamlit as st
from gmft.auto import AutoTableDetector, AutoTableFormatter

from detect import ingest_pdf
from pdf import create_temp_pdf

def main() -> None:
    st.title("PDF to CSV Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is None:
        return

    converting = st.empty()

    if converting.button("Convert PDF to CSV", disabled=False, key="convert_button1"):
        converting.button("Converting...", disabled=True, key="convert_button2")

        with create_temp_pdf(uploaded_file) as doc:
            detector = AutoTableDetector()
            formatter = AutoTableFormatter()

            for page, table_iter in ingest_pdf(detector, doc):
                st.header(f"{uploaded_file.name} - Page {page.page_number}")

                for i, table in enumerate(table_iter):
                    try:
                        ft = formatter.format(table)

                        st.subheader(f"Table {i + 1}")
                        st.image(ft.image())
                        st.dataframe(ft.df())

                    except Exception as e:
                        st.error(f"An error occurred: {e}")

        converting.button("Convert PDF to CSV", disabled=False, key="convert_button3")

if __name__ == "__main__":
    main()