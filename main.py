def on_button_pressed_b():
    global staafdiagram
    staafdiagram = True
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_button_pressed_a():
    global staafdiagram
    staafdiagram = False
    basic.show_number(input.magnetic_force(Dimension.STRENGTH))
    serial.write_number(input.magnetic_force(Dimension.STRENGTH))
input.on_button_pressed(Button.A, on_button_pressed_a)
staafdiagram = False
staafdiagram = True
def on_forever():
    if staafdiagram:
        led.plot_bar_graph(input.magnetic_force(Dimension.STRENGTH), 3000)
basic.forever(on_forever)