from tkinter import *

# GUI init
app = Tk()

windowWidth = 650
windowHeight = 450

EFFECT_REFRESH_RATE = 1

windowWidthSplit = windowWidth / 2
windowHeightSplit = windowHeight / 2

numberPickerSelection = IntVar()

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

def glitchState():
    CurrentState.set("Kamerastand: Glitch")

def pixelatedState():
    CurrentState.set("Kamerastand: Pixeliert")

def highPixelatedState():
    CurrentState.set("Kamerastand: Hoch-Pixeliert")

def lowPixelatedState():
    CurrentState.set("Kamerastand: Leicht Pixeliert")

def oldMovieState():
    CurrentState.set("Kamerastand: Altes Film")

def colorInvertState():
    CurrentState.set("Kamerastand: Invertierte Farben")

def objectDetectorState():
    CurrentState.set("Kamerastand: Objektmarkierer")

def blurFilterState():
    CurrentState.set("Kamerastand: Blurfilter-Effekt")

def asciiState():
    CurrentState.set("Kamerastand: ASCII-Effekt")

def recordState():
    CurrentState.set("Kamerastand: Aufzeichnen")

def refreshRateChanger():
    # gets the number and changes
    numberPickerSelection.set(numberPicker.get())
    print(numberPickerSelection.get())

def assign_widgets():
    currentState = Label(app, textvariable = CurrentState, background = LABEL_BACKGROUND, foreground = "#fff")
    currentState.place(x = 1, y = 1)

    btn_normalState = Button(app, text = "Normale Kamera", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = normalState)
    btn_normalState.place(x = 10, y = 30)

    btn_glitchState = Button(app, text = "Glitch-Kamera", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = glitchState)
    btn_glitchState.place(x = 147, y = 30)

    btn_pixelState = Button(app, text = "Pixeliert", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = pixelatedState)
    btn_pixelState.place(x = 268, y = 30)

    btn_highPixeled = Button(app, text = "Hoch-Pixeliert", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = highPixelatedState)
    btn_highPixeled.place(x = 355, y = 30)

    btn_oldMovie = Button(app, text = "Altes Film", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = oldMovieState)
    btn_oldMovie.place(x = 475, y = 30)

    btn_colorInvert = Button(app, text = "Farben invertieren", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = colorInvertState)
    btn_colorInvert.place(x = 10, y = 70)

    btn_lowPixeled = Button(app, text = "Leicht Pixeliert", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = lowPixelatedState)
    btn_lowPixeled.place(x = 153, y = 70)

    btn_objectHighlight = Button(app, text = "Objektmarkierer", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = objectDetectorState)
    btn_objectHighlight.place(x = 277, y = 70)

    btn_blurFilter = Button(app, text = "Blurfilter-Effekt", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = blurFilterState)
    btn_blurFilter.place(x = 407, y = 70)

    spinner_blurFilter = Scale(app, from_ = 1, to = 100, length = 142, orient = HORIZONTAL)
    spinner_blurFilter.place(x = 407, y = 98)

    btn_ascii = Button(app, text = "ASCII-Effekt", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = asciiState)
    btn_ascii.place(x = 10, y = 110)

    label0 = Label(app, text = "Bildwiederholfrequenz für Kameraeffekte (jede Sekunden):", border = 0, background = LABEL_BACKGROUND, foreground = "#fff")
    label0.place(x = 0, y = 170)

    numberPicker = Spinbox(app, from_ = 1, to = 60, width = 3, command = refreshRateChanger)
    numberPicker.place(x = 340, y = 168)

    btn_normalState = Button(app, text = "Fake Anwesenheit", border = 0, background = BUTTON_BACKGROUND_COLOR, foreground = TEXT_COLOR, command = recordState)
    btn_normalState.place(x = 153, y = 110)
    # end block

def create_window(title, favicon, window_geometry):
    app.title(title)
    app.geometry(window_geometry)

    faviconImg = PhotoImage(file = favicon)
    app.iconphoto(False, faviconImg)

    gradientBackground = GradientFrame(app, color1 = "#202a99", color2 = "#08044a", border = 0, relief = "sunken")
    gradientBackground.pack(fill = "both", expand = True)

    assign_widgets()

    app.resizable(False, False)
    app.mainloop()

# Window-Größe: (Horizontale Größe x Vertikale Größe)
create_window("Camera Call Chaos", "favicon.png", windowGeo)

# end file