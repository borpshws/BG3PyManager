import webview
import webview.menu as wm

def change_active_window_content():
    active = webview.active_window()
    if active:
        active.load_html('<h1>You changed this window!</h1>')
    
def click_me():
    active = webview.active_window()
    if active:
        active.load_html('<h1>You clicked me!</h1>')

def do_nothing():
    pass

def open_file_dialog():
    active = webview.active_window()
    active.create_file_dialog(webview.SAVE_DIALOG, directory='/', save_filename='test.file')

def make_sticky():
    active = webview.active_window()
    if active:
        if active.on_top is False:
            active.on_top = True
        else:
            active.on_top = False

if __name__ == '__main__':
    window_1 = webview.create_window(
        'Application Menu Example', 'https://pywebview.flowrl.com/hello'
    )
    window_2 = webview.create_window(
        'Another Window', html = '<h1>Another window to test application menu</h1>'
    )

    menu_items = [
        wm.Menu(
            'Test Menu',
            [
                wm.MenuAction('Change Active Window Content', change_active_window_content),
                wm.MenuSeparator(),
                wm.Menu(
                    'Random',
                    [
                        wm.MenuAction('Click Me', click_me),
                        wm.MenuAction('File Dialog', open_file_dialog),
                    ],
                ),
            ],
        ),
        wm.Menu('Nothing Here', [wm.MenuAction('This will do nothing', do_nothing)]),
    ]


    webview.start(menu=menu_items)