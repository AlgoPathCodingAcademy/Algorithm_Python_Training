'''
Components:
PositionComponent: Stores the unit's location on the game map.
RenderComponent: Handles how the unit is drawn on the screen.
HealthComponent: Keeps track of the unit's health and handles damage.
MovementComponent: Manages the movement abilities of the unit.
AttackComponent: Defines the attack behavior and damage the unit can inflict.
'''

class PositionComponent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RenderComponent:
    def __init__(self, sprite):
        self.sprite = sprite

class HealthComponent:
    def __init__(self, health):
        self.health = health

class MovementComponent:
    def __init__(self, speed):
        self.speed = speed

class AttackComponent:
    def __init__(self, damage):
        self.damage = damage

class Unit:
    def __init__(self, name, position, render, health, movement, attack):
        self.name = name
        self.position = position
        self.render = render
        self.health = health
        self.movement = movement
        self.attack = attack

# Creating components for the knight
knight_position = PositionComponent(100, 200)
knight_render = RenderComponent("knight_sprite.png")
knight_health = HealthComponent(150)
knight_movement = MovementComponent(4)
knight_attack = AttackComponent(25)

# Creating a knight unit with the components
knight = Unit("Knight", knight_position, knight_render, knight_health, knight_movement, knight_attack)

# Accessing the components directly
print(f"Knight's Health: {knight.health.health}")
print(f"Knight's Position: ({knight.position.x}, {knight.position.y})")
print(f"Knight's Attack Damage: {knight.attack.damage}")
