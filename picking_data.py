import gspread
import os
import time
import re

gc =    gspread.service_account(filename="C:\\Users\\kisho\\Downloads\\inventory_otomation\\inventorysmanagement-4593df092ae4.json")
worksheet =gc.open_by_key("1ttchdhSP_dNQ6hgT-B2yQCDwfN23kUcv_lcZps0KNQk")
surrent_sheet = worksheet.worksheet("RAW DATA")


def picking(ressser,data):
    cell_list = surrent_sheet.findall(ressser)
    asre=str(cell_list)
    sda= asre.replace('[<Cell R','')
    sdaaa= sda.replace("'>]",'')
    sdaaaw= sdaaa.replace(ressser,'')
    sdaa= sdaaaw.replace("'",'')
    row_value= sdaa.replace("C8",'')
    asr=f"{row_value}C"
    reds= asr.replace(' ','')
    coll_value= sdaa.replace(reds,'')
    row_value_int= int(row_value)
    coll_value_int=int(coll_value)
    coll_value_int_update= coll_value_int+3
    rss=surrent_sheet.row_values(row_value_int)
    trr = rss[10]
    sere= f'{trr}'
    if trr == "":
        surrent_sheet.update_cell(row_value_int,coll_value_int_update,data)
        # print("numder not exist")
    elif trr != "":
        sareew= int(trr)
        surrent_sheet.update_cell(row_value_int,coll_value_int_update,sareew+data)
        # print("numder exist")
    

def show_location(ressser):
    cell_list = surrent_sheet.findall(ressser)
    asre=str(cell_list)
    sda= asre.replace('[<Cell R','')
    sdaaa= sda.replace("'>]",'')
    sdaaaw= sdaaa.replace(ressser,'')
    sdaa= sdaaaw.replace("'",'')
    row_value= sdaa.replace("C8",'')
    asr=f"{row_value}C"
    reds= asr.replace(' ','')
    coll_value= sdaa.replace(reds,'')
    row_value_int= int(row_value)
    coll_value_int=int(coll_value)
    coll_value_int_update= coll_value_int+3
    rss=surrent_sheet.row_values(row_value_int)
    asrer = rss[7]
    asresr = rss[12]
    asreer = rss[13]
    rss.remove(asrer)
    rss.remove(asresr)
    rss.remove(asreer)
    return rss
# print(sfjasf)

# haer=show_location("R1-L1-P1-A")
# print(haer)

# pR=(show_location("R50-L1-P1-B"))
# print(pR)
# print(pR[0],pR[1],pR[2],pR[10])
# print(picking("R1-L1-P1-A",5))


