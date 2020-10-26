import pyautogui as pg

print('Type Ctrl-C to stop the program')

try:
    while True:
        x, y = pg.position()
        coordinates = 'X: ' + str(x).ljust(4) + 'Y: ' + str(y).ljust(4  )

        print(coordinates, end='')
        print('\b' * len(coordinates), end='', flush = True)
except KeyboardInterrupt:
        print('\nBye..')
