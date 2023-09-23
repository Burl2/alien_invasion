import pygame
import func.game_functions as gf
from cfg.settings import Settings
from entity.ship import Ship
from pygame.sprite import Group
from entity.game_stats import GameStats


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)

    gf.create_fleet(ai_settings, screen, aliens, ship)

    # bg_color = (230, 230, 230)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()
