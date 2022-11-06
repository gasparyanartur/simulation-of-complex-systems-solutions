import pygame as pg


display_size = 480, 480
framerate = 10


def main():
    pg.init()
    screen = pg.display.set_mode(display_size)
    clock = pg.time.Clock()
    screen.fill('#ffffff')

    while True:
        keys = pg.key.get_pressed()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)

        pg.display.update()
        clock.tick(framerate)


if __name__ == "__main__":
    main()