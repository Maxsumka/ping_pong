#Создай собственный Шутер!

from pygame import * 
from random import randint

score = 0
lose = 0


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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self. rect.centerx, self.rect.top, 25,50,10 )
        bullets.add(bullet)
        bullet_Sound.play()

        

    


class Enemy(GameSprits):
    def update(self):
        self.rect.y += self.speed
        global lose
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lose += 1
        
class Bullet(GameSprits):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
        
   
            


window = display.set_mode((win_width, win_height))
display.set_caption('Shuter Game')
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
        
playre = Playre('roket.png', 5, win_height - 110, 100 , 100, 10)


monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 50, 50, randint(1, 3))
    monsters.add(monster)

bullets = sprite.Group()





font.init()

font = font.Font(None, 30)
Lose = font.render('YOU LOSE', True, (255, 0, 0))
Win = font.render('YOU WIN', True, (0, 255, 0))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
bullet_Sound = mixer.Sound('fire.ogg')


finish = False
run = True
clock = time.Clock()
FPS = 60
while run:
    
    window.blit(background, (0, 0))
    playre.reset()
    playre.update()
    monsters.draw(window)
    monsters.update()
    bullets.draw(window)
    bullets.update()
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                playre.fire()

    
    
    sprites_list = sprite.groupcollide(
        monsters, bullets, True, True
    )
    for i in sprites_list:
        score += 1
        monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 50, 50, randint(1, 3))
        monsters.add(monster)
    if score == 10:
        window.blit(Win, (200, 200))
        break
        


    if lose == 3  or sprite.spritecollide(playre, monsters, False):
        window.blit(Lose, (300, 300))
        break
    





    SCORE = font.render('Сщётчик очков ' + str(score), 1, (215,215,21))
    LOSE = font.render('Сщётчик врагов ' + str(lose), 1, (215,215,21))
    window.blit(SCORE, (0, 0))
    window.blit(LOSE, (0, 21))
    

    #text = font.Font(None,30)
    
    display.update()
    clock.tick(FPS)

display.update()
time.delay(2000)
    



































































































































