import xlwings as xw

wb=xw.Book('myWorkbook.xlsx')
st1=wb.sheets['Sheet1']

st1.name = 'Changed name'


wb.save()
