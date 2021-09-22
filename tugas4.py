import pygame, sys
from pygame import rect
from pygame.locals import *
import time


#mendefinisikan lebar dan panjang layar
#memberikan judul pada output
WIDTH, HEIGHT = 600, 600
pygame.display.set_caption('Smooth Movement')

pygame.init()#menginisialisasi semua modul yang diperlukan untuk PyGame
win = pygame.display.set_mode((WIDTH, HEIGHT)) #memanggil nilai HEIGHT dan WIDTH
clock = pygame.time.Clock()#clock mengetahui waktu yang di perlukan untuk benda bergerak


#setwarna menggunakan RGBColors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (210, 43, 140, 1.0)
YELLOW = (255, 253, 0, 1.0)
GGRN = (25, 145, 112, 1.0)


#membuat sebuah objek 
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self): #mengupdate properti-properti pada object
        self.velX = 0 #memberikan arah gerak pada object yaitu secara horizontal, dimulai dari titik 0
        self.velY = 0 #memberikan arah gerak pada object yaitu secara vertical, dimulai dari titik 0
        if self.left_pressed and not self.right_pressed: #jika yang ditekan adalah tombol kiri dan bukan tombol kanan maka arah gerak menuju arah kiri (koordinat x negatif)
            if self.x >0: #memberikan batas agar objek tidak bergerak melewati batas display window (secara horizontal)
                self.velX = -self.speed
        if self.right_pressed and not self.left_pressed: #jika yang ditekan adalah tombol kanan dan bukan tombol kiri maka arah gerak menuju arah kanan (koordinat x positif)
            if self.x < 600 -32: #memberikan batas agar objek tidak bergerak melewati batas display window (secara horizontal)
                self.velX = self.speed
        if self.up_pressed and not self.down_pressed: #jika yang ditekan adalah tombol atas dan bukan tombol bawah maka arah gerak menuju arah atas (koordinat y positif)
            if self.y > 0: #memberikan batas agar objek tidak bergerak melewati batas display window (secara vertical)
                self.velY = -self.speed
        if self.down_pressed and not self.up_pressed: #jika yang ditekan adalah tombol bawah dan bukan tombol atas maka arah gerak menuju arah bawah (koordinat y negatif)
            if self.y < 600 - 32: #memberikan batas agar objek tidak bergerak melewati batas display window (secara vertical)
                self.velY = self.speed

        self.x += self.velX 
        self.y += self.velY 

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

#height dan width yaitu 600 dan 600 di bagi menjadi 2 
player = Player(WIDTH/2, HEIGHT/2)
#untuk merubah warna huruf
font_color = (255, 250, 250)
#membuat jenis font dan ukuran font
font_obj = pygame.font.Font("JasmineEstella.TTF", 25)
#menampilkan tulisan dilayar
text = "Intan Naumi"
#font akan muncul dan berubah warna menjadi PUTIH
img = font_obj.render(text, True, (WHITE))

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))


#untuk membuat keyboard down dan keybord up, keyboard left dan right
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
    


    
            if event.type == QUIT:
                    running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    img = font_obj.render(text, True, PINK)
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright
                    
    #menampilkan warna background
    win.fill((PINK))
    pygame.draw.rect(win, (WHITE), player)

    win.blit(img,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(win, PINK, cursor)
    pygame.display.update()

    player.update()
    #menampilkan hasil dari semuanya
    pygame.display.flip()

    clock.tick(120)
    pygame.display.update()
    
pygame.quit()
