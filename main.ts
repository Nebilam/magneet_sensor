input.onButtonPressed(Button.B, function () {
    staafdiagram = true
})
input.onButtonPressed(Button.A, function () {
    staafdiagram = false
    basic.showNumber(input.magneticForce(Dimension.Strength))
})
let staafdiagram = false
staafdiagram = true
basic.forever(function () {
    if (staafdiagram) {
        led.plotBarGraph(
        input.magneticForce(Dimension.Strength),
        3000
        )
    }
})
