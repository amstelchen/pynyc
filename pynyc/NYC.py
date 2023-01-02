import os
import sys
import tkinter as tk
from datetime import datetime
import pytz
import arrow
import calendar
import locale
import argparse
from pathlib import Path
from .DU import getDuration

PROGNAME = "PyNYC"
VERSION = "0.1.0"
AUTHOR = "Copyright (C) 2022, 2023, by Michael John"
DESC = "A New Years's Clock"


class NewYearsClock:
    def __init__(self):
        #locale.setlocale(locale.LC_TIME, locale.getdefaultlocale()[0])

        self.config = {
            "fg": "white",
            "bg": "black",
            "fontface": "Courier",
            "fontsize": "50",
            "screensaver": 1,
            "alarm": "60, 15, 1"
        }

        self.loadDefaults()

        self.window = tk.Tk()
        self.window.title('New Year\'s Clock')
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.quitNewYearsClock)
        self.window.bind("<Escape>", self.quitNewYearsClock)

        Font_tuple = (self.config['fontface'], self.config['fontsize'], "bold")  # "Courier", 50

        # self.window.grid_columnconfigure((0,1), weight=2)
        # self.window.grid_rowconfigure(0, weight=2)

        # self.console = tk.Frame(self.window,borderwidth=1)
        # self.console.grid(row = 0, column = 0, sticky = tk.W+tk.E+tk.N+tk.S)

        # self.console.grid_columnconfigure(0, weight=1)
        # self.console.grid_rowconfigure(2, weight=1)

        self.lbl_c = tk.Label(self.window, text="", bg='black', fg='white')
        self.lbl_c.configure(font=Font_tuple)
        self.lbl_c.configure(fg=self.config['fg'])
        self.lbl_c.configure(bg=self.config['bg'])
        # self.lbl_c.grid(row = 0, column = 0, sticky = tk.W+tk.E+tk.N+tk.S)
        self.lbl_c.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        # self.text = tk.Text(self.console)
        # self.text.grid(row = 2, column = 0,rowspan = 3, columnspan = 1,
        #   sticky = tk.W+tk.E+tk.N+tk.S)
        # self.text.insert(tk.END,"hi")

    def updateDisplay(self):

        City = pytz.country_timezones(locale.getdefaultlocale()[0][3:5])[0]
        # DatumUhrzeit_dt = str(datetime.now().astimezone())
        # DatumUhrzeit_ar = arrow.Arrow.humanize(arrow.now(), only_distance=True, granularity=["hour", "minute"], locale="de-de")
        DatumUhrzeit_ar = arrow.now().format("dddd, D MMMM YYYY\nHH:mm:ss ZZ ZZZ", locale=locale.getdefaultlocale()[0])
        # "Current time is Friday, 30 December 2022, 09:00:09 CET (local time in Vienna)"
        DatumUhrzeit = f"Current time is\n{DatumUhrzeit_ar}\n(local time in {City})"

        # print(DatumUhrzeit)
        # print(pytz.tzinfo)

        DatumNeujahr_dt = datetime(datetime.now().year + 1, 1, 1)
        # DatumNeujahr = arrow.Arrow.humanize(arrow.get(datetime(2023, 1, 1)),
        #    only_distance=False, granularity=["day", "hour", "minute"], locale="de-de")
        DatumNeujahr_ar = arrow.get(DatumNeujahr_dt).format("dddd, D MMMM YYYY", locale=locale.getdefaultlocale()[0])

        Countdown_du = getDuration(datetime.now(), DatumNeujahr_dt)
        # "1 day, 14 hours, 56 minutes, 34 seconds until Sunday, 1 January 2023 (Vienna time)"
        # Countdown = "1 day, 14 hours, 56 minutes, 34 seconds until Sunday, 1 January 2023 (Vienna time)"
        Countdown = Countdown_du + f"\n until {DatumNeujahr_ar}"

        self.lbl_c.config(text=DatumUhrzeit + '\n\n\n' + Countdown)
        self.window.after(100, self.updateDisplay)
        # self.window.mainloop()  # runs in main()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitNewYearsClock(self, event):
        exit()

    def loadDefaults(self):
        if os.sys.platform == 'win32':
            if os.path.isdir(os.path.join(os.environ['LOCALAPPDATA'])):
                userPath = os.path.join(os.environ['LOCALAPPDATA'], PROGNAME, 'pynyc.conf')
        if sys.platform == 'linux':
            userPath = str(Path('~').expanduser()) + "/.config/pynyc.conf"
        try:
            with open(userPath, "r") as configFile:
                # self.config= configFile.readlines()
                # print(self.config)
                self.config = {}
                for configLine in configFile.readlines():
                    name, value = configLine.strip().split(" = ")
                    self.config[name] = value
                #print(self.config)
        except FileNotFoundError as e:
            print(e)
            print("Using sane defaults.")


def main():
    parser = argparse.ArgumentParser(prog=PROGNAME, description=DESC)  #, epilog=EPILOG + criteria_str)
    parser.add_argument('-fg', dest='fg', help='foreground (text) color', type=str)
    parser.add_argument('-bg', dest='bg', help='background (wall) color', type=str)
    # parser.add_argument('-q', '--quiet', help='suppress output', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION + ' ' + AUTHOR)

    args = parser.parse_args()
    # quiet = vars(args)["quiet"]
    # if not quiet:
        # print(str(args).replace("Namespace", "Options"))
    
    app = NewYearsClock()
    # app.window.after(1000, app.updateDisplay)
    app.updateDisplay()
    app.window.mainloop()
