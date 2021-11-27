from tkinter import *
import threading
import sys
from main import run

DEBUGGING = False
RESIZEABLE = False

class State:
    recording = False
    glitch = False
    filter = ""

# GUI init
app = Tk()

windowWidth = 650
windowHeight = 450

spinnerValue = 1
EFFECT_REFRESH_RATE = 1

windowWidthSplit = windowWidth / 2
windowHeightSplit = windowHeight / 2

numberPickerSelection = IntVar()
spinnerSelection = IntVar()

WINDOW_BACKGROUND_COLOR = "#10286e"
BUTTON_BACKGROUND_COLOR = "#30536b"
TEXT_COLOR = "#00f7ff"
LABEL_BACKGROUND = "#2654de"

windowGeo = (str(windowWidth) + "x" + str(windowHeight))

CurrentState = StringVar()
CurrentState.set("Kamerastand: Normal")

currentState = Label(app)

spinner_blurFilter = Scale(app)
numberPicker = Spinbox(app)


state = State()

class GradientFrame(Canvas):
    def __init__(self, parent, color1="red", color2="black", **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

def normalState():
    CurrentState.set("Kamerastand: Normal")
    state.filter = ""
    if DEBUGGING:
        print("virtualCamera is back on Normal State")

def jpeg_corruption():
    state.filter = "jpeg_corruption"
    CurrentState.set("Kamerastand: JPEG corruption")
    if DEBUGGING:
        print("glitching through the camera (epilepsy warning)")

def jpeg_compression():
    state.filter = "jpeg_compression"
    CurrentState.set("Kamerastand: JPEG compression")
    if DEBUGGING:
        print("virtualCamera has now the default pixeled state")

def ascii():
    CurrentState.set("Kamerastand: ASCII")
    state.filter = "ascii"
    if DEBUGGING:
        print("virtualCamera has now the high pixeled state")

def lowPixelatedState():
    state.filter = "binary"
    CurrentState.set("Kamerastand: Binary")
    if DEBUGGING:
        print("virtualCamera has now the low pixeled state")

def oldMovieState():
    state.filter = "blurfilter"
    CurrentState.set("Kamerastand: Blur Filter")
    if DEBUGGING:
        print("setting virtualCamera filter as \"old movie\"")

def colorInvertState():
    state.filter = "edgeFilter"
    CurrentState.set("Kamerastand: Edge Filter")
    if DEBUGGING:
        print("inverting colors on virtualCamera")

def blurFilterState():
    state.filter = "waterfilter"
    CurrentState.set("Kamerastand: Water Filter")

    if DEBUGGING:
        print("onBlurFilterState")

def animalFilterState():
    state.filter = "animalfilter"
    CurrentState.set("Kamerastand: Animal Filter")

def asciiState():
    CurrentState.set("Kamerastand: ASCII-Effekt")
    if DEBUGGING:
        print("onAsciiState")

def recordStartState():
    CurrentState.set("Kamerastand: Aufzeichnen")
    state.recording = True
    state.glitch = False

def recordStopState():
    CurrentState.set("Kamerastand: Loop")
    state.recording = False

def goLiveState():
    CurrentState.set("Kamerastand: Live")
    state.glitch = True

    if DEBUGGING:
        print("onRecordState")

def spinnerChangeListener(value):
    spinnerValue = value
    if DEBUGGING:
        print("Spinner Value = " + str(spinnerValue))

def refreshRateChanger():
    EFFECT_REFRESH_RATE = numberPickerSelection.get()
    if DEBUGGING:
        print("Effect Refresh Rate = " + str(EFFECT_REFRESH_RATE))

def assign_widgets():
    if DEBUGGING:
        print("Assigning Widgets")

    currentState = Label(app, textvariable = CurrentState, background = LABEL_BACKGROUND, foreground = "#fff")
    currentState.place(x = 1, y = 1)

    btn_normalState = Button(app, text = "Normale Kamera", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = normalState)
    btn_normalState.place(x = 10, y = 30)

    btn_jpeg_corruption = Button(app, text = "JPEG corruption", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = jpeg_corruption)
    btn_jpeg_corruption.place(x = 147, y = 30)

    btn_pixelState = Button(app, text = "JPEG compression", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = jpeg_compression)
    btn_pixelState.place(x = 300, y = 30)

    btn_highPixeled = Button(app, text = "ASCII", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = ascii)
    btn_highPixeled.place(x = 500, y = 30)

    btn_oldMovie = Button(app, text = "Binary", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = lowPixelatedState)
    btn_oldMovie.place(x = 10, y = 70)

    btn_colorInvert = Button(app, text = "Blur", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = oldMovieState)
    btn_colorInvert.place(x = 90, y = 70)

    btn_lowPixeled = Button(app, text = "Edge", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = colorInvertState)
    btn_lowPixeled.place(x = 170, y = 70)

    btn_blurFilter = Button(app, text = "Animal Filter", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = animalFilterState)
    btn_blurFilter.place(x = 330, y = 70)

    btn_blurFilter = Button(app, text = "Water", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = blurFilterState)
    btn_blurFilter.place(x = 230, y = 70)

    # spinner_blurFilter = Scale(app, from_ = 1, to = 100, length = 142, orient = HORIZONTAL, command = spinnerChangeListener)
    # spinner_blurFilter.place(x = 407, y = 98)
    #
    # label0 = Label(app, text = "Bildwiederholfrequenz für Kameraeffekte (jede Sekunden):", border = 0, background = LABEL_BACKGROUND, foreground = "#fff")
    # label0.place(x = 0, y = 170)
    #
    # numberPicker = Spinbox(app, textvariable = numberPickerSelection, from_ = 1, to = 60, width = 3, command = refreshRateChanger)
    # numberPicker.place(x = 340, y = 168)

    btn_normalState = Button(app, text = "Aufzeichnung starten", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = recordStartState)
    btn_normalState.place(x = 0, y = 200)

    btn_normalState = Button(app, text = "Aufzeichnung stoppen", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = recordStopState)
    btn_normalState.place(x = 200, y = 200)

    btn_normalState = Button(app, text = "Live gehen", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = goLiveState)
    btn_normalState.place(x = 400, y = 200)
    # end block

def create_window(title, favicon, window_geometry):
    app.title(title)
    app.geometry(window_geometry)

    faviconImg = PhotoImage(file = favicon)
    app.iconphoto(False, faviconImg)

    gradientBackground = GradientFrame(app, color1 = "#202a99", color2 = "#08044a", border = 0, relief = "sunken")
    gradientBackground.pack(fill = "both", expand = True)

    assign_widgets()

    app.resizable(RESIZEABLE, RESIZEABLE)
    app.mainloop()

# Window-Größe: (Horizontale Größe x Vertikale Größe)
t = threading.Thread(target=run, args=(state,))
t.start()

if len(sys.argv) > 1:
    if (sys.argv[1] == "-d" or sys.argv[1] == '--debug') or (sys.argv[2] == "-d" or sys.argv[2] == '--debug'):
        # enable debugger
        DEBUGGING = True
    if (sys.argv[1] == "-r" or sys.argv[1] == '--resizeable') or (sys.argv[2] == "-r" or sys.argv[2] == '--resizeable'):
        RESIZEABLE = True

if DEBUGGING:
    print("creating window with favicon \"favicon.png\" and its window geometry on " + windowGeo)

create_window("Camera.Call.Chaos", "favicon.png", windowGeo)

# end file
