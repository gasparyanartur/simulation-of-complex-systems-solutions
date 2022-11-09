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

n_nbs_to_live = (
    {3}, {2, 3}
)

is_frozen = False
is_periodic_boundary = True


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
            grid = update_grid(grid, is_periodic_boundary)
            render_sim(grid, screen, clock)

        clock.tick(framerate)


def get_nb_range(value, min, max, is_periodic_boundary):
    if value == min:
        if is_periodic_boundary:
            return max, min, min+1
        else:
            return min, min+1
    elif value == max:
        if is_periodic_boundary:
            return max-1, max, min
        else:
            return max-1, max
    else:
        return value-1, value, value+1


def update_grid(grid, is_periodic_boundary):
    new_grid = np.zeros(shape=grid_size, dtype='uint8')
    w, h = grid_size
    for y in range(h):
        for x in range(w):
            xs = get_nb_range(x, 0, w-1, is_periodic_boundary)
            ys = get_nb_range(y, 0, h-1, is_periodic_boundary)
            nbgrid = np.ix_(ys, xs)

            value = grid[y, x]
            nbhood = grid[nbgrid]
            n_nbs = np.sum(nbhood) - value

            if n_nbs in n_nbs_to_live[value]:
                new_grid[y, x] = 1

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

    pg.display.update()



if __name__ == "__main__":
    main()
