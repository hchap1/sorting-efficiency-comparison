import pygame

pygame.init()
screen = pygame.display.set_mode((800,800), vsync=True)
w, h = screen.get_size()
font = pygame.font.Font("freesansbold.ttf", 25)
clock = pygame.time.Clock()

def graph(sets, max_n, max_time):
    running = True
    screen.fill((255,255,255))
    for algorithm in sets:
        px = 0
        py = 0
        for n, t in algorithm[2:]:
            rely = t / max_time
            relx = n / max_n
            pygame.draw.circle(screen, (255,0,0), (relx * w, h - rely * h), 5) 
            pygame.draw.line(screen, (255,0,0), (relx * w, h - rely * h), (px * w, h - py * h), 5)
            px = relx
            py = rely
        text = font.render(algorithm[0], False, (0, 0, 0))
        screen.blit(text, (px * w - 10 - text.get_width(), h - py * h + 10))
    pygame.display.update()
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
