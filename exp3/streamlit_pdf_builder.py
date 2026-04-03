from io import BytesIO
from pathlib import Path

import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Image, Paragraph, Preformatted, SimpleDocTemplate, Spacer

PAGE_WIDTH, PAGE_HEIGHT = letter


code_style = ParagraphStyle(
    "Code",
    fontName="Courier",
    fontSize=9,
    leading=14,
    backColor=colors.HexColor("#f5f5f5"),
    borderColor=colors.HexColor("#cccccc"),
    borderWidth=1,
    borderPadding=10,
    spaceAfter=12,
)

heading_style = ParagraphStyle(
    "CustomHeading",
    fontName="Helvetica-Bold",
    fontSize=14,
    leading=18,
    spaceAfter=8,
    spaceBefore=12,
)

label_style = ParagraphStyle(
    "Label",
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=14,
    spaceAfter=6,
    spaceBefore=10,
)


def add_page_border(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(2)
    margin = 20
    canvas.rect(margin, margin, PAGE_WIDTH - 2 * margin, PAGE_HEIGHT - 2 * margin)
    canvas.restoreState()


def build_pdf_bytes(
    title: str,
    program_code: str,
    image_bytes: bytes,
    image_name: str,
    image_height_inch: float,
) -> bytes:
    output_buffer = BytesIO()

    doc = SimpleDocTemplate(
        output_buffer,
        pagesize=letter,
        rightMargin=inch,
        leftMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    story = [
        Paragraph(title, heading_style),
        Spacer(1, 6),
        Paragraph("PROGRAM:", label_style),
        Preformatted(program_code, code_style),
        Paragraph("OUTPUT:", label_style),
        Spacer(1, 6),
    ]

    img_reader = ImageReader(BytesIO(image_bytes))
    img_width, img_height = img_reader.getSize()

    max_width = 6.5 * inch
    max_height = image_height_inch * inch
    scale = min(max_width / img_width, max_height / img_height, 1.0)

    draw_width = img_width * scale
    draw_height = img_height * scale

    image_flowable = Image(BytesIO(image_bytes), width=draw_width, height=draw_height)
    image_flowable.hAlign = "LEFT"
    story.append(image_flowable)

    doc.build(story, onFirstPage=add_page_border, onLaterPages=add_page_border)
    output_buffer.seek(0)
    return output_buffer.read()


def main():
    st.set_page_config(page_title="PDF Builder", page_icon="PDF", layout="wide")
    st.title("ReportLab PDF Builder")
    st.caption("Replace title, program, and output image, then download your PDF.")

    col1, col2 = st.columns([1.4, 1])

    with col1:
        title = st.text_input("Title", value="Your Program Title Here")

        program_file = st.file_uploader(
            "Upload program file (.pl/.py/.txt/.java)",
            type=["pl", "py", "txt", "java"],
        )

        default_code = ""
        if program_file is not None:
            try:
                default_code = program_file.getvalue().decode("utf-8")
            except UnicodeDecodeError:
                default_code = program_file.getvalue().decode("latin-1")

        program_code = st.text_area(
            "Program code (editable)",
            value=default_code,
            height=300,
            placeholder="Paste your code here...",
        )

        output_filename = st.text_input("Output PDF filename", value="output.pdf")

    with col2:
        output_image = st.file_uploader(
            "Upload output image",
            type=["png", "jpg", "jpeg", "gif", "bmp", "webp"],
        )

        if output_image is not None:
            st.image(output_image, caption="Output image preview", use_container_width=True)

        size_preset = st.selectbox(
            "Image height preset",
            options=[
                "Small (1.8 inch)",
                "Medium (2.0 inch)",
                "Large (3.2 inch)",
            ],
            index=1,
        )

        if size_preset.startswith("Small"):
            image_height_inch = 1.8
        elif size_preset.startswith("Large"):
            image_height_inch = 3.2
        else:
            image_height_inch = 2.0

    st.divider()

    can_generate = bool(title.strip() and program_code.strip() and output_image is not None)

    if not can_generate:
        st.info("Fill title, program code, and output image to enable PDF generation.")

    if st.button("Generate PDF", type="primary", disabled=not can_generate):
        filename = output_filename.strip() or "output.pdf"
        if not filename.lower().endswith(".pdf"):
            filename = f"{filename}.pdf"

        pdf_bytes = build_pdf_bytes(
            title=title.strip(),
            program_code=program_code,
            image_bytes=output_image.getvalue(),
            image_name=output_image.name,
            image_height_inch=image_height_inch,
        )

        st.success("PDF created successfully.")
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name=Path(filename).name,
            mime="application/pdf",
        )


if __name__ == "__main__":
    main()
