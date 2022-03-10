def get_status():
    filereader = open("output.xml", "r")
    readxmlfile = filereader.read()
    result = readxmlfile.split("published_date_sec=",2) 
    print(result[0])
    print(result[1])
    result2 = result[1]
    result3 = result2.split("status=",2)
    finalcheck = result3[1].split("/",2)
    status = finalcheck[0].replace("\"","")  
    return status


status = get_status()
print(status)

