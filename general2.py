from openpyxl import Workbook
from openpyxl import load_workbook


def create_workbook(project_name):
    wb = Workbook()
    ws = wb.active
    ws.title = "Summary"
    wb.save(filename=project_name+".xlsx")
