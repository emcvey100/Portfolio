import xlwings as xw

wb=xw.Book('myWorkbook.xlsx')
st1=wb.sheets['Cool']
st1.range('B1').value=[1,2,3]
st1.range('A2').options(
    transpose=True
    ).value=[1,2,3]
dataCells=st1.range('B2:D4')
for cell in dataCells:
    address=cell.address[1:].split('$')
    column=address[0]
    row=address[1]
    cell.value=f'=A{row}*{column}1'
    
wb.save()
