import pygame, colorsys

pygame.init()
screen = pygame.display.set_mode((800,800), vsync=True)
w, h = screen.get_size()
font_size = 20
font = pygame.font.Font("freesansbold.ttf", font_size)
clock = pygame.time.Clock()

def generate_unique_colors(n):
    colors = []
    for i in range(n):
        hue = i / n
        lightness = 0.5
        saturation = 0.8
        rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
        rgb = tuple(int(x * 255) for x in rgb)
        colors.append(rgb)
    return colors

n = 5
unique_colors = generate_unique_colors(n)
print(unique_colors)

def graph(sets, max_n, max_time):
    running = True
    screen.fill((255,255,255))
    colors = generate_unique_colors(len(sets))
    for idx, algorithm in enumerate(sets):
        px = 0
        py = 0
        for n, t in algorithm[2:]:
            rely = t / max_time
            relx = n / max_n
            pygame.draw.circle(screen, colors[idx], (relx * w, h - rely * h), 5) 
            pygame.draw.line(screen, colors[idx], (relx * w, h - rely * h), (px * w, h - py * h), 5)
            px = relx
            py = rely
        text = font.render(algorithm[0], False, colors[idx])
        screen.blit(text, (10, idx * font_size * 1.1 + 10))
    pygame.display.update()
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
