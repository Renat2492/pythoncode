# def hello_name(name: str):
# basic.show_string("Hello, " + name)
# basic.pause(100)
# basic.show_icon(IconNames.YES)
# basic.pause(1000)
# basic.clear_screen()
# hello_name("ALEX")
# 
# def on_forever():
# hello_name("Volodimir")
# basic.forever(on_forever)

def on_button_pressed_a():
    basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
                . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
                # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.pause(100)
    basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
                # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.pause(100)
    basic.show_leds("""
                . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)
