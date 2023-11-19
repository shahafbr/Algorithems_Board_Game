# utilities.py

from pygame import Color
from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pathlib import Path

def load_sprite(name, with_alpha=True):
    # Loading Sprite Images
    filename = Path(__file__).parent / Path("assets/sprites/" + name + ".png")  # Constructs the file path
    sprite = load(filename.resolve())  # Loads the image from the file system

    # Image Processing
    if with_alpha:
        return sprite.convert_alpha()  # Returns the image with alpha channel (transparency)
    return sprite.convert()  # Returns the image without alpha channel

def wrap_position(position, surface):
    # Wrapping Position for Continuous Movement
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)  # Uses modulo operation to wrap position around the surface

def load_sound(name):
    # Loading Sound Files
    filename = Path(__file__).parent / Path("assets/sounds/" + name + ".wav")  # Constructs the file path for sound
    return Sound(filename)  # Loads the sound file

def print_text(surface, text, font, color=Color("tomato")):
    # Rendering and Displaying Text
    text_surface = font.render(text, True, color)  # Creates a surface with the rendered text
    rect = text_surface.get_rect()  # Gets the rectangle area of the text surface
    rect.center = Vector2(surface.get_size()) / 2  # Centers the text
    surface.blit(text_surface, rect)  # Draws the text surface onto the main surface
