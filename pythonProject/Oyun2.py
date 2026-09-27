# ==============================================================================
# SPACE SHOOTER ARCADE GAME ENGINE - PYGAME IMPLEMENTATION
# ==============================================================================
# Author      : Muhammed Emin Korkunç (Student ID: 2021221054)
# Institution : Fatih Sultan Mehmet Vakıf Üniversitesi - Bilgisayar Mühendisliği
# GitHub      : https://github.com/muhammedkorkunc
# LinkedIn    : https://www.linkedin.com/in/muhammed-emin-korkun%C3%A7-100ba2215
# Email       : muhammedemin.korkunc@gmail.com
# License     : Proprietary - All Rights Reserved (c) 2026
# ==============================================================================
# NOTICE: Unauthorized copying, decompilation, redistribution or exploitation
# of this game source code, logic, or assets is strictly prohibited.
# ==============================================================================

__author_signature__ = "AUTH:MUHAMMED_EMIN_KORKUNC_2021221054_VERIFIED"

import pygame
import random

# Pygame Hazırlık
pygame.init()

# Pencere
GENISLIK, YUKSEKLIK = 1000, 650
pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))

# FPS
FPS = 60
saat = pygame.time.Clock()


# Sınıflarım
class Oyun():
    def __init__(self, oyuncu, uzayli_grup, oyuncu_mermi_grup, uzayli_mermi_grup):
        #Oyun değişkenleri
        self.bolum_no=2
        self.puan=0

        #Nesneler
        self.oyuncu=oyuncu
        self.uzayli_grup = uzayli_grup
        self.uzayli_mermi_grup = uzayli_mermi_grup
        self.oyuncu_mermi_grup = oyuncu_mermi_grup


        #Arka plan
        self.arka_plan1 = pygame.image.load("arka_plan1.png")
        self.arka_plan2 = pygame.image.load("arka_plan2.jpg")
        self.arka_plan3 = pygame.image.load("arka_plan3.png")
        self.tebrikler = pygame.image.load("tebrikler.png")

        #Şarkı ve Ses Efekti
        self.uzayli_vurus = pygame.mixer.Sound("uzayli_vurus.wav")
        self.oyuncu_vurus = pygame.mixer.Sound("oyuncu_vurus.wav")
        pygame.mixer.music.load("arka_plan_sarki.wav")
        pygame.mixer.music.play(-1)

        #Font
        self.oyun_font= pygame.font.Font("oyun_font.ttf",64)

    def update(self):
        self.uzayli_konum_degistirme()
        self.temas()
        self.tamamlandi()

    def cizdir(self):
        puan_yazi=self.oyun_font.render("Skor:"+str(self.puan),True,(255,0,255),(0,0,0))
        puan_yazi_konum = puan_yazi.get_rect()
        puan_yazi_konum.topleft=(10,10)

        bolum_no_yazi = self.oyun_font.render("Bölüm:"+str(self.bolum_no),True,(255,0,255),(0,0,0))
        bolum_no_yazi_konum = bolum_no_yazi.get_rect()
        bolum_no_yazi_konum.topleft = (GENISLIK-250,10)

        if self.bolum_no==1:
            pencere.blit(self.arka_plan1,(0,0))
        elif self.bolum_no ==2:
            pencere.blit(self.arka_plan2, (0, 0))
        elif self.bolum_no ==3:
            pencere.blit(self.arka_plan3,(0,0))
        elif self.bolum_no ==4:
            self.bitir()

        pencere.blit(puan_yazi, puan_yazi_konum)
        pencere.blit(bolum_no_yazi, bolum_no_yazi_konum)

    def uzayli_konum_degistirme(self):
        hareket,carpisma=False,False
        for uzayli in self.uzayli_grup.sprites():
            if uzayli.rect.left<=0 or uzayli.rect.right>=GENISLIK:
                hareket=True
        if hareket==True:
            for uzayli in self.uzayli_grup.sprites():
                uzayli.rect.y+=10*self.bolum_no
                uzayli.yon*=-1
                if uzayli.rect.bottom>=YUKSEKLIK-70:
                    carpisma=True

        if carpisma==True:
            self.oyuncu.can-=1
            self.oyun_durumu()

    def temas(self):
        if pygame.sprite.groupcollide(self.oyuncu_mermi_grup, self.uzayli_grup,True,True):
            self.oyuncu_vurus.play()
            self.puan+=100*self.bolum_no

        if pygame.sprite.spritecollide(self.oyuncu, self.uzayli_mermi_grup,True):
            self.uzayli_vurus.play()
            self.oyuncu.can-=1
            self.oyun_durumu()


    def bitir(self):
        bittimi=True
        pencere.blit(self.tebrikler,(0,0))
        pygame.display.update()
        while bittimi:
            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.KEYDOWN:
                    if etkinlik.key==pygame.K_RETURN:
                        self.oyun_reset()
                        bittimi=False

    def bolum(self):
        for i in range(6):
            for j in range(4):
                uzayli = Uzayli(64+i*64,100+j*64,self.bolum_no,self.uzayli_mermi_grup)
                self.uzayli_grup.add(uzayli)
    def oyun_durumu(self):
        self.uzayli_mermi_grup.empty()
        self.oyuncu_mermi_grup.empty()
        self.oyuncu.reset()
        for uzayli in self.uzayli_grup.sprites():
            uzayli.reset()

        if self.oyuncu.can==0:
            self.oyun_reset()
        else:
            self.durdur()

    def tamamlandi(self):
        if not self.uzayli_grup:
            self.bolum_no+=1
            self.bolum()

    def durdur(self):
        durdumu = True
        global durum
        yazi1 = self.oyun_font.render("Uzaylılar yüzünden " + str(self.oyuncu.can) + "canınız kaldı", True, (0, 110, 0),
                                      (255, 0, 0))
        yazi1_konum = yazi1.get_rect()
        yazi1_konum.topleft = (100, 150)

        yazi2 = self.oyun_font.render("Devam etmek için 'ENTER' tuşuna basınız", True, (0, 110, 0), (255, 0, 0))
        yazi2_konum = yazi2.get_rect()
        yazi2_konum.topleft = (100, 250)

        pencere.blit(yazi1, yazi1_konum)
        pencere.blit(yazi2, yazi2_konum)
        pygame.display.update()
        while durdumu:
            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.KEYDOWN:
                    if etkinlik.key == pygame.K_RETURN:
                        durdumu = False

                if etkinlik.type == pygame.QUIT:
                    durdumu = False
                    durum = False


    def oyun_reset(self):
        #Oyun değişkenleri
        self.bolum_no=1
        self.puan =0
        self.oyuncu.can=5
        #Grupları temizle
        self.uzayli_grup.empty()
        self.uzayli_mermi_grup.empty()
        self.oyuncu_mermi_grup.empty()
        self.bolum()

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self, oyuncu_mermi_grup):
        super().__init__()
        self.image = pygame.image.load("uzay_gemi.png")
        self.rect = self.image.get_rect()
        self.oyuncu_mermi_grup = oyuncu_mermi_grup
        self.rect.centerx = GENISLIK // 2
        self.rect.top = YUKSEKLIK - 70

        # Oyuncu Değişkenleri
        self.hiz = 10
        self.can = 5
        # Mermi Ses Efekti
        self.mermi_sesi = pygame.mixer.Sound("oyuncu_mermi.wav")

    def update(self):
        tus = pygame.key.get_pressed()
        if tus[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= self.hiz
        if tus[pygame.K_RIGHT] and self.rect.right <= GENISLIK:
            self.rect.x += self.hiz

    def ates(self):
        if len(self.oyuncu_mermi_grup) < 8:
            self.mermi_sesi.play()
            oyuncuMermi(self.rect.centerx, self.rect.top, self.oyuncu_mermi_grup)

    def reset(self):
        self.rect.centerx = GENISLIK // 2


class Uzayli(pygame.sprite.Sprite):  # çoklu uzaylıları vurma ve vurulma ve kordinata göre hareket etmek için spritedan kalıtım aldık
    def __init__(self, x, y, hiz, mermi_grup):
        super().__init__()
        self.image = pygame.image.load("uzayli.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # uzaylı özel değişkenleri
        self.basx = x
        self.basy = y
        self.yon = 1
        self.hiz = hiz
        self.mermi_grup = mermi_grup
        self.uzayli_mermi_sesi = pygame.mixer.Sound("uzayli_mermi.wav")

    def update(self):
        self.rect.x += self.yon*self.hiz
        if (random.randint(0, 100) > 99) and (len(self.mermi_grup) < 3):
            self.uzayli_mermi_sesi.play()
            self.ates()

    def ates(self):
        uzayliMermi(self.rect.centerx, self.rect.bottom, self.mermi_grup)

    def reset(self):
        self.rect.topleft = (self.basx, self.basy)
        self.yon = 1


class oyuncuMermi(pygame.sprite.Sprite):
    def __init__(self, x, y, oyuncu_mermi_grup):
        super().__init__()
        self.image = pygame.image.load("oyuncu_mermi.png")
        self.rect = self.image.get_rect()  # konum üzerinden işlem yapmak için gerekli
        self.rect.centerx = x
        self.rect.centery = y
        # Mermi Değişkeni
        self.hiz = 10
        oyuncu_mermi_grup.add(self)

    def update(self):
        self.rect.y -= self.hiz
        if self.rect.bottom < 0:
            self.kill()  # Grup işlemleri gerçekleştirdikten sonra grubumuzu temizlemek için kill fonk kullanıyoruz. Burda tane mermi sıktıktan sonra grubu temizliyor ve yeniden ateş etmemizi sağlıyor


class uzayliMermi(pygame.sprite.Sprite):
    def __init__(self,x,y,mermi_grup):
        super().__init__()
        self.image = pygame.image.load("uzayli_mermi.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        mermi_grup.add(self)
        self.hiz=10
    def update(self):
        self.rect.y+=self.hiz
        if self.rect.top>YUKSEKLIK:
            self.kill()


# Mermi Grubu
oyuncu_mermi = pygame.sprite.Group()
uzayli_mermi = pygame.sprite.Group()

# Oyuncu Tanımlama
oyuncu_grup = pygame.sprite.Group()
oyuncu = Oyuncu(oyuncu_mermi)
oyuncu_grup.add(oyuncu)

# Uzaylı Grup
uzayli_grup = pygame.sprite.Group()



#Oyun Sınıfı
oyun=Oyun(oyuncu, uzayli_grup, oyuncu_mermi, uzayli_mermi)
oyun.bolum()
# Oyun Döngüsü
durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False
        if etkinlik.type == pygame.KEYDOWN:
            if etkinlik.key == pygame.K_SPACE:
                oyuncu.ates()

    oyun.update()
    oyun.cizdir()

    oyuncu_grup.update()
    oyuncu_grup.draw(pencere)

    oyuncu_mermi.update()
    oyuncu_mermi.draw(pencere)

    uzayli_grup.update()
    uzayli_grup.draw(pencere)

    uzayli_mermi.update()
    uzayli_mermi.draw(pencere)

    # Pencere güncelleme ve FPS tanımlaması
    pygame.display.update()
    saat.tick(FPS)
pygame.quit()
