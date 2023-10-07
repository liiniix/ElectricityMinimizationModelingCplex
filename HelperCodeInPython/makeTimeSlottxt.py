from datetime import timedelta, time, datetime, timedelta, date

def makeTimeSlots():
    loopingTime = time(0, 0)
    print(loopingTime
                .strftime("%I:%M %p"),
        end="--------")


    for i in range(96):
        loopingTime = (datetime.combine(date.today(),
                                        loopingTime)
                    + timedelta(minutes=15)
                    )\
                    .time()

        print(loopingTime
                .strftime("%I:%M %p"),
            end="--------")

def makeTimeSlotIndices():
    for i in range(96):
        print(f"{i+1:02d}", end="-------------]")


def showPeakAndOffPeakHours():
    loopingTime = time(0, 0)
    print(loopingTime
                .strftime("%I:%M %p"),
        end="")


    for i in range(96):
        isInPeakHours = (time(6, 0) <= loopingTime and loopingTime < time(9, 0))\
                        or\
                        (time(17, 0) <= loopingTime and loopingTime < time(22, 0))

        print("++++++++" if isInPeakHours
                else "--------",
                end="")

        loopingTime = (datetime.combine(date.today(),
                                        loopingTime)
                    + timedelta(minutes=15)
                    )\
                    .time()

        print(loopingTime
                .strftime("%I:%M %p"),
            end="")

def isThisTimeSlotInPeakHours(formatted=True):
    loopingTime = time(0, 0)
    if formatted:
        print(loopingTime
                    .strftime("%I:%M %p"),
            end="")

    oneString =  "+++1++++" if formatted\
                            else "1 "
    zeroString = "---0----" if formatted\
                            else "0 "

    for i in range(96):
        isInPeakHours = (time(6, 0) <= loopingTime and loopingTime < time(9, 0))\
                        or\
                        (time(17, 0) <= loopingTime and loopingTime < time(22, 0))

        
        print(oneString if isInPeakHours
                        else zeroString,
                        end="")

        loopingTime = (datetime.combine(date.today(),
                                        loopingTime)
                    + timedelta(minutes=15)
                    )\
                    .time()
        if formatted:
            print(loopingTime
                    .strftime("%I:%M %p"),
                end="")


def isFridgeOnInThisTimeSlot(formatted=True):
    loopingTime = time(0, 0)
    if formatted:
        print(loopingTime
                    .strftime("%I:%M %p"),
            end="")

    fifteenMinutesOscillationTrack = 0

    onString  = "@@@@@@@@" if formatted\
                           else "1 "
    offString = "--------" if formatted\
                           else "0 "

    for i in range(96):
        isInPeakHours = (time(6, 0) <= loopingTime and loopingTime < time(9, 0))\
                        or\
                        (time(17, 0) <= loopingTime and loopingTime < time(22, 0))

        if isInPeakHours and fifteenMinutesOscillationTrack % 2 == 0:
            print(onString,  end="")
        else:
            print(offString, end="")
        
        fifteenMinutesOscillationTrack += 1

        loopingTime = (datetime.combine(date.today(),
                                        loopingTime)
                    + timedelta(minutes=15)
                    )\
                    .time()

        if formatted:
            print(loopingTime
                    .strftime("%I:%M %p"),
                end="")

def isEverybodyOutHomeInThisTimeSlot(formatted=True):
    loopingTime = time(0, 0)
    if formatted:
        print(loopingTime
                    .strftime("%I:%M %p"),
            end="")


    outHomeString  = "????????" if formatted\
                           else "1 "
    inHomeString = "--------" if formatted\
                           else "0 "

    for i in range(96):
        isInOutHomeHours = (time(9, 0) <= loopingTime and loopingTime < time(17, 0))

        print(outHomeString if isInOutHomeHours\
                else inHomeString,  end="")
        
        loopingTime = (datetime.combine(date.today(),
                                        loopingTime)
                    + timedelta(minutes=15)
                    )\
                    .time()

        if formatted:
            print(loopingTime
                    .strftime("%I:%M %p"),
                end="")

print("timeSlots:                                 ", end="");       makeTimeSlots()
print()
print("timeSlotIndices:                           ", end="");       makeTimeSlotIndices()
print()
print("Peak&OffPeak:                              ", end="");       showPeakAndOffPeakHours()
print()
print("isFridgeOnInThisTimeSlot:                  ", end="");       isFridgeOnInThisTimeSlot()
print()
print("isFridgeOnInThisTimeSlot[ForCode]:         ", end="");       isFridgeOnInThisTimeSlot(False)
print()
print("isThisTimeSlotInPeakHours:                 ", end="");       isThisTimeSlotInPeakHours()
print()
print("isThisTimeSlotInPeakHours[ForCode:         ", end="");       isThisTimeSlotInPeakHours(False)
print()
print("isEverybodyOutHomeInThisTimeSlot           ", end="");       isEverybodyOutHomeInThisTimeSlot(formatted=True)
print()
print("isEverybodyOutHomeInThisTimeSlot[ForCode]  ", end="");       isEverybodyOutHomeInThisTimeSlot(formatted=True)