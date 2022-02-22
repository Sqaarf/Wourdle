import pygame

pygame.init()


class GameUi:
    def __init__(self):
        self.win = pygame.display.set_mode((800, 650))
        pygame.display.set_caption('Wourdle')

        self.fps = 30
        self.run = True

        self.cases = []

        # print(self.cases)

        i = 0
        for y in range(20, 550, 160):
            self.cases.append([])
            for x in range(20, 800, 160):
                self.cases[i].append(pygame.Rect(x, y, 120, 120))
            i += 1

    def commands(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.run = False

    def render(self):
        for case in self.cases:
            for rect in case:
                pygame.draw.rect(self.win, (255, 255, 255), rect)

    def gameloop(self):
        while self.run:
            pygame.time.Clock().tick(self.fps)
            self.commands()
            self.render()
            pygame.display.update()


pygame.quit()