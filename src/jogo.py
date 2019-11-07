# -*- coding: utf-8 -*-

# Programa: Arrombado - O jogo de tomar cagada da pomba!
# Autor   : Rahul Martim Juliato (rahul.juliato@gmail.com)
# Data    : 20.03.2018


import pygame
import random

pygame.init()


################################################################## Tela
tela_largura=800
tela_altura=600
tela=pygame.display.set_mode((tela_largura,tela_altura), flags=0, depth=0, display=0)
pygame.display.set_caption("Arrombado!")


################################################################# Cores
preto=(0,0,0)
branco=(255,255,255)
vermelho=(255,0,0)

################################################################# Clock
clock=pygame.time.Clock()


##################################################### Variáveis globais
global bateu
global saidojogo
global x
global y
global deltax
global velocidade
global pausa

textogrande=pygame.font.SysFont(None,115)
textomedio=pygame.font.SysFont(None, 40)
textopequeno=pygame.font.SysFont(None,16)

############################################################### Sprites
arrombado_pic=pygame.image.load('arrombado.png')
arrombado_lar=80
deltax=0
velocidade=0
    
def arrombado(x,y):
    tela.blit(arrombado_pic, (x,y))


merda_pic=pygame.image.load('merda.png')
merda_lar=80
merda_alt=80

def merda(merdax, merday):
    tela.blit(merda_pic, (merdax,merday))


zoeiro_pic=pygame.image.load('zoeiro.png')
def zoeiro(x,y):
    tela.blit(zoeiro_pic,(x,y))

pomba_pic=pygame.image.load('pomba.png')
def pomba(x,y):
    tela.blit(pomba_pic,(x,y))

bonde_pic=pygame.image.load('bonde.png')
def bonde(x,y):
    tela.blit(bonde_pic,(x,y))
bonde_lar=579
bonde_alt=326


################################################### Funções Utilitárias

def textoobj(texto, font,cor=preto):
    textsuperf=font.render(texto, True, cor)
    return textsuperf, textsuperf.get_rect()


def mensagem(texto,tamanho=False,posx=False,posy=False,coloracao=preto,tempo=2):

    if coloracao:
        cor=coloracao
    
    tamanho_selecionado=textogrande

    if tamanho==1: tamanho_selecionado=textogrande
    if tamanho==2: tamanho_selecionado=textomedio
    if tamanho==3: tamanho_selecionado=textopequeno
        
    textosuperf,textoretan=textoobj(texto, tamanho_selecionado,cor)
    textoretan.center=((tela_largura/2),(tela_altura/2))
    
    if posx or posy:
        textoretan.center=((posx,posy))

    tela.blit(textosuperf,textoretan)

    pygame.time.delay(tempo*1000)


def tomou():
    mensagem('SE FODEU!')

    tela.fill(preto)
    bonde(tela_largura/2-bonde_lar/2,tela_altura/2-bonde_alt/2)

    pygame.display.update()
    
    pygame.time.wait(4*1000)
    loop_principal()


def pontuacao(cont):
    font=pygame.font.SysFont(None,25)
    text=font.render("Pontos: "+str(cont), True, preto)
    tela.blit(text,(1,0))

    text=font.render("(P)ausa - (S)ai - (A)juda", True, preto)
    tela.blit(text,(590,0))


def pausado():
    mensagem("Pausado!", tempo=0)

    pausa=True
    while pausa:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_p:
                    pausa=False
                
        pygame.display.update()
        clock.tick(15)


def ajuda():
    yinicial=200
    xinicial=tela_largura/2
    distancia=20

    tela.fill(branco)
    mensagem("Precisa de ajuda com essa merda?",tamanho=3, posx=xinicial,posy=yinicial, tempo=0)
    mensagem("Vá se foder, aprende jogando!",tamanho=3, posx=xinicial,posy=yinicial+distancia, tempo=0)
    mensagem("Tá vai... usa as setas para esquerda e direita!", tamanho=3, posx=xinicial, posy=yinicial+2*distancia, tempo=0)
    mensagem("Rahul Martim Juliato (rahul.juliato@gmail.com)", tamanho=3, posx=xinicial, posy=yinicial+8*distancia, tempo=0)
    mensagem("Versão: 0.1", tamanho=3, posx=xinicial, posy=yinicial+9*distancia, tempo=0)
    mensagem("Licença: GPL2", tamanho=3, posx=xinicial, posy=yinicial+10*distancia, tempo=3)
    pygame.display.update()
    
############################################################ Introdução
def intro():
    pombax=50
    pombay=50
    pombavelo=20



    tela.fill(preto)
    mensagem('Em um mundo cheio de vacilos...',2, coloracao=branco)
    tela.fill(preto)
    mensagem('O herói voador...',2, coloracao=branco)
    tela.fill(preto)
    mensagem('Fará sua justiça...',2, coloracao=branco)    
    
    tela.fill(branco)        
    pomba(50,50)
    mensagem('...não vai dar pipoca?...',2,450,230)
    zoeiro(580,400)
    mensagem('...HueHueHueHue...',2,490,360)
    tela.fill(branco)
    pomba(50,50)
    mensagem('ARROMBADO!',2,450,230)
    tela.fill(branco)
    pomba(pombax,pombay)
    mensagem('...pru pru pru pru...', 2, 450, 230)

    for i in range(pombax, pombax+200):
        pombax=pombax+1
        pombay=pombay-2
        pomba(pombax,pombay)
        pygame.display.update()

    
    
####################################################### Loop principal
def loop_principal():

    bateu=False
    saidojogo=False
    deltax=0

    arrombadovel=10
    
    x=int(tela_largura*0.45)
    y=int(tela_altura*0.8)

    merdaxini=random.randrange(0,tela_largura)
    merdayini=-600
    merdav=7
    desviado=0
    primero=True

    while not saidojogo:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_LEFT:
                    deltax=-arrombadovel
                if evento.key==pygame.K_RIGHT:
                    deltax=arrombadovel
                if evento.key==pygame.K_p:
                    pausado()
                if evento.key==pygame.K_s:
                    pygame.quit()
                    quit()
                if evento.key==pygame.K_a:
                    ajuda()
                
            if evento.type==pygame.KEYUP:
                if evento.key==pygame.K_LEFT or evento.key==pygame.K_RIGHT:
                    deltax=0

        x+=deltax
        tela.fill(branco)

        merda(merdaxini, merdayini)
        merdayini+=merdav
        
        arrombado(x,y)

        if primero:
            mensagem("Socorroooo!!!",2)
            primero=False
            
        pontuacao(desviado)
        
        pygame.display.update()
        
        # caso encoste no canto da tela
        if x > tela_largura - arrombado_lar or x < 0:
            tomou()

        # inteligência de pontuação
        if merdayini > tela_altura:
            merdayini=0-merda_alt
            merdaxini=random.randrange(0,tela_largura)
            desviado+=1
            merdav+=1
            
        # caso colida na merda
        if y < merdayini+merda_alt:
            print("passou por y")
            desviado+=1

            if x > merdaxini and x < merdaxini + merda_lar or x + arrombado_lar > merdaxini and x + arrombado_lar < merdaxini + merda_lar:
                print('passou por x')
                tomou()
            
            
        # caso o início de y esteja acima da tela
        if merdayini > tela_altura:
            merdayini=0-merda_lar
            merdaxini=random.randrange(0,tela_largura)
            

        clock.tick(60)


################################################# Processamento Inicial



intro()
loop_principal()
pygame.quit()
quit()
