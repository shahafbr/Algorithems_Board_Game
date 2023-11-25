"""

import pygame

class show_start_screen:
        # Define colors
        WHITE = (255, 255, 255)
        TRANSPARENT = (0, 0, 0, 0)
        screen_width, screen_height = 800, 600
        pygame.init()  # Initialize all imported pygame modules
        screen = pygame.display.set_mode((800, 600))  # Use your game's resolution
        pygame.display.set_caption('Space Game')

        # Load and scale the background image
        background_image = load_sprite("background")
        background_image = pygame.transform.scale(background_image, (800, 600))

        # Title properties using the custom font

        # Path to your font file
        font_path = " "  
        # Path to your font file
        font_size = 100  # Adjust the size to fit your design
        font = pygame.font.Font(font_path, font_size)
        text_surface = font.render('Space Game', True, WHITE).convert_alpha()
        text_rect = text_surface.get_rect(center=(screen_width // 2, 150))

        # Create a mask from the text surface
        mask = pygame.mask.from_surface(text_surface)
        mask_surface = mask.to_surface(setcolor=WHITE, unsetcolor=TRANSPARENT).convert_alpha()

        # Copy the background image to the text shape
        title_surface = pygame.Surface(text_rect.size, pygame.SRCALPHA)
        title_surface.blit(background_image, (0, 0), area=text_rect)
        title_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        # Draw a squircle shape behind the title text
        squircle_rect = text_rect.inflate(20, 20)  # Inflate the rect to make the squircle larger than the text

        # Button properties
        button_color = (0, 204, 153)  # A teal color; adjust as needed
        button_rect = pygame.Rect(0, 0, 200, 50)  # Adjust width and height as needed
        button_rect.center = (screen_width // 2, 450)  # Position of the button

        # Text properties for the button
        button_font = pygame.font.Font(None, 36)  # Use a font and size that fits the button
        button_text = button_font.render('START', True, WHITE)
        button_text_rect = button_text.get_rect(center=button_rect.center)

        running = True
        while running:
            # Draw the background
            screen.blit(background_image, (0, 0))

            # Draw the squircle and title
            pygame.draw.rect(screen, WHITE, squircle_rect, border_radius=25)  # Squircle behind the title
            screen.blit(title_surface, text_rect.topleft)  # Title text with background fill

            # Draw the button and text
            pygame.draw.rect(screen, button_color, button_rect)
            screen.blit(button_text, button_text_rect)

            pygame.display.flip()  # Update the display

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()  # Exit the game completely
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        running = False  # Button clicked, proceed to game

""" 

import pygame
from utilities import load_sprite, load_font, load_sound  # Ensure utilities.py is in the same directory

class ShowStartScreen:
    # Define colors
    WHITE = (255, 255, 255)
    TRANSPARENT = (0, 0, 0, 0)
    screen_width, screen_height = 800, 600

    def __init__(self):
        pygame.init()  # Initialize all imported pygame modules
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Space Game')

        # Load and scale the background image
        self.background_image = load_sprite("background")  # 'background' is the name of your image file without the extension
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

        # Title properties using the custom font
        self.font = load_font("font", 100)  # 'font' is the name of your font file without the extension
        self.text_surface = self.font.render('Space Game', True, self.WHITE).convert_alpha()
        self.text_rect = self.text_surface.get_rect(center=(self.screen_width // 2, 150))

        # Create a mask from the text surface
        self.mask = pygame.mask.from_surface(self.text_surface)
        self.mask_surface = self.mask.to_surface(setcolor=self.WHITE, unsetcolor=self.TRANSPARENT).convert_alpha()

        # Copy the background image to the text shape
        self.title_surface = pygame.Surface(self.text_rect.size, pygame.SRCALPHA)
        self.title_surface.blit(self.background_image, (0, 0), area=self.text_rect)
        self.title_surface.blit(self.mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        # Draw a squircle shape behind the title text
        self.squircle_rect = self.text_rect.inflate(20, 20)  # Inflate the rect to make the squircle larger than the text

        # Button properties
        button_color = (0, 204, 153)  # A teal color; adjust as needed
        self.button_rect = pygame.Rect(0, 0, 200, 50)  # Adjust width and height as needed
        self.button_rect.center = (self.screen_width // 2, 450)  # Position of the button

        # Text properties for the button
        self.button_font = pygame.font.Font(None, 36)  # Use a font and size that fits the button
        self.button_text = self.button_font.render('START', True, self.WHITE)
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)

    def run(self):
        running = True
        while running:
            # Draw the background
            self.screen.blit(self.background_image, (0, 0))

            # Draw the squircle and title
            pygame.draw.rect(self.screen, self.WHITE, self.squircle_rect, border_radius=25)  # Squircle behind the title
            self.screen.blit(self.title_surface, self.text_rect.topleft)  # Title text with background fill

            # Draw the button and text
            pygame.draw.rect(self.screen, button_color, self.button_rect)
            self.screen.blit(self.button_text, self.button_text_rect)

            pygame.display.flip()  # Update the display

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()  # Exit the game completely
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        running = False  # Button clicked, proceed to game
                    