import pygame
import sys
import time


def import_image_library():
    image_lib = [pygame.image.load('Images/Pac1.png'), pygame.image.load('Images/Pac2.png'),
                 pygame.image.load('Images/Pac3.png'), pygame.image.load('Images/Tile.png'),
                 pygame.image.load('Images/SmallPill.png'), pygame.image.load('Images/LargePill1.png'),
                 pygame.image.load('Images/LargePill2.png'), pygame.image.load('Images/LargePill3.png'),
                 pygame.image.load('Images/LargePill4.png'), pygame.image.load('Images/LargePill5.png'),
                 pygame.image.load('Images/LargePill6.png'), pygame.image.load('Images/LargePill7.png'),
                 pygame.image.load('Images/LargePill8.png'), pygame.image.load('Images/LargePill9.png'),
                 pygame.image.load('Images/LargePill10.png'), pygame.image.load('Images/LargePill11.png'),
                 pygame.image.load('Images/BlinkyDown1.png'), pygame.image.load('Images/BlinkyDown2.png'),
                 pygame.image.load('Images/BlinkyLeft1.png'), pygame.image.load('Images/BlinkyLeft2.png'),
                 pygame.image.load('Images/BlinkyUp1.png'), pygame.image.load('Images/BlinkyUp2.png'),
                 pygame.image.load('Images/BlinkyRight1.png'), pygame.image.load('Images/BlinkyRight2.png'),
                 pygame.image.load('Images/ClydeDown1.png'), pygame.image.load('Images/ClydeDown2.png'),
                 pygame.image.load('Images/ClydeLeft1.png'), pygame.image.load('Images/ClydeLeft2.png'),
                 pygame.image.load('Images/ClydeUp1.png'), pygame.image.load('Images/ClydeUp2.png'),
                 pygame.image.load('Images/ClydeRight1.png'), pygame.image.load('Images/ClydeRight2.png'),
                 pygame.image.load('Images/InkyDown1.png'), pygame.image.load('Images/InkyDown2.png'),
                 pygame.image.load('Images/InkyLeft1.png'), pygame.image.load('Images/InkyLeft2.png'),
                 pygame.image.load('Images/InkyUp1.png'), pygame.image.load('Images/InkyUp2.png'),
                 pygame.image.load('Images/InkyRight1.png'), pygame.image.load('Images/InkyRight2.png'),
                 pygame.image.load('Images/PinkyDown1.png'), pygame.image.load('Images/PinkyDown2.png'),
                 pygame.image.load('Images/PinkyLeft1.png'), pygame.image.load('Images/PinkyLeft2.png'),
                 pygame.image.load('Images/PinkyUp1.png'), pygame.image.load('Images/PinkyUp2.png'),
                 pygame.image.load('Images/PinkyRight1.png'), pygame.image.load('Images/PinkyRight2.png'),
                 pygame.image.load('Images/VulnerableGhost1.png'), pygame.image.load('Images/VulnerableGhost2.png'),
                 pygame.image.load('Images/VulnerableGhost3.png'), pygame.image.load('Images/VulnerableGhost4.png'),
                 pygame.image.load('Images/Death1.png'), pygame.image.load('Images/Death2.png'),
                 pygame.image.load('Images/Death3.png'), pygame.image.load('Images/Death4.png'),
                 pygame.image.load('Images/Death5.png'), pygame.image.load('Images/Death6.png')]
    return image_lib


def import_sound_library():
    sound_lib = [pygame.mixer.Sound('Sounds/Intro.wav'), pygame.mixer.Sound('Sounds/ConstantSound.wav'),
                 pygame.mixer.Sound('Sounds/Death.wav'), pygame.mixer.Sound('Sounds/Eating.wav'),
                 pygame.mixer.Sound('Sounds/Fruit.wav'), pygame.mixer.Sound('Sounds/GhostDeath.wav'),
                 pygame.mixer.Sound('Sounds/GhostDeathTravel.wav'), pygame.mixer.Sound('Sounds/Vulnerable.wav')]
    for sound in sound_lib:
        sound.set_volume(0.4)
    return sound_lib


def check_key_down_events(event, pacman):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        pacman.check_move("left")
    elif event.key == pygame.K_RIGHT:
        pacman.check_move("right")
    elif event.key == pygame.K_DOWN:
        pacman.check_move("down")
    elif event.key == pygame.K_UP:
        pacman.check_move("up")


def check_events(pacman):
    #   Responds to key presses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, pacman)
        else:
            return


def check_time(clock, delta_t, ghosts, large_pills, timer, timer2, timer3, pacman):
    timer -= delta_t
    timer2 -= delta_t
    timer3 -= delta_t
    if timer <= 0:
        pacman.change_image()
        timer = 1
    if timer2 <= 0:
        for pill in large_pills:
            pill.change_image()
        timer2 = 0.5
    if timer3 <= 0:
        for ghost in ghosts:
            ghost.change_image()
        timer3 = 1.5
    delta_t = clock.tick(60) / 60
    return delta_t, timer, timer2, timer3


def next_level(ghosts, pacman):
    pacman.reset()
    for obj in ghosts:
        obj.reset()


def check_ghost_collisions(ghosts, large_pills, maze, pacman, pills, scoreboard):
    for obj in ghosts:
        if pygame.Rect.colliderect(obj.rect, pacman.rect) and obj.vulnerable is False:
            pacman.die()
            scoreboard.update_lives(-1)
            for g in ghosts:
                g.reset()
            soft_reset(ghosts, large_pills, maze, pacman, pills, scoreboard)
            break


def soft_reset(ghosts, large_pills, maze, pacman, pills, scoreboard):
    scoreboard.screen.fill(scoreboard.settings.get_bg_color())
    for ghosts in ghosts:
        ghosts.blit()
    for pill in pills:
        pill.blit()
    for pill in large_pills:
        pill.blit()
    pacman.blit()
    maze.draw_part_maze()
    scoreboard.blit()
    scoreboard.blit_lives()


def check_collisions(ghosts, large_pills, maze, pacman, pills, scoreboard, sound):
    check_ghost_collisions(ghosts, large_pills, maze, pacman, pills, scoreboard)
    for index, pill in enumerate(pills):
        if pacman.rect.colliderect(pill.rect):
            scoreboard.update_score(pill.value)
            pygame.mixer.Sound.play(sound)
            del pills[index]
    for index, pill in enumerate(large_pills):
        if pacman.rect.colliderect(pill.rect):
            scoreboard.update_score(pill.value)
            for g in ghosts:
                g.set_vulnerable()
            del large_pills[index]
    if len(pills) == 0 and len(large_pills) == 0:
        next_level(ghosts, pacman)
        return True
    return False


def append_score(current_score):
    score_list = []
    try:
        with open('high score.txt', 'r') as f:
            new_one = f.readline()
            while new_one != "":
                score_list.append(int(new_one))
                new_one = f.readline()
            score_list.append(int(current_score))
            score_list.sort(reverse=True)
            while len(score_list) > 10:
                del (score_list[10])
            print(score_list)
            f.close()
        with open('high score.txt', 'w') as f:
            for line in score_list:
                f.write(str(line))
                f.write("\n")
            f.close()
    except FileNotFoundError:
        with open('high score.txt', 'w') as f:
            f.write(current_score)


def wait_for_space(current_score):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return False
            elif event.key == pygame.K_q:
                if current_score is not 0:
                    append_score(current_score)
                sys.exit(0)
    return True


def start_game(ghosts, large_pills, pacman, pills, sound):
    pacman.blit()
    for ghost in ghosts:
        ghost.blit()
    for pill in pills:
        pill.blit()
    for pill in large_pills:
        pill.blit()
    pygame.display.flip()
    pygame.mixer.Sound.play(sound)
    time.sleep(4.5)
