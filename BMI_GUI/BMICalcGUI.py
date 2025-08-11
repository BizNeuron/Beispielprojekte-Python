"""
Features to be implemented in the future:
- dynamic zoom 
- support for imperial units
- better colour theme system (maybe saved as JSON file) 
/
Zukünftig implementierbare Features:
- dynamische Vergrößerung/Verkleinerung
- Unterstützung von imperialen Einheiten
- effektiveres Farbthema-System (vielleicht als JSON-Datei gespeichert), ohne direkte händische Implementierung
"""

import tkinter as tk


THEME_PATH = "Theme.txt" 
ICON_PATH = "bmi_icon.png"


def calcBMI(weight: float, height: float) -> float:  # Weight in kg and height in m / Gewicht in kg und Größe in m
    result = weight / height ** 2
    result = round(result, 2)
    return result


def bodyBMI(bmi: float) -> str:  # Return the body form of the BMI / Körperform nach BMI 
    body = ""

    if bmi <= 18.5:
        if bmi < 16.0:
            body = "extreme underweight"
        elif 16.0 <= bmi < 17.0:
            body = "middle underweight"
        elif bmi >= 17.0:
            body = "lower underweight"
    elif bmi >= 25.0:
        if bmi >= 40:
            body = "Adipose Grade 3"
        elif bmi >= 35:
            body = "Adipose Grade 2"
        elif bmi >= 30:
            body = "Adipose Grade 1"
        else:
            body = "moderate overweight"
    else:
        body = "perfect"

    return body


def readTheme() -> str:
    try:
        with open(THEME_PATH, "r") as file:
            return file.read()
    except FileNotFoundError:
        with open(THEME_PATH, "w") as file:
            file.write("Light")
            return "Light"


def writeTheme(theme: str) -> None:
    with open(THEME_PATH, "w") as file:
        file.write(theme)


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("360x320")
        self.wm_maxsize(360, 320) # fixed size makes everything easier / feste Größen machen alles einfacher
        self.wm_minsize(360, 320)
        
        try:
            icon = tk.PhotoImage(file=ICON_PATH)
            self.iconphoto(False, icon)
        except tk.TclError:
            pass # no icon
        
        self.label_text = tk.Label(self)
        self.in_height = tk.Entry(self)
        self.height_txt = tk.Label(self)
        self.in_weight = tk.Entry(self)
        self.weight_txt = tk.Label(self)
        self.calc = tk.Button(self)
        self.switch = tk.Button(self)
        self.result_text = tk.Label(self)
        self.in_height_num = tk.StringVar()
        self.in_weight_num = tk.StringVar()

        self.set_widgets()
        self.set_style()
        self.add_elements()

    def calculate(self) -> None:
        try:
            in_weight = str(self.in_weight_num.get()).replace(",", ".")
            in_height = str(self.in_height_num.get()).replace(",", ".")

            if in_height == "":
                in_height = 0
            if in_weight == "":
                in_weight = 0

            bmi = calcBMI(float(in_weight), float(in_height))
            self.result_text["text"] = "BMI: {bmi} -> {result}".format(bmi=bmi, result=bodyBMI(bmi))
            print(self.result_text["text"])
        except tk.TclError:
            self.result_text["text"] = "Please enter Numbers"
        except ZeroDivisionError:
            self.result_text["text"] = "Please enter correct Numbers"

    def set_style(self):
        if readTheme() == "Light":
            self.set_style_light()
            self.switch["command"] = self.set_style_dark
        else:
            self.set_style_dark()
            self.switch["command"] = self.set_style_light

    def set_style_light(self) -> None: 
        self.config(bg="#F0F0F0")
        self.label_text.config(font=("Carlito", 20), fg="black", bg="#F0F0F0")
        self.weight_txt.config(font=("Carlito", 15), fg="black", bg="#F0F0F0")
        self.height_txt.config(font=("Carlito", 15), fg="black", bg="#F0F0F0")
        self.result_text.config(font=("Carlito", 15), fg="black", bg="#F0F0F0")
        self.in_weight.config(font=("Carlito", 15), fg="black", bg="white", insertbackground="black")
        self.in_height.config(font=("Carlito", 15), fg="black", bg="white", insertbackground="black")
        self.calc.config(font=("Carlito", 15), fg="black", bg="#F0F0F0")
        self.switch.config(font=("Carlito", 15), fg="black", bg="#F0F0F0")
        writeTheme("Light")
        self.switch["command"] = self.set_style_dark

    def set_style_dark(self) -> None:
        self.config(bg="#3c3f41")
        self.label_text.config(font=("Carlito", 20), fg="white", bg="#3c3f41")
        self.weight_txt.config(font=("Carlito", 15), fg="white", bg="#3c3f41")
        self.height_txt.config(font=("Carlito", 15), fg="white", bg="#3c3f41")
        self.result_text.config(font=("Carlito", 15), fg="white", bg="#3c3f41")
        self.in_weight.config(font=("Carlito", 15), fg="white", bg="#2b2b2b", insertbackground="white")
        self.in_height.config(font=("Carlito", 15), fg="white", bg="#2b2b2b", insertbackground="white")
        self.calc.config(font=("Carlito", 15), fg="white", bg="#3c3f41")
        self.switch.config(font=("Carlito", 15), fg="white", bg="#3c3f41")
        writeTheme("Dark")
        self.switch["command"] = self.set_style_light

    def set_widgets(self) -> None:
        self.label_text["text"] = "Body Index Mass Calculator"

        self.in_height["textvariable"] = self.in_height_num
        self.in_weight["textvariable"] = self.in_weight_num

        self.height_txt["text"] = "Height in Meters:"
        self.weight_txt["text"] = "Weight in kg:"

        self.calc["text"] = "Calculate"
        self.calc["command"] = self.calculate
        self.switch["text"] = "Switch Theme"

    def add_elements(self) -> None:
        self.label_text.pack()
        self.weight_txt.pack()
        self.in_weight.pack()
        self.height_txt.pack()
        self.in_height.pack()
        self.calc.pack(pady=5)
        self.switch.pack(pady=5)
        self.result_text.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
