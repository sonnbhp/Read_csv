file = open("test.csv", mode = "r", encoding = "utf8")
file_new = open("test_new.csv", mode = "w", encoding = "utf8")
header = file.readline()
file_new.write(header.strip()+",TB, Rank\n")
row = file.readline()
while row !="" :
    row_list =row.split(",")
    math = float(row_list[2])
    lit = float(row_list[3])
    ave = (math +lit)/2
    ave = round(ave,1)
    if ave >= 8:
        rank = "Good"
    elif ave >= 6 and ave < 8:
        rank = "Mid"
    else:
        rank = "Bad"
    row_new = row.strip()+","+str(ave)+","+rank +"\n"
    print(row_new)
    file_new.write(row_new)
    row = file.readline()
