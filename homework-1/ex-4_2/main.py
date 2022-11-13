import pygame as pg
import numpy as np


def create_grid(grid_size, rng):
    return rng.integers(0, 2, size=grid_size)


def are_configs_identical(config_1, config_2):
    return np.all(config_1 == config_2)


def shift_config(config, shift):
    h, w = config.shape
    new_config = np.zeros(config.shape)

    for y in range(h):
        for x in range(w):
            new_config[(y+shift[0])%h, (x+shift[1])%w] = config[y, x]
    
    return new_config


def find_config_shift(grid, config):
    h, w = grid.shape
    for y in range(h):
        for x in range(w):
            if y == 0 and x == 0:
                continue

            conf_shift = shift_config(y, x)
            # TODO: Fix logic



class Configs:
    block = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    beehive = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    loaf = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    boat = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    tub = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    blinker = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    toad = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    beacon = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    glider_1 = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
    ], dtype='uint8')    
    
    glider_2 = np.array([
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')

    glider_3 = np.array([
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ], dtype='uint8')    
    
    glider_4 = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ], dtype='uint8')


rng = np.random.default_rng()

screen = None
clock = None

display_size = 800, 800
framerate = 3

background_color = '#ffffff'
cell_color = '#346BA6'
active_cell_color = '#D55454'

key_config_map = {
    pg.K_1: Configs.block,
    pg.K_2: Configs.beehive,
    pg.K_3: Configs.loaf,
    pg.K_4: Configs.boat,
    pg.K_5: Configs.tub,
    pg.K_a: Configs.blinker,
    pg.K_s: Configs.toad,
    pg.K_d: Configs.beacon,
    pg.K_z: Configs.glider_1,
    pg.K_x: Configs.glider_2,
    pg.K_c: Configs.glider_3,
    pg.K_v: Configs.glider_4,
}

n_generations = 20

initial_grid = None

if initial_grid is None:
    grid_size = 10, 10
    grid = create_grid(grid_size, rng)
else:
    grid_size = initial_grid.shape
    grid = initial_grid

print(grid_size)

grid_margin = 40, 40


n_nbs_to_live = (
    {3}, {2, 3}
)

is_frozen = False
is_periodic_boundary = True


def main():
    global grid
    global initial_grid
    global grid_size
    global clock
    global screen
    global is_frozen
    global is_periodic_boundary

    pg.init()
    screen = pg.display.set_mode(display_size)
    clock = pg.time.Clock()
    screen.fill('#ffffff')
    screen.blit(pg.font.SysFont(None, 24).render(
        'Press space to start', True, cell_color), grid_margin)

    i_gen = 0
    reset = False
    while True:
        if reset:
            i_gen = 0
            reset = False

        render_sim(grid, grid_size, screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)

            elif event.type == pg.KEYUP:
                match event.key:
                    case pg.K_SPACE:
                        is_frozen = not is_frozen

                    case pg.K_p:
                        is_periodic_boundary = not is_periodic_boundary

                    case pg.K_r:
                        if initial_grid is not None:
                            grid = initial_grid
                        else:
                            grid = create_grid(grid_size, rng)

                        reset = True

                    case pg.K_0:
                        grid_size = 10, 10
                        initial_grid = None
                        grid = create_grid(grid_size, rng)
                        reset = True

                    case pg.K_ESCAPE:
                        exit(0)

                    case _:
                        if event.key in key_config_map:
                            grid = initial_grid = key_config_map[event.key]
                            grid_size = initial_grid.shape
                            reset = True

        if not is_frozen and not reset and i_gen < n_generations:
            grid = update_grid(grid, grid_size, is_periodic_boundary)
            i_gen += 1

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


def update_grid(grid, grid_size, is_periodic_boundary):
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


def render_sim(grid: np.ndarray, grid_size, screen: pg.Surface):
    screen.fill(background_color)
    cell_size = min(
        int((display_size[0] - 2*grid_margin[0])/grid_size[0]),
        int((display_size[1] - 2*grid_margin[1])/grid_size[1])
    )

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
