from tkinter import *

# Den GUI initialisieren
root = Tk()

windowWidth = 700
windowHeight = 500

windowWidthSplit = windowWidth / 2
windowHeightSplit = windowHeight / 2

WINDOW_BACKGROUND_COLOR = "#10286e"
BUTTON_BACKGROUND_COLOR = "#2f7375"

CurrentState = StringVar()
currentState = Label(root)

def normalState():
    CurrentState.set("Kamerstand: Normal")

def glitchState():
    CurrentState.set("Kamerastand: Glitch")

def pixelatedState():
    CurrentState.set("Kamerastand: Pixeliert")

def assign_widgets(obj):
    CurrentState.set("Kamerastand: Normal")

    currentState = Label(obj, textvariable=CurrentState, background=WINDOW_BACKGROUND_COLOR)
    currentState.place(x=(windowWidthSplit - 70), y=0)

    btn_normalState = Button(obj, text="Normale Kamera", background=BUTTON_BACKGROUND_COLOR, command=normalState)
    btn_normalState.place(x=0, y=50)

    btn_glitchState = Button(obj, text="Glich-Kamera", background=BUTTON_BACKGROUND_COLOR, command=glitchState)
    btn_glitchState.place(x=137, y=50)

    btn_pixelState = Button(obj, text="Pixeliert", background=BUTTON_BACKGROUND_COLOR, command=pixelatedState)
    btn_pixelState.place(x=255, y=50)

def create_window(title, favicon, window_geometry):
    root.title(title)
    root.configure(background=WINDOW_BACKGROUND_COLOR)
    root.geometry(window_geometry)

    faviconImg = PhotoImage(file=favicon)
    root.iconphoto(False, faviconImg)

    assign_widgets(root)

    root.mainloop()

# Window-Größe: (Horizontale Größe x Vertikale Größe)
create_window("Camera Call Chaos", "favicon.png", (str(windowWidth) + "x" + str(windowHeight)))