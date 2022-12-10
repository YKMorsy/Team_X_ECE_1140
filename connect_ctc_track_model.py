def connect_ctc_track_model(green_line, red_line, track_model_var):

    maintenance_green = green_line.maintenance_blocks

    for block in maintenance_green:
        track_model_var.clear_block_failure(int(block)-1)

    green_line.maintenance_blocks = []

    maintenance_red = red_line.maintenance_blocks

    for block in maintenance_red:
        track_model_var.clear_block_failure(int(block) + 149)

    red_line.maintenance_blocks = []

