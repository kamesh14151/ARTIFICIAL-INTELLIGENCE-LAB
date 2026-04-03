from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Preformatted,
    Image,
    PageBreak,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

PAGE_WIDTH, PAGE_HEIGHT = letter


# Draw border on every page.
def add_page_border(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(2)
    margin = 20
    canvas.rect(margin, margin, PAGE_WIDTH - 2 * margin, PAGE_HEIGHT - 2 * margin)
    canvas.restoreState()


# Change filename here.
doc = SimpleDocTemplate(
    "output.pdf",  # Change to your required PDF name (for example: 3-a_TSP.pdf)
    pagesize=letter,
    rightMargin=inch,
    leftMargin=inch,
    topMargin=inch,
    bottomMargin=inch,
)


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


# Paste your program code inside this triple-quoted string.
program_code = """
# paste your code here
print(\"Hello World\")
"""

story = []

# Change title here.
story.append(Paragraph("Your Program Title Here", heading_style))
story.append(Spacer(1, 6))

story.append(Paragraph("PROGRAM:", label_style))
story.append(Preformatted(program_code, code_style))

# Option A: plain text output
# story.append(Paragraph("OUTPUT:", label_style))
# output_text = """your output here"""
# story.append(Preformatted(output_text, code_style))

# Option B: screenshot output
# Put OUTPUT on a new page above the image.
# story.append(PageBreak())
# story.append(Paragraph("OUTPUT:", label_style))
# story.append(Spacer(1, 6))
# story.append(Image("output_screenshot.png", width=6.5 * inch, height=1.8 * inch))
# Height guide:
# 1-2 lines   -> 1.8 * inch
# medium      -> 2.0 * inch
# large/tall  -> 3.2 * inch


doc.build(story, onFirstPage=add_page_border, onLaterPages=add_page_border)
print("PDF created successfully.")
