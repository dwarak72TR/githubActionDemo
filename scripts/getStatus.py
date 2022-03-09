def get_status():
    filereader = open("output.xml", "r")
    readxmlfile = filereader.read()
    result = readxmlfile.split("published_date_sec=",2) #readxml[231:239]
    result2 = result[1]
    status = result2.split("status=",2)
    return status[1].split("/>",2)


status = get_status()
print(status)

