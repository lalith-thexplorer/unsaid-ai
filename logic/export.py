from fpdf import FPDF
import datetime

class ReflectionPDF(FPDF):
    def header(self):
        # Premium Header
        self.set_font('Arial', 'B', 20)
        self.set_text_color(50, 50, 50) # Dark Charcoal
        self.cell(0, 15, 'Unsaid', 0, 1, 'L')
        
        self.set_font('Arial', 'I', 10)
        self.set_text_color(100, 100, 100) # Grey
        self.cell(0, 5, 'Reflection Summary', 0, 0, 'L')
        
        # Date on right
        now = datetime.datetime.now().strftime("%B %d, %Y")
        self.cell(0, 5, now, 0, 1, 'R')
        
        # Horizontal Line
        self.set_draw_color(200, 200, 200)
        self.line(10, 35, 200, 35)
        self.ln(20)

    def footer(self):
        self.set_y(-20)
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y() - 2, 200, self.get_y() - 2)
        
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Unsaid provides emotional support only and does not offer medical advice.', 0, 0, 'C')

def generate_pdf_report(mood_history, notes=""):
    """
    Generates a PDF file from the mood history and user notes.
    """
    pdf = ReflectionPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # 1. Mood Section
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(0)
    pdf.cell(0, 10, "Mood Log", 0, 1)
    
    pdf.set_font("Arial", size=11)
    if not mood_history:
        pdf.set_text_color(100)
        pdf.cell(0, 10, "No recent data available.", 0, 1)
    else:
        # Table-like structure
        pdf.set_fill_color(245, 245, 245)
        pdf.set_font("Arial", 'B', 10)
        pdf.cell(40, 8, "Timestamp", 0, 0, 'L', 1)
        pdf.cell(0, 8, "Emotions", 0, 1, 'L', 1)
        
        pdf.set_font("Arial", size=10)
        pdf.set_text_color(50)
        
        for i, entry in enumerate(mood_history[-15:]): # Last 15 entries
            ts = entry['timestamp'].strftime("%H:%M")
            moods = ", ".join(entry['moods'])
            
            # Alternating rows
            fill = True if i % 2 != 0 else False
            if fill:
                pdf.set_fill_color(250, 250, 250)
            
            pdf.cell(40, 8, ts, 0, 0, 'L', fill)
            pdf.cell(0, 8, moods, 0, 1, 'L', fill)
            
    pdf.ln(10)

    # 2. Reflection Notes
    if notes:
        pdf.set_font("Arial", 'B', 14)
        pdf.set_text_color(0)
        pdf.cell(0, 10, "Your Notes", 0, 1)
        
        pdf.set_font("Arial", size=11)
        pdf.set_text_color(50)
        
        # Draw a light box for notes
        pdf.set_fill_color(252, 252, 252)
        pdf.set_draw_color(230, 230, 230)
        pdf.multi_cell(0, 8, notes, 1, 'L', True)
        pdf.ln(10)

    # Return as bytes
    return pdf.output(dest='S').encode('latin-1')
