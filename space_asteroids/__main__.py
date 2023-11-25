import pygame
from game import Asteroids
from intro import ShowStartScreen


if __name__ == "__main__":
    ShowStartScreen()
    space_asteroids = Asteroids()
    space_asteroids.main_loop()  # Start the main game loop after the start screen
