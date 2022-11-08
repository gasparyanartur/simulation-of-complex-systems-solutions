import pygame as pg
import numpy as np


def create_grid(grid_size, rng):
    return rng.integers(0, 2, size=grid_size)


screen = None
clock = None

display_size = 800, 800
framerate = 30

background_color = '#ffffff'
cell_color = '#346BA6'
active_cell_color = '#D55454'

grid_size = 80, 80

rng = np.random.default_rng()
grid = create_grid(grid_size, rng)

grid_margin = 40, 40
cell_size = min(
    int((display_size[0] - 2*grid_margin[0])/grid_size[0]),
    int((display_size[1] - 2*grid_margin[1])/grid_size[1])
)

n_nbs_to_remain = (
    {3}, {2, 3}
)

is_frozen = False


def main():
    global grid
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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)

            elif event.type == pg.KEYUP:
                match event.key:
                    case pg.K_SPACE:
                        is_frozen = not is_frozen

                    case pg.K_r:
                        grid = create_grid(grid_size, rng)

                    case pg.K_ESCAPE:
                        exit(0)

        if not is_frozen:
            grid = update_grid(grid)
            render_sim(grid, screen, clock)

        pg.display.update()
        clock.tick(framerate)


def update_grid(grid):
    new_grid = np.zeros(shape=grid_size, dtype='uint8')
    w, h = grid_size
    for y in range(1, h-1):
        for x in range(1, w-1):
            value = grid[y, x]
            n_nbs = np.sum(grid[y-1:y+2, x-1:x+2]) - 1

            if n_nbs not in n_nbs_to_remain[value]:
                new_grid[y, x] = 1 - value


    # TODO - edges

    return new_grid


def render_sim(grid: np.ndarray, screen: pg.Surface, clock: pg.time.Clock):
    screen.fill(background_color)

    w, h = grid_size

    for y in range(h):
        for x in range(w):
            p_y = grid_margin[0] + y * cell_size
            p_x = grid_margin[1] + x * cell_size
            cell_value = grid[y, x]
            color = active_cell_color if cell_value else cell_color

            screen.fill(color=color, rect=pg.Rect(
                (p_x, p_y), (cell_size, cell_size)))


if __name__ == "__main__":
    main()
