import pygame
import func.game_functions as gf
from cfg.settings import Settings
from entity.button import Button
from entity.ship import Ship
from pygame.sprite import Group
from entity.game_stats import GameStats
from entity.scoreborad import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, aliens, ship)

    # bg_color = (230, 230, 230)
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button, sb)


run_game()
