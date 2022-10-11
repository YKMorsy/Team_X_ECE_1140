def getSpeedLimitRed(lastStop, direction, distance):
    outsideLights = False
    match(lastStop):
        case "YARD":
            speedLimit = 40
            nextStop = "SHADYSIDE"
            direction = 0
        case "SHADYSIDE":
            speedLimit = 40
            nextStop = "HERRON AVE"
            direction = 0
        case "HERRON AVE":
            speedLimit = 40
            if direction == 1:
                nextStop = "SHADYSIDE"
            else:
                nextStop = "SWISSVALE"
                if distance > 50 and distance <= 250 or distance > 1250:
                    speedLimit = 55
                elif distance > 250:
                    speedLimit = 70
        case "SWISSVALE":
            speedLimit = 55
            if direction == 1:
                nextStop = "HERRON AVE"
                if distance > 50 and distance <= 250 or distance > 1250:
                    speedLimit = 55
                elif distance > 250:
                    speedLimit = 70
            else:
                nextStop = "PENN STATION"
                if distance > 300:
                    outsideLights = True
                    speedLimit = 70
        case "PENN STATION":
            speedLimit = 70
            if direction == 1:
                nextStop = "SWISSVALE"
                if distance > 100:
                    speedLimit = 55
                    outsideLights = True
            else:
                nextStop = "STEEL PLAZA"
                outsideLights = True
        case "STEEL PLAZA":
            speedLimit = 70
            outsideLights = True
            if direction == 1:
                nextStop = "PENN STATION"
            else:
                nextStop = "FIRST AVE"
        case "FIRST AVE":
            outsideLights = True
            speedLimit = 70
            if direction == 1:
                nextStop = "STEEL PLAZA"
            else:
                nextStop = "STATION SQUARE"
        case "STATION SQUARE":
            speedLimit = 70
            if direction == 1:
                outsideLights = True
                nextStop = "FIRST AVE"
            else:
                nextStop = "SOUTH HILLS JUNCTION"
                if distance > 75 and distance <= 175:
                    speedLimit = 60
                elif distance > 175:
                    speedLimit = 55
        case "SOUTH HILLS JUNCTION":
            direction = 1
            nextStop = "STATION SQUARE"
            speedLimit = 55
            if distance > 618.2:
                speedLimit = 60
    insideLights = outsideLights
    return speedLimit, direction, nextStop, outsideLights, insideLights

def getSpeedLimitGreen(lastStop, direction, distance):
    outsideLights = False
    match(lastStop):
        case "YARD":
            nextStop = "GLENBURY"
            speedLimit = 70
            direction = 0
        case "GLENBURY":
            if direction == 1:
                speedLimit = 30
                nextStop = "OVERBROOK"
                if distance > 362 and distance <= 572:
                    speedLimit = 15
                elif distance > 572:
                    speedLimit = 20
                    outsideLights = True
            else:
                speedLimit = 40
                nextStop = "DORMONT"
                if distance > 400:
                    speedLimit = 40
        case "DORMONT":
            if direction == 1:
                speedLimit = 28
                nextStop = "GLENBURY"
                if distance > 490:
                    speedLimit = 30
            else:
                speedLimit = 40
                nextStop = "MT LEBANON"
                if distance > 400:
                    speedLimit = 70
        case "MT LEBANON":
            speedLimit = 70
            if direction == 1:
                nextStop = "DORMONT"
                if distance > 300 and distance <= 335:
                    speedLimit = 26
                elif distance > 225:
                    speedLimit = 28
            else:
                nextStop = "POPLAR"
                if distance > 2700:
                    speedLimit = 25
        case "POPLAR":
            speedLimit = 25
            nextStop = "CASTLE SHANNON"
        case "CASTLE SHANNON":
            speedLimit = 25
            nextStop = "MT LEBANON"
            direction = 1
            if distance > 490:
                speedLimit = 70
        case "OVERBROOK":
            speedLimit = 20
            if direction == 1:
                outsideLights = True
                nextStop = "INGLEWOOD"
            else:
                speedLimit = 30
                if distance > 350:
                    speedLimit = 70
                if distance <= 100:
                    outsideLights = True
                nextStop = "GLENBURY"
        case "INGLEWOOD":
            speedLimit = 20
            if direction == 1:
                nextStop = "CENTRAL"
                outsideLights = True
            else:
                speedLimit = 30
                outsideLights = True
                nextStop = "OVERBROOK"
        case "CENTRAL":
            speedLimit = 30
            if direction == 1:
                speedLimit = 20
                nextStop = "WHITED"
                if distance > 659 and distance <= 809:
                    speedLimit = 30
                elif distance > 809:
                    speedLimit = 70
                if distance <= 150:
                    outsideLights = True
            else:
                outsideLights = True
                nextStop = "INGLEWOOD"
        case "WHITED":
            speedLimit = 70
            if direction == 1:
                nextStop = "STATION"
                if distance > 600 and distance <= 1200:
                    speedLimit = 60
            else:
                nextStop = "SOUTH BANK"
                if distance > 1200:
                    speedLimit = 30
        case "SOUTH BANK":
            speedLimit = 30
            nextStop = "CENTRAL"
            if distance > 250:
                outsideLights = True

        case "STATION":
            speedLimit = 70
            if direction == 1:
                nextStop = "EDGEBROOK"
                if distance > 600:
                    speedLimit = 45
            else:
                nextStop = "WHITED"
                if distance > 150 and distance <= 750:
                    speedLimit = 60
        case "EDGEBROOK":
            speedLimit = 45
            nextStop = "PIONEER"
        case "PIONEER":
            speedLimit = 45
            nextStop = "STATION"
            direction = 0
            if distance > 300:
                speedLimit = 70
    insideLights = outsideLights
    return speedLimit, direction, nextStop, outsideLights, insideLights