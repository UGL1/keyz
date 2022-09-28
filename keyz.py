from ui import *
import km

overlay = UI(shortcut_list)
overlay.start()
overlay.make_non_clickable()
overlay.set_colorkey_black()
overlay.set_opacity(192)
overlay.show_topmost()
overlay.display_all_tiles()

while not km.is_pressed(STOP_PROGRAM_KEY):
    km.sleep(0.01)
    overlay.process_events()
    if km.is_pressed(SELECT_KEY):
        overlay.actualize_display()
    else:
        code = overlay.get_shortcut()
        overlay.hide()
        if code:
            code.trigger()

overlay.stop()
