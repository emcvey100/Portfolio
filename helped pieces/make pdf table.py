data = [
    ['Name','Emily', 'Alex', 'Izzy'],
    ['Age','17', '17', '16'],
    ['No Alevels', '4', '3', '4']
    ]
fileName='pdfTable.pdf'

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter

pdf = SimpleDocTemplate(
    fileName,
    pagesize=letter
    )
from reportlab.platypus import Table
table = Table(data)

from reportlab.platypus import TableStyle
from reportlab.lib import colors

style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.green),
    ('TEXTCOLOR', (0,0),(-1,0), colors.whitesmoke),
    ('ALIGN', (0,0),(-1,-1),'CENTER'),
    ('FONTNAME', (0,0),(-1,0), 'Courier-Bold'),
    ('FONTSIZE', (0,0),(-1,0), 14),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ])
table.setStyle(style)
ts=TableStyle([
    ('BOX',(0,0),(-1,-1),2,colors.black),
    ('LINEBEFORE', (2,1), (2,-1),2,colors.red),
    ('LINEABOVE', (2,1), (2,-1),2,colors.green),
    ]
              )
table.setStyle(ts)

rowNumb=len(data)

elems=[]
elems.append(table)
for i in range(rowNumb):
    if i%2==0:
        bc =colors.burlywood
    else:
        bc=colors.beige
    ts = TableStyle(
        [('BACKGROUND', (0,i), (-1,i), bc)]
        )
    table.setStyle(ts)


pdf.build(elems)
