import pygame
from pygame.color import THECOLORS
import sys
import requests

pygame.init() # Обязательная инициализация библиотеки!

mini_font = pygame.font.SysFont(None,24)  
max_font = pygame.font.SysFont(None,36)


#цВЕТА
PINK = (255, 0, 213)
VIOLET =(204, 0, 255)
BLUE = (4, 0, 255)
RED = (255, 0, 0)

cards_for_game = [
    {'name': 'Golgari Grave-Troll', 'cost' : '5', 'type': 'Creature', 'strength' : '0' , 'health' : '0' },
    {'name': 'Force of Negation', 'cost' : '3', 'type': 'Instant', 'effect': 'If its not your turn, you may exile a blue card from your hand rather than pay this spells mana cost'},
    {'name': 'Ather Vial', 'cost' : '1', 'type': 'Artifact', 'strength' : '' , 'health' : ''},
    {'name': 'Shamans Trance', 'cost' : '3', 'type': 'Instant', 'strength' : '' , 'health' : ''},
    {'name': 'Cabal Ritual', 'cost' : '2', 'type': 'Instant', 'strength' : '' , 'health' : ''} #найти человеков 
]

def draw_text(text,font,colour,x,y,surface):
    object_text = font.render(text,True,colour)
    rect_text = object_text.get_rect()
    rect_text.topleft = (x,y)
    surface.blit(object_text,rect_text)

# Реализуйте в этом методе создание окна размером 1280х720
def create_screen():
    screen_size = length, width = (1280, 720)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Все будет хорощо :)')
    return screen


def information_about_card(screen,card_info):
    font = pygame.font.SysFont(None,25)
    all_information = f"Название карты {card_info['name']}, Цена {card_info['cost']},Тип {card_info['type']}"
    if 'strenght' in card_info and 'health' in card_info:
        all_information += f"Сила {card_info['strength']}, Выносливость {card_info['health']}"
    elif 'effect' in card_info:
        all_information += f"Эффект {card_info['effect']}"
    render_text = font.render(all_information,True,THECOLORS['black'])
    screen.blit(render_text,(720,360))
    
    
def textures():
    enter = pygame.image.load('pictures/inter/play.png')
    enter = pygame.transform.scale(enter,(180,180))
    enter_ance = enter.get_rect()
    enter_ance.center = (550,360)
    enter_settings = enter_ance,enter
    
    exit = pygame.image.load('pictures/inter/exit.png')
    exit = pygame.transform.scale(exit,(180,180))
    exit_ance = exit.get_rect()
    exit_ance.center = (760,360)
    exit_settings = exit_ance,exit
    
    return enter_settings, exit_settings

def loading_background():
    background = pygame.image.load('pictures/playing_field/field.jpg')
    background = pygame.transform.scale(background,(1280,720))
    return background
    
    

def new_game():
    print('ghbdndnn')


# Опишите базовый цикл, который считывает и выводит на экран нажатие клавиш
# Если нажата клавиша ESC, то окно закрывается
def game_loop(screen):
    
    user_name = ''
    password = ''
    text_box_user_name = pygame.Rect(180,100,200,30) #игр
    text_box_password = pygame.Rect(180,135,200,30) #
    activate_user_name = False
    activate_password = False
    message = ''
    
    background = loading_background()
    start_button,exit_button = textures()
    
    running = True
    while running:
        #Фон    
        screen.blit(background,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if activate_user_name:
                    if event.key == pygame.K_RETURN:
                        activate_user_name = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        user_name += event.unicode
                elif activate_password:
                    if event.key == pygame.K_RETURN:
                        activate_password = False
                    elif event.key == pygame.K_BACKSPACE:
                        password = user_name[:-1]
                    else:
                        password += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button[0].collidepoint(event.pos):
                    new_game()
                elif exit_button[0].collidepoint(event.pos):
                    running = False
                elif text_box_user_name.collidepoint(event.pos):
                    activate_user_name = True
                    activate_password = False
                elif text_box_password.collidepoint(event.pos):
                    activate_user_name = False
                    activate_password = True
                else:
                    activate_user_name = False
                    activate_password = False
        
        if pygame.mouse.get_pressed()[0] and start_button[0].collidepoint(pygame.mouse.get_pos()):
            if len(password) > 0 and len(user_name) > 0:
                try: 
                    answer = requests.post('http://127.0.0.1:8000/auth', json= {'user_name': user_name,'password': password})
                    if answer.status_code == 200: 
                        message = f'Авторизация прошла. ID:{answer.json()["id"]}' 
                    else:
                        message = f'Ошибка входа. {answer.status_code}'
                except Exception as e:
                    message = 'Ошибка на сервере'
            else:
                message = f'Ошибка ввода.'
            
        draw_text(message, max_font, BLUE,400,150,screen)    
        
        
        #Кнопки
        screen.blit(start_button[1],start_button[0])
        screen.blit(exit_button[1],exit_button[0])
        
        pygame.draw.rect(screen, BLUE , text_box_user_name,2)
        draw_text(user_name,mini_font,BLUE,200,100,screen) # 
        
        pygame.draw.rect(screen,RED, text_box_password,2)
        draw_text(password,mini_font,RED,200,145,screen) # 

        #Текст
        draw_text('username: ', max_font, PINK, 50, 100, screen)
        draw_text('password: ', max_font, VIOLET, 50, 140, screen)
        
        pygame.display.flip()
    pygame.quit()
    sys.exit()
    
    
    
  
# main функция, из которой будет запускаться игра
if __name__ == '__main__':
  screen = create_screen()
  game_loop(screen)
  
  
  
  