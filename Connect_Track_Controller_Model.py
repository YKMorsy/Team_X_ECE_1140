def Connect_Track_Control_And_Model(trcControl, model):
    #Track Control - > Track Model
    #switch 
    sw = trcControl[0].get_switch_positions() | trcControl[1].get_switch_positions() | trcControl[2].get_switch_positions() | trcControl[3].get_switch_positions() | trcControl[4].get_switch_positions() | trcControl[5].get_switch_positions()
    model.set_switch_position(sw)

    #authority
    auth = trcControl[0].get_authority() | trcControl[1].get_authority() | trcControl[2].get_authority() | trcControl[3].get_authority() | trcControl[4].get_authority() | trcControl[5].get_authority()
    model.set_total_authority(auth)

    #commanded speed
    cs = trcControl[0].get_commanded_speed() | trcControl[1].get_commanded_speed() | trcControl[2].get_commanded_speed() | trcControl[3].get_commanded_speed() | trcControl[4].get_commanded_speed() | trcControl[5].get_commanded_speed()
    model.set_commanded_speed(cs)

    #lights
    li = trcControl[0].set_light_colors() | trcControl[1].set_light_colors() | trcControl[2].set_light_colors() | trcControl[3].set_light_colors() | trcControl[4].set_light_colors() | trcControl[5].set_light_colors()
    model.set_lights(li)

    #railway crossings
    rc = trcControl[0].set_railway_crossings() | trcControl[1].set_railway_crossings() | trcControl[2].set_railway_crossings() | trcControl[3].set_railway_crossings() | trcControl[4].set_railway_crossings() | trcControl[5].set_railway_crossings()
    model.set_crossings(rc)

    #Track Model - > Track Control
    #occupancy
    trcControl[0].set_occupancy(model.get_occupancy_0())
    trcControl[1].set_occupancy(model.get_occupancy_1())
    trcControl[2].set_occupancy(model.get_occupancy_2())
    trcControl[3].set_occupancy(model.get_occupancy_3())
    trcControl[4].set_occupancy(model.get_occupancy_4())
    trcControl[5].set_occupancy(model.get_occupancy_5())

    trcControl[0].set_statuses(model.get_fault_0())
    trcControl[1].set_statuses(model.get_fault_1())
    trcControl[2].set_statuses(model.get_fault_2())
    trcControl[3].set_statuses(model.get_fault_3())
    trcControl[4].set_statuses(model.get_fault_4())
    trcControl[5].set_statuses(model.get_fault_5())
