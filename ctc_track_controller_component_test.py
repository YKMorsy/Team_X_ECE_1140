from CTC_App.Iteration3.Line import Line
from CTC_App.Iteration3.Dispatcher import Dispatcher
from track_controller.sign_in_window import sign_in_window
from track_controller.track_control_controller import track_control_controller
from connect_ctc_track_controller import connect_ctc_track_controller

if __name__ == '__main__':

    # Initialize objects
    controller = track_control_controller()
    trcControl = controller.get_all_track_controllers()
    green_line = Line("./CTC_App/Iteration3/Track_Layout_Green.xlsx")
    red_line = Line("./CTC_App/Iteration3/Track_Layout_Red.xlsx")
    dispatcher = Dispatcher()

    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, False)

    # check if setting authority from ctc updates in track controller (before dispatch)
    trcControl_Authority = trcControl[5].get_authority()
    authority_val = trcControl_Authority[1063]
    assert(authority_val == False)

    # create train, set occupancy in wayside and check train location from dispatcher
    dispatcher.scheduleSingle([1, 3, 4, 5, 6], green_line)
    trcControl[5].set_an_occ(1000, True)
    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, False)
    assert(dispatcher.all_trains[0].current_position == 0)

    trcControl[5].set_an_occ(1063, True)
    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, False)
    assert(dispatcher.all_trains[0].current_position == 63)

    # check if setting authority from ctc updates in track controller (after dispatch)
    trcControl_Authority = trcControl[5].get_authority()
    authority_val = trcControl_Authority[1063]
    assert(authority_val == True)

    # check if track switches from track controller updates in ctc
    trcControl[5].set_a_switch(1077, True)
    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, False)
    assert(green_line.getSwitchState() == [[13, 1], [29, 30], [57, 0], [63, 0], [77, 101], [85, 86]])

    trcControl[5].set_a_switch(1077, False)
    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, False)
    assert(green_line.getSwitchState() == [[13, 1], [29, 30], [57, 0], [63, 0], [77, 76], [85, 86]])

    # check if manual ctc new switches updates in track controller
    green_line.setSwitchPosition({1013: True, 1029: True, 1057: True, 1063: True, 1077: False, 1085: True})
    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, True)
    assert(trcControl[5].get_switch_positions() == {1057: True, 1063: True, 1077: False, 1085: True})

    green_line.setSwitchPosition({1013: True, 1029: True, 1057: True, 1063: True, 1077: True, 1085: True})
    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, True)
    assert(trcControl[5].get_switch_positions() == {1057: True, 1063: True, 1077: True, 1085: True})

    # check if block status from track controller updates in ctc
    trcControl[5].set_a_stat(1077, False)
    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, False)
    assert(green_line.getClosedBlocks() == [77])

    trcControl[5].set_a_stat(1077, True)
    connect_ctc_track_controller(dispatcher, green_line, red_line, trcControl, False)
    assert(green_line.getClosedBlocks() == [])




