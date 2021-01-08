import openpyxl
excel_files= []
how_many = int(input("How Many files would you like to extract data from?"))
for i in range(0, how_many):
   print("Enter element No-{}: ".format(i+1))
   elm = int(input())
   excel_files.append(elm)

values= []
for file in excel_files:
    wrkbk = openpyxl.load_workbook(file)
    worksheet = wrkbk['Sheet2']
    cell_val = worksheet['K23'].value
    values.append(cell_val)


    print(cell_val)



