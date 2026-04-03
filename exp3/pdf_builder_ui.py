import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Image, Paragraph, Preformatted, SimpleDocTemplate, Spacer

PAGE_WIDTH, PAGE_HEIGHT = letter


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


class PDFBuilderUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ReportLab PDF Builder")
        self.root.geometry("980x760")

        self.title_var = tk.StringVar(value="Your Program Title Here")
        self.program_file_var = tk.StringVar(value="")
        self.image_file_var = tk.StringVar(value="")
        self.output_pdf_var = tk.StringVar(value="output.pdf")
        self.size_var = tk.StringVar(value="Slightly Big (2.8 inch)")

        self._build_ui()

    def _build_ui(self):
        pad = {"padx": 10, "pady": 6}

        main = ttk.Frame(self.root)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="PDF Title:").grid(row=0, column=0, sticky="w", **pad)
        ttk.Entry(main, textvariable=self.title_var, width=85).grid(
            row=0, column=1, columnspan=3, sticky="ew", **pad
        )

        ttk.Label(main, text="Program File (.pl/.py/etc):").grid(
            row=1, column=0, sticky="w", **pad
        )
        ttk.Entry(main, textvariable=self.program_file_var, width=70).grid(
            row=1, column=1, sticky="ew", **pad
        )
        ttk.Button(main, text="Browse", command=self.browse_program).grid(
            row=1, column=2, sticky="ew", **pad
        )
        ttk.Button(main, text="Load into Editor", command=self.load_program_code).grid(
            row=1, column=3, sticky="ew", **pad
        )

        ttk.Label(main, text="Program Code (editable):").grid(
            row=2, column=0, sticky="nw", **pad
        )
        self.code_text = tk.Text(main, wrap="none", height=18, font=("Courier", 10))
        self.code_text.grid(row=2, column=1, columnspan=3, sticky="nsew", **pad)

        ttk.Label(main, text="Output Image:").grid(row=3, column=0, sticky="w", **pad)
        ttk.Entry(main, textvariable=self.image_file_var, width=70).grid(
            row=3, column=1, sticky="ew", **pad
        )
        ttk.Button(main, text="Browse", command=self.browse_image).grid(
            row=3, column=2, sticky="ew", **pad
        )

        ttk.Label(main, text="Image Height Preset:").grid(
            row=4, column=0, sticky="w", **pad
        )
        ttk.Combobox(
            main,
            textvariable=self.size_var,
            values=[
                "Small (1.8 inch)",
                "Medium (2.4 inch)",
                "Slightly Big (2.8 inch)",
                "Large (3.2 inch)",
            ],
            state="readonly",
            width=30,
        ).grid(row=4, column=1, sticky="w", **pad)

        ttk.Label(main, text="Output PDF File:").grid(row=5, column=0, sticky="w", **pad)
        ttk.Entry(main, textvariable=self.output_pdf_var, width=70).grid(
            row=5, column=1, sticky="ew", **pad
        )
        ttk.Button(main, text="Save As", command=self.choose_output_pdf).grid(
            row=5, column=2, sticky="ew", **pad
        )

        ttk.Button(main, text="Generate PDF", command=self.generate_pdf).grid(
            row=6, column=1, sticky="ew", padx=10, pady=16
        )

        help_text = (
            "How to use:\n"
            "1) Set title\n"
            "2) Load or paste program code\n"
            "3) Select output screenshot image\n"
            "4) Choose output pdf name\n"
            "5) Click Generate PDF"
        )
        ttk.Label(main, text=help_text, foreground="#333333", justify="left").grid(
            row=7, column=0, columnspan=4, sticky="w", padx=10, pady=8
        )

        main.columnconfigure(1, weight=1)
        main.columnconfigure(2, weight=0)
        main.columnconfigure(3, weight=0)
        main.rowconfigure(2, weight=1)

    def browse_program(self):
        path = filedialog.askopenfilename(
            title="Select Program File",
            filetypes=[("Code Files", "*.pl *.py *.txt *.java"), ("All Files", "*.*")],
        )
        if path:
            self.program_file_var.set(path)

    def load_program_code(self):
        path = self.program_file_var.get().strip()
        if not path:
            messagebox.showwarning("Missing Program File", "Please choose a program file.")
            return

        try:
            content = Path(path).read_text(encoding="utf-8")
            self.code_text.delete("1.0", tk.END)
            self.code_text.insert("1.0", content)
        except Exception as exc:
            messagebox.showerror("Error", f"Unable to load file:\n{exc}")

    def browse_image(self):
        path = filedialog.askopenfilename(
            title="Select Output Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All Files", "*.*")],
        )
        if path:
            self.image_file_var.set(path)

    def choose_output_pdf(self):
        path = filedialog.asksaveasfilename(
            title="Save PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            initialfile=self.output_pdf_var.get().strip() or "output.pdf",
        )
        if path:
            self.output_pdf_var.set(path)

    def _height_inches(self):
        value = self.size_var.get()
        if value.startswith("Small"):
            return 1.8
        if value.startswith("Slightly Big"):
            return 2.8
        if value.startswith("Large"):
            return 3.2
        return 2.4

    def generate_pdf(self):
        title = self.title_var.get().strip()
        program_code = self.code_text.get("1.0", tk.END).rstrip()
        image_path = self.image_file_var.get().strip()
        output_pdf = self.output_pdf_var.get().strip()

        if not title:
            messagebox.showwarning("Missing Title", "Please enter a title.")
            return
        if not program_code:
            messagebox.showwarning("Missing Program", "Please load or paste program code.")
            return
        if not image_path:
            messagebox.showwarning("Missing Image", "Please choose an output image.")
            return
        if not output_pdf:
            messagebox.showwarning("Missing Output PDF", "Please enter output PDF file name.")
            return

        image_file = Path(image_path)
        output_file = Path(output_pdf)

        if not image_file.exists():
            messagebox.showerror("Image Not Found", f"Image file not found:\n{image_file}")
            return

        if not output_file.is_absolute():
            output_file = Path.cwd() / output_file

        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)

            doc = SimpleDocTemplate(
                str(output_file),
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

            max_width = 6.5 * inch
            max_height = self._height_inches() * inch
            img_reader = ImageReader(str(image_file))
            img_width, img_height = img_reader.getSize()

            # Allow moderate upscaling so screenshots are easier to read.
            scale = min(max_width / img_width, max_height / img_height, 1.35)
            draw_width = img_width * scale
            draw_height = img_height * scale

            image_flowable = Image(str(image_file), width=draw_width, height=draw_height)
            image_flowable.hAlign = "LEFT"
            story.append(image_flowable)

            doc.build(story, onFirstPage=add_page_border, onLaterPages=add_page_border)
            messagebox.showinfo("Success", f"PDF created successfully:\n{output_file}")
        except Exception as exc:
            messagebox.showerror("Generation Failed", f"Could not generate PDF:\n{exc}")


def main():
    root = tk.Tk()
    PDFBuilderUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
