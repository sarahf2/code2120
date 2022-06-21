from flask import Flask
from rhino3dm import *
from openpyxl.workbook import Workbook

wb=Workbook()
ws=wb.active

ws.title="Week 4 website"

ws['A1']='Welcome!'
c=ws['A1']
print(c.value)

wb.save("Week 4.xlsx")

###

app=Flask(__name__)

@app.route('/')
def hello_world():
	return c.value

