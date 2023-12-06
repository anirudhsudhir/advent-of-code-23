secondInputData = {40709879:215105121471005}

totalRecordBreaks = 1

for time in secondInputData:
    speed = 0
    recordBreaks = 0
    timeRange = range(1,time)
    for buttonTime in timeRange:
        speed += 1
        travelTime = time - buttonTime
        distanceTravelled = travelTime * speed
        if distanceTravelled > secondInputData[time]:
            recordBreaks += 1
    if recordBreaks >= 1:
        totalRecordBreaks *= recordBreaks

print(totalRecordBreaks)