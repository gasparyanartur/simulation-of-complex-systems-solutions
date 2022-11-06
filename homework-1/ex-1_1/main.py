import pygame as pg
import numpy as np


def decode_rule(rule_number: int) -> dict[tuple[int, int, int], int]:
    binary_numbers = [
        (1, 1, 1), (1, 1, 0), (1, 0, 1), (1, 0, 0),
        (0, 1, 1), (0, 1, 0), (0, 0, 1), (0, 0, 0)
    ]

    rule = dict()
    num = rule_number
    for i in range(8):
        num, rem = divmod(num, 2)
        rule[binary_numbers[-i-1]] = rem

    return rule


def create_grid(n_cells, n_generations, rng):
    parent_generation = rng.integers(0, 2, size=(n_cells,))
    grid = np.zeros(shape=(n_generations, n_cells), dtype='uint8')
    grid[0, :] = parent_generation 

    return grid


screen = None
clock = None

display_size = 800, 800
framerate = 30

background_color = '#ffffff'
cell_color = '#346BA6'
active_cell_color = '#D55454'

n_cells = 80
n_generations = 80

rng = np.random.default_rng()
grid = create_grid(n_cells, n_generations, rng)

grid_margin = 40, 40
cell_size = min(
    int((display_size[0] - 2*grid_margin[0])/n_generations),
    int((display_size[1] - 2*grid_margin[1])/n_cells)
)
print(cell_size)

rule_number = 184
rules = decode_rule(rule_number)

is_frozen = False

down_keys = set()


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
                        grid = create_grid(n_cells, n_generations, rng)

                    case pg.K_ESCAPE:
                        exit(0)

        if not is_frozen:
            grid = update_grid(grid, rules, rng)
            render_sim(grid, screen, clock)

        pg.display.update()
        clock.tick(framerate)


def update_grid(grid, rules, rng):
    grid = np.roll(grid, 1, 0)
    for i in range(1, n_cells-1):
        pattern = grid[1, i-1:i+2]
        grid[0, i] = rules[tuple(pattern)]

    left_pattern = np.zeros(shape=(3,))
    left_pattern[0] = rng.integers(0, 2, size=(1,))
    left_pattern[1:] = grid[1, :2]

    right_pattern = np.zeros(shape=(3,))
    left_pattern[-1] = rng.integers(0, 2, size=(1,))
    right_pattern[:2] = grid[1, -2:]

    grid[0, 0] = rules[tuple(left_pattern)]
    grid[0, -1] = rules[tuple(right_pattern)]

    return grid


def render_sim(grid: np.ndarray, screen: pg.Surface, clock: pg.time.Clock):
    screen.fill(background_color)
    for gen in range(n_generations):
        for i_cell in range(n_cells):
            y = grid_margin[0] + gen * cell_size
            x = grid_margin[1] + i_cell * cell_size
            cell_value = grid[gen, i_cell]
            color = active_cell_color if cell_value else cell_color

            screen.fill(color=color, rect=pg.Rect(
                (x, y), (cell_size, cell_size)))


if __name__ == "__main__":
    main()
