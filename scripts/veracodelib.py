import os
import xml.etree.ElementTree as ET
buildinfo = open("buildinfo.xml", "r")
build_info="<?xml"+buildinfo.read().split("<?xml")[-1]
mytree = ET.ElementTree(ET.fromstring(build_info))
root = mytree.getroot()

os.system('python $GITHUB_WORKSPACE/scripts/buildinfo_xml_extract.py')
print(root.attrib['build_id'])