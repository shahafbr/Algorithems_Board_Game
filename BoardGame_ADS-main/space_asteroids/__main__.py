from game import Asteroids
from Start_page import show_start_screen
if __name__ == "__main__":
    show_start_screen()
    space_asteroids = Asteroids()
    space_asteroids.main_loop()  # Start the main game loop after the start screen 