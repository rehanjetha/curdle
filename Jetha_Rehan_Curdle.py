from Interfaces.panel import Panel  # import curdle configuration panel
from Interfaces.game import game  # import curdle pygame function

running = True  # flag for game restart loop
pan = Panel()  # start config panel (once)

while running:
    pan.mainloop()  # run tkinter panel
    restart_flag = game()  # run game
    if (restart_flag != True):  # check if restart needed
        running = False  # close game if not needed