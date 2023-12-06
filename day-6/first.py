firstInputData = {40:215, 70: 1051, 98:2147, 79:1005}

totalRecordBreaks = 1

for time in firstInputData:
    speed = 0
    recordBreaks = 0
    timeRange = range(1,time)
    for buttonTime in timeRange:
        speed += 1
        travelTime = time - buttonTime
        distanceTravelled = travelTime * speed
        if distanceTravelled > firstInputData[time]:
            recordBreaks += 1
    if recordBreaks >= 1:
        totalRecordBreaks *= recordBreaks

print(totalRecordBreaks)