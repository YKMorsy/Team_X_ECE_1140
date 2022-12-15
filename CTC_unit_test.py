
from CTC_App.Iteration3.Line import Line
from CTC_App.Iteration3.Dispatcher import Dispatcher

if __name__ == '__main__':

    # Green Line Unit Testing

    # Load green line track
    green_line = Line("./CTC_App/Iteration3/Track_Layout_Green.xlsx")

    # check route
    green_route = green_line.getRoute()
    assert(green_route == [0, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 
                        74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 
                        87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 
                        100, 85, 84, 83, 82, 81, 80, 79, 78, 77, 101, 102, 
                        103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 
                        113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 
                        123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 
                        134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 
                        145, 146, 147, 148, 149, 150, 29, 28, 27, 26, 25, 24, 
                        23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 
                        9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 14, 15, 16, 17, 18, 19, 
                        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 
                        34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 
                        48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 0])

    # check block status
    green_line.setBlockStatus({1003: False})
    assert(green_line.getClosedBlocks() == [3])
    green_line.setBlockStatus({1003: True})
    assert(green_line.getClosedBlocks() == [])

    # check crossing state
    green_line.setRailWayCrossing({1019: True})
    assert(green_line.getCrossingState() == [[19, True]])
    green_line.setRailWayCrossing({1019: False})
    assert(green_line.getCrossingState() == [[19, False]])

    # check switch state
    green_line.setSwitchPosition({1013: True, 1029: True, 1057: True, 1063: True, 1077: True, 1085: True})
    assert(green_line.getSwitchState() == [[13, 12], [29, 150], [57, 58], [63, 62], [77, 101], [85, 100]])
    green_line.setSwitchPosition({1013: False, 1029: False, 1057: False, 1063: False, 1077: False, 1085: False})
    assert(green_line.getSwitchState() == [[13, 1], [29, 30], [57, 0], [63, 0], [77, 76], [85, 86]])

    # Dispatcher Unit Testing

    # create dispatcher
    dispatcher = Dispatcher()

    # check schedule
    dispatcher.scheduleSingle([1, 3, 4, 5, 6], green_line)
    assert(dispatcher.all_trains[0].station_list == [1, 3, 4, 5, 6])

    # check update station
    dispatcher.scheduleSingle([1, 3, 5, 6], green_line)
    assert(dispatcher.all_trains[1].station_list == [1, 3, 5, 6])
    dispatcher.updateStations(1, [1, 3, 4, 5, 6])
    assert(dispatcher.all_trains[1].station_list == [1, 3, 4, 5, 6])

    # Red Line Unit Testing

    # Load green line track
    red_line = Line("./CTC_App/Iteration3/Track_Layout_Red.xlsx")

    # check route
    red_route = red_line.getRoute()
    assert(red_route == [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 
                        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
                        32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 
                        44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 
                        56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 52, 
                        51, 50, 49, 48, 47, 46, 45, 44, 67, 68, 69, 70, 
                        71, 38, 37, 36, 35, 34, 33, 72, 73, 74, 75, 76, 
                        27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 
                        1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    # check block status
    red_line.setBlockStatus({2003: False})
    assert(red_line.getClosedBlocks() == [3])
    red_line.setBlockStatus({2003: True})
    assert(red_line.getClosedBlocks() == [])

    # check crossing state
    red_line.setRailWayCrossing({2047: True})
    assert(red_line.getCrossingState() == [[47, True]])
    red_line.setRailWayCrossing({2047: False})
    assert(red_line.getCrossingState() == [[47, False]])

    # check switch state
    red_line.setSwitchPosition({2009: True, 2016: True, 2027: True, 2033: True, 2038: True, 2044: True, 2052: True})
    assert(red_line.getSwitchState() == [[9, 10], [16, 15], [27, 76], [33, 72], [38, 71], [44, 67], [52, 66]])
    red_line.setSwitchPosition({2009: False, 2016: False, 2027: False, 2033: False, 2038: False, 2044: False, 2052: False})
    assert(red_line.getSwitchState() == [[9, 0], [16, 1], [27, 28], [33, 32], [38, 39], [44, 43], [52, 53]])

    # Dispatcher Unit Testing

    # check schedule
    dispatcher.scheduleSingle([1, 3, 4, 5, 6], red_line)
    assert(dispatcher.all_trains[2].station_list == [1, 3, 4, 5, 6])

    # check update station
    dispatcher.scheduleSingle([1, 3, 5, 6], red_line)
    assert(dispatcher.all_trains[3].station_list == [1, 3, 5, 6])
    dispatcher.updateStations(3, [1, 3, 4, 5, 6])
    assert(dispatcher.all_trains[3].station_list == [1, 3, 4, 5, 6])