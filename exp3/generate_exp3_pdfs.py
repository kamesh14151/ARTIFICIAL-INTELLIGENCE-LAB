from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    Image,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
)

PAGE_WIDTH, PAGE_HEIGHT = letter
ROOT = Path(__file__).resolve().parent


def add_page_border(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(2)
    margin = 20
    canvas.rect(margin, margin, PAGE_WIDTH - 2 * margin, PAGE_HEIGHT - 2 * margin)
    canvas.restoreState()


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


def build_pdf(output_pdf, title, program_path, output_image_path, image_height_inch):
    program_code = program_path.read_text(encoding="utf-8")

    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=letter,
        rightMargin=inch,
        leftMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    story = []
    story.append(Paragraph(title, heading_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("PROGRAM:", label_style))
    story.append(Preformatted(program_code, code_style))

    story.append(Paragraph("OUTPUT:", label_style))
    story.append(Spacer(1, 6))

    max_width = 6.5 * inch
    max_height = image_height_inch * inch
    img_reader = ImageReader(str(output_image_path))
    img_width, img_height = img_reader.getSize()

    # Preserve aspect ratio and allow mild upscaling so screenshots are readable.
    scale = min(max_width / img_width, max_height / img_height, 1.35)
    draw_width = img_width * scale
    draw_height = img_height * scale

    image_flowable = Image(
        str(output_image_path),
        width=draw_width,
        height=draw_height,
    )
    image_flowable.hAlign = "LEFT"
    story.append(image_flowable)

    doc.build(story, onFirstPage=add_page_border, onLaterPages=add_page_border)


def main():
    jobs = [
        {
            "folder": "3-a-simple-facts",
            "title": "3-a Simple Facts in Prolog",
            "program": "programs/first-order.pl",
            "image": "output-images/3-a-simple-facts-output.png",
            "pdf": "3-a_SimpleFacts.pdf",
            "height": 3.0,
        },
        {
            "folder": "3-b-family-facts",
            "title": "3-b Family Facts in Prolog",
            "program": "programs/family-facts.pl",
            "image": "output-images/3-b-family-facts-output.png",
            "pdf": "3-b_FamilyFacts.pdf",
            "height": 3.0,
        },
        {
            "folder": "3-c-monkey-banana",
            "title": "3-c Monkey Banana in Prolog",
            "program": "programs/monkey-banana.pl",
            "image": "output-images/3-c-monkey-banana-output.png",
            "pdf": "3-c_MonkeyBanana.pdf",
            "height": 3.0,
        },
        {
            "folder": "3-d-arithmetic",
            "title": "3-d Arithmetic in Prolog",
            "program": "programs/arithmetic.pl",
            "image": "output-images/3-d-arithmetic-output.png",
            "pdf": "3-d_Arithmetic.pdf",
            "height": 3.0,
        },
        {
            "folder": "3-e-facorial",
            "title": "3-e Factorial in Prolog",
            "program": "programs/factorial.pl",
            "image": "output-images/3-e-facorial-output.png",
            "pdf": "3-e_Factorial.pdf",
            "height": 3.0,
        },
        {
            "folder": "3-f-fibonacci",
            "title": "3-f Fibonacci in Prolog",
            "program": "programs/Fibonacci.pl",
            "image": "output-images/3-f-fibonacci-output.png",
            "pdf": "3-f_Fibonacci.pdf",
            "height": 3.0,
        },
        {
            "folder": "3-g-toh",
            "title": "3-g Tower of Hanoi in Prolog",
            "program": "programs/toh.pl",
            "image": "output-images/toh-output.png",
            "pdf": "3-g_TOH.pdf",
            "height": 3.0,
        },
        {
            "folder": "3-h-water-jug",
            "title": "3-h Water Jug in Prolog",
            "program": "programs/water-jug.pl",
            "image": "output-images/3-h-water-jug-output.png",
            "pdf": "3-h_WaterJug.pdf",
            "height": 3.0,
        },
    ]

    for job in jobs:
        exp_dir = ROOT / job["folder"]
        xerox_dir = exp_dir / "xerox"
        xerox_dir.mkdir(exist_ok=True)

        program_path = exp_dir / job["program"]
        image_path = exp_dir / job["image"]
        output_pdf = xerox_dir / job["pdf"]

        build_pdf(
            output_pdf=output_pdf,
            title=job["title"],
            program_path=program_path,
            output_image_path=image_path,
            image_height_inch=job["height"],
        )
        print(f"Created: {output_pdf}")


if __name__ == "__main__":
    main()
