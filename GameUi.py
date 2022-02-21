import pygame

pygame.init()


class GameUi:
    def __init__(self):
        self.win = pygame.display.set_mode((800, 650))
        pygame.display.set_caption('Mario')

        self.fps = 30
        self.run = True

    def commands(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.run = False

    def render(self):
        self.win.fill((0, 0, 0))
        for y in range(20, 550, 160):
            for x in range(20, 800, 160):
                pygame.draw.rect(self.win, (255, 255, 255), (x, y, 120, 120))

    def gameloop(self):
        while self.run:
            pygame.time.Clock().tick(self.fps)
            self.commands()
            self.render()
            pygame.display.update()


pygame.quit()

'''
win = pygame.display.set_mode((600,400))
pygame.display.set_caption('Mario')

FPS = 30 #Change if you want to speed up the animation
run = True

x = 0
y = 323

def commands():
    global run, x, y, rindex, lindex, is_right
    keys = pygame.key.get_pressed()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    
    if keys[pygame.K_RIGHT]:
        is_right = True
        x += vel
        rindex += 1
    if not keys[pygame.K_RIGHT]:
        rindex = 0

        if keys[pygame.K_LEFT]:
            is_right = False
            x -= vel
            lindex += 1
        if not keys[pygame.K_LEFT]:
            lindex = 0
        
def render():
    global rindex, lindex
    win.blit(bg,(0, 0))
    if is_right:
        win.blit(mario_right[rindex], (x,y))
        if rindex >= len(mario_right) - 1:
            rindex = 0
    else:
        win.blit(mario_left[lindex], (x,y))
        if lindex >= len(mario_left) - 1:
            lindex = 0
    

while run:
    pygame.time.Clock().tick(FPS)
    commands()
    render()
    #print(hitbox)
    pygame.display.update()
'''
