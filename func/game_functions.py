import sys
import pygame
from entity.bullet import Bullet
from entity.alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_row = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row in range(number_row):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, alien.rect.width, row)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(available_space_x / (1.5 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, alien_width, row_number):
    new_alien = Alien(ai_settings, screen)
    new_alien.x = 0.5 * alien_width + 1.5 * alien_width * alien_number
    new_alien.y = new_alien.rect.y + 1.5 * new_alien.rect.height * row_number
    new_alien.rect.x = new_alien.x
    new_alien.rect.y = new_alien.y
    aliens.add(new_alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - ship_height - 2.5 * alien_height
    return int(available_space_y / (1.5 * alien_height))



