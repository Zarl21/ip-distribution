
def split(filename, filesize)

    f_read = open(filename,"r")

    f_write = open("Data/Split/data_1.csv","w")
    count = 0
    ind = 1
    for line in f_read:  
        if count < filesize:
            f_write.write(line)
        elif count == filesize:
            ind = ind + 1
            f_write.close()
            f_write = open("Data/Split/data_"+str(ind)+".csv","w")
            f_write.write(line)
            count = -1
        count = count + 1

    f_read.close()
    f_write.close()
    return 1