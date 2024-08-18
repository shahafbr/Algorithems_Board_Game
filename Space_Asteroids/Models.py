# models.py
from pygame.math import Vector2
from pygame.transform import rotozoom
import random
from Utils import load_sprite, load_sound, wrap_position, print_text

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
        # Collision detection using distance and radius
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius

class Spaceship(GameObject):
    # Constants for spaceship behavior
    ROTATION_SPEED = 4
    ACCELERATION = 0.20
    BULLET_SPEED = 3

    def __init__(self, position, asteroids_instance):
        # Spaceship initialization
        self.direction = Vector2(DIRECTION_UP)
        self.pew_pew = load_sound("Laser")  # Sound effect for shooting
        super().__init__(position, load_sprite("Spaceship"), Vector2(0))
        self.asteroids_instance = asteroids_instance

    def rotate(self, clockwise=True):
        # Rotating the spaceship
        sign = 1 if clockwise else -1
        angle = self.ROTATION_SPEED * sign
        self.direction.rotate_ip(angle)

    def accelerate(self):
        # Accelerating the spaceship
        self.velocity += self.direction * self.ACCELERATION
    
    def decelerate(self):
        # Deceleration logic
        self.velocity -= self.direction * self.ACCELERATION
        if self.velocity.length() < 0:
            self.velocity = Vector2(0, 0)

    def shoot(self):
        # Shooting a bullet
        velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, velocity)
        self.asteroids_instance.bullets.append(bullet)
        self.pew_pew.play()

        """ 
        if self.asteroids_instance:
            bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
            bullet = Bullet(self.position, bullet_velocity)
            self.asteroids_instance.bullets.append(bullet)  # Corrected line to append bullet
            self.pew_pew.play()
        """

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
        if size == 3:
            scale = 1.0
        elif size == 2:
            scale = 0.5
        else:
            scale = 0.25

        sprite = rotozoom(load_sprite("Asteroid"), 0, scale)
        
        # Random velocity
        speed = random.randint(self.MIN_SPEED, self.MAX_SPEED)
        angle = random.randint(0, 360)
        velocity = Vector2(speed, 0).rotate(angle)
        super().__init__(position, sprite, velocity)

    def split(self):
        # Splitting the rock into smaller pieces
        if self.size > 1:
            from Game import rocks
            # Create two smaller rocks
            rocks.append(Rock(self.position, self.size - 1))
            rocks.append(Rock(self.position, self.size - 1))

class Bullet(GameObject):
    def __init__(self, position, velocity):
        # Bullet initialization
        super().__init__(position, load_sprite("Bullet"), velocity, False)
