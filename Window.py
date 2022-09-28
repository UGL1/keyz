import win32con, win32gui


class Window:
    """
    Basic class to handle Win32 windows
    """
    TOPMOST = 0
    NOT_TOPMOST = 1
    HIDDEN = 2

    def __init__(self, left: int, top: int, width: int, height: int):
        """
        DataClass to store Win32 info
        :param left: int
        :param top: int
        :param width: int
        :param height: int
        """
        # - WIN32 STUFF ------------------------------------------------------------------------------------------------
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.hwnd = 0
        self.opacity = 255
        self.clickable = True
        self.black_is_transparent = False
        self.z_position = Window.TOPMOST

    def make_non_clickable(self) -> None:
        """
        Sets the window to click through
        """
        self.clickable = False
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE,
                               win32con.WS_EX_LAYERED |
                               win32con.WS_EX_TRANSPARENT)

    def make_clickable(self) -> None:
        """
        Sets the window to be clickable
        """
        self.clickable = True
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, win32con.WS_EX_LAYERED)

    def show_topmost(self) -> None:
        """
        Place the window topmost in z-order
        """
        if self.z_position != Window.TOPMOST:
            self.z_position = Window.TOPMOST
            win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST,
                                  self.left, self.top, 0, 0,
                                  win32con.SWP_NOSIZE |
                                  win32con.SWP_SHOWWINDOW |
                                  win32con.SWP_NOACTIVATE)

    def show_not_topmost(self) -> None:
        """
        Window will be hidden by other active windows
        """
        self.z_position = Window.NOT_TOPMOST
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_NOTOPMOST,
                              self.left, self.top, 0, 0,
                              win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)

    def hide(self) -> None:
        """
        Hides window
        """
        if self.z_position != Window.HIDDEN:
            self.z_position = Window.HIDDEN
            win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST,
                                  0, 0, 0, 0,
                                  win32con.SWP_NOSIZE |
                                  win32con.SWP_NOMOVE |
                                  win32con.SWP_HIDEWINDOW |
                                  win32con.SWP_NOACTIVATE)

    def is_hidden(self) -> bool:
        return self.z_position == Window.HIDDEN

    def set_opacity(self, opacity: int = 255) -> None:
        """
        Sets window opacity
        """
        self.opacity = opacity
        win32gui.SetLayeredWindowAttributes(self.hwnd, 0, opacity,
                                            win32con.LWA_ALPHA | (win32con.LWA_COLORKEY * self.black_is_transparent))

    def set_colorkey_black(self) -> None:
        """
        Sets black as a transparent color key.
        """
        clickable = False
        if self.clickable:
            clickable = True
            self.make_non_clickable()
        self.black_is_transparent = True
        win32gui.SetLayeredWindowAttributes(self.hwnd, 0, self.opacity, win32con.LWA_ALPHA | win32con.LWA_COLORKEY)
        if clickable:
            self.make_clickable()
