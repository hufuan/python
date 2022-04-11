import re
import os
import csv
write_csv_lines = []
def process(file):
    global write_csv_lines
    tableHead = ['no','area', 'builder', 'room', 'content', 'mobile']
    write_csv_lines.append(tableHead)
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
            #print(f'line_content = {line_content}')
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
            m = re.search("\\D*(\\d{1,3})(\\D+)(\\d{3,4})\\s*\\u5ba4?\\s*(.*)", line_content)
            if '期' in line_content:
                m = re.search("\\u671f\\D*(\\d{1,3})(\\D+)(\\d{3,4})\\s*\\u5ba4?\\s*(.*)", line_content)
            if '联排' in line_content:
                m = re.search("\\u671f?\\D*(\\d{1,3})(\\D+)(\\u8054\\u6392)\\s*\\u5ba4?\\s*(.*)", line_content)
                print("handling lian pai")
            if m:
                addr1 = m.group(1)
                addr2 = m.group(3)
                comments = m.group(4)
                #print("find addr1: %s addr2: %s " % (addr1, addr2))
            else:
                #print("addr not found in line: %d"% line_seq)
                m = re.search("\\u671f?\\D*(\\d{1,3})\\u53f7(.*)", line_content)
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
            write_csv_lines.append(csv_columns)
            line_seq += 1
        print("Done!")

def write_to_csv():
    outputFileName = "ouput.csv"
    csvfile=open(outputFileName, 'w',encoding='utf-8-sig')
    csvWriter = csv.writer(csvfile, lineterminator='\n')
    for line in write_csv_lines:
        csvWriter.writerow(line)
    csvfile.close()
file = "t2.txt"
if os.path.exists(file):
    process(file)
else:
    print("File: %r is not found" %(file))

write_to_csv()