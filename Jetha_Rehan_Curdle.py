from Interfaces.panel import Panel
from Interfaces.game import game

running = True

while running:
    pan = Panel()
    pan.mainloop()

    restart_flag = game()
    if (restart_flag != True):
        running = False