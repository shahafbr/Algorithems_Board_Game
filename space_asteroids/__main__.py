from game2 import Asteroids
from startPage import Start_Screen


if __name__ == "__main__":
    """ 
    Start_Screen()
    space_asteroids = Asteroids()
    space_asteroids.main_loop()  # Start the main game loop after the start screen
    """

    start_screen = Start_Screen()
    username = start_screen.run()  # Capture the returned username
    print("Username entered:", username)
    space_asteroids = Asteroids(username)  # Pass the username to the game class
    space_asteroids.main_loop()  # Start the main game loop
  
