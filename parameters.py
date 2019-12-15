def serviceValues():
    matchServiceDetails = '(?<=\()(.*?)(?=\))'
    return matchServiceDetails

def dateTime():
    matchdateTime = '\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2},\d{3}'
    return matchdateTime

def timeType():
    typeOfTime = '(?<=\]).{6}'
    return typeOfTime