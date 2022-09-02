let line0 = 0
let line1 = 0
let line2 = 0
basic.forever(function () {
    line0 = pins.digitalReadPin(DigitalPin.P2)
    line1 = pins.digitalReadPin(DigitalPin.P8)
    line2 = pins.digitalReadPin(DigitalPin.P1)
})
