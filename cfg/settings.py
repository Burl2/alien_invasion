class Settings:
    """Store project All configution"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Aline settings
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        # fleet_direction value is 1 -> right move, is -1 -> left move
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 4
