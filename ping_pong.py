from pygame import * 
from random import randint


win_width = 700
win_height = 500
class  GameSprits(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Playre(GameSprits):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self. rect.centerx, self.rect.top, 25,50,10 )
        bullets.add(bullet)
        bullet_Sound.play()





window = display.set_mode((win_width, win_height))
display.set_caption('Shuter Game')
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))



playre1 = Playre('roket.png', 5, 250, 100 , 100, 4)
playre2 = Playre('roket2.png', 590, 230, 130 , 130, 4)
playre3 = Playre('ball.png', 320, 300, 50, 50, 2)





finish = False
run = True
clock = time.Clock()
FPS = 60
while run:

    window.blit(background, (0, 0))
    playre1.reset()
    playre1.update_l()
    playre2.reset()
    playre2.update_r()
    playre3.reset()
    playre3.update()
    # monsters.draw(window)
    # monsters.update()
    # bullets.draw(window)
    # bullets.update()
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                playre.fire()

    
    

    

    #text = font.Font(None,30)
    
    display.update()
    clock.tick(FPS)

display.update()






















































































