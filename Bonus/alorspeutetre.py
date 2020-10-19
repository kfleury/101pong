#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## oui
## File description:
## oui
##

import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

lanched_jeu = True
lanched = True
fenetre = pygame.display.set_mode((800, 600))
fenetre2 = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 35)
myfont = pygame.font.SysFont('Helvetic', 100)
myfont2 = pygame.font.SysFont('Helvetic', 90)
myfont3 = pygame.font.SysFont('Helvetic', 35)
myfont4 = pygame.font.SysFont('Helvetic', 180)
myfont5 = pygame.font.SysFont('Helvetic', 50)
myfont6 = pygame.font.SysFont('Helvetic', 60)
player = pygame.font.SysFont('Helvetic', 35)
player2 = pygame.font.SysFont('Helvetic', 35)

fenetre.fill((255, 255, 255))

def on_off():
    global lanched
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lanched = False

def biballe(fond):
    print("oui")
    balle = pygame.image.load("ball.jpg").convert()
    position_balle = balle.get_rect()
    position_balle.center = 400, 300
    fond.blit(balle, position_balle)
    pygame.display.flip()
    position_balle = position_balle.move(0, 50)
    print('oui')
    pygame.display.flip()

def pong(plyr1, plyr2):
    fond = pygame.image.load("sketch-1573480666268.jpg").convert()
    raquette = pygame.image.load("sketch-1573481517826.jpg").convert()
    position_raquette = raquette.get_rect()
    position_raquette.center = 100,300
    raquette2 = pygame.image.load("sketch-1573481517826.jpg").convert()
    position_raquette2 = raquette2.get_rect()
    position_raquette2.center = 700,300
    text = myfont6.render(plyr1, True, (255, 255, 255))
    text1 = myfont6.render(plyr2, True, (255, 255, 255))
    fond.blit(text, (80, 50))
    fond.blit(text1, (430, 50))
    pygame.key.set_repeat(50, 50)
    pygame.display.flip()
    biballe(fond)
    while lanched:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    position_raquette = position_raquette.move(0,50)
                if position_raquette.top < 167:
                    position_raquette.top = 550
                if event.key == K_UP:
                    position_raquette = position_raquette.move(0,-50)
                if position_raquette.bottom > 575:
                    position_raquette.bottom = 195
                if event.key == K_s:
                    position_raquette2 = position_raquette2.move(0,50)
                if position_raquette2.top < 167:
                    position_raquette2.top = 550
                if event.key == K_z:
                    position_raquette2 = position_raquette2.move(0,-50)
                if position_raquette2.bottom > 575:
                    position_raquette2.bottom = 195
        fenetre2.blit(fond, (0, 0))
        fenetre2.blit(raquette, position_raquette)
        fenetre2.blit(raquette2, position_raquette2)
        pygame.display.flip()

def fade_screen():
    fade = pygame.Surface((800, 600))
    fade.fill((0, 0, 0))
    for alpha in range (0, 300):
        fade.set_alpha(alpha)
        fenetre.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

def name(player):
    font = pygame.font.Font(None, 35)
    while lanched:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    player += event.unicode
                    print(player)
                if event.key == pygame.K_BACKSPACE:
                    player = player[:-1]
                    print(player)
                if event.unicode.isnumeric():
                    player += event.unicode
                    print(player)
                if event.key == pygame.K_RETURN:
                    return player

def mouse_play(plyr1, plyr2):
    while lanched:
        for event in pygame.event.get():
            souris = pygame.mouse.get_pressed()
            if souris[0]:
                pos_mouse = pygame.mouse.get_pos()
                if 350 < pos_mouse[0] < 450 and 540 < pos_mouse[1] < 590:
                    fade_screen()
                    main_jeu(plyr1, plyr2)

def name_entry():
    plyr1 = ""
    plyr2 = ""
    plyr1 = name(plyr1)
    plyr2 = name(plyr2)
    disp = font.render(plyr1, True, (0, 0, 0))
    disp2 = font.render(plyr2, True, (0, 0, 0))
    fenetre.blit(disp, (350, 450))
    fenetre.blit(disp2, (350, 500))
    pygame.display.flip()
    pygame.draw.rect(fenetre, (0, 0, 0), (350, 540, 100, 50))
    play = myfont5.render("PLAY", False, (255, 255, 255))
    fenetre.blit(play, (355, 547))
    pygame.display.flip()
    mouse_play(plyr1, plyr2)

def souris_menu():
    global lanched
    souris = pygame.mouse.get_pressed()
    text = myfont3.render("Nom Joueur 1:", False, (0, 0, 0))
    text2 = myfont3.render("Nom Joueur 2:", False, (0, 0, 0))
    if souris[0]:
        pos_souris = pygame.mouse.get_pos()
        if 250 < pos_souris[0] < 550 and 300 < pos_souris[1] < 400:
            fenetre.blit(text, (150, 450))
            fenetre.blit(text2, (150, 500))
            pygame.display.flip()
            name_entry()

def menu():
    Titre = myfont4.render("101-PONG", True, (0, 0, 0))
    pygame.draw.rect(fenetre, (0, 0, 0), (250, 160, 300, 100))
    pygame.draw.rect(fenetre, (0, 0, 0), (250, 300, 300, 100))
    Text = myfont.render("1 Joueur", False, (255, 255, 255))
    Text2 = myfont2.render("2 Joueurs", False, (255, 255, 255))
    fenetre.blit(Titre, (100, 30))
    fenetre.blit(Text, (250, 180))
    fenetre.blit(Text2, (250, 325))
    pygame.display.flip()
    souris_menu()

afficher = menu

def main_jeu(plyr1, plyr2):
    fenetre2 = pygame.display.set_mode((800, 600))
    while lanched_jeu:
        pong(plyr1, plyr2)
        pygame.display.update()
    pygame.quit()

def main():
    while lanched:
        on_off()
        afficher()
        pygame.display.update()
    pygame.quit()
if __name__ == '__main__':
    main()
