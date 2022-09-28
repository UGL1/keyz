from constants import *

font_name = pygame.font.get_default_font()
tile_font = pygame.font.Font(font_name, TILE_FONT_SIZE)


class Tile(pygame.Rect):

    def __init__(self, left, top, width, height, shortcut: Shortcut):
        super(Tile, self).__init__(left, top, width, height)

        self.shortcut = shortcut

        self.bmp_off = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.bmp_off.fill(TILE_BG_OFF_COLOR)
        text_bmp = tile_font.render(shortcut.symbol, True, TILE_FG_OFF_COLOR, TILE_BG_OFF_COLOR)
        text_bmp_width, text_bmp_height = text_bmp.get_size()
        self.bmp_off.blit(text_bmp, ((TILE_SIZE - text_bmp_width) // 2, (TILE_SIZE - text_bmp_height) // 2))

        self.bmp_on = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.bmp_on.fill(TILE_BG_ON_COLOR)
        text_bmp = tile_font.render(shortcut.symbol, True, TILE_FG_ON_COLOR, TILE_BG_ON_COLOR)
        self.bmp_on.blit(text_bmp, ((TILE_SIZE - text_bmp_width) // 2, (TILE_SIZE - text_bmp_height) // 2))

    def display(self, surface, on=False):
        if isinstance(surface, PygameWindow):
            surface = surface.surface
        bmp = self.bmp_off if not on else self.bmp_on
        surface.blit(bmp, (self.left, self.top))



