import random
import time

#créer un personnage
panier = Actor('panier', midtop=(400, 500))
pomme = Actor('pomme01', midbottom=(400, 0))

#Constantes
WIDTH = 800
HEIGHT = 600
APPLE_SPEED = 4
BASKET_SPEED = 6
VERT_FLUO = 66, 245, 69

#Variables
score = 0
nombre_vies = 3
game_over = False
# highscore = storage.setdefault("highscore", 0)

#on dessine le fond et les acteurs
def draw():
    screen.clear()
    #screen.fill((137, 216, 245))
    screen.blit('verger',(0,0))
    pomme.draw()
    panier.draw()
    screen.draw.text("Score " + str(score), (30, 550), color=(VERT_FLUO), fontname="arcadeclassic", fontsize=48)
    screen.draw.text("Vies " + str(nombre_vies), (600, 550), color=(VERT_FLUO), fontname="arcadeclassic", fontsize=48)
    if game_over:
        screen.draw.text("GAME OVER", (220, 200), color=(VERT_FLUO), fontname="arcadeclassic", fontsize=72)
        screen.draw.text("Appuyer sur Espace pour recommencer", (100, 300), color=(VERT_FLUO), fontname="arcadeclassic", fontsize=32)

# on déplace le personnage
def update():
    global wait_timer
    global game_over
    global score
    global nombre_vies

    if game_over:
        if keyboard.space:
            game_over = False
            score = 0
            nombre_vies = 3
        else:
            return
    else:
        deplacerPanier()
        deplacerPomme()

#déplacement panier
def deplacerPanier():
    if keyboard.left:
        panier.x -= BASKET_SPEED
    elif keyboard.right:
        panier.x += BASKET_SPEED
    if panier.right > WIDTH:
        panier.right = WIDTH
    if panier.left < 0:
        panier.left = 0

#déplacement de la pomme
def deplacerPomme():
    global score
    global nombre_vies
    global game_over
    pomme.bottom += APPLE_SPEED
    if pomme.bottom > HEIGHT:
        sounds.impact_sol.play()
        mettrePommeEnPositionDepart()
        nombre_vies -= 1
        print("Raté! Il te reste = " + str(nombre_vies) + " vies")
        if nombre_vies <= 0:
            game_over = True
    if pomme.colliderect(panier):
        sounds.impact_panier.play()
        mettrePommeEnPositionDepart()
        score += 1
        print("Tu m'as eu! Nouveau Score = " + str(score))

def mettrePommeEnPositionDepart():
    pomme.bottom = 0
    pomme.left = random.randint(0, WIDTH)