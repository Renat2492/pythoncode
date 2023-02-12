//  def hello_name(name: str):
//  basic.show_string("Hello, " + name)
//  basic.pause(100)
//  basic.show_icon(IconNames.YES)
//  basic.pause(1000)
//  basic.clear_screen()
//  hello_name("ALEX")
//  
//  def on_forever():
//  hello_name("Volodimir")
//  basic.forever(on_forever)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
                . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
                # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    `)
    basic.pause(100)
    basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
                # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    `)
    basic.pause(100)
    basic.showLeds(`
                . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    `)
})
