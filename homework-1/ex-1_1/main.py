import pygame as pg
import numpy as np

screen = None
clock = None

display_size = 480, 480
framerate = 10

background_color = '#ffffff'
cell_color = '#000000'

n_cells = 20
n_generations = 20

rng = np.random.default_rng(69420)
parent_generation = rng.integers(0, 2, size=(n_cells,))
grid = np.zeros(shape=(n_generations, n_cells))
is_frozen = True

grid_margin = 40, 40
cell_size = (
    int((display_size[0] - 2*grid_margin[0])/n_generations),
    int((display_size[1] - 2*grid_margin[1])/n_cells)
)
cell_border = 2, 2
cell_inner_size = (
    cell_size[0] - 2*cell_border[0],
    cell_size[1] - 2*cell_border[1]
)


def main():
    global clock
    global screen
    global is_frozen

    pg.init()
    screen = pg.display.set_mode(display_size)
    clock = pg.time.Clock()
    screen.fill('#ffffff')
    screen.blit(pg.font.SysFont(None, 24).render(
        'Press space to start', True, cell_color), grid_margin)

    while True:
        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            is_frozen = False

        if keys[pg.K_ESCAPE]:
            exit(0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)

        if not is_frozen:
            update_sim()

        pg.display.update()
        clock.tick(framerate)


def update_sim():
    global screen
    global clock

    surf: pg.Surface = screen
    clk: pg.time.Clock = clock

    surf.fill(background_color)
    for gen in range(n_generations):
        for i_cell in range(n_cells):
            cell = grid[gen, i_cell]
            y = grid_margin[0] + gen * cell_size[0]
            x = grid_margin[1] + i_cell * cell_size[1]
            surf.fill(color=cell_color, rect=pg.Rect((x, y), cell_size))
            surf.fill(color=background_color, rect=pg.Rect(
                (x+cell_border[1], y+cell_border[0]), cell_inner_size))


if __name__ == "__main__":
    main()
