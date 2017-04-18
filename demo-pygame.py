# Stephanie K. Ananth (sananth)

import pygame


class Struct(object): pass


data = Struct()


def init(data):
    data.message = 'Hello World! :: Sortify :: Analyize. Vizualize. Organize.'
    data.font = pygame.font.Font(None, 30)


def drawMessage(data, screen):
    text = data.font.render(data.message, True, (0, 0, 0))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2,
                       screen.get_height() // 2 - text.get_height() // 2))


def redrawAll(data, screen):
    drawMessage(data, screen)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 300))

init(data)

while True:
    time = clock.tick(50)  # waits for the next frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
    screen.fill((255, 255, 255))
    redrawAll(data, screen)
    pygame.display.flip()

pygame.quit()
print('Bye!')
