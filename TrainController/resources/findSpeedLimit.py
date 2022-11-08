def get_speed_limit_red(last_stop, direction, distance):
    outside_lights = False
    distance_to_station = 0.0
    match(last_stop):
        case "YARD":
            next_stop = "SHADYSIDE"
            direction = 0
            distance_to_station = 37.5
        case "SHADYSIDE":
            next_stop = "HERRON AVE"
            direction = 0
            distance_to_station = 25
        case "HERRON AVE":
            if direction == 1:
                next_stop = "SHADYSIDE"
                distance_to_station = 37.5
            else:
                next_stop = "SWISSVALE"
                distance_to_station = 50
        case "SWISSVALE":
            if direction == 1:
                next_stop = "HERRON AVE"
                distance_to_station = 25
            else:
                next_stop = "PENN STATION"
                distance_to_station = 25
                if distance > 300:
                    outside_lights = True
        case "PENN STATION":
            if direction == 1:
                next_stop = "SWISSVALE"
                distance_to_station = 50
                if distance > 100:
                    outside_lights = True
            else:
                next_stop = "STEEL PLAZA"
                outside_lights = True
                distance_to_station = 25
        case "STEEL PLAZA":
            outside_lights = True
            if direction == 1:
                next_stop = "PENN STATION"
                distance_to_station = 25
            else:
                next_stop = "FIRST AVE"
                distance_to_station = 25
        case "FIRST AVE":
            outside_lights = True
            if direction == 1:
                next_stop = "STEEL PLAZA"
                distance_to_station = 25
            else:
                next_stop = "STATION SQUARE"
                distance_to_station = 37.5
        case "STATION SQUARE":
            if direction == 1:
                outside_lights = True
                next_stop = "FIRST AVE"
                distance_to_station = 25
            else:
                next_stop = "SOUTH HILLS JUNCTION"
                distance_to_station = 37.5
        case "SOUTH HILLS JUNCTION":
            direction = 1
            next_stop = "STATION SQUARE"
            distance_to_station = 37.5
    insideLights = outside_lights
    return direction, next_stop, outside_lights, insideLights, distance_to_station

def get_speed_limit_green(last_stop, direction, distance):
    outside_lights = False
    distance_to_station = 0
    match(last_stop):
        case "YARD":
            next_stop = "GLENBURY"
            direction = 0
            distance_to_station = 100
        case "GLENBURY":
            if direction == 1:
                next_stop = "OVERBROOK"
                distance_to_station = 25
                if distance > 572:
                    outside_lights = True
            else:
                next_stop = "DORMONT"
                distance_to_station = 50
        case "DORMONT":
            if direction == 1:
                next_stop = "GLENBURY"
                distance_to_station = 81
            else:
                next_stop = "MT LEBANON"
                distance_to_station = 150
        case "MT LEBANON":
            if direction == 1:
                next_stop = "DORMONT"
                distance_to_station = 50
            else:
                next_stop = "POPLAR"
                distance_to_station = 50
        case "POPLAR":
            next_stop = "CASTLE SHANNON"
            distance_to_station = 37.5
        case "CASTLE SHANNON":
            next_stop = "MT LEBANON"
            distance_to_station = 150
            direction = 1
        case "OVERBROOK":
            if direction == 1:
                outside_lights = True
                next_stop = "INGLEWOOD"
                distance_to_station = 25
            else:
                if distance <= 100:
                    outside_lights = True
                next_stop = "GLENBURY"
                distance_to_station = 100
        case "INGLEWOOD":
            if direction == 1:
                next_stop = "CENTRAL"
                outside_lights = True
                distance_to_station = 25
            else:
                outside_lights = True
                next_stop = "OVERBROOK"
                distance_to_station = 25
        case "CENTRAL":
            if direction == 1:
                next_stop = "WHITED"
                distance_to_station = 150
                if distance <= 150:
                    outside_lights = True
            else:
                outside_lights = True
                next_stop = "INGLEWOOD"
                distance_to_station = 25
        case "WHITED":
            if direction == 1:
                next_stop = "STATION"
                distance_to_station = 75
            else:
                next_stop = "SOUTH BANK"
                distance_to_station = 25
        case "SOUTH BANK":
            next_stop = "CENTRAL"
            distance_to_station = 25
            if distance > 250:
                outside_lights = True

        case "STATION":
            if direction == 1:
                next_stop = "EDGEBROOK"
                distance_to_station = 50
            else:
                next_stop = "WHITED"
                distance_to_station = 150
        case "EDGEBROOK":
            next_stop = "PIONEER"
            distance_to_station = 50
        case "PIONEER":
            next_stop = "STATION"
            distance_to_station = 75
            direction = 0
    insideLights = outside_lights
    return direction, next_stop, outside_lights, insideLights, distance_to_station