import win32api
from PygameWindow import *
from shortcut import *

pygame.init()

# Lengthes and dimensions

SCREEN_WIDTH, SCREEN_HEIGHT = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

TILE_SIZE = 128  #
Y_PADDING = TILE_SIZE // 10
TILE_FONT_SIZE = TILE_SIZE - 2 * Y_PADDING

# Colors

TILE_BG_ON_COLOR = pygame.Color(0, 255, 0)
TILE_BG_OFF_COLOR = pygame.Color(0, 0, 0)

TILE_FG_ON_COLOR = pygame.Color(0, 0, 0)
TILE_FG_OFF_COLOR = pygame.Color(0, 255, 0)

# Keys

STOP_PROGRAM_KEY = "pause"

SELECT_KEY = "lalt"
