def connect_ctc_track_controller(dispatcherCTC, greenLineCTC, redLineCTC, trcControl):
    
    # Setters of CTC (WAYSIDE -> CTC)
    # occupancy_from_trc = trcControl[0].get_occupancy() | trcControl[1].get_occupancy() | trcControl[2].get_occupancy() | trcControl[3].get_occupancy() | trcControl[4].get_occupancy() | trcControl[5].get_occupancy()

    occupancy_from_trc = trcControl[3].get_occupancy() | trcControl[4].get_occupancy() | trcControl[5].get_occupancy()

    dispatcherCTC.setOccupancy(occupancy_from_trc)

    green_switch_position_trc = trcControl[3].get_switch_positions() | trcControl[4].get_switch_positions() | trcControl[5].get_switch_positions()

    greenLineCTC.setSwitchPosition(green_switch_position_trc)

    # red_switch_position_trc = trcControl[0].get_switch_positions() | trcControl[1].get_switch_positions() | trcControl[2].get_switch_positions()
    # redLineCTC.setSwitchPosition(red_switch_position_trc)

    green_block_status_trc = trcControl[3].get_statuses() | trcControl[4].get_statuses() | trcControl[5].get_statuses()
    greenLineCTC.setBlockStatus(green_block_status_trc)

    # red_block_status_trc = trcControl[0].get_statuses() | trcControl[1].get_statuses() | trcControl[2].get_statuses()
    # redLineCTC.setBlockStatus(red_block_status_trc)

    green_crossing_trc = trcControl[3].get_railway_crossings() | trcControl[4].get_railway_crossings() | trcControl[5].get_railway_crossings() 
    greenLineCTC.setRailWayCrossing(green_crossing_trc)

    # red_crossing_trc = trcControl[0].get_railway_crossings() | trcControl[1].get_railway_crossings() | trcControl[2].get_railway_crossings()
    # redLineCTC.setRailWayCrossing(red_crossing_trc)

    # Setters of Wayside (CTC -> WAYSIDE)
    # Authority - Green
    green_authority_total = greenLineCTC.getBlockAuthority()
    print("Auth 1063 " + str(green_authority_total[1063]))
    print("Auth 1064 " + str(green_authority_total[1064]))
    print("Auth 1065 " + str(green_authority_total[1065]))
    print("Auth 1066 " + str(green_authority_total[1066]))
    for_ws_3 = {}
    for_ws_5 = {}
    for_ws_4 = {}

    for key in green_authority_total:
        if ((key-1000) >= 1) and ((key-1000) <= 21):
            for_ws_3[key] = green_authority_total[key]
        elif (((key-1000) >= 35) and ((key-1000) <= 105)) or (key-1000) == 0:
            for_ws_5[key] = green_authority_total[key]
        elif (((key-1000) >= 20) and ((key-1000) <= 36)) or (((key-1000) >= 104) and ((key-1000) <= 150)):
            for_ws_4[key] = green_authority_total[key]


    trcControl[3].set_authority(for_ws_3)
    trcControl[5].set_authority(for_ws_5)
    trcControl[4].set_authority(for_ws_4)

    # # Authority - Red
    # red_authority_total = redLineCTC.getBlockAuthority()
    # for_ws_0 = {}
    # for_ws_1 = {}
    # for_ws_2 = {}

    # for key in red_authority_total:
    #     if (((key-2000) >= 1) and ((key-2000) <= 24)) or (key-2000) == 0:
    #         for_ws_0[key] = red_authority_total[key]
    #     elif (((key-2000) >= 23) and ((key-2000) <= 46)) or (((key-2000) >= 67) and ((key-1000) <= 76)):
    #         for_ws_1[key] = red_authority_total[key]
    #     elif (((key-2000) >= 45) and ((key-2000) <= 66)):
    #         for_ws_2[key] = red_authority_total[key]


    # trcControl[0].set_authority(for_ws_0)
    # trcControl[1].set_authority(for_ws_1)
    # trcControl[2].set_authority(for_ws_2)


    # Suggested Speed - Green
    green_speed_total = greenLineCTC.getBlockSuggestedSpeed()
    for_ws_3 = {}
    for_ws_5 = {}
    for_ws_4 = {}

    for key in green_speed_total:
        if ((key-1000) >= 1) and ((key-1000) <= 20):
            for_ws_3[key] = green_speed_total[key]
        elif (((key-1000) >= 36) and ((key-1000) <= 104)) or (key-1000) == 0:
            for_ws_5[key] = green_speed_total[key]
        elif (((key-1000) >= 21) and ((key-1000) <= 35)) or (((key-1000) >= 105) and ((key-1000) <= 150)):
            for_ws_4[key] = green_speed_total[key]


    trcControl[3].set_suggested_speed(for_ws_3)
    trcControl[5].set_suggested_speed(for_ws_5)
    trcControl[4].set_suggested_speed(for_ws_4)

    # # Suggested Speed - Red
    # red_speed_total = redLineCTC.getBlockSuggestedSpeed()
    # for_ws_0 = {}
    # for_ws_1 = {}
    # for_ws_2 = {}

    # for key in red_speed_total:
    #     if (((key-2000) >= 1) and ((key-2000) <= 23)) or (key-2000) == 0:
    #         for_ws_0[key] = red_speed_total[key]
    #     elif (((key-2000) >= 24) and ((key-2000) <= 45)) or (((key-2000) >= 67) and ((key-1000) <= 76)):
    #         for_ws_1[key] = red_speed_total[key]
    #     elif (((key-2000) >= 46) and ((key-2000) <= 66)):
    #         for_ws_2[key] = red_speed_total[key]


    # trcControl[0].set_suggested_speed(for_ws_0)
    # trcControl[1].set_suggested_speed(for_ws_1)
    # trcControl[2].set_suggested_speed(for_ws_2)
