import random
import time
from random import randint

import pygame
import pygame.mixer


class Player:
    def __init__(self, x1, y1, w1, h1, filename1, speed):
        self.rect = pygame.Rect(x1, y1, w1, h1)
        self.image = pygame.image.load(filename1)
        self.speed = speed

    def draw(self, window):
        screen.blit(self.image, [self.rect.x, self.rect.y])


class Ball:
    def __init__(self, x1, y1, w1, h1, filename1, speed, speed_x, speed_y):
        self.rect = pygame.Rect(x1, y1, w1, h1)
        self.image = pygame.image.load(filename1)
        self.speed = speed
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self, window):
        screen.blit(self.image, [self.rect.x, self.rect.y])




health = 100

ok = 0

pygame.init()
fps = pygame.time.Clock()
enemyhp = 100

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def startmenu(screen):
    fps = pygame.time.Clock()
    background = pygame.image.load('start.png')
    back = 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                if event.key == pygame.K_F4:
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_x:
                    if back == 1:
                        background = pygame.image.load('start1.png')
                        back = back + 1
                    elif back == 2:
                        background = pygame.image.load('start2.png')
                        back = back + 1
                    elif back == 3:
                        background = pygame.image.load('start3.png')
                        back = back + 1
                    elif back == 4:
                        background = pygame.image.load('start4.jpg')
                        back = back + 1
                    elif back == 5:
                        background = pygame.image.load('start5.png')
                        back = back + 1
                    elif back == 6:
                        background = pygame.image.load('start6.png')
                        back = back + 1
                    elif back == 7:
                        background = pygame.image.load('start7.png')
                        back = back + 1
                    elif back == 8:
                        background = pygame.image.load('start8.jpg')
                        back = back + 1
                    elif back == 9:
                        background = pygame.image.load('start9.png')
                        back = back + 1
                    elif back == 10:
                        background = pygame.image.load('start10.png')
                        back = back + 1
                    elif back == 11:
                        background = pygame.image.load('start11.png')
                        back = back + 1
                    elif back == 12:
                        return

        screen.fill(BLACK)
        screen.blit(background, [0, 0])

        pygame.display.flip()
        pygame.display.update()

        fps.tick(30)


def menu(screen):
    global enemyhp
    global ok
    global health
    fps = pygame.time.Clock()

    startTime = time.time()
    timer = int(time.time() - startTime)
    attacken = randint(1, 20)

    dialog = ['There are errors in the program',
              "You tried to fix",
              "Python is still buggy",
              'You tried to fix the errors',
              'You have recovered 20 HP',
              '',
              '',
              ]
    now = 0
    background = pygame.image.load('backgroundmenu.png')
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                if event.key == pygame.K_F4:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                if event.key == pygame.K_x:
                    now = now + 1
                    if now >= 3:
                        now = 0
                        return
                if event.key == pygame.K_c:
                    timer = int(time.time() - startTime)
                    if now < 3:
                        now = 2
                    if now == 4:
                        if health == 100:
                            health = 100
                            now = 0
                            return
                        else:
                            health = health + 20
                            now = 0
                            return

                    now = now + 1
                if event.key == pygame.K_z:

                    if now < 5:
                        now = 5
                    background = pygame.image.load('attack.png')

                    if now == 6:
                        background = pygame.image.load('attack1.png')

                        enemyhp = enemyhp - attacken
                        font = pygame.font.SysFont("calibri", 70)
                        text = font.render("" + str(attacken), True, (255, 255, 255))
                        text_rect = text.get_rect()
                        text_rect = (250, 250)
                        screen.blit(text, text_rect)
                        pygame.display.flip()

                        now = 0
                        return
                    now = now + 1
                if event.key == pygame.K_v:
                    ok = 1
                    return

        screen.fill(BLACK)
        screen.blit(background, [0, 0])

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(enemyhp)+"/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (795, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(health)+"/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (534, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 48)
        text = font.render(dialog[now], True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (239, 414)
        screen.blit(text, text_rect)

        pygame.display.flip()
        pygame.display.update()

        fps.tick(30)


def attack(screen):
    global health
    global enemyhp
    background = pygame.image.load('background.png')
    fps = pygame.time.Clock()

    a = 150

    startTime = time.time()
    timer = int(time.time() - startTime)

    randhel = randint(0, 9)

    enemies = []

    player = (Player(644, 445, 25, 25, "player.png", 5))

    b = (Ball(644, 465, 35, 35, "enemy.png", 5, 5, 5))

    enemy_image = pygame.image.load('enemy.png')
    enemy_width, enemy_height = enemy_image.get_size()
    for enemy in enemies:
        enemy_rect = pygame.Rect(400, 300, 35, 35)

    player_image = pygame.image.load('player.png')

    # Основной цикл игры
    while True:
        timer = int(time.time() - startTime)

        # Очистка экрана
        screen.fill(BLACK)
        screen.blit(background, [0, 0])

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(enemyhp) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (795, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(health) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (534, 597)
        screen.blit(text, text_rect)

        # Згенеруємо нового ворога
        if random.randint(1, 100) < 7:
            enemy = {'x': 0, 'y': random.randint(0, SCREEN_HEIGHT), 'speed': random.randint(1, 5)}
            enemies.append(enemy)

        for enemy in enemies:
            enemy['x'] += enemy['speed']
            if enemy['x'] > SCREEN_WIDTH:
                enemies.remove(enemy)

        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 35, 35)
            if player.rect.colliderect(enemy_rect):
                randhel = 1
                health = health - randhel

        # Відображаємо ворогів
        for enemy in enemies:
            screen.blit(enemy_image, (enemy['x'], enemy['y']))

        b.rect.x += b.speed_x
        b.rect.y += b.speed_y

        # Получение состояния клавиатуры
        keys = pygame.key.get_pressed()

        # Перемещение персонажа
        if keys[pygame.K_LEFT]:
            player.rect.x -= player.speed
        elif keys[pygame.K_RIGHT]:
            player.rect.x += player.speed
        elif keys[pygame.K_UP]:
            player.rect.y -= player.speed
        elif keys[pygame.K_DOWN]:
            player.rect.y += player.speed

        if b.rect.x > 492:
            b.speed_x = -(b.speed_x)

        if b.rect.y > 303:
            b.speed_y = -(b.speed_y)

        if b.rect.x < 740:
            b.speed_x = -(b.speed_x)

        if b.rect.y < 550:
            b.speed_y = -(b.speed_y)

        if player.rect.x < 492:
            player.rect.x = 493
        if player.rect.x > 740:
            player.rect.x = 740
        if player.rect.y < 302:
            player.rect.y = 303
        if player.rect.y > 550:
            player.rect.y = 550

        if player.rect.colliderect(b.rect):
            b.speed_y *= -1
            randhel = randint(5, 20)
            health = health - 50

        if health <= 0:
            break

        if timer > 10:
            break

        player.draw(screen)
        b.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        pygame.display.update()

        fps.tick(60)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def attack2(screen):
    global health
    global enemyhp
    background = pygame.image.load('background.png')
    fps = pygame.time.Clock()

    a = 150

    startTime = time.time()
    timer = int(time.time() - startTime)

    randhel = randint(0, 9)

    enemies = []

    player = (Player(250, 300, 25, 25, "player.png", 5))

    b = (Ball(644, 465, 35, 35, "enemy.png", 5, 5, 5))

    enemy_image = pygame.image.load('enemy.png')
    enemy_width, enemy_height = enemy_image.get_size()
    for enemy in enemies:
        enemy_rect = pygame.Rect(400, 300, 35, 35)

    player_image = pygame.image.load('player.png')

    # Основной цикл игры
    while True:
        timer = int(time.time() - startTime)

        # Очистка экрана
        screen.fill(BLACK)
        screen.blit(background, [0, 0])

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(enemyhp) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (795, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(health) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (534, 597)
        screen.blit(text, text_rect)

        # Згенеруємо нового ворога
        if random.randint(1, 100) < 7:
            enemy = {'x': random.randint(0, SCREEN_WIDTH), 'y': 0, 'speed': random.randint(1, 5)}
            enemies.append(enemy)

        for enemy in enemies:
            enemy['y'] += enemy['speed']
            if enemy['y'] > SCREEN_HEIGHT:
                enemies.remove(enemy)

        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 35, 35)
            if player.rect.colliderect(enemy_rect):
                randhel = 1
                health = health - randhel

        # Відображаємо ворогів
        for enemy in enemies:
            screen.blit(enemy_image, (enemy['x'], enemy['y']))

        b.rect.x += b.speed_x
        b.rect.y += b.speed_y

        # Получение состояния клавиатуры
        keys = pygame.key.get_pressed()

        # Перемещение персонажа
        if keys[pygame.K_LEFT]:
            player.rect.x -= player.speed
        elif keys[pygame.K_RIGHT]:
            player.rect.x += player.speed
        elif keys[pygame.K_UP]:
            player.rect.y -= player.speed
        elif keys[pygame.K_DOWN]:
            player.rect.y += player.speed

        if b.rect.x > 492:
            b.speed_x = -(b.speed_x)

        if b.rect.y > 303:
            b.speed_y = -(b.speed_y)

        if b.rect.x < 740:
            b.speed_x = -(b.speed_x)

        if b.rect.y < 550:
            b.speed_y = -(b.speed_y)

        if player.rect.x < 492:
            player.rect.x = 493
        if player.rect.x > 740:
            player.rect.x = 740
        if player.rect.y < 302:
            player.rect.y = 303
        if player.rect.y > 550:
            player.rect.y = 550

        if player.rect.colliderect(b.rect):
            b.speed_y *= -1
            randhel = randint(5, 20)
            health = health - 50

        if health <= 0:
            break

        if timer > 10:
            break

        player.draw(screen)
        b.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        pygame.display.update()

        fps.tick(60)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def attack1(screen):
    global health
    global enemyhp
    fps = pygame.time.Clock()
    background = pygame.image.load('background.png')

    startTime = time.time()
    timer = int(time.time() - startTime)

    enemies = []
    enemy_image = pygame.image.load('enemywall.png')
    enemy_width, enemy_height = enemy_image.get_size()
    for enemy in enemies:
        enemy_rect = pygame.Rect(400, 300, 50, 80)

    # Визначаємо розмір та швидкість гравця
    PLAYER_WIDTH = 25
    PLAYER_HEIGHT = 25
    PLAYER_VELOCITY = 3
    PLAYER_JUMP_VELOCITY = -10
    PLAYER_GRAVITY = 0.5

    # Визначаємо початкові координати гравця
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT - 100
    player_velocity_x = 0
    player_velocity_y = 0
    player_on_ground = False
    player_image = pygame.image.load('playerblue.png')

    # Головний цикл гри
    running = True
    while running:
        timer = int(time.time() - startTime)

        # Обробка руху гравця
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_velocity_x = -PLAYER_VELOCITY
        elif keys[pygame.K_RIGHT]:
            player_velocity_x = PLAYER_VELOCITY
        else:
            player_velocity_x = 0

        if keys[pygame.K_UP] and player_on_ground:
            player_velocity_y = PLAYER_JUMP_VELOCITY
            player_on_ground = False

        player_velocity_y += PLAYER_GRAVITY
        player_x += player_velocity_x
        player_y += player_velocity_y

        # Обмеження руху гравця
        if player_x < 492:
            player_x = 493
        elif player_x > 740:
            player_x = 740

        if player_y < 302:
            player_y = 302
        elif player_y > 550:
            player_y = 550
            player_on_ground = True

        fps.tick(120)

        # Відображення екрану
        screen.fill(BLACK)
        screen.blit(background, [0, 0])
        screen.blit(player_image, [player_x, player_y])

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(enemyhp) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (795, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(health) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (534, 597)
        screen.blit(text, text_rect)

        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Згенеруємо нового ворога
        if random.randint(1, 100) < 2:
            enemy = {'x': 0, 'y': 520, 'speed': random.randint(1, 5)}
            enemies.append(enemy)

        for enemy in enemies:
            enemy['x'] += enemy['speed']
            if enemy['x'] > SCREEN_WIDTH:
                enemies.remove(enemy)

        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 35, 35)
            playrect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
            if playrect.colliderect(enemy_rect):
                randhel = 1
                health = health - randhel

        # Відображаємо ворогів
        for enemy in enemies:
            screen.blit(enemy_image, (enemy['x'], enemy['y']))

        if timer > 10:
            break

        if health <= 0:
            break

        pygame.display.flip()

def attack4(screen):
    global health
    global enemyhp
    fps = pygame.time.Clock()
    background = pygame.image.load('background.png')

    startTime = time.time()
    timer = int(time.time() - startTime)

    enemies = []
    enemy_image = pygame.image.load('enemywall.png')
    enemy_width, enemy_height = enemy_image.get_size()
    for enemy in enemies:
        enemy_rect = pygame.Rect(400, 300, 50, 80)

    # Визначаємо розмір та швидкість гравця
    PLAYER_WIDTH = 25
    PLAYER_HEIGHT = 25
    PLAYER_VELOCITY = 3
    PLAYER_JUMP_VELOCITY = -10
    PLAYER_GRAVITY = 0.5

    # Визначаємо початкові координати гравця
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT - 100
    player_velocity_x = 0
    player_velocity_y = 0
    player_on_ground = False
    player_image = pygame.image.load('playerblue.png')

    # Головний цикл гри
    running = True
    while running:
        timer = int(time.time() - startTime)

        # Обробка руху гравця
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_velocity_x = -PLAYER_VELOCITY
        elif keys[pygame.K_RIGHT]:
            player_velocity_x = PLAYER_VELOCITY
        else:
            player_velocity_x = 0

        if keys[pygame.K_UP] and player_on_ground:
            player_velocity_y = PLAYER_JUMP_VELOCITY
            player_on_ground = False

        player_velocity_y += PLAYER_GRAVITY
        player_x += player_velocity_x
        player_y += player_velocity_y

        # Обмеження руху гравця
        if player_x < 492:
            player_x = 493
        elif player_x > 740:
            player_x = 740

        if player_y < 302:
            player_y = 302
        elif player_y > 550:
            player_y = 550
            player_on_ground = True

        fps.tick(120)

        # Відображення екрану
        screen.fill(BLACK)
        screen.blit(background, [0, 0])
        screen.blit(player_image, [player_x, player_y])

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(enemyhp) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (795, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(health) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (534, 597)
        screen.blit(text, text_rect)

        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Згенеруємо нового ворога
        if random.randint(1, 100) < 2:
            enemy = {'x': SCREEN_WIDTH, 'y': 520, 'speed': random.randint(1, 5)}
            enemies.append(enemy)

        for enemy in enemies:
            enemy['x'] -= enemy['speed']
            if enemy['x'] + enemy_width < 0:
                enemies.remove(enemy)

        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy_width, enemy_height)
            playrect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
            if playrect.colliderect(enemy_rect):
                randhel = 1
                health = health - randhel

        # Відображаємо ворогів
        for enemy in enemies:
            screen.blit(enemy_image, (enemy['x'], enemy['y']))

        if timer > 10:
            break

        if health <= 0:
            break

        pygame.display.flip()


def secret(screen):
    pygame.mixer.init()
    pygame.mixer.music.load('seret.wav')
    pygame.mixer.music.play(-1)

    fps = pygame.time.Clock()

    dialog = ["☟✋",
              '❄☟✋💧 ✋💧 💧☜👍☼☜❄',
              "✡⚐🕆 ✌☼☜ ☹🕆👍😐✡",
              '👌✡☜',
              'the stranger gone',
              ]
    now = 0
    font = pygame.font.SysFont("calibri", 25)
    background = pygame.image.load('secret menu.png')
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    now = now + 1
                    if now == 5:
                        now = 0
                        return

        screen.fill(BLACK)
        screen.blit(background, [0, 0])

        text = font.render(dialog[now], True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (120, 410)
        screen.blit(text, text_rect)

        pygame.display.flip()
        pygame.display.update()

        fps.tick(30)


def death(screen):
    global health
    global enemyhp
    pygame.mixer.init()
    pygame.mixer.music.load('game_over.wav')
    pygame.mixer.music.play(-1)
    startTime = time.time()
    timer = int(time.time() + startTime)
    fps = pygame.time.Clock()
    background = pygame.image.load('deathmenu1.png')
    dead = 1
    while True:
        timer = int(time.time() - startTime)
        if timer == 1:
            background = pygame.image.load('deathmenu.png')
        if timer == 2:
            background = pygame.image.load('deathmenu2.png')
        if timer == 5:
            break

        screen.fill(BLACK)
        screen.blit(background, [0, 0])
        pygame.display.flip()
        pygame.display.update()

        fps.tick(30)


def endeath(screen):
    startTime = time.time()
    timer = int(time.time() + startTime)
    fps = pygame.time.Clock()
    background = pygame.image.load('deathmenu1.png')
    pygame.mixer.init()
    pygame.mixer.music.load('end.wav')
    pygame.mixer.music.play(-1)

    while True:
        timer = int(time.time() - startTime)
        if timer == 1:
            background = pygame.image.load('endeath.png')
        if timer == 2:
            background = pygame.image.load('endeath1.png')
        if timer == 3:
            background = pygame.image.load('endeath2.png')
        if timer == 4:
            background = pygame.image.load('endeath3.png')
        if timer == 5:
            background = pygame.image.load('endeath4.png')
        if timer == 6:
            return

        screen.fill(BLACK)

        screen.blit(background, [0, 0])
        pygame.display.flip()
        pygame.display.update()

        fps.tick(30)


def Ok(screen):
    pygame.mixer.init()
    pygame.mixer.music.load('ok.wav')
    pygame.mixer.music.play(-1)

    startTime = time.time()
    startTime = time.time()
    back = 1
    timer = int(time.time() + startTime)
    background = pygame.image.load('ok.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    if back == 1:
                        background = pygame.image.load('ok1.png')
                        back = back + 1
                    elif back == 2:
                        background = pygame.image.load('ok2.jpg')
                        back = back + 1
                    elif back == 3:
                        return

        screen.fill(BLACK)
        screen.blit(background, [0, 0])
        pygame.display.flip()
        pygame.display.update()

        fps.tick(30)

def attack3(screen):
    global health
    global enemyhp
    background = pygame.image.load('background.png')
    fps = pygame.time.Clock()

    a = 150

    startTime = time.time()
    timer = int(time.time() - startTime)

    randhel = randint(0, 9)

    enemies = []

    player = (Player(250, 300, 25, 25, "player.png", 5))

    b = (Ball(644, 465, 35, 35, "enemy.png", 5, 5, 5))

    enemy_image = pygame.image.load('enemy.png')
    enemy_width, enemy_height = enemy_image.get_size()
    for enemy in enemies:
        enemy_rect = pygame.Rect(400, 300, 35, 35)

    player_image = pygame.image.load('player.png')

    # Основной цикл игры
    while True:
        timer = int(time.time() - startTime)

        # Очистка экрана
        screen.fill(BLACK)
        screen.blit(background, [0, 0])

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(enemyhp) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (795, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(health) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (534, 597)
        screen.blit(text, text_rect)

        # Згенеруємо нового ворога
        if random.randint(1, 100) < 7:
            enemy = {'x': SCREEN_WIDTH, 'y': random.randint(0, SCREEN_HEIGHT), 'speed': random.randint(1, 5)}
            enemies.append(enemy)

        for enemy in enemies:
            enemy['x'] -= enemy['speed']
            if enemy['x'] < 0:
                enemies.remove(enemy)

        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 35, 35)
            if player.rect.colliderect(enemy_rect):
                randhel = 1
                health = health - randhel

        # Відображаємо ворогів
        for enemy in enemies:
            screen.blit(enemy_image, (enemy['x'], enemy['y']))

        b.rect.x += b.speed_x
        b.rect.y += b.speed_y

        # Получение состояния клавиатуры
        keys = pygame.key.get_pressed()

        # Перемещение персонажа
        if keys[pygame.K_LEFT]:
            player.rect.x -= player.speed
        elif keys[pygame.K_RIGHT]:
            player.rect.x += player.speed
        elif keys[pygame.K_UP]:
            player.rect.y -= player.speed
        elif keys[pygame.K_DOWN]:
            player.rect.y += player.speed

        if b.rect.x > 492:
            b.speed_x = -(b.speed_x)

        if b.rect.y > 303:
            b.speed_y = -(b.speed_y)

        if b.rect.x < 740:
            b.speed_x = -(b.speed_x)

        if b.rect.y < 550:
            b.speed_y = -(b.speed_y)

        if player.rect.x < 492:
            player.rect.x = 493
        if player.rect.x > 740:
            player.rect.x = 740
        if player.rect.y < 302:
            player.rect.y = 303
        if player.rect.y > 550:
            player.rect.y = 550

        if player.rect.colliderect(b.rect):
            b.speed_y *= -1
            randhel = randint(5, 20)
            health = health - 50

        if health <= 0:
            break

        if timer > 10:
            break

        player.draw(screen)
        b.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        pygame.display.update()

        fps.tick(60)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def attack6(screen):
    global health
    global enemyhp
    background = pygame.image.load('background.png')
    fps = pygame.time.Clock()

    a = 150

    startTime = time.time()
    timer = int(time.time() - startTime)

    randhel = randint(0, 9)

    enemies = []

    player = (Player(250, 300, 25, 25, "player.png", 5))

    b = (Ball(644, 465, 35, 35, "enemy.png", 5, 5, 5))

    enemy_image = pygame.image.load('enemy.png')
    enemy_width, enemy_height = enemy_image.get_size()
    for enemy in enemies:
        enemy_rect = pygame.Rect(400, 300, 35, 35)

    player_image = pygame.image.load('player.png')

    # Основной цикл игры
    while True:
        timer = int(time.time() - startTime)

        # Очистка экрана
        screen.fill(BLACK)
        screen.blit(background, [0, 0])

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(enemyhp) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (795, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(health) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (534, 597)
        screen.blit(text, text_rect)

        # Згенеруємо нового ворога
        if random.randint(1, 100) < 7:
            side = random.randint(1, 4)  # Вибір сторони: 1 - зліва, 2 - справа, 3 - зверху, 4 - знизу
            if side == 1:  # Зліва
                enemy = {'x': 0, 'y': random.randint(0, SCREEN_HEIGHT), 'speed': random.randint(1, 5)}
            elif side == 2:  # Справа
                enemy = {'x': SCREEN_WIDTH, 'y': random.randint(0, SCREEN_HEIGHT), 'speed': random.randint(1, 5)}
            elif side == 3:  # Зверху
                enemy = {'x': random.randint(0, SCREEN_WIDTH), 'y': 0, 'speed': random.randint(1, 5)}
            elif side == 4:  # Знизу
                enemy = {'x': random.randint(0, SCREEN_WIDTH), 'y': SCREEN_HEIGHT, 'speed': random.randint(1, 5)}
            enemies.append(enemy)

        for enemy in enemies:
            if enemy['x'] < 0 or enemy['x'] > SCREEN_WIDTH or enemy['y'] < 0 or enemy['y'] > SCREEN_HEIGHT:
                enemies.remove(enemy)
            else:
                enemy['x'] += enemy['speed']
                enemy['y'] += enemy['speed']

        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 35, 35)
            if player.rect.colliderect(enemy_rect):
                randhel = 1
                health = health - randhel

        # Відображаємо ворогів
        for enemy in enemies:
            screen.blit(enemy_image, (enemy['x'], enemy['y']))

        b.rect.x += b.speed_x
        b.rect.y += b.speed_y

        # Получение состояния клавиатуры
        keys = pygame.key.get_pressed()

        # Перемещение персонажа
        if keys[pygame.K_LEFT]:
            player.rect.x -= player.speed
        elif keys[pygame.K_RIGHT]:
            player.rect.x += player.speed
        elif keys[pygame.K_UP]:
            player.rect.y -= player.speed
        elif keys[pygame.K_DOWN]:
            player.rect.y += player.speed

        if b.rect.x > 492:
            b.speed_x = -(b.speed_x)

        if b.rect.y > 303:
            b.speed_y = -(b.speed_y)

        if b.rect.x < 740:
            b.speed_x = -(b.speed_x)

        if b.rect.y < 550:
            b.speed_y = -(b.speed_y)

        if player.rect.x < 492:
            player.rect.x = 493
        if player.rect.x > 740:
            player.rect.x = 740
        if player.rect.y < 302:
            player.rect.y = 303
        if player.rect.y > 550:
            player.rect.y = 550

        if player.rect.colliderect(b.rect):
            b.speed_y *= -1
            randhel = randint(5, 20)
            health = health - 50

        if health <= 0:
            break

        if timer > 10:
            break

        player.draw(screen)
        b.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        pygame.display.update()

        fps.tick(60)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
def attack5(screen):
    global health
    global enemyhp
    background = pygame.image.load('background.png')
    fps = pygame.time.Clock()

    a = 150

    startTime = time.time()
    timer = int(time.time() - startTime)

    randhel = randint(0, 9)

    enemies = []

    player = (Player(250, 300, 25, 25, "player.png", 5))

    b = (Ball(644, 465, 35, 35, "enemy.png", 5, 5, 5))

    enemy_image = pygame.image.load('enemy.png')
    enemy_width, enemy_height = enemy_image.get_size()
    for enemy in enemies:
        enemy_rect = pygame.Rect(400, 300, 35, 35)

    player_image = pygame.image.load('player.png')

    # Основной цикл игры
    while True:
        timer = int(time.time() - startTime)

        # Очистка экрана
        screen.fill(BLACK)
        screen.blit(background, [0, 0])

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(enemyhp) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (795, 597)
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(health) + "/100", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect = (534, 597)
        screen.blit(text, text_rect)

        # Згенеруємо нового ворога
        if random.randint(1, 100) < 7:
            enemy = {'x': random.randint(0, SCREEN_WIDTH), 'y': random.randint(0, SCREEN_HEIGHT), 'speed_x': 0, 'speed_y': 0}

            # Встановлюємо напрямок руху для кожного ворога
            if enemy['x'] < SCREEN_WIDTH // 2:
                enemy['speed_x'] = 5  # Вороги зліва рухаються вправо
            else:
                enemy['speed_x'] = -5  # Вороги справа рухаються вліво

            if enemy['y'] < SCREEN_HEIGHT // 2:
                enemy['speed_y'] = 5  # Вороги зверху рухаються вниз
            else:
                enemy['speed_y'] = -5  # Вороги знизу рухаються вгору

            enemies.append(enemy)

        for enemy in enemies:
            enemy['x'] += enemy['speed_x']
            enemy['y'] += enemy['speed_y']
            if enemy['x'] < 0 or enemy['x'] > SCREEN_WIDTH or enemy['y'] < 0 or enemy['y'] > SCREEN_HEIGHT:
                enemies.remove(enemy)

        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 35, 35)
            if player.rect.colliderect(enemy_rect):
                randhel = 1
                health = health - randhel

        # Відображаємо ворогів
        for enemy in enemies:
            screen.blit(enemy_image, (enemy['x'], enemy['y']))

        b.rect.x += b.speed_x
        b.rect.y += b.speed_y

        # Получение состояния клавиатуры
        keys = pygame.key.get_pressed()

        # Перемещение персонажа
        if keys[pygame.K_LEFT]:
            player.rect.x -= player.speed
        elif keys[pygame.K_RIGHT]:
            player.rect.x += player.speed
        elif keys[pygame.K_UP]:
            player.rect.y -= player.speed
        elif keys[pygame.K_DOWN]:
            player.rect.y += player.speed

        if b.rect.x > 492:
            b.speed_x = -(b.speed_x)

        if b.rect.y > 303:
            b.speed_y = -(b.speed_y)

        if b.rect.x < 740:
            b.speed_x = -(b.speed_x)

        if b.rect.y < 550:
            b.speed_y = -(b.speed_y)

        if player.rect.x < 492:
            player.rect.x = 493
        if player.rect.x > 740:
            player.rect.x = 740
        if player.rect.y < 302:
            player.rect.y = 303
        if player.rect.y > 550:
            player.rect.y = 550

        if player.rect.colliderect(b.rect):
            b.speed_y *= -1
            randhel = randint(5, 20)
            health = health - 50

        if health <= 0:
            break

        if timer > 10:
            break

        player.draw(screen)
        b.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        pygame.display.update()

        fps.tick(60)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
pygame.mixer.init()
pygame.mixer.music.load('start.wav')
pygame.mixer.music.play()
startmenu(screen)

pygame.mixer.init()
pygame.mixer.music.load('megalovania.wav')
pygame.mixer.music.play(-1)
while True:
    level = randint(1, 151)
    if level > 0 and level < 25:
        menu(screen)
        if ok == 1:
            Ok(screen)
            break
        if enemyhp <= 0:
            endeath(screen)
            break
        attack(screen)
        if health <= 0:
            death(screen)
            break
    if level > 25 and level < 50:
        menu(screen)
        if ok == 1:
            Ok(screen)
            break
        attack1(screen)
        if health <= 0:
            death(screen)
            break
    if level == 151:
        secret(screen)
        pygame.mixer.init()
        pygame.mixer.music.load('megalovania.wav')
        pygame.mixer.music.play(-1)
    if level > 50 and level < 75:
        menu(screen)
        if ok == 1:
            Ok(screen)
            break
        attack2(screen)
        if health <= 0:
            death(screen)
            break
    if level > 75 and level < 100:
        menu(screen)
        if ok == 1:
            Ok(screen)
            break
        attack3(screen)
        if health <= 0:
            death(screen)
            break
    if level > 100 and level < 125:
        menu(screen)
        if ok == 1:
            Ok(screen)
            break
        attack4(screen)
        if health <= 0:
            death(screen)
            break
    if level > 125 and level < 151:
        menu(screen)
        if ok == 1:
            Ok(screen)
            break
        attack5(screen)
        if health <= 0:
            death(screen)
            break


