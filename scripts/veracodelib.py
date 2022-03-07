import os

def get_buildID():
    filereader = open("output.xml", "r")
    readxmlfile = filereader.read()
    result = readxmlfile.split("build_id=",2) #readxml[231:239]
    buildid = (result[1])[1:9]
    print(buildid)

#build_id = get_buildID()

# #os.system('python $GITHUB_WORKSPACE/scripts/buildinfo_xml_extract.py')
#print(build_id)