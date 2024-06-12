import pygame
import sys
import os
import random


# init pygame
pygame.init()

# creaate screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption('Resistor Color Value')
icon = pygame.image.load('resistoricon.png')
pygame.display.set_icon(icon)

rcolor = (240, 240, 150)

user_font = pygame.font.Font(None, 30)
o_user_text = '0'
e_user_text = '0'
o_input_rect = pygame.Rect(50, 285, 225, 30)
e_input_rect = pygame.Rect(50, 320, 225, 30)

color_active = (255, 255, 255)
color_passive = (200, 200, 200)

o_color = color_passive
e_color = color_passive
o_active = False
e_active = False
result_active = False
lanjut = False
user_o = 0
user_e = 0
e_result = 0
o_result = 0

# color value

RC = {
0: (0, 0, 0),
1: (102, 51, 0),
2: (255, 0, 0),
3: (255, 128, 0),
4: (255, 255, 0),
5: (0, 255, 0),
6: (0, 0, 255),
7: (102, 0, 102),
8: (100, 100, 100),
9: (255, 255, 255),
10: (200, 175, 0),
11: (210, 210, 210)
}

# logic

c1 = 100
c2 = 100
c3 = 100
c4 = 100
e_c = (1, 2, 5, 6, 7, 8 ,10,  11)

e_values = {
1: 1,
2: 2,
5: 0.5,
6: 0.25,
7: 0.10,
8: 0.05,
10: 5,
11: 10
}

o_value_l = []
o_value = 0

for i in range(3):
    if c1 == 100:
        c_random = random.randint(0, 9)
        c1 = c_random
        o_value_l.append(c_random)
        continue
    if c2 == 100:
        c_random = random.randint(0, 9)
        c2 = c_random
        o_value_l.append(c_random)
        continue
    if c3 == 100:
        c_random = random.randint(0, 11)
        c3 = c_random
        if c_random == 10:
            c_random = -1
        elif c_random == 11:
            c_random = -2
        
        s_o = [str(integer) for integer in o_value_l]
        o_string = "".join(s_o)
        o_value = float(o_string)
        o_value = o_value * 10 ** c_random
        continue

while c4 == 100:
    c_random = random.choice(e_c)
    if c_random != 10:
        if random.random() < .5:
            c_random = 10
        c4 = c_random
        e_value = e_values[c_random]


# color r

def rc1():
    pygame.draw.rect(screen, RC[c1], pygame.Rect(145, 25, 20, 200))
    
def rc2():
    pygame.draw.rect(screen, RC[c2], pygame.Rect(230, 50, 20, 150))
    
def rc3():
    pygame.draw.rect(screen, RC[c3], pygame.Rect(305, 50, 20, 150))
    
def rc4():
    pygame.draw.rect(screen, RC[c4], pygame.Rect(435, 25, 20, 200))

# game loop

while True:
    
    screen.fill((40, 20, 20))
    
    pygame.draw.rect(screen, (180, 180, 180), pygame.Rect(0, 120, 600, 15),)
    pygame.draw.rect(screen, rcolor, pygame.Rect(105, 25, 100, 200), border_radius=18)
    pygame.draw.rect(screen, rcolor, pygame.Rect(395, 25, 100, 200), border_radius=18)
    pygame.draw.rect(screen, rcolor, pygame.Rect(205, 50, 190, 150))
    pygame.draw.rect(screen, RC[9], pygame.Rect(290, 285, 30, 30), border_radius=5)
    pygame.draw.rect(screen, RC[9], pygame.Rect(290, 320, 30, 30), border_radius=5)
    
    check_rect = pygame.draw.rect(screen, RC[5],
    pygame.Rect(335, 285, 100, 65), border_radius=18)
    
    new_rect = pygame.draw.rect(screen, RC[5],
    pygame.Rect(450, 285, 100, 65), border_radius=18)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if o_input_rect.collidepoint(event.pos):
                o_active = True
            else:
                o_active = False
            if e_input_rect.collidepoint(event.pos):
                e_active = True
            else:
                e_active = False
            if check_rect.collidepoint(event.pos):
                result_active = True
            if new_rect.collidepoint(event.pos):
                os.execl(sys.executable, sys.executable, *sys.argv)
            
        if event.type == pygame.KEYDOWN:
            if o_active == True:
                if event.key == pygame.K_BACKSPACE:
                    o_user_text = o_user_text[0:-1]
                elif event.key == pygame.K_COMMA or event.key == pygame.K_PERIOD:
                    if '.' not in o_user_text:
                        o_user_text += '.'
                elif event.unicode.isdigit():
                    o_user_text += event.unicode
            if e_active == True:
                if event.key == pygame.K_BACKSPACE:
                    e_user_text = e_user_text[0:-1]
                elif event.key == pygame.K_COMMA or event.key == pygame.K_PERIOD:
                    if '.' not in e_user_text:
                        e_user_text += '.'
                elif event.unicode.isdigit():
                    e_user_text += event.unicode
                    
    if o_user_text != '':
        if e_user_text != '':
            user_o = float(o_user_text)
            user_e = float(e_user_text)
                    
    if result_active == True:
        lanjut = True
        if o_value == user_o:
            o_result = RC[5]
        else:
            o_result = RC[2]                
        if e_value == user_e:
            e_result = RC[5]
        else:
            e_result = RC[2]
    
    if lanjut == True:
        pygame.draw.rect(screen, o_result, pygame.Rect(295, 290, 20, 20),
        border_radius=10)
        pygame.draw.rect(screen, e_result, pygame.Rect(295, 325, 20, 20),
        border_radius=10)
        result_active = False
    
    if o_active:
        o_color = color_active
    else:
        o_color = color_passive
    if e_active:
        e_color = color_active
    else:
        e_color = color_passive
                
    pygame.draw.rect(screen, o_color, o_input_rect, border_radius=5)
    pygame.draw.rect(screen, e_color, e_input_rect, border_radius=5)
    
    o_indicator = user_font.render('R(Ω) :', True, (0, 0, 0))
    screen.blit(o_indicator, (o_input_rect.x + 5, o_input_rect.y + 5))
    e_indicator = user_font.render('±(%) :', True, (0, 0, 0))
    screen.blit(e_indicator, (e_input_rect.x + 5, e_input_rect.y + 5))
    check_letter = user_font.render('CHECK', True, RC[0])
    screen.blit(check_letter, (check_rect.x + 15, check_rect.y + 24))
    new_letter = user_font.render('NEW', True, RC[0])
    screen.blit(new_letter, (new_rect.x + 27, new_rect.y + 24))
            
    o_text_surface = user_font.render(o_user_text, True, (0, 0, 0))
    screen.blit(o_text_surface, (o_input_rect.x + 70, o_input_rect.y + 5)) 
    e_text_surface = user_font.render(e_user_text, True, (0, 0, 0))
    screen.blit(e_text_surface, (e_input_rect.x + 70, e_input_rect.y + 5))     
    
    
    rc1()
    rc2()
    rc3()
    rc4()
    
    pygame.display.flip()
    clock.tick(60)
