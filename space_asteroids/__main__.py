import pygame
from game2 import Asteroids
from startPage import Start_Screen
from leaderBoard import Leaderboard


if __name__ == "__main__":

    start_screen = Start_Screen()
    username = start_screen.run()  # Capture the returned username
    space_asteroids = Asteroids(username)  # Pass the username to the game class
    score = space_asteroids.main_loop()  # Start the main game loop
    leaderboard = Leaderboard()
    leaderboard.run_leaderb((username,score))
    pygame.quit()
 
