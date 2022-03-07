
from matplotlib.pyplot import get


def get_buildID():
    filereader = open("output.xml", "r")
    readxmlfile = filereader.read()
    result = readxmlfile.split("build_id=",2) #readxml[231:239]
    buildid = (result[1])[1:9]
    return buildid


build_id = get_buildID()
print(build_id)

