#    Copyright (C) 2022 gekofroot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed WITHOUT ANY WARRANTY; 
#    See the GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.



# modules
from tkinter import *
from os import sys


def main():

    # variables
    window_width = 500
    window_height = 300
    main_window = Tk()
    main_window.geometry(f"{window_width}x{window_height}")
    FG = "#ffffff"
    BG = "#000000"
    BD = 4
    FONT = ("Helvetica", 14)
    RLF_1 = FLAT

    # functions
    def enter_button_pressed():
        try:
            get_item_price = float(item_price.get())
            get_tip_percent = float(tip_percent.get())
            tip_total = (get_tip_percent / get_item_price) * 100
            total_amount = get_item_price + tip_total
            display_total.configure(text = f"{total_amount:.2f}", fg = FG, bg = BG)
            item_price.delete(0, END)
            tip_percent.delete(0, END)
        except ValueError:
            display_total.configure(text = (f"numbers only"), fg = "#ff0000", bg = "#ffffff")

    def clear_button_pressed():
        display_total.configure(text = "", fg = FG, bg = BG)
        item_price.delete(0, END)
        tip_percent.delete(0, END)
    
    def close_cmd():
        sys.exit()

    # widgets
    title = Label(text = "Tica", font = FONT, bd = BD, fg = FG, bg = BG, relief = RLF_1)
    item_price = Entry(font = FONT, bd = BD, fg = FG, bg = BG, relief = RLF_1, justify = CENTER)
    tip_percent = Entry(font = FONT, bd = BD, fg = FG, bg = BG, relief = RLF_1, justify = CENTER)
    display_total = Label(font = FONT, bd = BD, fg = FG, bg = BG, relief = RLF_1)
    enter_button = Button(text = "[ Enter ]", font = FONT, bd = BD, fg = FG, bg = BG, relief = RLF_1,
            command = enter_button_pressed)
    clear_button = Button(text = "[ Clear ]", font = FONT, bd = BD, fg = FG, bg = BG, relief = RLF_1,
            command = clear_button_pressed)

    # place widgets
    x_pos = window_width / 2
    y_pos = window_height / 4

    title.place(x = 0, y = 0, width = x_pos * 2, height = y_pos)
    item_price.place(x = 0, y = y_pos, width = x_pos, height = y_pos)
    tip_percent.place(x = x_pos, y = y_pos, width = x_pos, height = y_pos)
    display_total.place(x = 0, y = y_pos * 2, width = x_pos * 2, height = y_pos)
    enter_button.place(x = 0, y = y_pos * 3, width = x_pos, height = y_pos)
    clear_button.place(x = x_pos, y = y_pos * 3, width = x_pos, height = y_pos)

    
    # set menu
    top_menu = Menu(main_window)
    settings_menu = Menu(top_menu)
    settings_menu.add_command(label = "Close", command = close_cmd)
    top_menu.add_cascade(label = "Settings", menu = settings_menu)
    main_window.config(menu = top_menu)
    
    main_window.mainloop()


if __name__ == "__main__":
    main()
