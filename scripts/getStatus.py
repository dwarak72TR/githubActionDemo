def get_status():
    filereader = open("output.xml", "r")
    readxmlfile = filereader.read()
    result = readxmlfile.split("status=",2) #readxml[231:239]
    buildid = (result[1])[1:9]
    return buildid


status = get_status()
print(status)

