import re
import os
import csv
write_csv_lines = []
def process(file):
    global write_csv_lines
    tableHead = ['no', 'building', 'room', 'content', 'mobile']
    write_csv_lines.append(tableHead)
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
            addr1 = ""
            addr2 = ""
            comments = ""
            m = re.search("\\D*(\\d{2})(.+)(\\d{3})(.+)", line_content)
            if m:
                addr1 = m.group(1)
                addr2 = m.group(3)
                comments = m.group(4)
                #print("find addr1: %s addr2: %s " % (addr1, addr2))
            else:
                #print("addr not found in line: %d"% line_seq)
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
            print(f"\tParse result,No: {line_no} building#: {addr1}, room: {addr2}, phone num: {phone_num}, comments: {comments}")
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
file = "t1.txt"
if os.path.exists(file):
    process(file)
else:
    print("File: %r is not found" %(file))

write_to_csv()