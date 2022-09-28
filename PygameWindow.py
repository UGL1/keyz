import km as kmhook
from timer import *
from Window import Window
import pygame
import win32api


class PygameWindow(Window):
    """
    class handling a pygame window
    """

    def __init__(self, left, top, width, height):

        # Win32 Stuff --------------------------------------------------------------------------------------------------

        super().__init__(left, top, width, height)

        # pygame stuff -------------------------------------------------------------------------------------------------

        self.surface = None
        self.frame_duration = 1000 / 60
        self.next_frame_timer = Timer(self.frame_duration)

        # Move stuff ---------------------------------------------------------------------------------------------------

        self.is_being_moved = False
        self.drag_and_drop_elsewhere = False
        self.move_key = "mouse_left"
        self.grab_x = 0
        self.grab_y = 0

    def set_frame_rate(self, frame_rate: int) -> None:
        self.frame_duration = 1000 / (frame_rate or 60)
        # self.next_frame_timer = Timer(self.frame_duration)

        self.next_frame_timer = Timer(self.frame_duration)

    def get_frame_rate(self) -> int:
        return int(round(1000 / self.frame_duration))

    def set_move_key(self, key: str) -> None:
        self.move_key = key

    def get_move_key(self) -> str:
        return self.move_key

    def start(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        self.hwnd = pygame.display.get_wm_info()['window']
        self.next_frame_timer.start()
        self.show_not_topmost()

    def next_frame(self) -> bool:
        has_expired, delay = self.next_frame_timer.has_expired(delay=True)
        if has_expired:
            self.next_frame_timer.start(self.frame_duration - delay)
            return True
        return False

    def process_events(self) -> None:
        pygame.event.pump()

    def process_move(self) -> None:
        drag = kmhook.is_pressed(self.move_key)

        if not self.is_being_moved and drag and not self.drag_and_drop_elsewhere:
            x, y = win32api.GetCursorPos()
            if self.left <= x < self.left + self.width and self.top <= y < self.top + self.height:
                self.grab_x = self.left - x
                self.grab_y = self.top - y
                self.is_being_moved = True
            else:
                self.drag_and_drop_elsewhere = True

        elif self.is_being_moved and drag:
            x, y = win32api.GetCursorPos()
            self.left = x + self.grab_x
            self.top = y + self.grab_y
            self.show_topmost()
        elif self.is_being_moved and not drag:
            self.is_being_moved = False
            self.show_not_topmost()

        elif not drag:
            self.drag_and_drop_elsewhere = False

    @staticmethod
    def stop() -> None:
        pygame.quit()
