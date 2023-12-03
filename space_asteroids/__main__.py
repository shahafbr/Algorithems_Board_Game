from game4 import Asteroids
from startPage import Start_Screen


if __name__ == "__main__":
    Start_Screen()
    space_asteroids = Asteroids()
    space_asteroids.main_loop()  # Start the main game loop after the start screen

