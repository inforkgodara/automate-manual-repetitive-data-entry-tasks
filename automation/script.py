import pyautogui
import pandas
import time

# Read data from excel
excel_data = pandas.read_excel('Sales Orders.xlsx', sheet_name='Orders')
count = 0
time.sleep(5)
# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():

    pyautogui.typewrite(excel_data['Order ID'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Order Date'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Ship Date'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Ship Mode'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Customer ID'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Customer Name'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Segment'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['City'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['State'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Region'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Product ID'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Product Name'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Category'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(excel_data['Sub Category'][count])
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['Sales'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['Quantity'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['Discount'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['Profit'][count]))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('tab')
    time.sleep(1)
    if count == 9:
        break;
    count = count + 1
