from tile import *


class UI(PygameWindow):
    def __init__(self, width, height, shortcut_list=None):
        super(UI, self).__init__(0, 0, width, height)
        self.shortcut_list = shortcut_list
        self.current_selected_tile = None
        self.tile_list = None
        self.active = False
        if shortcut_list:
            self.build_tiles_from_list(self.shortcut_list)

    def build_tiles_from_list(self, lst: list[Shortcut]):
        row_width = SCREEN_WIDTH // TILE_SIZE
        self.tile_list = []
        for i in range(len(lst)):
            self.tile_list.append(
                Tile(left=(i % row_width) * TILE_SIZE, top=i // row_width * TILE_SIZE, width=TILE_SIZE,
                     height=TILE_SIZE,
                     shortcut=lst[i]))
        return self.tile_list

    def get_tile_number(self) -> Tile | None:
        for tile in self.tile_list:
            if tile.collidepoint(win32api.GetCursorPos()):
                return tile

    def display_all_tiles(self):
        for tile in self.tile_list:
            tile.display(self.surface)
        pygame.display.flip()

    def actualize_display(self):
        self.show_topmost()
        self.active = True
        new_tile_on = self.get_tile_number()
        if new_tile_on != self.current_selected_tile:
            if self.current_selected_tile:
                self.current_selected_tile.display(self.surface)
            self.current_selected_tile = new_tile_on
            if new_tile_on:
                self.current_selected_tile.display(self.surface, True)
            pygame.display.flip()

    def get_shortcut(self) -> Shortcut | None:
        if self.active:
            self.active = False
            if self.current_selected_tile:
                return self.current_selected_tile.shortcut

