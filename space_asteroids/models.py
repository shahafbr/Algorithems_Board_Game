from pygame.math import Vector2
from pygame.transform import rotozoom
import random
from utilities import load_sprite, load_sound, wrap_position

# Constants
DIRECTION_UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity, wraps=True):
        # Object Initialization
        self.position = Vector2(position)  # Using Vector for position for easy manipulation
        self.sprite = sprite  # Sprite for the object
        self.radius = sprite.get_width() / 2  # Radius for collision detection
        self.velocity = Vector2(velocity)  # Velocity vector
        self.wraps = wraps  # Whether the object wraps around the screen

    def draw(self, surface):
        # Drawing the object on the screen
        position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, position)

    def move(self, surface):
        # Moving the object
        move_to = self.position + self.velocity
        # Wrapping position around the screen if necessary
        if self.wraps:
            self.position = wrap_position(move_to, surface)
        else:
            self.position = move_to

    def collides_with(self, other):
        # add
        # Collision detection using distance and radius
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius

class Spaceship(GameObject):
    # Constants for spaceship behavior
    ROTATION_SPEED = 3
    ACCELERATION = 0.25
    BULLET_SPEED = 3

    def __init__(self, position):
        # Spaceship initialization
        self.direction = Vector2(DIRECTION_UP)
        self.pew_pew = load_sound("laser")  # Sound effect for shooting
        super().__init__(position, load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        # Rotating the spaceship
        sign = 1 if clockwise else -1
        angle = self.ROTATION_SPEED * sign
        self.direction.rotate_ip(angle)

    def accelerate(self):
        # Accelerating the spaceship
        self.velocity += self.direction * self.ACCELERATION
    
    def decelerate(self):
        # Accelerating the spaceship
        self.velocity -= self.direction * self.ACCELERATION

    def shoot(self):
        # Shooting a bullet
        velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, velocity)
        from game import bullets
        bullets.append(bullet)
        self.pew_pew.play()

    def draw(self, surface):
        # Drawing a rotated spaceship
        angle = self.direction.angle_to(DIRECTION_UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

class Rock(GameObject):
    # Constants for rock behavior
    MIN_START_GAP = 250
    MIN_SPEED = 1
    MAX_SPEED = 3

    @classmethod
    def create_random(cls, surface, ship_position):
        # Creating rocks at random positions
        while True:
            position = Vector2(
                random.randrange(surface.get_width()),
                random.randrange(surface.get_height()),
            )
            if position.distance_to(ship_position) > cls.MIN_START_GAP:
                break
        return Rock(position)

    def __init__(self, position, size=3):
        # Rock initialization with varying sizes
        self.size = size
        scale = {3: 1.0, 2: 0.5, 1: 0.25}[size]  # Scale based on size
        sprite = rotozoom(load_sprite("asteroid"), 0, scale)
        # Random velocity
        speed = random.randint(self.MIN_SPEED, self.MAX_SPEED)
        angle = random.randint(0, 360)
        velocity = Vector2(speed, 0).rotate(angle)
        super().__init__(position, sprite, velocity)

    def split(self):
        # Splitting the rock into smaller pieces
        if self.size > 1:
            from game import rocks
            rocks.append(Rock(self.position, self.size - 1))
            rocks.append(Rock(self.position, self.size - 1))

class Bullet(GameObject):
    def __init__(self, position, velocity):
        # Bullet initialization
        super().__init__(position, load_sprite("bullet"), velocity, False)
