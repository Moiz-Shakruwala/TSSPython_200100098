import pygame, sys, time, random
from pygame.sprite import collide_rect

#initial game variables

#Variables that can be changed
frame_size_x = 720
frame_size_y = 480
bg_color = (40,255,40)
snake_color = (0,150,150)
food_color = (100,80,80)
game_speed = 20

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = ['RIGHT']
change_to = direction

#Parameters for food
food_pos = [0,0]
food_spawn = [True]

score = [0]

# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
font1 = pygame.font.Font('freesansbold.ttf',20)
font2 = pygame.font.Font('freesansbold.ttf',40)
# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()

def check_for_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction[0] != 'DOWN' :
                direction[0] = 'UP'
            elif event.key == pygame.K_DOWN and direction[0] != 'UP':
                direction[0] = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction[0] != 'LEFT':  
                direction[0] = 'RIGHT' 
            elif event.key == pygame.K_LEFT and direction[0] != 'RIGHT' :  
                direction[0] = 'LEFT'

def update_snake():
    
    if direction[0]=='RIGHT':
        snake_pos[0]+=10
    elif direction[0]=='LEFT':
        snake_pos[0]-=10
    elif direction[0]=='DOWN':
        snake_pos[1]+=10
    elif direction[0]=='UP':
        snake_pos[1]-=10
    rect1 =pygame.Rect(snake_pos[0], snake_pos[1], 10, 10)
    rect2 =pygame.Rect(food_pos[0], food_pos[1], 10, 10)
    list =[]
    for i in range(len(snake_body)-2):
        list.append(pygame.Rect(snake_body[i+2][0], snake_body[i+2][1], 10, 10))
    if rect1.colliderect(rect2) :
        score[0] += 1
        snake_body.insert(0,snake_pos.copy())
        food_spawn[0]=True
    elif rect1.bottom > frame_size_y or rect1.right > frame_size_x or rect1.top < 0 or rect1.left < 0   :
        game_over()
    elif rect1.collidelist(list) != -1:
        game_over()
    else:
        snake_body.pop()
        snake_body.insert(0,snake_pos.copy())
    
def create_food():
    if food_spawn[0]==True:
        food_spawn[0]=False
        food_pos[0]=random.randrange(0,frame_size_x,10)
        food_pos[1]=random.randrange(0,frame_size_y,10)
   

def show_score(pos, color):
    score_show = font1.render("Score: "+str(score[0]),True,color)
    game_window.blit(score_show,(pos[0],pos[1]))
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
  
def update_screen():
    game_window.fill(bg_color)
    pygame.draw.rect(game_window,(70,70,0),pygame.Rect(snake_body[0][0], snake_body[0][1], 10, 10))
    for i in range(len(snake_body)-1):
        pygame.draw.rect(game_window,snake_color,pygame.Rect(snake_body[i+1][0], snake_body[i+1][1], 10, 10))
    pygame.draw.rect(game_window,food_color,pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    show_score([10,10],(255,255,0))
    pygame.display.flip()

def game_over():
    message = font2.render("YOU DIED", True, (215,0,215))
    message_rect = message.get_rect()
    message_rect.centerx = frame_size_x/2
    message_rect.top = 40
    game_window.blit(message,message_rect)
    show_score([10,10], (20,34,190))
    pygame.display.flip()
    time.sleep(3)
    sys.exit(0)

# Main loop
while True:
    check_for_events()
    
    update_snake()
    
    create_food()

    update_screen()

    fps_controller.tick(game_speed)