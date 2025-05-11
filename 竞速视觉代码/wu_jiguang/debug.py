import flag
black=0
white=255

# 这一部分是探测点探测，然后发出指令，并且显示发出的指令

def ser_control(color,pixel_left,pixel_right,last_state,current_state):
    """视觉反馈数据串口控制逻辑"""
    if flag == 0:
        if ( pixel_left == black and color == black and pixel_right == white) or (
                pixel_left == black and color == white and pixel_right == white) or (
                pixel_left == black and color == white and pixel_right == black):
                if current_state != 'll':
                    current_state = 'll'
                    print("左转")

        if (pixel_left == white and color == black and pixel_right == black) or (
                pixel_left == white and color == white and pixel_right == black):
                if current_state != 'rr':
                    current_state = 'rr'
                    print("右转")

        if color == 0 and pixel_left == 0 and pixel_right == 0:
            if current_state != 'ww':
                current_state = 'ww'
                print("直走")
        last_state = current_state

    if flag.flag == 1:
        if (pixel_left == black and color == black and pixel_right == white) or (
                pixel_left == black and color == white and pixel_right == white) or (
                pixel_left == black and color == white and pixel_right == black):
            if current_state != 'rr':
                current_state = 'rr'
                print("右转")

        if (pixel_left == white and color == black and pixel_right == black) or (
                pixel_left == white and color == white and pixel_right == black):
            if current_state != 'll':
                current_state = 'll'
                print("左转")

        if color == 0 and pixel_left == 0 and pixel_right == 0:
            if current_state != 'ww':
                current_state = 'ww'
                print("直走")


    return last_state,current_state

