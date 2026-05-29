import pdfkit

def pdf_yaratish():
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }

    pdfkit.from_string('Siz Google va Meta tajribasiga ega arxitektor-dasturchisiz. Faqat 100% shartlarga javob beradigan, hech qanday Markdown bloklarsiz (```) toza va optimal kod yozasiz. Izoh yozish qatiyan man etiladi.', 'output.pdf', options=options)

pdf_yaratish()
