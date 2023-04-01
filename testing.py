import keyboard  # using module keyboard

running = True


while running:  

    if keyboard.read_key() == "p":
        print('You Pressed q Key!')

    if keyboard.read_key() == "1":
        print('You Pressed q11Key!')
        break
    