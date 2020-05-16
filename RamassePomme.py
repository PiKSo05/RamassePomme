import random

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
nb_vies = 3

#on dessine le fond et les acteurs
def draw():
    screen.clear()
    #screen.fill((137, 216, 245))
    screen.blit('verger',(0,0))
    pomme.draw()
    panier.draw()
    screen.draw.text("Score " + str(score), (30, 550), color=(VERT_FLUO), fontname="arcadeclassic", fontsize=48)
    screen.draw.text("Vie " + str(nb_vies), (650, 550), color=(VERT_FLUO), fontname="arcadeclassic", fontsize=48)

# on déplace le personnage
def update():
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
    global nb_vies
    pomme.bottom += APPLE_SPEED
    if pomme.bottom > HEIGHT:
        sounds.impact_sol.play()
        mettrePommeEnPositionDepart()
        nb_vies -= 1
        print("Rate! Il te reste " + str(nb_vies) + " vies!")
    if pomme.colliderect(panier):
        sounds.impact_panier.play()
        mettrePommeEnPositionDepart()
        score += 1
        print("Tu m'as eu! Nouveau Score = " + str(score))

def mettrePommeEnPositionDepart():
    pomme.bottom = 0
    pomme.left = random.randint(0, WIDTH)