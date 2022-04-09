import re
import os
import xlwt
excel_filepath_prefix='输出整理文档'
import datetime
"""
"""
write_xls_lines = []
def process(file):
    global write_xls_lines
    validLine = False
    DIST_1 = '一期'
    DIST_1_2 = '1期'
    DIST_2 = '二期'
    DIST_2_2 = '2期'
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_seq = 1
        for line in lines:
            line = line.strip()
            csv_columns = []
            line_no = line.split('.')[0]
            line_content = line[(line.index(".") +1):].strip()
            print(f'line_content = {line_content}')
            csv_columns.append(line_no)
            print("Line#: %d, whole line: %s" %  (line_seq, line))
            area = ""
            if DIST_1 in line_content or DIST_1_2 in line_content or ' 1-' in line_content:
                area = DIST_1
            elif DIST_2 in line_content or DIST_2_2 in line_content or ' 2-' in line_content:
                area = DIST_2
            else:
                print("unknow area")
            csv_columns.append(area)
            addr1 = ""
            addr2 = ""
            comments = ""
            m = re.search("(\\d{1,3})(\\D+)(\\d{3})\\s*\\u5ba4?\\s*(.*)", line_content)
            if '联排' in line_content:
                m = re.search("(\\d{1,3})(\\D+)(\\u8054\\u6392)\\s*\\u5ba4?\\s*(.*)", line_content)
            if m:
                addr1 = m.group(1)
                addr2 = m.group(3)
                comments = m.group(4)
                #print("find addr1: %s addr2: %s " % (addr1, addr2))
            else:
                #print("addr not found in line: %d"% line_seq)
                m = re.search("(\\d{1,3})\\u53f7(.*)", line_content)
                addr1 = m.group(1)
                comments = m.group(2)
                pass

            csv_columns.append(addr1)
            csv_columns.append(addr2)
            csv_columns.append(comments)
            result = re.findall("(86)?(1\\d{10})", line)
            phone_num = ""
            if result != []:
                print(result[0][1])
                phone_num = result[0][1]
            else:
                #print("phone num not found in %s" % line_seq)
                pass
            csv_columns.append(phone_num)
            print(f"\tParse result,No: {line_no} area: {area} building#: {addr1}, room: {addr2}, phone num: {phone_num}, comments: {comments}")
            write_xls_lines.append(csv_columns)
            line_seq += 1
        print("Done!")

def WriteSheetRow(sheet,rowValueList,rowIndex,isHeader):
    i = 0
    #style = xlwt.easyxf('font: bold 1') #bold font
    styleHeadr = xlwt.easyxf('font: name Calibri, bold on, height 280, color blue;align: wrap on, horiz right') #font
    styleBody = xlwt.easyxf('font: name Calibri, height 280, color black;align: wrap on, horiz right')  # font
    for svalue in rowValueList:
        #strValue = unicode(str(svalue),'utf-8')
        if isHeader:
            sheet.write(rowIndex,i,svalue,styleHeadr)
        else:
            sheet.write(rowIndex,i,svalue, styleBody)
        i = i + 1

def addSheet1(workbook):
    sheet_name = '统计'
    sheet = workbook.add_sheet(sheet_name)
    sheet.col(0).width = 256 * 20
    sheet.col(1).width = 256 * 15
    sheet.col(2).width = 256 * 10
    sheet.col(3).width = 256 * 10
    sheet.col(4).width = 256 * 40
    sheet.col(5).width = 256 * 20
    tableHead = ['接龙序号','一期/二期', '楼号', '门牌号', '内容', '手机']
    rowIndex = 0
    WriteSheetRow(sheet, tableHead, rowIndex, True)
    rowIndex = rowIndex + 1

    for line_columns in write_xls_lines:
        WriteSheetRow(sheet, line_columns, rowIndex, False)
        rowIndex = rowIndex + 1
    pass
def write_to_xsl():
    workbook = xlwt.Workbook(encoding='utf-8')
    addSheet1(workbook)
    timeStr = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    file_name = excel_filepath_prefix + " " +  timeStr + ".xls"
    workbook.save(file_name)

file = "输入信息.txt"
if os.path.exists(file):
    process(file)
else:
    print("File: %r is not found" %(file))

write_to_xsl()