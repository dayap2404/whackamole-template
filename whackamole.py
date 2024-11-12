import pygame
import random

# new comment after token initializaton
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        x, y = 0, 0  # top left, starting mole pos

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


                if event.type == pygame.MOUSEBUTTONDOWN:
                    a, b = event.pos
                    row = a // 32
                    col = b // 32

                    # if they clicked correctly
                    if (x//32,y//32) == (row, col):
                        # put new mole in random place
                        x = random.randrange(0,19) * 32
                        y = random.randrange(0,15) * 32

            # reset the grid and screen
            screen.fill("light green")
            # this is to create the grid

            # draw horizontal lines
            for i in range(1, 16):
                pygame.draw.line(
                    screen,  # where are drawing the lines
                    (0, 0, 0),  # what color
                    (0, i * 32),  # whats the starting point
                    (640, i * 32)
                )

            # DRAW VERTICAL LINE
            for i in range(1, 20):  # same thing
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (i * 32, 0),
                    (i * 32, 512)
                )
            # draw the mole at new position
            screen.blit(mole_image, (x,y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
