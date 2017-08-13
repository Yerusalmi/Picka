from pokemon import pokemon

p1 = pokemon.Pikatchu()
p2 = pokemon.Aipom()

gameOn = True


def wait_minute():
    import time
    time.sleep(3)

while gameOn:
    wait_minute()
    print(p1.getAttackNoise())
    print(p1.getName() + p1.getAttackNoise() + (" hit!" if p1.attack(p2) else " miss!"))
    if not p2.isDead():
        wait_minute()
        print(p2.getAttackNoise())
        print(p2.getName() + p2.getAttackNoise() + (" hit!" if p2.attack(p1) else " miss!"))
    if p1.isDead() or p2.isDead():
        gameOn = False
        print("game is over... ")
    if p1.isDead():
        print(p2.getName() + " won")
    else:
        print(p1.getName() + " won")