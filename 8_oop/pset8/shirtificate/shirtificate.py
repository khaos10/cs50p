from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", size=46)
        self.set_y(30)
        self.cell(w=self.epw, txt="CS50 Shirtificate", align="C")
        self.ln()

    def print_image(self, image):
        self.image(image, y=70, w=self.epw)

    def print_text(self, name):
        self.set_font("helvetica", size=24)
        self.set_text_color(255, 255, 255)
        self.set_y(140)
        self.cell(w=self.epw, txt=f"{name} took CS50", align="C")


def main():
    pdf = PDF()
    pdf.add_page()
    pdf.print_image("shirtificate.png")
    pdf.print_text(input("Name: "))
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
