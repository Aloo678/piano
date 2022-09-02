line0 = 0
line1 = 0
line2 = 0

def on_forever():
    global line0, line1, line2
    line0 = pins.digital_read_pin(DigitalPin.P2)
    line1 = pins.digital_read_pin(DigitalPin.P8)
    line2 = pins.digital_read_pin(DigitalPin.P1)
basic.forever(on_forever)
