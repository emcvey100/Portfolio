import xlwings as xw

wb=xw.Book('myWorkbook.xlsx')
st1=wb.sheets['Sheet1']

white=(255,255,255)
blue=(31, 73, 125)
yellow=(255, 192, 0)

rowHeader=st1.range("B1:D1")
colHeader=st1.range("A2:A4")

rowHeader.api.Font.Bold=True
colHeader.api.Font.Bold=True

rowHeader.color = blue
colHeader.color = blue

B6 = st1.range('B6')
C6 = st1.range('C6')
D6 = st1.range('D6')
E6 = st1.range('E6')

dataCells=st1.range('B2:D4')

dataCells.api.Borders(1).Weight = 3#L
dataCells.api.Borders(2).Weight = 3#R
dataCells.api.Borders(3).Weight = 3#T
dataCells.api.Borders(4).Weight = 3#B


dataCells.color = yellow

allCells = st1.range('A1:D4')
center = xw.constants.HAlign.xlHAlignCenter
allCells.api.HorizontalAlignment = center



wb.save()
