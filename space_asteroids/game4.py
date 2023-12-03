import pygame
from models3 import Rock, Spaceship, Bullet
from utils import load_sprite, print_text
from startPage import Start_Screen

# Global lists to hold bullets and rocks
rocks = []

# Points system based on rock size
rock_points = {3: 100, 2: 50, 1: 25}

# Initialize the score
score = 0

# Function to update the score, this should be called whenever a rock is destroyed
def update_score(rock_size):
    global score
    score += rock_points[rock_size]

class Asteroids:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.ship = Spaceship((400, 300), self)
        self.bullets = []
        # Populate the game with rocks
        global rocks
        rocks = [Rock.create_random(self.screen, self.ship.position) for _ in range(6)]

    def main_loop(self):
        while True:  # Main game loop
            self.handles_input()
            self.game_logic()
            self.draw()

    def handles_input(self):
        # Process user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ship.shoot()

        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_ESCAPE] or is_key_pressed[pygame.K_q]:
            quit()

        # Ship movement controls
        if self.ship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.ship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.ship.rotate(clockwise=False)
            elif is_key_pressed[pygame.K_UP]:
                self.ship.accelerate()
            elif is_key_pressed[pygame.K_DOWN]:
                self.ship.decelerate()

    @property
    def game_objects(self):
        # Consolidate all game objects
        return [*self.bullets, *rocks, self.ship] if self.ship else [*self.bullets, *rocks]

    def game_logic(self):
        # Main game logic
        for obj in self.game_objects:
            obj.move(self.screen)

        rect = self.screen.get_rect()
        # Bullet behavior
        for bullet in self.bullets[:]:
            if not rect.collidepoint(bullet.position):
                self.bullets.remove(bullet)

        # Collision detection
        for bullet in self.bullets[:]:
            for rock in rocks[:]:
                if rock.collides_with(bullet):
                    update_score(rock.size)
                    rocks.remove(rock)
                    rock.split()
                    self.bullets.remove(bullet)
                    break

        # Ship collision detection
        if self.ship:
            for rock in rocks[:]:
                if rock.collides_with(self.ship):
                    self.ship = None
                    self.message = "You Lost!"
                    break

        # Winning condition
        if not rocks and self.ship:
            self.message = "You Won!"

    def draw(self):
        # Drawing game objects
        self.screen.blit(self.background, (0, 0))

        for obj in self.game_objects:
            obj.draw(self.screen)

        # Display the score
        print_text(self.screen, f"Score: {score}", self.font, (255, 255, 255), top_right=True)

        if self.message:
            print_text(self.screen, self.message, self.font)

        pygame.display.flip()
        self.clock.tick(30)
