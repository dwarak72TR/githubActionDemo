def get_score():
    filereader = open("summaryreport.xml", "r")
    readxmlfile = filereader.read()
    result = readxmlfile.split("score=",2) #readxml[231:239]
    score = (result[1])[1:3]
    return score

score = get_score()
print(score)