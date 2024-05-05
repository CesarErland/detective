import pygame
import sys
import random

# Inicializar pygame
pygame.init()
font = pygame.font.Font(None, 36)

# Definir colores
BLANCO = (255, 255, 255)

# Obtener el tamaño de la pantalla
ANCHO = pygame.display.Info().current_w
ALTO = pygame.display.Info().current_h

# Configurar la pantalla en modo de pantalla completa
pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
pygame.display.set_caption("Detective")

# Cargar imágenes
fondo = pygame.image.load("detectiveportada.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))  # Redimensionar al tamaño de la pantalla
boton_jugar_img = pygame.image.load("detectivejugar.png")
boton_jugar_img = pygame.transform.scale(boton_jugar_img, (ANCHO // 10, ALTO // 10))  # Redimensionar
instrucciones = pygame.image.load("detectiveinstrucciones.png")
instrucciones = pygame.transform.scale(instrucciones, (ANCHO, ALTO))  # Redimensionar al tamaño de la pantalla
boton_continuar_img = pygame.image.load("detectivecontinuar.png")
boton_continuar_img = pygame.transform.scale(boton_continuar_img, (ANCHO // 10, ALTO // 10))  # Redimensionar
boton_salir_img = pygame.image.load("detectivesalir.png")
boton_salir_img = pygame.transform.scale(boton_salir_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
mapa_img = pygame.image.load("detective.png")
mapa_img = pygame.transform.scale(mapa_img, (ANCHO // 1.5, ALTO // 1.5))
fondo_juego = pygame.image.load("detectivefondo.png")
fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))  # Redimensionar al tamaño de la pantalla
boton_rnc_img = pygame.image.load("detectivereiniciar.png")
boton_rnc_img = pygame.transform.scale(boton_rnc_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_sheldon_img = pygame.image.load("sheldon.png")
boton_sheldon_img = pygame.transform.scale(boton_sheldon_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_patricio_img = pygame.image.load("patricio.png")
boton_patricio_img = pygame.transform.scale(boton_patricio_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_eduardo_img = pygame.image.load("eduardo.png")
boton_eduardo_img = pygame.transform.scale(boton_eduardo_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_eugenio_img = pygame.image.load("eugenio.png")
boton_eugenio_img = pygame.transform.scale(boton_eugenio_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_roberto_img = pygame.image.load("roberto.png")
boton_roberto_img = pygame.transform.scale(boton_roberto_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_dormitorio_img = pygame.image.load("dormitorio.png")
boton_dormitorio_img = pygame.transform.scale(boton_dormitorio_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_patio_img = pygame.image.load("patio.png")
boton_patio_img = pygame.transform.scale(boton_patio_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_baño_img = pygame.image.load("baño.png")
boton_baño_img = pygame.transform.scale(boton_baño_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_sala_img = pygame.image.load("sala.png")
boton_sala_img = pygame.transform.scale(boton_sala_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_cocina_img = pygame.image.load("cocina.png")
boton_cocina_img = pygame.transform.scale(boton_cocina_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_espatula_img = pygame.image.load("espatula.png")
boton_espatula_img = pygame.transform.scale(boton_espatula_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_tridente_img = pygame.image.load("tridente.png")
boton_tridente_img = pygame.transform.scale(boton_tridente_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_cuerda_img = pygame.image.load("cuerda.png")
boton_cuerda_img = pygame.transform.scale(boton_cuerda_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_pistola_img = pygame.image.load("pistola.png")
boton_pistola_img = pygame.transform.scale(boton_pistola_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_bate_img = pygame.image.load("bate.png")
boton_bate_img = pygame.transform.scale(boton_bate_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
boton_acusar_img = pygame.image.load("acusar.png")
boton_acusar_img = pygame.transform.scale(boton_acusar_img, (ANCHO // 12, ALTO // 12))  # Redimensionar

# Imagen para rellenar cuando se necesite cambiar el texto
prellenar_img = pygame.image.load("rellenar.png")
prellenar_img2 = pygame.transform.scale(prellenar_img, (ANCHO // 4.5  , ALTO // 30))  # Redimensionar
prellenar_img = pygame.transform.scale(prellenar_img, (ANCHO // 1.4, ALTO // 3.5))  # Redimensionar

# Definir la posición de los botones 
boton_jugar_rect = boton_jugar_img.get_rect()
boton_jugar_rect.center = (ANCHO // 2, ALTO // 1.2)
boton_continuar_rect = boton_continuar_img.get_rect()
boton_continuar_rect.center = (ANCHO // 2, ALTO // 1.2)
boton_salir_rect = boton_salir_img.get_rect()
boton_salir_rect.center = (ANCHO // 20, ALTO // 18)
boton_rnc_rect = boton_rnc_img.get_rect()
boton_rnc_rect.center = (ANCHO // 7.5, ALTO // 18)
boton_acusar_rect = boton_acusar_img.get_rect()
boton_acusar_rect.center = (ANCHO // 4.7, ALTO // 1.5)

boton_sheldon_rect = boton_sheldon_img.get_rect()
boton_sheldon_rect.center = (ANCHO // 11.5, ALTO // 5.3)
boton_patricio_rect = boton_patricio_img.get_rect()
boton_patricio_rect.center = (ANCHO // 11.5, ALTO // 3.9)
boton_eduardo_rect = boton_eduardo_img.get_rect()
boton_eduardo_rect.center = (ANCHO // 11.5, ALTO // 3.09)
boton_eugenio_rect = boton_eugenio_img.get_rect()
boton_eugenio_rect.center = (ANCHO // 11.5, ALTO // 2.555)
boton_roberto_rect = boton_roberto_img.get_rect()
boton_roberto_rect.center = (ANCHO // 11.5, ALTO // 2.181)

boton_dormitorio_rect = boton_dormitorio_img.get_rect()
boton_dormitorio_rect.center = (ANCHO // 11.5, ALTO // 1.76)
boton_patio_rect = boton_patio_img.get_rect()
boton_patio_rect.center = (ANCHO // 11.5, ALTO // 1.574)
boton_baño_rect = boton_baño_img.get_rect()
boton_baño_rect.center = (ANCHO // 11.5, ALTO // 1.422)
boton_sala_rect = boton_sala_img.get_rect()
boton_sala_rect.center = (ANCHO // 11.5, ALTO // 1.297)
boton_cocina_rect = boton_cocina_img.get_rect()
boton_cocina_rect.center = (ANCHO // 11.5, ALTO // 1.193)

boton_espatula_rect = boton_espatula_img.get_rect()
boton_espatula_rect.center = (ANCHO // 5.3, ALTO // 5.3)
boton_tridente_rect = boton_tridente_img.get_rect()
boton_tridente_rect.center = (ANCHO // 5.3, ALTO // 3.9)
boton_cuerda_rect = boton_cuerda_img.get_rect()
boton_cuerda_rect.center = (ANCHO // 5.3, ALTO // 3.09)
boton_pistola_rect = boton_pistola_img.get_rect()
boton_pistola_rect.center = (ANCHO // 5.3, ALTO // 2.555)
boton_bate_rect = boton_bate_img.get_rect()
boton_bate_rect.center = (ANCHO // 5.3, ALTO // 2.181)

# Opciones restantes
personajes_restantes = [0,1,2,3,4]
armas_restantes = [0,1,2,3,4]
lugares_restantes = [0,1,2,3,4]


personajes = ["Sheldon", "Patricio", "Eduardo", "Eugenio", "Roberto"]
lugares = ["dormitorio","patio","baño","sala","cocina"]
armas = ["espátula","tridente","cuerda","pistola","bate"]

#propiedades = shel, pat, edu, eug, rob
#propiedades = persona, lugar, arma
asesino = 0
propiedades = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
asesinato = [6,6,6]
culpable = [2,2,2,2,2]
acusacion = [6,6,6]

# Etapa
etapa = 0

# Función para asignar armas y lugares
def propied():
    for x in range(5):
        pers = random.choice(personajes_restantes)
        luga = random.choice(lugares_restantes)
        arma = random.choice(armas_restantes)
        propiedades[x][0] = pers
        propiedades[x][1] = luga
        propiedades[x][2] = arma
        personajes_restantes.remove(pers)
        lugares_restantes.remove(luga)
        armas_restantes.remove(arma)

# Función para matar a alguien
def matar():
    muerto = random.choice(personajes_restantes)
    personajes_restantes.remove(muerto)
    asesino = random.choice(personajes_restantes)
    culpable[0]=0
    culpable[1]=0
    culpable[2]=0
    culpable[3]=0
    culpable[4]=0
    culpable[asesino]=1
    for x in range(5):
        if propiedades[x][0] == muerto:
            asesinato[0] = propiedades[x][0]
            asesinato[1] = propiedades[x][1]
            asesinato[2] = propiedades[x][2]
        

# Función para dibujar la pantalla
def dibujar_pantalla():
    pantalla.fill(BLANCO)
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(boton_jugar_img, boton_jugar_rect)
    pygame.display.update()
    i = 1
    while i == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se ha hecho clic en el botón "Jugar"
                if boton_jugar_rect.collidepoint(event.pos):
                    i = 0

# Función para dibujar las instrucciones
def dibujar_instrucciones():
    pantalla.fill(BLANCO)
    pantalla.blit(instrucciones, (0, 0))
    pantalla.blit(boton_continuar_img, boton_continuar_rect)
    pygame.display.update()
    i = 1
    while i == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se ha hecho clic en el botón "Continuar"
                if boton_continuar_rect.collidepoint(event.pos):
                    i = 0

# Función para mostrar la pantalla de juego con una pregunta aleatoria
def mostrar_pantalla_juego():
    preguntas_restantes = 5
    i = 1
    etapa = 0
    while i == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Verificar si se ha hecho clic en el botón "Salir"
                if boton_salir_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

                # Verificar si se ha hecho clic en el botón "Reiniciar"
                elif boton_rnc_rect.collidepoint(event.pos):
                    for x in range(1,6):
                        if preguntas_restantes < 4:
                            preguntas_restantes + 1
                    personajes_restantes.clear()
                    personajes_restantes.append(0)
                    personajes_restantes.append(1)
                    personajes_restantes.append(2)
                    personajes_restantes.append(3)
                    personajes_restantes.append(4)
                    armas_restantes.clear()
                    armas_restantes.append(0)
                    armas_restantes.append(1)
                    armas_restantes.append(2)
                    armas_restantes.append(3)
                    armas_restantes.append(4)
                    lugares_restantes.clear()
                    lugares_restantes.append(0)
                    lugares_restantes.append(1)
                    lugares_restantes.append(2)
                    lugares_restantes.append(3)
                    lugares_restantes.append(4)
                    i = 0
                    etapa = 0

                # Verificar si se ha hecho clic en el botón "Sheldon"
                elif boton_sheldon_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pygame.display.update()
                    if asesinato[0] == 0:
                        prueba = 1
                    else:
                        if preguntas_restantes >=1:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if culpable[0] == 0:
                                    if propiedades[x][0] == 0:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textos = "Observas a " + str(personajes[propiedades[x][0]])+" tranquilo en la habitacion "+ str(lugares[propiedades[x][1]]+" jugando con su "+str(armas[propiedades[x][2]]))+"."
                                        texto = font.render(textos, True, (0,0,0))
                                        pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                                elif culpable[0] == 1:
                                    if propiedades[x][0] == 0:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textosheldonin = "Observas a " + str(personajes[propiedades[x][0]])+" nervioso en la habitacion "+ str(lugares[propiedades[x][1]]+" empuñando su "+str(armas[propiedades[x][2]]))+"."
                                        textosheld = font.render(textosheldonin, True, (0,0,0))
                                        pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                        else:
                            if etapa < 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 10:
                                if etapa <= 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("Ya has culpado a " + str(personajes[acusacion[0]])+".", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                                if etapa > 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("El juego ha terminado", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                            if etapa == 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                acusacion[0] = 0
                                teext = font.render("Has culpado a " + str(personajes[acusacion[0]])+", ¿En que habitación afirmas que mató?", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                                etapa = 20

                                
                # Verificar si se ha hecho clic en el botón "Patricio"
                elif boton_patricio_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pygame.display.update()
                    if asesinato[0] == 1:
                        prueba = 1
                    else:
                        if preguntas_restantes >=1:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if culpable[1] == 0:
                                    if propiedades[x][0] == 1:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textos = "Observas a " + str(personajes[propiedades[x][0]])+" tranquilo en la habitacion "+ str(lugares[propiedades[x][1]]+" jugando con su "+str(armas[propiedades[x][2]]))+"."
                                        texto = font.render(textos, True, (0,0,0))
                                        pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                                elif culpable[1] == 1:
                                    if propiedades[x][0] == 1:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textosheldonin = "Observas a " + str(personajes[propiedades[x][0]])+" nervioso en la habitacion "+ str(lugares[propiedades[x][1]]+" empuñando su "+str(armas[propiedades[x][2]]))+"."
                                        textosheld = font.render(textosheldonin, True, (0,0,0))
                                        pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                        else:
                            if etapa < 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 10:
                                if etapa <= 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("Ya has culpado a " + str(personajes[acusacion[0]])+".", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                                if etapa > 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("El juego ha terminado", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                            if etapa == 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                acusacion[0] = 1
                                teext = font.render("Has culpado a " + str(personajes[acusacion[0]])+", ¿En que habitación afirmas que mató?", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                                etapa = 20
                            

                # Verificar si se ha hecho clic en el botón "Eduardo"
                elif boton_eduardo_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pygame.display.update()
                    if asesinato[0] == 2:
                        prueba = 1
                    else:
                        if preguntas_restantes >=1:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if culpable[2] == 0:
                                    if propiedades[x][0] == 2:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textos = "Observas a " + str(personajes[propiedades[x][0]])+" tranquilo en la habitacion "+ str(lugares[propiedades[x][1]]+" jugando con su "+str(armas[propiedades[x][2]]))+"."
                                        texto = font.render(textos, True, (0,0,0))
                                        pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                                elif culpable[2] == 1:
                                    if propiedades[x][0] == 2:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textosheldonin = "Observas a " + str(personajes[propiedades[x][0]])+" nervioso en la habitacion "+ str(lugares[propiedades[x][1]]+" empuñando su "+str(armas[propiedades[x][2]]))+"."
                                        textosheld = font.render(textosheldonin, True, (0,0,0))
                                        pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                        else:
                            if etapa < 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 10:
                                if etapa <= 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("Ya has culpado a " + str(personajes[acusacion[0]])+".", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                                if etapa > 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("El juego ha terminado", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                            if etapa == 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                acusacion[0] = 2
                                teext = font.render("Has culpado a " + str(personajes[acusacion[0]])+", ¿En que habitación afirmas que mató?", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                                etapa = 20
                            

                # Verificar si se ha hecho clic en el botón "Eugenio"
                elif boton_eugenio_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pygame.display.update()
                    if asesinato[0] == 3:
                        prueba = 1
                    else:
                        if preguntas_restantes >=1:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if culpable[3] == 0:
                                    if propiedades[x][0] == 3:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textos = "Observas a " + str(personajes[propiedades[x][0]])+" tranquilo en la habitacion "+ str(lugares[propiedades[x][1]]+" jugando con su "+str(armas[propiedades[x][2]]))+"."
                                        texto = font.render(textos, True, (0,0,0))
                                        pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                                elif culpable[3] == 1:
                                    if propiedades[x][0] == 3:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textosheldonin = "Observas a " + str(personajes[propiedades[x][0]])+" nervioso en la habitacion "+ str(lugares[propiedades[x][1]]+" empuñando su "+str(armas[propiedades[x][2]]))+"."
                                        textosheld = font.render(textosheldonin, True, (0,0,0))
                                        pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                        else:
                            if etapa < 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 10:
                                if etapa <= 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("Ya has culpado a " + str(personajes[acusacion[0]])+".", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                                if etapa > 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("El juego ha terminado", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                            if etapa == 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                acusacion[0] = 3
                                teext = font.render("Has culpado a " + str(personajes[acusacion[0]])+", ¿En que habitación afirmas que mató?", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                                etapa = 20
                            

                # Verificar si se ha hecho clic en el botón "Roberto"
                elif boton_roberto_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pygame.display.update()
                    if asesinato[0] == 4:
                        prueba = 1
                    else:
                        if preguntas_restantes >=1:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if culpable[4] == 0:
                                    if propiedades[x][0] == 4:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textos = "Observas a " + str(personajes[propiedades[x][0]])+" tranquilo en la habitacion "+ str(lugares[propiedades[x][1]]+" jugando con su "+str(armas[propiedades[x][2]]))+"."
                                        texto = font.render(textos, True, (0,0,0))
                                        pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                                elif culpable[4] == 1:
                                    if propiedades[x][0] == 4:
                                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                        textosheldonin = "Observas a " + str(personajes[propiedades[x][0]])+" nervioso en la habitacion "+ str(lugares[propiedades[x][1]]+" empuñando su "+str(armas[propiedades[x][2]]))+"."
                                        textosheld = font.render(textosheldonin, True, (0,0,0))
                                        pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                        pygame.display.update()
                        else:
                            if etapa < 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 10:
                                if etapa <= 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("Ya has culpado a " + str(personajes[acusacion[0]])+".", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                                if etapa > 30:
                                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                    preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                    pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                    teext = font.render("El juego ha terminado", True, (0,0,0))
                                    pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                    pygame.display.update()
                            if etapa == 10:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                acusacion[0] = 4
                                teext = font.render("Has culpado a " + str(personajes[acusacion[0]])+", ¿En que habitación afirmas que mató?", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                                etapa = 20
                            

                # Verificar si se ha hecho clic en el botón "Dormitorio"
                elif boton_dormitorio_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[1] == 0:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = str(personajes[asesinato[0]])+" está en el suelo de la habitación " + str(lugares[asesinato[1]])+", sin vida. Se observa el arma "+str(armas[asesinato[2]])+" cerca de él."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][1] == 0:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" tranquilo, jugando con su "+str(armas[propiedades[x][2]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" nervioso, empuñando su "+str(armas[propiedades[x][2]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 20:
                            if etapa == 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya has afirmado que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+".", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("El juego ha terminado", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                        if etapa == 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[1] = 0
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" ¿Qué arma piensas que usó?", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                            etapa = 30
                        
                    
                # Verificar si se ha hecho clic en el botón "Patio"
                elif boton_patio_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[1] == 1:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = str(personajes[asesinato[0]])+" está en el suelo de la habitación " + str(lugares[asesinato[1]])+", sin vida. Se observa el arma "+str(armas[asesinato[2]])+" cerca de él."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][1] == 1:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" tranquilo, jugando con su "+str(armas[propiedades[x][2]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" nervioso, empuñando su "+str(armas[propiedades[x][2]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 20:
                            if etapa == 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya has afirmado que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+".", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("El juego ha terminado", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                        if etapa == 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[1] = 1
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" ¿Qué arma piensas que usó?", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                            etapa = 30
                                            
                    
                # Verificar si se ha hecho clic en el botón "Baño"
                elif boton_baño_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[1] == 2:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = str(personajes[asesinato[0]])+" está en el suelo de la habitación " + str(lugares[asesinato[1]])+", sin vida. Se observa el arma "+str(armas[asesinato[2]])+" cerca de él."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][1] == 2:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" tranquilo, jugando con su "+str(armas[propiedades[x][2]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" nervioso, empuñando su "+str(armas[propiedades[x][2]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 20:
                            if etapa == 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya has afirmado que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+".", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("El juego ha terminado", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                        if etapa == 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[1] = 2
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" ¿Qué arma piensas que usó?", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                            etapa = 30

                    
                # Verificar si se ha hecho clic en el botón "Sala"
                elif boton_sala_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[1] == 3:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = str(personajes[asesinato[0]])+" está en el suelo de la habitación " + str(lugares[asesinato[1]])+", sin vida. Se observa el arma "+str(armas[asesinato[2]])+" cerca de él."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][1] == 3:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" tranquilo, jugando con su "+str(armas[propiedades[x][2]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" nervioso, empuñando su "+str(armas[propiedades[x][2]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 20:
                            if etapa == 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya has afirmado que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+".", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("El juego ha terminado", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                        if etapa == 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[1] = 3
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" ¿Qué arma piensas que usó?", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                            etapa = 30

                    
                # Verificar si se ha hecho clic en el botón "Cocina"
                elif boton_cocina_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[1] == 4:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = str(personajes[asesinato[0]])+" está en el suelo de la habitación " + str(lugares[asesinato[1]])+", sin vida. Se observa el arma "+str(armas[asesinato[2]])+" cerca de él."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][1] == 4:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" tranquilo, jugando con su "+str(armas[propiedades[x][2]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Revisas la habitación " + str(lugares[propiedades[x][1]])+", ves a " + str(personajes[propiedades[x][0]])+" nervioso, jugando con su "+str(armas[propiedades[x][2]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 20:
                            if etapa == 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("Ya has afirmado que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+".", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                            if etapa > 30:
                                pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                                preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                                pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                                pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                teext = font.render("El juego ha terminado", True, (0,0,0))
                                pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                                pygame.display.update()
                        if etapa == 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[1] = 4
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" ¿Qué arma piensas que usó?", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                            etapa = 30
                    

                # Verificar si se ha hecho clic en el botón "Espatula"
                elif boton_espatula_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[2] == 0:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = "Buscas el arma " + str(armas[asesinato[2]])+", la encuentras cerca de " + str(personajes[asesinato[0]])+", que yace muerto en la habitación " + str(lugares[asesinato[1]]) + "."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][2] == 0:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que juega en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que se acurruca en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("El juego ha terminado", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa == 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[2] = 0
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" utilizando el arma " + str(armas[acusacion[2]]), True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            errores = 0
                            if culpable[acusacion[0]] == 1:
                                prueba = 1
                            else:
                                errores = errores + 1
                            if asesinato[1] == acusacion[1]:
                                prueba = 1
                            else:
                                errores = errores +1
                            if asesinato[2] == acusacion[2]:
                                prueba = 1
                            else:
                                errores = errores +1
                                
                            if errores == 0:
                                ttcxt = font.render("Felicitaciones, has dado en el clavo. ¡Eres un gran detective!", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 1:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elemento, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 2:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elementos, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 3:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar todos los elementos, lo siento, has fallado horriblemente.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            pygame.display.update()
                            etapa = 40
                            
                # Verificar si se ha hecho clic en el botón "Tridente"
                elif boton_tridente_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[2] == 1:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = "Buscas el arma " + str(armas[asesinato[2]])+", la encuentras cerca de " + str(personajes[asesinato[0]])+", que yace muerto en la habitación " + str(lugares[asesinato[1]]) + "."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][2] == 1:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que juega en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que se acurruca en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("El juego ha terminado", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa == 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[2] = 1
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" utilizando el arma " + str(armas[acusacion[2]]), True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            errores = 0
                            if culpable[acusacion[0]] == 1:
                                prueba = 1
                            else:
                                errores = errores + 1
                            if asesinato[1] == acusacion[1]:
                                prueba = 1
                            else:
                                errores = errores +1
                            if asesinato[2] == acusacion[2]:
                                prueba = 1
                            else:
                                errores = errores +1
                                
                            if errores == 0:
                                ttcxt = font.render("Felicitaciones, has dado en el clavo. ¡Eres un gran detective!", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 1:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elemento, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 2:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elementos, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 3:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar todos los elementos, lo siento, has fallado horriblemente.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            pygame.display.update()
                            etapa = 40

                    
                # Verificar si se ha hecho clic en el botón "Cuerda"
                elif boton_cuerda_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[2] == 2:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = "Buscas el arma " + str(armas[asesinato[2]])+", la encuentras cerca de " + str(personajes[asesinato[0]])+", que yace muerto en la habitación " + str(lugares[asesinato[1]]) + "."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][2] == 2:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que juega en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que se acurruca en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("El juego ha terminado", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa == 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[2] = 2
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" utilizando el arma " + str(armas[acusacion[2]]), True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            errores = 0
                            if culpable[acusacion[0]] == 1:
                                prueba = 1
                            else:
                                errores = errores + 1
                            if asesinato[1] == acusacion[1]:
                                prueba = 1
                            else:
                                errores = errores +1
                            if asesinato[2] == acusacion[2]:
                                prueba = 1
                            else:
                                errores = errores +1
                                
                            if errores == 0:
                                ttcxt = font.render("Felicitaciones, has dado en el clavo. ¡Eres un gran detective!", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 1:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elemento, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 2:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elementos, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 3:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar todos los elementos, lo siento, has fallado horriblemente.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            pygame.display.update()
                            etapa = 40

                    
                # Verificar si se ha hecho clic en el botón "Pistola"
                elif boton_pistola_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[2] == 3:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = "Buscas el arma " + str(armas[asesinato[2]])+", la encuentras cerca de " + str(personajes[asesinato[0]])+", que yace muerto en la habitación " + str(lugares[asesinato[1]]) + "."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][2] == 3:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que juega en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que se acurruca en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("El juego ha terminado", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa == 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[2] = 3
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" utilizando el arma " + str(armas[acusacion[2]]), True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            errores = 0
                            if culpable[acusacion[0]] == 1:
                                prueba = 1
                            else:
                                errores = errores + 1
                            if asesinato[1] == acusacion[1]:
                                prueba = 1
                            else:
                                errores = errores +1
                            if asesinato[2] == acusacion[2]:
                                prueba = 1
                            else:
                                errores = errores +1
                                
                            if errores == 0:
                                ttcxt = font.render("Felicitaciones, has dado en el clavo. ¡Eres un gran detective!", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 1:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elemento, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 2:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elementos, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 3:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar todos los elementos, lo siento, has fallado horriblemente.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            pygame.display.update()
                            etapa = 40

                    
                # Verificar si se ha hecho clic en el botón "Bate"
                elif boton_bate_rect.collidepoint(event.pos):
                    pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                    pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                    pygame.display.update()
                    if preguntas_restantes >= 1:
                        if asesinato[2] == 4:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            textos = "Buscas el arma " + str(armas[asesinato[2]])+", la encuentras cerca de " + str(personajes[asesinato[0]])+", que yace muerto en la habitación " + str(lugares[asesinato[1]]) + "."
                            texto = font.render(textos, True, (0,0,0))
                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                            pygame.display.update()
                        else:
                            preguntas_restantes = preguntas_restantes - 1
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            for x in range(5):
                                if propiedades[x][2] == 4:
                                    if culpable[propiedades[x][0]] == 0:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textos = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que juega en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            texto = font.render(textos, True, (0,0,0))
                                            pantalla.blit(texto, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                                    elif culpable[propiedades[x][0]] == 1:
                                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                                            textosheldonin = "Buscas el arma "+str(armas[propiedades[x][2]])+", la encuentras en manos de "+str(personajes[propiedades[x][0]])+", que se acurruca en la habitación " + str(lugares[propiedades[x][1]])+"."
                                            textosheld = font.render(textosheldonin, True, (0,0,0))
                                            pantalla.blit(textosheld, (ANCHO // 3, ALTO // 10))
                                            pygame.display.update()
                    else:
                        if etapa < 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Ya no quedan pistas restantes.", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa > 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("El juego ha terminado", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa == 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            acusacion[2] = 4
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" utilizando el arma " + str(armas[acusacion[2]]), True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            errores = 0
                            if culpable[acusacion[0]] == 1:
                                prueba = 1
                            else:
                                errores = errores + 1
                            if asesinato[1] == acusacion[1]:
                                prueba = 1
                            else:
                                errores = errores +1
                            if asesinato[2] == acusacion[2]:
                                prueba = 1
                            else:
                                errores = errores +1
                                
                            if errores == 0:
                                ttcxt = font.render("Felicitaciones, has dado en el clavo. ¡Eres un gran detective!", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 1:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elemento, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 2:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar "+str(errores)+" elementos, lo siento, has fallado.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            if errores == 3:
                                ttcxt = font.render("Lamentablemente has fallado en averiguar todos los elementos, lo siento, has fallado horriblemente.", True, (0,0,0))
                                pantalla.blit(ttcxt, (ANCHO // 3, ALTO // 8.5))    
                            pygame.display.update()
                            etapa = 40

                
                # Verificar si se ha hecho clic en el botón "Acusar"
                elif boton_acusar_rect.collidepoint(event.pos):
                    if(preguntas_restantes == 0):
                        if etapa > 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("El juego ha terminado", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa == 30:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Afirmas que " + str(personajes[acusacion[0]])+" mató en la habitación " + str(lugares[acusacion[1]])+" ¿Qué arma piensas que usó?", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa == 20:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            teext = font.render("Has culpado a " + str(personajes[acusacion[0]])+", ¿En que habitación afirmas que mató?", True, (0,0,0))
                            pantalla.blit(teext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                        if etapa == 0:
                            pantalla.blit(prellenar_img2, (ANCHO // 17, ALTO // 11))  # Borrar el texto
                            preg_res = font.render("Pistas restantes: " + str(preguntas_restantes)+".", True, (0,0,0))
                            pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
                            pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                            ttext = font.render("¿A quien quieres culpar?", True, (0,0,0))
                            pantalla.blit(ttext, (ANCHO // 3, ALTO // 10))    
                            pygame.display.update()
                            etapa = 10
                    else:
                        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
                        ttext = font.render("Aun te quedan pistas disponibles. ¡Ùsalas todas!", True, (0,0,0))
                        pantalla.blit(ttext, (ANCHO // 3, ALTO // 10))    
                        pygame.display.update()
                        pygame.display.update()
# Iniciar el juego
if __name__ == "__main__":
    dibujar_pantalla()
    dibujar_instrucciones()
    j = 1
    while j == 1:
        propiedades = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        asesinato = [6,6,6]
        culpable = [2,2,2,2,2]
        acusacion = [6,6,6]
        propied()
        personajes_restantes = [0,1,2,3,4]
        armas_restantes = [0,1,2,3,4]
        lugares_restantes = [0,1,2,3,4]
        etapa = 0
        matar()
        
        # Texto introduccion
        pantalla.blit(fondo_juego, (0, 0))
        for x in range (5):
            
            if x == asesinato[0]:
                introduccion = font.render("Han matado a " + personajes[x], True, (0,0,0))
            else:
                pruebaaaa = 1
        pantalla.blit(introduccion, (ANCHO // 1.8, ALTO // 23))
        preg_res = font.render("Pistas restantes: " + str(5), True, (0,0,0))
        pantalla.blit(preg_res, (ANCHO // 16, ALTO // 10))
        pantalla.blit(mapa_img, (ANCHO // 3.5, ALTO // 3))
        pantalla.blit(boton_salir_img, boton_salir_rect)
        pantalla.blit(boton_rnc_img, boton_rnc_rect)
        pantalla.blit(boton_acusar_img, boton_acusar_rect)
        if 0 in personajes_restantes:
            pantalla.blit(boton_sheldon_img, boton_sheldon_rect)
        if 1 in personajes_restantes:
            pantalla.blit(boton_patricio_img, boton_patricio_rect)
        if 2 in personajes_restantes:
            pantalla.blit(boton_eduardo_img, boton_eduardo_rect)
        if 3 in personajes_restantes:
            pantalla.blit(boton_eugenio_img, boton_eugenio_rect)
        if 4 in personajes_restantes:
            pantalla.blit(boton_roberto_img, boton_roberto_rect)
        pantalla.blit(boton_dormitorio_img, boton_dormitorio_rect)
        pantalla.blit(boton_patio_img, boton_patio_rect)
        pantalla.blit(boton_baño_img, boton_baño_rect)
        pantalla.blit(boton_sala_img, boton_sala_rect)
        pantalla.blit(boton_cocina_img, boton_cocina_rect)
        pantalla.blit(boton_espatula_img, boton_espatula_rect)
        pantalla.blit(boton_tridente_img, boton_tridente_rect)
        pantalla.blit(boton_cuerda_img, boton_cuerda_rect)
        pantalla.blit(boton_pistola_img, boton_pistola_rect)
        pantalla.blit(boton_bate_img, boton_bate_rect)
        pers = font.render("Personajes:", True, (0,0,0))
        pantalla.blit(pers, (ANCHO // 20, ALTO // 8))
        luga = font.render("Lugares:", True, (0,0,0))
        pantalla.blit(luga, (ANCHO // 16.5, ALTO // 2))
        arma = font.render("Armas:", True, (0,0,0))
        pantalla.blit(arma, (ANCHO //6, ALTO // 8))
        pantalla.blit(prellenar_img, (ANCHO // 3.24, ALTO // 15))  # Borrar el texto
        pygame.display.update()
        mostrar_pantalla_juego()
        