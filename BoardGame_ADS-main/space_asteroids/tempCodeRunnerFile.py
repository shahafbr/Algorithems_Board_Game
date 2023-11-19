import pygame
from game import Asteroids

# Define the start screen function
def show_start_screen():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((800, 600))  # Use your game's resolution
    pygame.display.set_caption('Start Game')

    # Load and scale the background image
    background_image = pygame.image.load("C:\\Users\\Shaha\\OneDrive\\Desktop\\BoardGame_ADS-main\\Background.png")
    background_image = pygame.transform.scale(background_image, (800, 600))

    # Create the title text with the background image fill
    title_font = pygame.font.Font(None, 74)  # Use a futuristic font if available
    title_text = title_font.render('Space Game', True, (255, 255, 255))
    title_text_rect = title_text.get_rect(center=(screen.get_width() // 2, 150))

    # Create a mask from the text surface
    mask = pygame.mask.from_surface(title_text)
    mask_surface = mask.to_surface(setcolor=(255, 255, 255), unsetcolor=(0, 0, 0, 0)).convert_alpha()

    # Copy the background image to the text shape
    title_surface = pygame.Surface(title_text_rect.size, pygame.SRCALPHA)
    title_surface.blit(background_image, (0, 0), area=title_text_rect)
    title_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    # Button properties
    button_color = (0, 204, 153)  # A teal color; adjust as needed
    button_rect = pygame.Rect(0, 0, 200, 50)  # Adjust width and height as needed
    button_rect.center = (400, 450)  # Position of the button

    # Text properties for the button
    button_font = pygame.font.Font(None, 36)  # Use a font and size that fits the button
    text_color = (255, 255, 255)  # White color text
    button_text = button_font.render('START', True, text_color)
    button_text_rect = button_text.get_rect(center=button_rect.center)

    running = True
    while running:
        screen.blit(background_image, (0, 0))  # Blit the background image

        # Draw the title text with background image fill
        screen.blit(title_surface, title_text_rect.topleft)

        # Draw the button and button text
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

if __name__ == "__main__":
    show_start_screen()
    space_asteroids = Asteroids()
    space_asteroids.main_loop()  # Start the main game loop after the start screen