#!/usr/bin/env python
# Credits!!!
# (YT) Clear Code - Particle System
# (YT) Python Simplified - Python to .app
# jay3332 - Number Abbreviation
# Cryptogrounds / Considera Core
# https://github.com/Gooodgis/dont-touch-my-presents

# To Do List:
# Make Clicker Heroes after 1k score
# 2nd layer prestige

import pygame
import random
from decimal import *
import math
import threading
import sys
import time
import os
#import svg
import datetime
import pickle
import json
import csv
import asyncio
import io
from io import BytesIO
import numpy as np
#pynanosvg
import raylibpy as rl
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
rl.init_audio_device()
rl.set_target_fps(0)
GameFPS = 24
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        #https://stackoverflow.com/a/13790741
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class ParticlePrinciple:
    def __init__(self):
        self.particles = []
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
                WindowXscale = WindowWidth / screen_width
                WindowYscale = WindowHeight / screen_height
                if WindowXscale < 0 and WindowYscale < 0:
                    WindowScale2 = min(WindowXscale, WindowYscale)
                elif WindowXscale > 0 and WindowYscale > 0:
                    WindowScale2 = min(WindowXscale, WindowYscale)
                else:
                    WindowScale2 = 0
                particle[0][0] += particle[3] * math.sin(particle[2]) * 60/GameFPS * WindowScale2
                particle[0][1] += particle[3] * math.cos(particle[2]) * 60/GameFPS * WindowScale2
                particle[1] -= 24/GameFPS
                particle_surface = pygame.Surface((constrain(particle[1], 0, math.inf)*WindowScale2 * 2, constrain(particle[1], 0, math.inf)*WindowScale2 * 2), pygame.SRCALPHA)
                pygame.draw.circle(particle_surface, (255, 255, 255, constrain(constrain(particle[1], 0, math.inf)*25.6, 0, 255)), (constrain(particle[1], 0, math.inf)*WindowScale2,particle[1]*WindowScale2), constrain(particle[1], 0, math.inf)*WindowScale2)
                screen.blit(particle_surface, (particle[0][0] - constrain(particle[1], 0, math.inf)*WindowScale2, particle[0][1] - constrain(particle[1], 0, math.inf)*WindowScale2))
    def add_particles(self, posx, posy, radiuss, directionn, sped):
        pos_x = posx
        pos_y = posy
        radius = radiuss
        direction = directionn
        speed = sped
        particle_circle = [[pos_x, pos_y], radius, direction, speed]
        self.particles.append(particle_circle)
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

# Initialize Pygame
pygame.init()
def semitone_ratio(n):
    return 2 ** (n / 12)
def speed_ratio(n):
    (math.log(math.e, n) / math.log(math.e, 2))*12
# Long Suffixes Add
for _ in range(1):
    LongSuffixes = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion"]
    UniSuffixes = ["", "un", "duo", "tre", "quattor", "quin", "sex", "septen", "octo", "novem", ""]
    BiSuffixes = ["", "decillion", "vigintillion", "trigintillion", "quadragintillion", "quinquagintillion", "sexagintillion", "septuagintillion", "octogintillion", "nonagintillion", ""]
    BiSuffixesShort = ["", "deci", "viginti", "triginti", "quadraginti", "quinquaginti", "sexaginti", "septuaginti", "octoginti", "nonaginti", ""]
    TriSuffixes = ["", "centillion", "ducentillion", "trecentillion", "quadracentillion", "quintacentillion", "sesagintillion", "septacentillion", "octocentillion", "nongincentillion", ""]
    TriSuffixesShort = ["", "centi", "ducenti", "trecenti", "quadracenti", "quintacenti", "sesaginti", "septacenti", "octogincenti", "nongincenti", ""]
    QuadSuffixes = ["", "millillion", "dumillillion", "trimillillion", "quadrimillillion", "quinmillillion", "sexamillillion", "septimillillion", "octomillillion", "nonamillillion", ""]
    unicount = 1
    bicount = 1
    for _ in range(9):
        for _ in range(9):
            LongSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount])
            unicount += 1
        LongSuffixes.append(BiSuffixes[bicount+1])
        unicount = 1
        bicount += 1
    tricount = 1
    for _ in range(9):
        LongSuffixes[len(LongSuffixes)-1] = TriSuffixes[tricount]
        unicount = 1
        for _ in range(9):
            LongSuffixes.append(UniSuffixes[unicount] + TriSuffixes[tricount])
            unicount += 1
        unicount = 1
        bicount = 1
        LongSuffixes.append(BiSuffixesShort[bicount] + TriSuffixes[tricount])
        for _ in range(9):
            for _ in range(9):
                LongSuffixes.append(UniSuffixes[unicount] + BiSuffixesShort[bicount] + TriSuffixes[tricount])
                unicount += 1
            LongSuffixes.append(BiSuffixesShort[bicount+1] + TriSuffixes[tricount])
            unicount = 1
            bicount += 1
        tricount += 1
    LongSuffixes[len(LongSuffixes)-1] = "millillion"
    quadcount = 1
    for _ in range(9):
        LongSuffixes[len(LongSuffixes)-1] = QuadSuffixes[quadcount]
        unicount = 1
        for _ in range(9):
            LongSuffixes.append(UniSuffixes[unicount] + QuadSuffixes[quadcount])
            unicount += 1
        unicount = 1
        bicount = 1
        LongSuffixes.append(BiSuffixesShort[bicount] + QuadSuffixes[quadcount])
        for _ in range(9):
            for _ in range(9):
                LongSuffixes.append(UniSuffixes[unicount] + BiSuffixesShort[bicount] + QuadSuffixes[quadcount])
                unicount += 1
            LongSuffixes.append(BiSuffixesShort[bicount+1] + QuadSuffixes[quadcount])
            unicount = 1
            bicount = 1
        tricount = 1
        for _ in range(9):
            LongSuffixes[len(LongSuffixes)-1] = TriSuffixesShort[tricount] + QuadSuffixes[quadcount]
            unicount = 1
            for _ in range(9):
                LongSuffixes.append(UniSuffixes[unicount] + TriSuffixesShort[tricount] + QuadSuffixes[quadcount])
                unicount += 1
            unicount = 1
            bicount = 1
            LongSuffixes.append(BiSuffixesShort[bicount] + TriSuffixesShort[tricount] + QuadSuffixes[quadcount])
            for _ in range(9):
                for _ in range(9):
                    LongSuffixes.append(UniSuffixes[unicount] + BiSuffixesShort[bicount] + TriSuffixesShort[tricount] + QuadSuffixes[quadcount])
                    unicount += 1
                LongSuffixes.append(BiSuffixesShort[bicount+1] + TriSuffixesShort[tricount] + QuadSuffixes[quadcount])
                unicount = 1
                bicount += 1
            tricount += 1
        quadcount += 1
    LongSuffixes[len(LongSuffixes)-1] = "myrnillion"
    LongSuffCount = 1
    for _ in range(len(LongSuffixes)):
        LongSuffixes[LongSuffCount-1] = " " + LongSuffixes[LongSuffCount-1]
        LongSuffCount += 1

# Short Suffixes Add
for _ in range(1):
    ShortSuffixes = ["", "k", "M", "B", "T", "Qa", "Qi", "Sx", "Sp", "O", "N", "d"]
    UniSuffixes = ["", "U", "D", "T", "Qa", "Qi", "Sx", "Sp", "O", "N", ""]
    BiSuffixes = ["", "d", "Vg", "Tg", "Qag", "Qig", "Sxg", "Spg", "Og", "Ng", ""]
    TriSuffixes = ["", "Cnt", "Ducnt", "Trcnt", "Qacnt", "Qicnt", "Secnt", "Spcnt", "Ocnt", "Ncnt", ""]
    QuadSuffixes = ["", "Mlln", "Dmln", "Tmln", "Qdmln", "Qimln", "Sxmln", "Spmln", "Omln", "Nmln", ""]
    unicount = 1
    bicount = 1
    for _ in range(9):
        for _ in range(9):
            ShortSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount])
            unicount += 1
        ShortSuffixes.append(BiSuffixes[bicount+1])
        unicount = 1
        bicount += 1
    tricount = 1
    for _ in range(9):
        ShortSuffixes[len(ShortSuffixes)-1] = TriSuffixes[tricount]
        unicount = 1
        for _ in range(9):
            ShortSuffixes.append(UniSuffixes[unicount] + TriSuffixes[tricount])
            unicount += 1
        unicount = 1
        bicount = 1
        ShortSuffixes.append(BiSuffixes[bicount] + TriSuffixes[tricount])
        for _ in range(9):
            for _ in range(9):
                ShortSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount] + TriSuffixes[tricount])
                unicount += 1
            ShortSuffixes.append(BiSuffixes[bicount+1] + TriSuffixes[tricount])
            unicount = 1
            bicount += 1
        tricount += 1
    ShortSuffixes[len(ShortSuffixes)-1] = "Mlln"
    quadcount = 1
    for _ in range(9):
        ShortSuffixes[len(ShortSuffixes)-1] = QuadSuffixes[quadcount]
        unicount = 1
        for _ in range(9):
            ShortSuffixes.append(UniSuffixes[unicount] + QuadSuffixes[quadcount])
            unicount += 1
        unicount = 1
        bicount = 1
        ShortSuffixes.append(BiSuffixes[bicount] + QuadSuffixes[quadcount])
        for _ in range(9):
            for _ in range(9):
                ShortSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount] + QuadSuffixes[quadcount])
                unicount += 1
            ShortSuffixes.append(BiSuffixes[bicount+1] + QuadSuffixes[quadcount])
            unicount = 1
            bicount = 1
        tricount = 1
        for _ in range(9):
            ShortSuffixes[len(ShortSuffixes)-1] = TriSuffixes[tricount] + QuadSuffixes[quadcount]
            unicount = 1
            for _ in range(9):
                ShortSuffixes.append(UniSuffixes[unicount] + TriSuffixes[tricount] + QuadSuffixes[quadcount])
                unicount += 1
            unicount = 1
            bicount = 1
            ShortSuffixes.append(BiSuffixes[bicount] + TriSuffixes[tricount] + QuadSuffixes[quadcount])
            for _ in range(9):
                for _ in range(9):
                    ShortSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount] + TriSuffixes[tricount] + QuadSuffixes[quadcount])
                    unicount += 1
                ShortSuffixes.append(BiSuffixes[bicount+1] + TriSuffixes[tricount] + QuadSuffixes[quadcount])
                unicount = 1
                bicount += 1
            tricount += 1
        quadcount += 1
    ShortSuffixes[len(ShortSuffixes)-1] = "Myrn"

def fexp(f):
    return Decimal(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(f))))) if f != 0 else 0

def fman(f):
    return Decimal(f/10**fexp(f))

def decimal_sign(x):
    x = Decimal(x)
    return 1 if x > 0 else -1 if x < 0 else 0

def abbreviate(number, suffixes, decimals, greaterthan, rounda):
    if Decimal.__abs__(Decimal(number)) < greaterthan:
        if rounda:
            return Decimal.__round__(number)
        else:
            return Decimal.__round__(number*(10**decimals))/(10**decimals)
    if fexp(Decimal(number)) < 10002 * 3 and fexp(Decimal(number)) > -1:
        if suffixes == "l":
            return (str(round(fman(Decimal(number)) * (10**(fexp(Decimal(number))%3)) * (10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3)-decimals)))) / 10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals)) + LongSuffixes[Decimal.__floor__(Decimal(fexp(Decimal(number))/3))+0])
        elif suffixes == "s":
            return (str(round(fman(Decimal(number)) * (10**(fexp(Decimal(number))%3)) * (10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals))) / 10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals)) + ShortSuffixes[Decimal.__floor__(Decimal(fexp(Decimal(number))/3))+0])
        elif suffixes == "sci":
            return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number))))
        elif suffixes == "eng":
            if Decimal(fexp(Decimal(number)))%3 == 0:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number))))
            if Decimal(fexp(Decimal(number)))%3 == 1:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals+1)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number/10))))
            if Decimal(fexp(Decimal(number)))%3 == 2:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals+2)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number/100))))
    elif Decimal.__abs__(Decimal(fexp(Decimal(number)))) < 10**6:
        if suffixes == "sci":
            return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number))))
        elif suffixes == "eng":
            if Decimal(fexp(Decimal(number)))%3 == 0:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number))))
            if Decimal(fexp(Decimal(number)))%3 == 1:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals+1)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number/10))))
            if Decimal(fexp(Decimal(number)))%3 == 2:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals+2)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number/100))))
        else:
            return (str(round(fman(Decimal(number)), decimals)) + "e" + str(fexp(Decimal(number))))
    elif Decimal.__abs__(Decimal(fexp(Decimal(number)))) < 10**10002 * 3:
        if suffixes == "l":
            return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)*3), 3)) + LongSuffixes[Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)+0])
        elif suffixes == "s":
            return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)*3), 3)) + ShortSuffixes[Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)+0])
        elif suffixes == "sci":
            return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number))))
        elif suffixes == "eng":
            if Decimal(fexp(Decimal(number)))%3 == 0:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number))))
            if Decimal(fexp(Decimal(number)))%3 == 1:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals+1)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number/10))))
            if Decimal(fexp(Decimal(number)))%3 == 2:
                return str(str(Decimal.__round__(Decimal(fman(Decimal(number)))*(Decimal(10)**Decimal(decimals+2)))/Decimal(Decimal(10)**Decimal(decimals))) + "e" + str(fexp(Decimal(number/100))))
    else:
        return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number))))))), 3)) + "e" + Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))))

# Screen and clock
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE, pygame.SRCALPHA)
pygame.display.set_caption("Clicker Game")
clock = pygame.time.Clock()

particle1 = ParticlePrinciple()

PARTICLE_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(PARTICLE_EVENT, 20)

# Font
font = pygame.font.Font(resource_path(str(THIS_DIR / "./assets/fonts/Lato/Lato-Bold.ttf")), 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
score = Decimal(0)
click_value = Decimal(1)
auto_click_value = Decimal(0)
auto_click_rate = Decimal(1)
click_value_multi = Decimal(1)
cps_to_cpc = Decimal(0)
upgrades = []
def resetupgrades():
    global upgrades
    upgrades = []
    upgrades.append(
        {"num": 1,
        "name": "+1 Per Click",
        "cost": Decimal(0),
        "startcost": Decimal(40/1.1),
        "costcoefficient": Decimal(1.1),
        "bought": Decimal(1)}
    )
    upgrades.append(
        {"num": 2,
        "name": "Auto Clicker +0.1",
        "cost": Decimal(0),
        "startcost": Decimal(80),
        "costcoefficient": Decimal(1.1),
        "bought": Decimal(0)}
    )
    upgrades.append(
        {"num": 3,
        "name": "Auto Click Rate +0.1",
        "cost": Decimal(0),
        "startcost": Decimal(500),
        "costcoefficient": Decimal(1.1),
        "bought": Decimal(0)}
    )
    upgrades.append(
        {"num": 4,
        "name": "Double Clicks (X2)",
        "cost": Decimal(0),
        "startcost": Decimal(10000),
        "costcoefficient": Decimal(7),
        "bought": Decimal(0)}
    )
    upgrades.append(
        {"num": 5,
        "name": "Auto Clicker +1",
        "cost": Decimal(0),
        "startcost": Decimal(1200),
        "costcoefficient": Decimal(1.07),
        "bought": Decimal(0)}
    )
    upgrades.append(
        {"num": 6,
        "name": "Double Click Rate (X2)",
        "cost": Decimal(0),
        "startcost": Decimal(35000),
        "costcoefficient": Decimal(9),
        "bought": Decimal(0)}
    )
    upgrades.append(
        {"num": 7,
        "name": "Auto Clicker +10",
        "cost": Decimal(0),
        "startcost": Decimal(18000),
        "costcoefficient": Decimal(1.07),
        "bought": Decimal(0)}
    )
    upgrades.append(
        {"num": 8,
        "name": "+10 Per Click",
        "cost": Decimal(0),
        "startcost": Decimal(1000),
        "costcoefficient": Decimal(1.06),
        "bought": Decimal(0)}
    )
    upgrades.append(
        {"num": 9,
        "name": "Triple Click Rate (X3)",
        "cost": Decimal(0),
        "startcost": Decimal(500000),
        "costcoefficient": Decimal(15),
        "bought": Decimal(0)}
    )
    upgrades.append(
        {"num": 10,
        "name": "+1% CPS per click",
        "cost": Decimal(0),
        "startcost": Decimal(1000000),
        "costcoefficient": Decimal(5),
        "bought": Decimal(0)}
    )
resetupgrades()
upgrade_buttons = []
upgrade_button_width = [300, 360, 400, 380, 360, 440, 360, 320, 460, 440]
upgrade_button_height = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
upgrade_button_x = []
for __ in range(1):
    a = 40
    for _ in range(len(upgrade_button_width)):
        upgrade_button_x.append(a)
        a += upgrade_button_width[_] + 20
# upgrade_button_x = [40, 360, 680, 1040, 1420, 1740, 2160, 2480]
(UpgradeButtonColorRed, UpgradeButtonColorGreen, UpgradeButtonColorBlue) = (
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
) #(200, 200, 200)
(UpgradeTargetButtonColorRed, UpgradeTargetButtonColorGreen, UpgradeTargetButtonColorBlue) = (
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
) #(0, 0, 0)
(UpgradeButtonOutlineColorRed, UpgradeButtonOutlineColorGreen, UpgradeButtonOutlineColorBlue) = (
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
) #(200, 200, 200)
(UpgradeTargetButtonOutlineColorRed, UpgradeTargetButtonOutlineColorGreen, UpgradeTargetButtonOutlineColorBlue) = (
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
) #(0, 0, 0)
Upgrade_Button_X_scroll = 0
Upgrade_Button_X_scroll_vel = 0

Settings = [
    {"num": 1,
    "name": "SFX",
    "value": Decimal(100),
    "percent": True,
    "round": True,
    "holdable": True,
    "held": False,
    "min": Decimal(0),
    "max": Decimal(100)},

    {"num": 2,
    "name": "Music",
    "value": Decimal(25),
    "percent": True,
    "round": True,
    "holdable": True,
    "held": False,
    "min": Decimal(0),
    "max": Decimal(100)},

    {"num": 3,
    "name": "Save Game",
    "value": "",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},

    {"num": 4,
    "name": "Load Game",
    "value": "",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},

    {"num": 5,
    "name": "Prestige",
    "value": "",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
    
    {"num": 6,
    "name": "Reset",
    "value": "",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},

    {"num": 7,
    "name": "Notation",
    "value": "Short",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
]
Settings_buttons = []
NoSettings_buttons = []
Settings_button_width = [300, 300, 300, 300, 300, 300, 300]
Settings_button_height = [50, 50, 50, 50, 50, 50, 50]
Settings_button_x = [490, 490, 490, 490, 490, 490, 490]
Settings_button_y = [70, 140, 210, 280, 350, 420, 490]
BuyThing = [
    {"num": 1,
    "name": "Buy",
    "value": "X1",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
    {"num": 2,
    "name": "OCD Buy",
    "value": "OFF",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
    {"num": 3,
    "name": "Mode",
    "value": "Clicker",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
]
Buy_buttons = []
NoBuy_buttons = []
Buy_button_Width = [150, 200, 300]
Buy_button_Height = [25, 25, 25]
Buy_button_X = [30, 30, 490]
Buy_button_Y = [460, 510, 50]
(SettingsButtonColorRed, SettingsButtonColorGreen, SettingsButtonColorBlue) = (
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
) #(200, 200, 200)
(SettingsTargetButtonColorRed, SettingsTargetButtonColorGreen, SettingsTargetButtonColorBlue) = (
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
) #(0, 0, 0)
(SettingsButtonOutlineColorRed, SettingsButtonOutlineColorGreen, SettingsButtonOutlineColorBlue) = (
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
) #(200, 200, 200)
(SettingsTargetButtonOutlineColorRed, SettingsTargetButtonOutlineColorGreen, SettingsTargetButtonOutlineColorBlue) = (
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
) #(0, 0, 0)
(BuyButtonColorRed, BuyButtonColorGreen, BuyButtonColorBlue) = (
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
) #(200, 200, 200)
(BuyTargetButtonColorRed, BuyTargetButtonColorGreen, BuyTargetButtonColorBlue) = (
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
) #(0, 0, 0)
(BuyButtonOutlineColorRed, BuyButtonOutlineColorGreen, BuyButtonOutlineColorBlue) = (
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
) #(200, 200, 200)
(BuyTargetButtonOutlineColorRed, BuyTargetButtonOutlineColorGreen, BuyTargetButtonOutlineColorBlue) = (
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
) #(0, 0, 0)
Settings_Button_Y_scroll = 0
Settings_Button_Y_scroll_vel = 0
# Clicker button
clicker_button_image = pygame.image.load(resource_path(str(THIS_DIR / "./assets/img/python-logo-generic.png"))).convert_alpha()
# clicker_button_rect = clicker_button_image.get_rect(center=(screen_width // 2, screen_height // 2))
arrow_down_img1 = pygame.image.load(resource_path(str(THIS_DIR / "./assets/img/Arrow1-c.png"))).convert_alpha()
arrow_up_img1 = pygame.image.load(resource_path(str(THIS_DIR / "./assets/img/Arrow1-d.png"))).convert_alpha()

# Upgrade button setup
for i, upgrade in enumerate(upgrades):
    x = upgrade_button_x[i]
    y = screen_height - upgrade_button_height[i] - 20
    upgrade_buttons.append(pygame.Rect(x, y, upgrade_button_width[i], upgrade_button_height[i]))
    upgrade_buttons[i] = pygame.Rect(x, y, upgrade_button_width[i], upgrade_button_height[i])
for i, setting in enumerate(Settings):
    Settings_buttons.append(pygame.Rect(Settings_button_x[i], Settings_button_y[i], Settings_button_width[i], Settings_button_height[i]))
    NoSettings_buttons.append(pygame.Rect(Settings_button_x[i], Settings_button_y[i], Settings_button_width[i], Settings_button_height[i]))
    Settings_buttons[i] = pygame.Rect(Settings_button_x[i], Settings_button_y[i], Settings_button_width[i], Settings_button_height[i])
for i, buything in enumerate(BuyThing):
    Buy_buttons.append(pygame.Rect(Buy_button_X[i], Buy_button_Y[i], Buy_button_Width[i], Buy_button_Height[i]))
    NoBuy_buttons.append(pygame.Rect(Buy_button_X[i], Buy_button_Y[i], Buy_button_Width[i], Buy_button_Height[i]))
    Buy_buttons[i] = pygame.Rect(Buy_button_X[i], Buy_button_Y[i], Buy_button_Width[i], Buy_button_Height[i])

# Game loop
running = True
frames = 0
scale_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scale_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target_scale_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target_scale_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
offlineBoxAlpha = 0
start_time = time.time()
delta_time = 0.000001
game_time = -0.000001
GameFPS = 1/delta_time
musicplays = 0
musicplays2 = 0
bulkbuy = 1
CamPos = [float(0.0), float(0.0)]
CamPos2 = [float(0.0), float(0.0)]
gems = Decimal(0)
gemstoget = Decimal(0)
gemboosttoget = Decimal(0)
differenceTimeOffline = 0
def constrain(val, min_val, max_val):
    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

pygame.mixer.init()
pygamemixermusic = 1
musicfilepath = ""
musicintrofilepath = ""
pymusictype = ""

def PlayMusic(musNum):
    #pygame.mixer.music.stop()
    global pygamemixermusic, musicfilepath, musicintrofilepath, music1, music2
    pygamemixermusic = 1
    if musNum == 1:
        pygamemixermusic = 0.25
        pymusictype = "wav"
        musicfilepath = "./assets/audio/Debug Menu Unused   Paper Mario  The Thousand Year Door.wav"
        #musicfilepath = "./assets/audio/Debug Menu Unused   Paper Mario  The Thousand Year Door.mp3"
        musicintrofilepath = "./assets/audio/nosound.wav"
    elif musNum == 2:
        pygamemixermusic = 1
        pymusictype = "wav"
        musicfilepath = "./assets/audio/SpongeBob SquarePants OST - Dombummel (LQ).wav"
        musicintrofilepath = "./assets/audio/nosound.wav"
    elif musNum == 3:
        pygamemixermusic = 0.7
        pymusictype = "wav"
        musicfilepath = "./assets/audio/Kevin MacLeod - Hep Cats.wav"
        #musicfilepath = "./assets/audio/Kevin MacLeod - Hep Cats.mp3"
        musicintrofilepath = "./assets/audio/nosound.wav"
    elif musNum == 4:
        pygamemixermusic = 1
        pymusictype = "wav"
        musicfilepath = "./assets/audio/(Object Break) Kevin MacLeod - Padanaya Blokov - loop.wav"
        musicintrofilepath = "./assets/audio/(Object Break) Kevin MacLeod - Padanaya Blokov - intro.wav"
    elif musNum == 5:
        pygamemixermusic = .9
        pymusictype = "wav"
        musicfilepath = "./assets/audio/(radzlan - Miami Hotline Vol.3 (feat. Demonicity)) 673473_-Miami-Hotline--Vol3.wav"
        #musicfilepath = "./assets/audio/(radzlan - Miami Hotline Vol.3 (feat. Demonicity)) 673473_-Miami-Hotline--Vol3.mp3"
        musicintrofilepath = "./assets/audio/nosound.wav"
    elif musNum == 6:
        pygamemixermusic = .9
        pymusictype = "wav"
        musicfilepath = "./assets/audio/INOSSI - Got you-loop.wav"
        musicintrofilepath = "./assets/audio/INOSSI - Got you-start.wav"
    elif musNum == 7:
        pygamemixermusic = .8
        pymusictype = "wav"
        musicfilepath = "./assets/audio/Casino Park - Sonic Heroes [OST]-loop.wav"
        musicintrofilepath = "./assets/audio/Casino Park - Sonic Heroes [OST]-start.wav"
    elif musNum == 8:
        pygamemixermusic = 1.2
        pymusictype = "wav"
        musicfilepath = "./assets/audio/MVBit - delfino plaza but it's in a kirby soundfont loop.wav"
        musicintrofilepath = "./assets/audio/MVBit - delfino plaza but it's in a kirby soundfont intro.wav"
    elif musNum == 9:
        pygamemixermusic = .9
        pymusictype = "mp3"
        musicfilepath = "./assets/audio/584141_Echo-My-World-Club-Mix-WIP.mp3"
        musicintrofilepath = "./assets/audio/nosound.mp3"
    elif musNum == 10:
        pygamemixermusic = .9
        pymusictype = "mp3"
        musicfilepath = "./assets/audio/636200_Rumux.mp3"
        musicintrofilepath = "./assets/audio/nosound.mp3"
    elif musNum == 11:
        pygamemixermusic = .9
        pymusictype = "mp3"
        musicfilepath = "./assets/audio/637714_Bass-Beat.mp3"
        musicintrofilepath = "./assets/audio/nosound.mp3"
    elif musNum == 12:
        pygamemixermusic = 1.1
        pymusictype = "wav"
        musicfilepath = "./assets/audio/Sakurasou Pet na Kanojo Original Sountrack - 17. Virus toka Okucchauzo (Warai) (I'm Gonna Send You A Virus).wav"
        musicintrofilepath = "./assets/audio/nosound.wav"
    elif musNum == 13:
        pygamemixermusic = 1
        pymusictype = "wav"
        musicfilepath = "./assets/audio/Laurent Lombard - Exotico Speedo-loop.wav"
        musicintrofilepath = "./assets/audio/Laurent Lombard - Exotico Speedo-intro.wav"
    elif musNum == 14:
        pygamemixermusic = .9
        pymusictype = "wav"
        musicfilepath = "./assets/audio/Mr Weebl - Slightly More Evil Penguins-loop.wav"
        musicintrofilepath = "./assets/audio/nosound.wav"
    elif musNum == 15:
        pygamemixermusic = 1.2
        pymusictype = "wav"
        musicfilepath = "./assets/audio/vibingleaf - Infinite Money Glitch Trojan Extended Loop-loop.wav"
        musicintrofilepath = "./assets/audio/vibingleaf - Infinite Money Glitch Trojan Extended Loop-start.wav"
    # Load audio file
    if musicintrofilepath == "./assets/audio/nosound.wav":
        musicintrofilepath = musicfilepath
    if musicintrofilepath == "./assets/audio/nosound.mp3":
        musicintrofilepath = musicfilepath
    #pygame.mixer.music.load(str(THIS_DIR / musicintrofilepath))
    music1 = rl.load_music_stream(str(THIS_DIR / musicintrofilepath))
    music2 = rl.load_music_stream(str(THIS_DIR / musicfilepath))
    #pygame.mixer.music.set_volume(pygamemixermusic)
    #pygame.mixer.music.play()
    rl.set_music_volume(music1, pygamemixermusic)
    rl.set_music_volume(music2, pygamemixermusic)
    rl.stop_music_stream(music1)
    rl.stop_music_stream(music2)
    rl.play_music_stream(music1)
PlayMusic(random.randint(1,15))
#pygame.mixer.music.set_volume(pygamemixermusic * float(Settings[1]["value"] / 100))
rl.set_music_volume(music1, pygamemixermusic * float(Settings[1]["value"] / 100))
rl.set_music_volume(music2, pygamemixermusic * float(Settings[1]["value"] / 100))
click_sound = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/Click mouse - Fugitive Simulator - The-Nick-of-Time.wav")))
hover_sound = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/251389__deadsillyrabbit__button_hover-wav.wav")))
upgrade_sound = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/Upgrade SOund 0001.wav")))
punch_sound1 = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/normal/punch_general_body_impact_05-resources.wav")))
punch_sound2 = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/normal/punch_general_body_impact_06-resources.wav")))
punch_sound3 = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/normal/punch_general_body_impact_07-resources.wav")))
punch_sound4 = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/normal/punch_general_body_impact_08-resources.wav")))
punch_sound_crit1 = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/crit/Punch.wav")))
punch_sound_crit2 = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/crit/puncher.mp3")))
punch_sound_crit3 = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/crit/puncher.ogg")))
punch_sound_crit4 = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/crit/punchp.wav")))
punch_sound_death = pygame.mixer.Sound(resource_path(str(THIS_DIR / "./assets/audio/punch/crit/punchMachineHit-sharedassets3.assets-853.wav")))

Hovering_Buttons = [0,0,0,0,0,0,0,0,0,0]
framestofixload = 0
offlineOldTime = time.time()
offlineCurrentTime = time.time()
gemboost = 1
offlineTime = 0
GameStuff = []
GameStuff2 = []
def save_game():
    global offlineTime
    offlineTime = time.time()
    GameStuff = [gems, score, start_time, offlineTime, bulkbuy, ClickSecondList, MaxClicksPerSecond, TotalClicks, enemy_hp, monsterskilled, enemy_max_hp, click_damage]
    GameStuff2 = [Settings, upgrades, GameStuff, BuyThing]
    with open (resource_path(str(THIS_DIR / "./save/SaveData.pickle")), 'wb') as fileSave:
        pickle.dump(GameStuff2, fileSave, protocol=pickle.HIGHEST_PROTOCOL)
def load_game():
    try:
        global Settings, upgrades, gems, score, start_time, game_time, offlineCurrentTime, offlineOldTime, framestofixload, auto_click_rate, auto_click_value, click_value, click_value_multi, cps_to_cpc, offlineBoxAlpha, differenceTimeOffline, offlineCurrentTime, offlineOldTime, gemboost, GameStuff, bulkbuy, GameStuff2, ClickSecondList, MaxClicksPerSecond, TotalClicks, BuyThing, enemy_hp, monsterskilled, enemy_max_hp, click_damage
        with open (resource_path(str(THIS_DIR / "./save/SaveData.pickle")), 'rb') as fileSave:
            GameStuff2 = pickle.load(fileSave)
            GameStuff = GameStuff2[2]
            upgrades = GameStuff2[1]
            Settings = GameStuff2[0]
            BuyThing = GameStuff2[3]
        score = GameStuff[1]
        bulkbuy = GameStuff[4]
        ClickSecondList = GameStuff[5]
        MaxClicksPerSecond = GameStuff[6]
        TotalClicks = GameStuff[7]
        enemy_hp = GameStuff[8]
        monsterskilled = GameStuff[9]
        enemy_max_hp = GameStuff[10]
        click_damage = GameStuff[11]
        click_value = Decimal(upgrades[0]["bought"]) + (Decimal(upgrades[7]["bought"])*Decimal(10))
        auto_click_value = (Decimal(upgrades[1]["bought"])*Decimal(0.1)) + Decimal(upgrades[4]["bought"]) + (Decimal(upgrades[6]["bought"])*Decimal(10))
        cps_to_cpc = (Decimal(upgrades[9]["bought"])*Decimal(0.01))
        auto_click_rate = 1 + ((Decimal(upgrades[2]["bought"])*Decimal(0.1)) * (Decimal(2)**Decimal(upgrades[5]["bought"])) * (Decimal(3)**Decimal(upgrades[8]["bought"])))
        click_value_multi = (Decimal(2)**Decimal(upgrades[3]["bought"]))
        start_time = GameStuff[2]
        gems = GameStuff[0]
        gemboost = Decimal((50+gems)/50)
        #delta_time = (time.time() - start_time) - game_time
        game_time = time.time() - start_time
        tempOfflineTime = GameStuff[3]
        offlineOldTime = tempOfflineTime
        offlineCurrentTime = time.time()
        differenceTimeOffline = (offlineCurrentTime - offlineOldTime) * .1
        framestofixload = 0
        offlineBoxAlpha = 255
        score += (Decimal(differenceTimeOffline) * Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(gemboost))
    except FileNotFoundError:
        save_game()
def reset():
    global gems, gemboost, score, bulkbuy, ClickSecondList, MaxClicksPerSecond, TotalClicks, YouWillNotUpgradeUnlessToldTo_Time, ClicksPerSecond, speedmusic
    prestige()
    gems = Decimal(0)
    gemboost = Decimal(0)
    score = Decimal(0)
    bulkbuy = 1
    YouWillNotUpgradeUnlessToldTo_Time = 0.3
    ClicksPerSecond = 0
    ClickSecondList = []
    MaxClicksPerSecond = 0
    TotalClicks = 0
    speedmusic = 1.0

"""
    if event.button == 1:
        print("You pressed the left mouse button")
    elif event.button == 3:
        print("You pressed the right mouse button")
"""
YouWillNotUpgradeUnlessToldTo_Time = 0.3
ClicksPerSecond = 0
ClickSecondList = []
MaxClicksPerSecond = 0
TotalClicks = 0
speedmusic = 1.0
# Create nested directories
try:
    os.makedirs(str(THIS_DIR / "save"))
    print(f"save folder created successfully.")
except FileExistsError:
    print(f"One or more directories in the save folder already exist.")
except PermissionError:
    print(f"Permission denied: Unable to create a save folder.")
except Exception as e:
    print(f"An error occurred: {e}")
print("You can also reset the game by deleting the save folder. Of course, you need to restart the game in order to fully reset the game.")

enemy_hp = Decimal(10)
monsterskilled = Decimal(0)
enemy_max_hp = Decimal(10)
click_damage = Decimal(1)
buttonshake = [0,0]
buttonshake2 = [0,0]
notation = "s"
enemyhealthsmoothper = 1.0
while running:
    click_damage = Decimal(click_value)*Decimal(click_value_multi) + Decimal(cps_to_cpc)*Decimal(auto_click_value)*Decimal(auto_click_rate)
    def checkenemyded(clickorwait):
        global enemy_hp, enemy_max_hp, score, monsterskilled
        if clickorwait == "click":
            while Decimal(enemy_hp) <= 0:
                monsterskilled += Decimal(1)
                score += Decimal(random.uniform(.5, 1.5))*Decimal(enemy_max_hp)
                enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(Decimal(monsterskilled) // Decimal(5))))
                enemy_hp += Decimal(enemy_max_hp)
                punch_sound_death.play()
                while Decimal((Decimal(click_value)*Decimal(random.uniform(0.95, 1.05))*Decimal(click_value_multi) + Decimal(cps_to_cpc)*Decimal(auto_click_value)*Decimal(auto_click_rate))*Decimal(gemboost)) / (Decimal(1.1**100)) >= Decimal(enemy_max_hp):
                    monsterskilled += Decimal(500)
                    score += Decimal(random.uniform(.5, 1.5))*Decimal(10) * Decimal(Decimal(1.1)**Decimal(Decimal(monsterskilled-1) // Decimal(5)))
                    enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(Decimal(monsterskilled) // Decimal(5))))
                    enemy_hp += Decimal(enemy_max_hp)
                    punch_sound_death.play()
                    while Decimal((Decimal(click_value)*Decimal(random.uniform(0.95, 1.05))*Decimal(click_value_multi) + Decimal(cps_to_cpc)*Decimal(auto_click_value)*Decimal(auto_click_rate))*Decimal(gemboost)) / (Decimal(1.1**1000)) >= Decimal(enemy_max_hp):
                        monsterskilled += Decimal(5000)
                        score += Decimal(random.uniform(.5, 1.5))*Decimal(10) * Decimal(Decimal(1.1)**Decimal(Decimal(monsterskilled-1) // Decimal(5)))
                        enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(Decimal(monsterskilled) // Decimal(5))))
                        enemy_hp += Decimal(enemy_max_hp)
                        punch_sound_death.play()
                        while Decimal((Decimal(click_value)*Decimal(random.uniform(0.95, 1.05))*Decimal(click_value_multi) + Decimal(cps_to_cpc)*Decimal(auto_click_value)*Decimal(auto_click_rate))*Decimal(gemboost)) / Decimal.__pow__(Decimal(1.1),Decimal(10000)) >= Decimal(enemy_max_hp):
                            monsterskilled += Decimal(50000)
                            score += Decimal(random.uniform(.5, 1.5))*Decimal(10) * Decimal(Decimal(1.1)**Decimal(Decimal(monsterskilled-1) // Decimal(5)))
                            enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(monsterskilled) // Decimal(5)))
                            enemy_hp += Decimal(enemy_max_hp)
                            punch_sound_death.play()
                            while Decimal((Decimal(click_value)*Decimal(random.uniform(0.95, 1.05))*Decimal(click_value_multi) + Decimal(cps_to_cpc)*Decimal(auto_click_value)*Decimal(auto_click_rate))*Decimal(gemboost)) / Decimal.__pow__(Decimal(1.1),Decimal(100000)) >= Decimal(enemy_max_hp):
                                monsterskilled += Decimal(500000)
                                score += Decimal(random.uniform(.5, 1.5))*Decimal(10) * Decimal.__pow__(Decimal(1.1),Decimal(Decimal(monsterskilled-1) // Decimal(5)))
                                enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(monsterskilled) // Decimal(5)))
                                enemy_hp += Decimal(enemy_max_hp)
                                punch_sound_death.play()
        if clickorwait == "wait":
            while Decimal(enemy_hp) <= 0:
                monsterskilled += Decimal(1)
                score += Decimal(random.uniform(.5, 1.5))*Decimal(enemy_max_hp)
                enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(Decimal(monsterskilled) // Decimal(5))))
                enemy_hp += Decimal(enemy_max_hp)
                punch_sound_death.play()
                while Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(delta_time) * Decimal(gemboost) / (Decimal(1.1**100)) >= Decimal(enemy_max_hp):
                    monsterskilled += Decimal(500)
                    score += Decimal(random.uniform(.5, 1.5))*Decimal(10) * Decimal(Decimal(1.1)**Decimal(Decimal(monsterskilled-1) // Decimal(5)))
                    enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(Decimal(monsterskilled) // Decimal(5))))
                    enemy_hp += Decimal(enemy_max_hp)
                    punch_sound_death.play()
                    while Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(delta_time) * Decimal(gemboost) / (Decimal(1.1**1000)) >= Decimal(enemy_max_hp):
                        monsterskilled += Decimal(5000)
                        score += Decimal(random.uniform(.5, 1.5))*Decimal(10) * Decimal(Decimal(1.1)**Decimal(Decimal(monsterskilled-1) // Decimal(5)))
                        enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(Decimal(monsterskilled) // Decimal(5))))
                        enemy_hp += Decimal(enemy_max_hp)
                        punch_sound_death.play()
                        while Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(delta_time) * Decimal(gemboost) / Decimal.__pow__(Decimal(1.1),Decimal(10000)) >= Decimal(enemy_max_hp):
                            monsterskilled += Decimal(50000)
                            score += Decimal(random.uniform(.5, 1.5))*Decimal(10) * Decimal(Decimal(1.1)**Decimal(Decimal(monsterskilled-1) // Decimal(5)))
                            enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(monsterskilled) // Decimal(5)))
                            enemy_hp += Decimal(enemy_max_hp)
                            punch_sound_death.play()
                            while Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(delta_time) * Decimal(gemboost) / Decimal.__pow__(Decimal(1.1),Decimal(100000)) >= Decimal(enemy_max_hp):
                                monsterskilled += Decimal(500000)
                                score += Decimal(random.uniform(.5, 1.5))*Decimal(10) * Decimal.__pow__(Decimal(1.1),Decimal(Decimal(monsterskilled-1) // Decimal(5)))
                                enemy_max_hp = Decimal(10) * Decimal(Decimal.__pow__(Decimal(1.1),Decimal(monsterskilled) // Decimal(5)))
                                enemy_hp += Decimal(enemy_max_hp)
                                punch_sound_death.play()
    speedmusic = constrain(speedmusic + (1-speedmusic)/(0.75/delta_time), 1, 3)
    rl.set_music_pitch(music1, speedmusic)
    rl.set_music_pitch(music2, speedmusic)
    rl.update_music_stream(music1)
    rl.update_music_stream(music2)
    framestofixload += 1
    gemboost = Decimal((50+gems)/50)
    mos_x, mos_y = pygame.mouse.get_pos()
    frames += 1
    (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
    WindowXscale = WindowWidth / screen_width
    WindowYscale = WindowHeight / screen_height
    if WindowXscale < 1 and WindowYscale < 1:
        WindowScale = max(WindowXscale, WindowYscale)
    elif WindowXscale > 1 and WindowYscale > 1:
        WindowScale = min(WindowXscale, WindowYscale)
    else:
        WindowScale = 1.0
    if WindowXscale < 0 and WindowYscale < 0:
        WindowScale2 = min(WindowXscale, WindowYscale)
    elif WindowXscale > 0 and WindowYscale > 0:
        WindowScale2 = min(WindowXscale, WindowYscale)
    else:
        WindowScale2 = 0
    delta_time = (time.time() - start_time) - game_time
    game_time = time.time() - start_time
    if delta_time > 0:
        GameFPS = 1/delta_time
    else:
        GameFPS = math.inf
    if mos_y > WindowHeight - 160:
        if mos_x - CamPos[0]*WindowXscale > WindowWidth/1.1:
            Upgrade_Button_X_scroll_vel -= 60*delta_time
        elif mos_x - CamPos[0]*WindowXscale < WindowWidth - WindowWidth/1.1:
            Upgrade_Button_X_scroll_vel += 60*delta_time
    #if mos_y > WindowHeight*0.35 and mos_x - CamPos[1]*WindowYscale > WindowWidth*.75 and mos_y < WindowHeight*0.5:
    #    Settings_Button_Y_scroll_vel -= 60*delta_time
    #elif mos_y < WindowHeight*0.1 and mos_x - CamPos[1]*WindowYscale > WindowWidth*.75:
    #    Settings_Button_Y_scroll_vel += 60*delta_time

    Upgrade_Button_X_scroll = constrain(Upgrade_Button_X_scroll+Upgrade_Button_X_scroll_vel, screen_width*-2.5, 0)
    Upgrade_Button_X_scroll_vel /= 1.1
    for i, upgrade in enumerate(upgrade_buttons):
        x = upgrade_button_x[i] + Upgrade_Button_X_scroll + Upgrade_Button_X_scroll_vel
        y = (screen_height - upgrade_button_height[i]) - 20
        upgrade_buttons[i] = pygame.Rect(x*WindowScale2, y*WindowYscale, upgrade_button_width[i]*WindowScale2, upgrade_button_height[i]*WindowScale2)
        UpgradeButtonColorRed[i] += (UpgradeTargetButtonColorRed[i] - UpgradeButtonColorRed[i])/(0.15/delta_time)
        UpgradeButtonColorGreen[i] += (UpgradeTargetButtonColorGreen[i] - UpgradeButtonColorGreen[i])/(0.15/delta_time)
        UpgradeButtonColorBlue[i] += (UpgradeTargetButtonColorBlue[i] - UpgradeButtonColorBlue[i])/(0.15/delta_time)
        UpgradeButtonOutlineColorRed[i] += (UpgradeTargetButtonOutlineColorRed[i] - UpgradeButtonOutlineColorRed[i])/(0.15/delta_time)
        UpgradeButtonOutlineColorGreen[i] += (UpgradeTargetButtonOutlineColorGreen[i] - UpgradeButtonOutlineColorGreen[i])/(0.15/delta_time)
        UpgradeButtonOutlineColorBlue[i] += (UpgradeTargetButtonOutlineColorBlue[i] - UpgradeButtonOutlineColorBlue[i])/(0.15/delta_time)
        UpgradeButtonColorRed[i] = constrain(UpgradeButtonColorRed[i], 0, 255)
        UpgradeButtonColorGreen[i] = constrain(UpgradeButtonColorGreen[i], 0, 255)
        UpgradeButtonColorBlue[i] = constrain(UpgradeButtonColorBlue[i], 0, 255)
        UpgradeButtonOutlineColorRed[i] = constrain(UpgradeButtonOutlineColorRed[i], 0, 255)
        UpgradeButtonOutlineColorGreen[i] = constrain(UpgradeButtonOutlineColorGreen[i], 0, 255)
        UpgradeButtonOutlineColorBlue[i] = constrain(UpgradeButtonOutlineColorBlue[i], 0, 255)
    """Settings_Button_Y_scroll = constrain(Settings_Button_Y_scroll+Settings_Button_Y_scroll_vel, screen_height*-.45, screen_height*0.05)
    Settings_Button_Y_scroll_vel /= 1.1"""
    for i, setting in enumerate(Settings):
        x = Settings_button_x[i]
        y = Settings_button_y[i] + Settings_Button_Y_scroll + Settings_Button_Y_scroll_vel
        Settings_buttons[i] = pygame.Rect(x*WindowScale2, y*WindowYscale, Settings_button_width[i]*WindowScale2, Settings_button_height[i]*WindowScale2)
        NoSettings_buttons[i] = pygame.Rect((Settings_button_x[i] + CamPos[0]*WindowXscale)*WindowXscale, (constrain(Settings_button_y[i] + Settings_Button_Y_scroll + Settings_Button_Y_scroll_vel, screen_height*0.05, screen_height*0.8) + CamPos[1]*WindowYscale/WindowYscale)*WindowYscale, Settings_button_width[i]*WindowXscale, Settings_button_height[i]*WindowYscale)
        SettingsButtonColorRed[i] += (SettingsTargetButtonColorRed[i] - SettingsButtonColorRed[i])/(0.15/delta_time)
        SettingsButtonColorGreen[i] += (SettingsTargetButtonColorGreen[i] - SettingsButtonColorGreen[i])/(0.15/delta_time)
        SettingsButtonColorBlue[i] += (SettingsTargetButtonColorBlue[i] - SettingsButtonColorBlue[i])/(0.15/delta_time)
        SettingsButtonOutlineColorRed[i] += (SettingsTargetButtonOutlineColorRed[i] - SettingsButtonOutlineColorRed[i])/(0.15/delta_time)
        SettingsButtonOutlineColorGreen[i] += (SettingsTargetButtonOutlineColorGreen[i] - SettingsButtonOutlineColorGreen[i])/(0.15/delta_time)
        SettingsButtonOutlineColorBlue[i] += (SettingsTargetButtonOutlineColorBlue[i] - SettingsButtonOutlineColorBlue[i])/(0.15/delta_time)
        SettingsButtonColorRed[i] = constrain(SettingsButtonColorRed[i], 0, 255)
        SettingsButtonColorGreen[i] = constrain(SettingsButtonColorGreen[i], 0, 255)
        SettingsButtonColorBlue[i] = constrain(SettingsButtonColorBlue[i], 0, 255)
        SettingsButtonOutlineColorRed[i] = constrain(SettingsButtonOutlineColorRed[i], 0, 255)
        SettingsButtonOutlineColorGreen[i] = constrain(SettingsButtonOutlineColorGreen[i], 0, 255)
        SettingsButtonOutlineColorBlue[i] = constrain(SettingsButtonOutlineColorBlue[i], 0, 255)
    for i, buything in enumerate(BuyThing):
        x = Buy_button_X[i]
        y = Buy_button_Y[i]
        Buy_buttons[i] = pygame.Rect(x*WindowScale2, y*WindowYscale, Buy_button_Width[i]*WindowScale2, Buy_button_Height[i]*WindowScale2)
        NoBuy_buttons[i] = pygame.Rect((Buy_button_X[i] + CamPos[0]*WindowXscale)*WindowXscale, (Buy_button_Y[i] + CamPos[1]*WindowYscale/WindowYscale)*WindowYscale, Buy_button_Width[i]*WindowXscale, Buy_button_Height[i]*WindowYscale)
        BuyButtonColorRed[i] += (BuyTargetButtonColorRed[i] - BuyButtonColorRed[i])/(0.15/delta_time)
        BuyButtonColorGreen[i] += (BuyTargetButtonColorGreen[i] - BuyButtonColorGreen[i])/(0.15/delta_time)
        BuyButtonColorBlue[i] += (BuyTargetButtonColorBlue[i] - BuyButtonColorBlue[i])/(0.15/delta_time)
        BuyButtonOutlineColorRed[i] += (BuyTargetButtonOutlineColorRed[i] - BuyButtonOutlineColorRed[i])/(0.15/delta_time)
        BuyButtonOutlineColorGreen[i] += (BuyTargetButtonOutlineColorGreen[i] - BuyButtonOutlineColorGreen[i])/(0.15/delta_time)
        BuyButtonOutlineColorBlue[i] += (BuyTargetButtonOutlineColorBlue[i] - BuyButtonOutlineColorBlue[i])/(0.15/delta_time)
        BuyButtonColorRed[i] = constrain(BuyButtonColorRed[i], 0, 255)
        BuyButtonColorGreen[i] = constrain(BuyButtonColorGreen[i], 0, 255)
        BuyButtonColorBlue[i] = constrain(BuyButtonColorBlue[i], 0, 255)
        BuyButtonOutlineColorRed[i] = constrain(BuyButtonOutlineColorRed[i], 0, 255)
        BuyButtonOutlineColorGreen[i] = constrain(BuyButtonOutlineColorGreen[i], 0, 255)
        BuyButtonOutlineColorBlue[i] = constrain(BuyButtonOutlineColorBlue[i], 0, 255)
    x_inside = [0,0,0,0,0,0,0,0,0,0]
    y_inside = [0,0,0,0,0,0,0,0,0,0]
    button_rect_x = [(WindowWidth//2) + (CamPos[0] + buttonshake[0])*WindowXscale, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    button_rect_y = [(WindowHeight//2) + (math.sin(game_time*5))*30*WindowScale2 + (CamPos[1] + buttonshake[1])*WindowYscale, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # clicker_button_rect = clicker_button_image.get_rect(center=(scale_x[0], scale_y[0]))
    mos_x, mos_y = pygame.mouse.get_pos()
    target_scale_x[0] = 400
    for button_i in range(0, 3):
        if mos_x > button_rect_x[button_i]-(scale_x[button_i]/2)*WindowScale2 and mos_x < button_rect_x[button_i]+(scale_x[button_i]/2)*WindowScale2:
            x_inside[button_i] = 1
        else: x_inside[button_i] = 0
        if mos_y > button_rect_y[button_i]-(scale_y[button_i]/2)*WindowScale2 and mos_y < button_rect_y[button_i]+(scale_y[button_i]/2)*WindowScale2:
            y_inside[button_i] = 1
        else: y_inside[button_i] = 0
        if x_inside[button_i] == 1 and y_inside[button_i] == 1:
            if Hovering_Buttons[button_i] == 0:
                hover_sound.play()
            Hovering_Buttons[button_i] = 1
            if button_i == 0:
                target_scale_x[0] = 450
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        target_scale_x[0] = 350
                        scale_x[0] = constrain(scale_x[0]-40, 200, math.inf)
                        if BuyThing[2]["value"] == "Clicker":
                            score += Decimal(click_value)*Decimal(random.uniform(0.95, 1.05))*Decimal(click_value_multi)*Decimal(gemboost) + Decimal(cps_to_cpc)*Decimal(auto_click_value)*Decimal(auto_click_rate)*Decimal(gemboost)
                            click_sound.play()
                            ClickSecondList.append(1)
                            TotalClicks+=1
                            speedmusic += 0.025/(speedmusic**5)
                        elif BuyThing[2]["value"] == "Fight":
                            enemy_hp -= (Decimal(click_value)*Decimal(random.uniform(0.95, 1.05))*Decimal(click_value_multi) + Decimal(cps_to_cpc)*Decimal(auto_click_value)*Decimal(auto_click_rate))*Decimal(gemboost)
                            checkenemyded("click")
                            soundipunch = random.randint(1,4)
                            if soundipunch == 1:
                                punch_sound1.play()
                            elif soundipunch == 2:
                                punch_sound2.play()
                            elif soundipunch == 3:
                                punch_sound3.play()
                            elif soundipunch == 4:
                                punch_sound4.play()
                            click_sound.play()
                            ClickSecondList.append(1)
                            TotalClicks+=1
                            buttonshake2 = [10, 10]
                            speedmusic += 0.025/(speedmusic**5)
                        for i in range(10):
                            particle1.add_particles(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, random.randrange(-180, 180), 4)
            elif button_i == 1:
                pass
        else:
            Hovering_Buttons[button_i] = 0
    for i in range(len(ClickSecondList)):
        if not i >= len(ClickSecondList):
            ClickSecondList[i-1] -= delta_time
            if ClickSecondList[i-1] <= 0:
                ClickSecondList.remove(ClickSecondList[i-1])
    ClicksPerSecond = len(ClickSecondList)
    if ClicksPerSecond >= MaxClicksPerSecond:
        MaxClicksPerSecond = ClicksPerSecond
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for i, button in enumerate(upgrade_buttons):
            if button.collidepoint((mos_x - CamPos[0]*WindowXscale, mos_y - CamPos[1]*WindowYscale)):
                UpgradeTargetButtonColorRed[i] = 0
                UpgradeTargetButtonColorGreen[i] = 100
                UpgradeTargetButtonColorBlue[i] = 0
                UpgradeTargetButtonOutlineColorRed[i] = 0
                UpgradeTargetButtonOutlineColorGreen[i] = 255
                UpgradeTargetButtonOutlineColorBlue[i] = 0
            else:
                UpgradeTargetButtonColorRed[i] = 0
                UpgradeTargetButtonColorGreen[i] = 0
                UpgradeTargetButtonColorBlue[i] = 0
                UpgradeTargetButtonOutlineColorRed[i] = 0
                UpgradeTargetButtonOutlineColorGreen[i] = 0
                UpgradeTargetButtonOutlineColorBlue[i] = 0
        for i, button in enumerate(NoSettings_buttons):
            if button.collidepoint((mos_x, mos_y)):
                SettingsTargetButtonColorRed[i] = 0
                SettingsTargetButtonColorGreen[i] = 100
                SettingsTargetButtonColorBlue[i] = 0
                SettingsTargetButtonOutlineColorRed[i] = 0
                SettingsTargetButtonOutlineColorGreen[i] = 255
                SettingsTargetButtonOutlineColorBlue[i] = 0
            else:
                SettingsTargetButtonColorRed[i] = 0
                SettingsTargetButtonColorGreen[i] = 0
                SettingsTargetButtonColorBlue[i] = 0
                SettingsTargetButtonOutlineColorRed[i] = 0
                SettingsTargetButtonOutlineColorGreen[i] = 0
                SettingsTargetButtonOutlineColorBlue[i] = 0
        for i, button in enumerate(NoBuy_buttons):
            if button.collidepoint((mos_x - (CamPos[0]*WindowXscale), mos_y - (CamPos[1]*WindowYscale))):
                BuyTargetButtonColorRed[i] = 0
                BuyTargetButtonColorGreen[i] = 100
                BuyTargetButtonColorBlue[i] = 0
                BuyTargetButtonOutlineColorRed[i] = 0
                BuyTargetButtonOutlineColorGreen[i] = 255
                BuyTargetButtonOutlineColorBlue[i] = 0
            else:
                BuyTargetButtonColorRed[i] = 0
                BuyTargetButtonColorGreen[i] = 0
                BuyTargetButtonColorBlue[i] = 0
                BuyTargetButtonOutlineColorRed[i] = 0
                BuyTargetButtonOutlineColorGreen[i] = 0
                BuyTargetButtonOutlineColorBlue[i] = 0
        if event.type == pygame.MOUSEBUTTONUP:
            for i, button in enumerate(NoSettings_buttons):
                Settings[i]["held"] = False
            for i, button in enumerate(NoBuy_buttons):
                BuyThing[i]["held"] = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, button in enumerate(upgrade_buttons):
                if button.collidepoint((mos_x - CamPos[0]*WindowXscale, mos_y - CamPos[1]*WindowYscale)):
                    UpgradeTargetButtonColorRed[i] = 150
                    UpgradeTargetButtonColorGreen[i] = 75
                    UpgradeTargetButtonColorBlue[i] = 0
                    UpgradeTargetButtonOutlineColorRed[i] = 0
                    UpgradeTargetButtonOutlineColorGreen[i] = 128
                    UpgradeTargetButtonOutlineColorBlue[i] = 255
                    if bulkbuy == "Max":
                        buy00001 = Decimal(calcmax())
                        upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(calcmax()) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
                    elif BuyThing[1]["value"] == "ON":
                        buy00001 = Decimal(upgrades[i]["bought"]) - Decimal(upgrades[i]["bought"]) % Decimal(bulkbuy) + Decimal(bulkbuy) - Decimal(upgrades[i]["bought"])
                        upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(Decimal(upgrades[i]["bought"]) - Decimal(upgrades[i]["bought"]) % Decimal(bulkbuy) + Decimal(bulkbuy) - Decimal(upgrades[i]["bought"])) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
                    else:
                        buy00001 = Decimal(bulkbuy)
                        upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(bulkbuy) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
                    if Decimal(score) >= Decimal(upgrades[i]["cost"]) and YouWillNotUpgradeUnlessToldTo_Time <=0:
                        score -= Decimal(upgrades[i]["cost"])
                        upgrades[i]["bought"] += Decimal(buy00001)
                        upgrade_sound.stop()
                        upgrade_sound.play()
                        click_sound.play()
                        YouWillNotUpgradeUnlessToldTo_Time = 1/24
            for i, button in enumerate(NoSettings_buttons):
                if button.collidepoint(event.pos) and event.pos[1] == event.pos[1]:
                    click_sound.play()
                    SettingsTargetButtonColorRed[i] = 150
                    SettingsTargetButtonColorGreen[i] = 75
                    SettingsTargetButtonColorBlue[i] = 0
                    SettingsTargetButtonOutlineColorRed[i] = 0
                    SettingsTargetButtonOutlineColorGreen[i] = 128
                    SettingsTargetButtonOutlineColorBlue[i] = 255
                    Settings[i]["held"] = True
                    if i == 2:
                        save_game()
                    if i == 3:
                        load_game()
                    if i == 4:
                        prestige()
                    if i == 5:
                        reset()
                    if i == 6:
                        if Settings[6]["value"] == "Short":
                            Settings[6]["value"] = "Long"
                        elif Settings[6]["value"] == "Long":
                            Settings[6]["value"] = "Scientific"
                        elif Settings[6]["value"] == "Scientific":
                            Settings[6]["value"] = "Engineering"
                        elif Settings[6]["value"] == "Engineering":
                            Settings[6]["value"] = "Short"
            for i, button in enumerate(NoBuy_buttons):
                if button.collidepoint(event.pos):
                    click_sound.play()
                    BuyTargetButtonColorRed[i] = 150
                    BuyTargetButtonColorGreen[i] = 75
                    BuyTargetButtonColorBlue[i] = 0
                    BuyTargetButtonOutlineColorRed[i] = 0
                    BuyTargetButtonOutlineColorGreen[i] = 128
                    BuyTargetButtonOutlineColorBlue[i] = 255
                    BuyThing[i]["held"] = True
                    if i == 0:
                        if bulkbuy == 1:
                            bulkbuy = 5
                        elif bulkbuy == 5:
                            bulkbuy = 10
                        elif bulkbuy == 10:
                            bulkbuy = 25
                        elif bulkbuy == 25:
                            bulkbuy = 50
                        elif bulkbuy == 50:
                            bulkbuy = 100
                        elif bulkbuy == 100:
                            bulkbuy = 500
                        elif bulkbuy == 500:
                            bulkbuy = 1000
                        elif bulkbuy == 1000:
                            bulkbuy = "Max"
                        elif bulkbuy == "Max":
                            bulkbuy = 1
                    if i == 1:
                        if BuyThing[1]["value"] == "OFF":
                            BuyThing[1]["value"] = "ON"
                        elif BuyThing[1]["value"] == "ON":
                            BuyThing[1]["value"] = "OFF"
                    if i == 2:
                        if BuyThing[2]["value"] == "Clicker":
                            BuyThing[2]["value"] = "Fight"
                        elif BuyThing[2]["value"] == "Fight":
                            BuyThing[2]["value"] = "Clicker"
    if Settings[6]["value"] == "Short":
        notation = "s"
    if Settings[6]["value"] == "Long":
        notation = "l"
    if Settings[6]["value"] == "Scientific":
        notation = "sci"
    if Settings[6]["value"] == "Engineering":
        notation = "eng"
    scale_x[0] += (target_scale_x[0]-scale_x[0])/(0.15/delta_time)
    scale_y[0] = scale_x[0]
    smalclicrimg = pygame.transform.scale(clicker_button_image, (constrain(scale_x[0]*WindowScale2, 1, math.inf), constrain(scale_y[0]*WindowScale2, 1, math.inf)))
    realarrowdownimg1 = pygame.transform.scale(arrow_down_img1, (32 * WindowScale2, 32 * WindowScale2))
    realarrowupimg1 = pygame.transform.scale(arrow_up_img1, (32 * WindowScale2, 32 * WindowScale2))
    # Update auto click
    click_value = Decimal(upgrades[0]["bought"]) + (Decimal(upgrades[7]["bought"])*Decimal(10))
    auto_click_value = (Decimal(upgrades[1]["bought"])*Decimal(0.1)) + Decimal(upgrades[4]["bought"]) + (Decimal(upgrades[6]["bought"])*Decimal(10))
    cps_to_cpc = (Decimal(upgrades[9]["bought"])*Decimal(0.01))
    auto_click_rate = 1 + ((Decimal(upgrades[2]["bought"])*Decimal(0.1)) * (Decimal(2)**Decimal(upgrades[5]["bought"])) * (Decimal(3)**Decimal(upgrades[8]["bought"])))
    click_value_multi = (Decimal(2)**Decimal(upgrades[3]["bought"]))
    if framestofixload >= 1:
        score += Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(delta_time) * Decimal(gemboost)
        if BuyThing[2]["value"] == "Fight":
            enemy_hp -= Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(delta_time) * Decimal(gemboost)
    gemstoget = (Decimal(100) * Decimal.sqrt(Decimal(score) / Decimal(1000000000000))) + Decimal(0)
    gemboosttoget = Decimal(gemstoget/50)

    # Draw screen
    screen.fill((30, 30, 30))
    screen.blit(smalclicrimg, (button_rect_x[0]-(scale_x[0]/2)*WindowScale2, button_rect_y[0]-(scale_y[0]/2)*WindowScale2))
    # Draw text
    font = pygame.font.Font(resource_path(str(THIS_DIR / "./assets/fonts/Lato/Lato-Bold.ttf")), int(24*WindowScale2))
    def draw_text(text, font, color, x, y, align, alpha):
        text_surface = font.render(text, True, color)
        text_surface.set_alpha(alpha)
        text_rect = text_surface.get_rect()
        if align == "left":
            screen.blit(text_surface, (x, y))
        elif align == "center":
            text_rect.center = (x, y)
            screen.blit(text_surface, text_rect)
    draw_text(f"Score: {abbreviate(score, notation, 3, 100000, False)}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 10*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
    if BuyThing[2]["value"] == "Clicker":
        draw_text(f"Score Per Click: {abbreviate(click_value + (cps_to_cpc*auto_click_value*auto_click_rate), notation, 3, 100000, False)}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 40*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Click Value Multiplier: x{abbreviate(click_value_multi, notation, 3, 100000, False)}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 70*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Score Per Second: {abbreviate(auto_click_value, notation, 3, 100000, False)}/s", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 100*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        if delta_time > 0:
            draw_text(f"FPS: {Decimal(1/delta_time):.2f}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 130*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        else:
            draw_text(f"FPS: INFINITY", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 130*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Seconds Per Second: {abbreviate(auto_click_rate, notation, 3, 1000, False)}/s", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 160*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Gems: {abbreviate(gems, notation, 3, 100000, True)} (+ {abbreviate(gemstoget, notation, 3, 100000, True)})", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 190*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"{abbreviate(Decimal(gemboost), notation, 3, 100000, False)}x boost (+{abbreviate(Decimal(gemboosttoget), notation, 3, 100000, False)})", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 220*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Total Score Per Second: {abbreviate(auto_click_value * auto_click_rate * gemboost, notation, 3, 1000, False)}/s", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 250*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Total Score Per Click: {abbreviate((click_value*click_value_multi + cps_to_cpc*auto_click_value*auto_click_rate)*gemboost, notation, 3, 100000, False)}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 280*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Clicks Per Second: {ClicksPerSecond}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 310*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Max Clicks Per Second: {MaxClicksPerSecond}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 340*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Total Clicks: {TotalClicks}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 370*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
    elif BuyThing[2]["value"] == "Fight":
        if delta_time > 0:
            draw_text(f"FPS: {Decimal(1/delta_time):.2f}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 40*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        else:
            draw_text(f"FPS: INFINITY", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 40*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Gems: {abbreviate(gems, notation, 3, 100000, True)} (+ {abbreviate(gemstoget, notation, 3, 100000, True)})", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 70*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"{abbreviate(Decimal(gemboost), notation, 3, 100000, False)}x boost (+{abbreviate(Decimal(gemboosttoget), notation, 3, 100000, False)})", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 100*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Click Damage: {abbreviate(click_damage, notation, 3, 1000, False)}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 130*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"HP: {abbreviate(enemy_hp, notation, 3, 100000, False)} / {abbreviate(enemy_max_hp, notation, 3, 100000, False)}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 160*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Killed Monsters: {abbreviate(monsterskilled, notation, 3, 100000, True)}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 190*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Clicks Per Second: {ClicksPerSecond}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 220*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Max Clicks Per Second: {MaxClicksPerSecond}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 250*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        draw_text(f"Total Clicks: {TotalClicks}", font, WHITE, 10*WindowScale2 + CamPos[0]*WindowXscale, 280*WindowScale2 + CamPos[1]*WindowYscale, "left", 255)
        enemyhealthsmoothper += (float(Decimal(enemy_hp)/Decimal(enemy_max_hp))-enemyhealthsmoothper)/(0.15/delta_time)
        enemyhealthsmoothper = constrain(enemyhealthsmoothper, 0, 1)
        smoothhealthbarenemy_rect_surface = pygame.Surface((constrain(300*enemyhealthsmoothper, 0, 300)*WindowScale2, 40*WindowScale2), pygame.SRCALPHA)
        smoothhealthbarenemy_rect_surface.fill((int(constrain(math.cos((math.pi/2)*constrain(enemyhealthsmoothper, 0, 1))*256, 0, 255)), int(constrain(math.sin((math.pi/2)*constrain(enemyhealthsmoothper, 0, 1))*256, 0, 255)), 0, 192))  # Fill with white and set alpha to 128 (50% transparent)
        pygame.draw.rect(screen, (0, 0, 0), (10*WindowScale2 + CamPos[0]*WindowXscale, 310*WindowScale2 + CamPos[1]*WindowYscale, 300*WindowScale2, 40*WindowScale2))
        pygame.draw.rect(screen, (constrain(math.cos((math.pi/2)*constrain(float(Decimal(enemy_hp)/Decimal(enemy_max_hp)), 0, 1))*256, 0, 255), constrain(math.sin((math.pi/2)*constrain(float(Decimal(enemy_hp)/Decimal(enemy_max_hp)), 0, 1))*256, 0, 255), 0), (10*WindowScale2 + CamPos[0]*WindowXscale, 310*WindowScale2 + CamPos[1]*WindowYscale, (float(Decimal(enemy_hp)/Decimal(enemy_max_hp)))*300*WindowScale2, 40*WindowScale2))
        screen.blit(smoothhealthbarenemy_rect_surface, (10*WindowScale2 + CamPos[0]*WindowXscale, 310*WindowScale2 + CamPos[1]*WindowYscale))
    def prestige():
        global score, gems, musicplays, musicplays2, enemy_hp, enemy_max_hp, monsterskilled, click_damage
        score = 0
        resetupgrades()
        PlayMusic(random.randint(1,15))
        musicplays = 0
        musicplays2 = 0
        #pygame.mixer.music.set_volume(pygamemixermusic * float(Settings[1]["value"] / 100))
        rl.set_music_volume(music1, pygamemixermusic * float(Settings[1]["value"] / 100))
        rl.set_music_volume(music2, pygamemixermusic * float(Settings[1]["value"] / 100))
        gems += gemstoget
        enemy_hp = Decimal(10)
        monsterskilled = Decimal(0)
        enemy_max_hp = Decimal(10)
        click_damage = Decimal(1)

    # Draw upgrade buttons
    for i, button in enumerate(Settings_buttons):
        setx = Settings_button_x[i] + CamPos[0]*WindowXscale/WindowScale2
        sety = constrain(Settings_button_y[i] + Settings_Button_Y_scroll + Settings_Button_Y_scroll_vel, screen_height*-3, screen_height*0.8) + CamPos[1]*WindowYscale/WindowYscale
        if isinstance(Settings[i]["value"], Decimal):
            if Settings[i]["held"] and Settings[i]["holdable"]:
                if mos_x/WindowXscale <= setx + Settings_button_width[i]/2:
                    Settings[i]["value"] -= Decimal(20*delta_time)
                if mos_x/WindowXscale >= setx + Settings_button_width[i]/2:
                    Settings[i]["value"] += Decimal(20*delta_time)
            Settings[i]["value"] = constrain(Decimal(Settings[i]["value"]), Decimal(Settings[i]["min"]), Decimal(Settings[i]["max"]))
        Settings_buttons[i] = pygame.Rect(setx*WindowXscale, sety*WindowYscale, Settings_button_width[i]*WindowXscale, Settings_button_height[i]*WindowYscale)
        pygame.draw.rect(screen, (SettingsButtonOutlineColorRed[i], SettingsButtonOutlineColorGreen[i], SettingsButtonOutlineColorBlue[i]), (setx*WindowXscale - 5*WindowScale2, sety*WindowYscale - 5*WindowScale2, Settings_button_width[i]*WindowXscale + 10*WindowScale2, Settings_button_height[i]*WindowYscale + 10*WindowScale2), 30)
        pygame.draw.rect(screen, (SettingsButtonColorRed[i], SettingsButtonColorGreen[i], SettingsButtonColorBlue[i]), (Settings_buttons[i]))
        if Settings[i]["round"] and not isinstance(Settings[i]["value"], str):
            if Settings[i]["percent"]:
                draw_text(f"{Settings[i]['name']} - {Decimal.__round__((Settings[i]['value']))}%", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + (Settings_button_height[i]*WindowScale2)/2, "center", 255)
            else:
                draw_text(f"{Settings[i]['name']} - {Decimal.__round__((Settings[i]['value']))}", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + (Settings_button_height[i]*WindowScale2)/2, "center", 255)
        elif Settings[i]["percent"] and not isinstance(Settings[i]["value"], str):
            draw_text(f"{Settings[i]['name']} - {Decimal(Settings[i]['value'])}%", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + (Settings_button_height[i]*WindowScale2)/2, "center", 255)
        elif Settings[i]['value'] != "":
            draw_text(f"{Settings[i]['name']} - {Settings[i]['value']}", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + (Settings_button_height[i]*WindowScale2)/2, "center", 255)
        else:
            draw_text(f"{Settings[i]['name']}", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + (Settings_button_height[i]*WindowScale2)/2, "center", 255)
    #pygame.draw.rect(screen, (30, 30, 30), (900*WindowXscale + CamPos[0]*WindowXscale, WindowHeight*0.35 + CamPos[1]*WindowYscale, 380*WindowXscale, WindowHeight*1))
    for i, button in enumerate(Buy_buttons):
        setx = Buy_button_X[i] + CamPos[0]*WindowXscale/WindowScale2
        sety = Buy_button_Y[i] + CamPos[1]*WindowYscale
        if isinstance(BuyThing[i]["value"], Decimal):
            if BuyThing[i]["held"] and BuyThing[i]["holdable"]:
                if mos_x/WindowXscale <= setx + Buy_button_Width[i]/2:
                    BuyThing[i]["value"] -= Decimal(20*delta_time)
                if mos_x/WindowXscale >= setx + Buy_button_Width[i]/2:
                    BuyThing[i]["value"] += Decimal(20*delta_time)
            BuyThing[i]["value"] = constrain(Decimal(BuyThing[i]["value"]), Decimal(BuyThing[i]["min"]), Decimal(BuyThing[i]["max"]))
        if not bulkbuy == "Max":
            BuyThing[0]["value"] = "X" + str(bulkbuy)
        else:
            BuyThing[0]["value"] = "Max"
        Buy_buttons[i] = pygame.Rect(setx*WindowXscale, sety*WindowYscale, Buy_button_Width[i]*WindowXscale, Buy_button_Height[i]*WindowYscale)
        pygame.draw.rect(screen, (BuyButtonOutlineColorRed[i], BuyButtonOutlineColorGreen[i], BuyButtonOutlineColorBlue[i]), (setx*WindowXscale - 5*WindowScale2, sety*WindowYscale - 5*WindowScale2, Buy_button_Width[i]*WindowXscale + 10*WindowScale2, Buy_button_Height[i]*WindowYscale + 10*WindowScale2), 30)
        pygame.draw.rect(screen, (BuyButtonColorRed[i], BuyButtonColorGreen[i], BuyButtonColorBlue[i]), (Buy_buttons[i]))
        if BuyThing[i]["round"] and not isinstance(BuyThing[i]["value"], str):
            if BuyThing[i]["percent"]:
                draw_text(f"{BuyThing[i]['name']} - {Decimal.__round__((BuyThing[i]['value']))}%", font, WHITE, setx*WindowXscale + Buy_button_Width[i]*WindowXscale/2, sety*WindowYscale + Buy_button_Height[i]*WindowScale2/2, "center", 255)
            else:
                draw_text(f"{BuyThing[i]['name']} - {Decimal.__round__((BuyThing[i]['value']))}", font, WHITE, setx*WindowXscale + Buy_button_Width[i]*WindowXscale/2, sety*WindowYscale + Buy_button_Height[i]*WindowScale2/2, "center", 255)
        elif BuyThing[i]["percent"] and not isinstance(BuyThing[i]["value"], str):
            draw_text(f"{BuyThing[i]['name']} - {Decimal(BuyThing[i]['value'])}%", font, WHITE, setx*WindowXscale + Buy_button_Width[i]*WindowXscale/2, sety*WindowYscale + Buy_button_Height[i]*WindowScale2/2, "center", 255)
        elif BuyThing[i]['value'] != "":
            draw_text(f"{BuyThing[i]['name']} - {BuyThing[i]['value']}", font, WHITE, setx*WindowXscale + Buy_button_Width[i]*WindowXscale/2, sety*WindowYscale + Buy_button_Height[i]*WindowScale2/2, "center", 255)
        else:
            draw_text(f"{BuyThing[i]['name']}", font, WHITE, setx*WindowXscale + Buy_button_Width[i]*WindowXscale/2, sety*WindowYscale + Buy_button_Height[i]*WindowScale2/2, "center", 255)
    #pygame.draw.rect(screen, (30, 30, 30), (900*WindowXscale + CamPos[0]*WindowXscale, WindowHeight*0.35 + CamPos[1]*WindowYscale, 380*WindowXscale, WindowHeight*1))
    #pygame.draw.rect(screen, (30, 30, 30), (900*WindowXscale + CamPos[0]*WindowXscale, WindowHeight*0.0 + CamPos[1]*WindowYscale, 380*WindowXscale, WindowHeight*0.1))
    draw_text(f"Options", pygame.font.Font(resource_path(str(THIS_DIR / "./assets/fonts/Lato/Lato-Bold.ttf")), int(36*WindowScale2)), WHITE, 1920*WindowXscale + CamPos[0]*WindowXscale, 18 * WindowYscale + CamPos[1]*WindowYscale, "center", 255)
    #draw_text(f"Log", pygame.font.Font(resource_path(str(THIS_DIR / "./assets/fonts/Lato/Lato-Bold.ttf")), int(36*WindowScale2)), WHITE, 1110*WindowXscale + CamPos[0]*WindowXscale, 318 * WindowYscale + CamPos[1]*WindowYscale, "center", 255) # IT'S CLONE RIGGY!
    draw_text(f"Upgrades", pygame.font.Font(resource_path(str(THIS_DIR / "./assets/fonts/Lato/Lato-Bold.ttf")), int(36*WindowScale2)), WHITE, 30*WindowXscale + CamPos[0]*WindowXscale, 540 * WindowYscale + CamPos[1]*WindowYscale, "left", 255)
    for i, button in enumerate(upgrade_buttons):
        def calcmax():
            return constrain(Decimal.__floor__( Decimal.log10( (Decimal(score) * (Decimal(upgrades[i]["costcoefficient"]) - 1)) / Decimal(upgrades[i]["startcost"] * (Decimal(upgrades[i]["costcoefficient"]) ** Decimal(upgrades[i]["bought"]))) + 1) / Decimal.log10(Decimal(upgrades[i]["costcoefficient"]))), Decimal(1), math.inf)
        if bulkbuy == "Max":
            upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(calcmax()) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
        elif BuyThing[1]["value"] == "ON":
            upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(Decimal(upgrades[i]["bought"]) - Decimal(upgrades[i]["bought"]) % Decimal(bulkbuy) + Decimal(bulkbuy) - Decimal(upgrades[i]["bought"])) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
        else:
            upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(bulkbuy) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
        upgx = upgrade_button_x[i] + Upgrade_Button_X_scroll + Upgrade_Button_X_scroll_vel + CamPos[0]*WindowXscale/WindowScale2
        upgy = (screen_height - upgrade_button_height[i])*WindowYscale - 20*WindowYscale + CamPos[1]*WindowYscale
        upgrade_buttons[i] = pygame.Rect(upgx*WindowScale2, upgy, upgrade_button_width[i]*WindowScale2, upgrade_button_height[i]*WindowScale2)
        pygame.draw.rect(screen, (UpgradeButtonColorRed[i], UpgradeButtonColorGreen[i], UpgradeButtonColorBlue[i]), (upgx*WindowScale2 - 5*WindowScale2, upgy - 40*WindowScale2, 300*WindowScale2, upgrade_button_height[i]*WindowScale2 - 15*WindowScale2), 30)
        pygame.draw.rect(screen, (UpgradeButtonOutlineColorRed[i], UpgradeButtonOutlineColorGreen[i], UpgradeButtonOutlineColorBlue[i]), (upgx*WindowScale2 - 5*WindowScale2, upgy - 5*WindowScale2, upgrade_button_width[i]*WindowScale2 + 10*WindowScale2, upgrade_button_height[i]*WindowScale2 + 10*WindowScale2), 30)
        pygame.draw.rect(screen, (UpgradeButtonColorRed[i], UpgradeButtonColorGreen[i], UpgradeButtonColorBlue[i]), (upgx*WindowScale2, upgy, upgrade_button_width[i]*WindowScale2, upgrade_button_height[i]*WindowScale2))
        draw_text(f"{upgrades[i]['name']} - {abbreviate(upgrades[i]['cost'], notation, 3, 10000, False)}", font, WHITE, upgx*WindowScale2 + upgrade_button_width[i]*WindowScale2/2, upgy + upgrade_button_height[i]*WindowScale2/2, "center", 255)
        if bulkbuy == "Max":
            draw_text(f"{abbreviate(upgrades[i]["bought"], notation, 3, 1000, True)} + Max ({abbreviate(Decimal(calcmax()), notation, 3, 1000, True)})", font, WHITE, upgx*WindowScale2, upgy - 38*WindowScale2, "left", 255)
        elif BuyThing[1]["value"] == "ON":
            draw_text(f"{abbreviate(upgrades[i]["bought"], notation, 3, 1000, True)} + {Decimal(upgrades[i]["bought"]) - Decimal(upgrades[i]["bought"]) % Decimal(bulkbuy) + Decimal(bulkbuy) - Decimal(upgrades[i]["bought"])}", font, WHITE, upgx*WindowScale2, upgy - 38*WindowScale2, "left", 255)
        else:
            draw_text(f"{abbreviate(upgrades[i]["bought"], notation, 3, 1000, True)} + {bulkbuy}", font, WHITE, upgx*WindowScale2, upgy - 38*WindowScale2, "left", 255)
    def distance_to(ax, ay, bx, by):
        return math.sqrt((ax - bx)**2 + (ay - by)**2)
    """realarrowdownimg1.set_alpha(200 - distance_to(mos_x, mos_y, 1100*WindowXscale + CamPos[0]*WindowXscale, 252*WindowYscale + CamPos[1]*WindowYscale))
    screen.blit(realarrowdownimg1, (1100*WindowXscale + CamPos[0]*WindowXscale, 252*WindowYscale + mos_y/40 + CamPos[1]*WindowYscale))
    realarrowupimg1.set_alpha(200 - distance_to(mos_x, mos_y, 1100*WindowXscale + CamPos[0]*WindowXscale, 34*WindowYscale + CamPos[1]*WindowYscale))
    screen.blit(realarrowupimg1, (1100*WindowXscale + CamPos[0]*WindowXscale, (34*WindowYscale) + mos_y/40 + CamPos[1]*WindowYscale))
"""
    if not isinstance(Settings[1]["value"], str):
        #pygame.mixer.music.set_volume(pygamemixermusic * float(Settings[1]["value"] / 100))
        rl.set_music_volume(music1, pygamemixermusic * float(Settings[1]["value"] / 100))
        rl.set_music_volume(music2, pygamemixermusic * float(Settings[1]["value"] / 100))
    if not isinstance(Settings[0]["value"], str):
        upgrade_sound.set_volume(Decimal(Settings[0]["value"]/100))
        hover_sound.set_volume(Decimal(Settings[0]["value"]/100))
        click_sound.set_volume(Decimal(Settings[0]["value"]/100))

        punch_sound1.set_volume(Decimal(Settings[0]["value"]/365))
        punch_sound2.set_volume(Decimal(Settings[0]["value"]/365))
        punch_sound3.set_volume(Decimal(Settings[0]["value"]/365))
        punch_sound4.set_volume(Decimal(Settings[0]["value"]/365))
        punch_sound_crit1.set_volume(Decimal(Settings[0]["value"]/100))
        punch_sound_crit2.set_volume(Decimal(Settings[0]["value"]/100))
        punch_sound_crit3.set_volume(Decimal(Settings[0]["value"]/100))
        punch_sound_crit4.set_volume(Decimal(Settings[0]["value"]/100))
        punch_sound_death.set_volume(Decimal(Settings[0]["value"]/300))
    if offlineBoxAlpha < 255:
        offlineBoxOutline_rect_surface = pygame.Surface((960*WindowScale2 + 10*WindowXscale, 360*WindowScale2 + 10*WindowYscale), pygame.SRCALPHA)
        offlineBoxOutline_rect_surface.fill((128, 192, 255, offlineBoxAlpha))  # Fill with red and set alpha to 128 (50% transparent)
        screen.blit(offlineBoxOutline_rect_surface, ((635*WindowXscale) - (480*WindowScale2), (355*WindowYscale) - (180*WindowScale2)))
        offlineBox_rect_surface = pygame.Surface((960*WindowScale2, 360*WindowScale2), pygame.SRCALPHA)
        offlineBox_rect_surface.fill((0, 64, 128, offlineBoxAlpha))  # Fill with red and set alpha to 128 (50% transparent)
        screen.blit(offlineBox_rect_surface, ((640*WindowXscale) - (480*WindowScale2), (360*WindowYscale) - (180*WindowScale2)))
        draw_text(f"While you were away for {abbreviate((Decimal(offlineCurrentTime) - Decimal(offlineOldTime)), notation, 3, 10000, False)} seconds,", pygame.font.Font(resource_path(str(THIS_DIR / "./assets/fonts/Lato/Lato-Bold.ttf")), int(30*WindowScale2)), (255, 64, 128, offlineBoxAlpha), 640*WindowXscale, 330*WindowYscale, "center", offlineBoxAlpha)
        draw_text(f"You earned {abbreviate(Decimal(differenceTimeOffline) * Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(gemboost), notation, 3, 100000, False)} points.", pygame.font.Font(resource_path(str(THIS_DIR / "./assets/fonts/Lato/Lato-Bold.ttf")), int(30*WindowScale2)), (255, 64, 128, offlineBoxAlpha), 640*WindowXscale, 390*WindowYscale, "center", offlineBoxAlpha)
    offlineBoxAlpha = constrain(offlineBoxAlpha - 51*delta_time, 0, 255)
    YouWillNotUpgradeUnlessToldTo_Time -= delta_time
    # Update display
    particle1.emit()
    pygame.display.flip()
    #clock.tick(24)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        CamPos2 = [1280, 0]
    if keys[pygame.K_s]:
        CamPos2 = [0, 0]
    if keys[pygame.K_d]:
        CamPos2 = [-1280, 0]
    if keys[pygame.K_q]:
        CamPos2 = [1280, 720]
    if keys[pygame.K_w]:
        CamPos2 = [0, 720]
    if keys[pygame.K_e]:
        CamPos2 = [-1280, 720]
    if keys[pygame.K_z]:
        CamPos2 = [1280, -720]
    if keys[pygame.K_x]:
        CamPos2 = [0, -720]
    if keys[pygame.K_c]:
        CamPos2 = [-1280, -720]
    buttonshake2[0]+=(0-buttonshake2[0])/(0.15/delta_time)
    buttonshake2[1]+=(0-buttonshake2[1])/(0.15/delta_time)
    buttonshake[0] = random.uniform(-buttonshake2[0], buttonshake2[0])
    buttonshake[1] = random.uniform(-buttonshake2[1], buttonshake2[1])
    CamPos = [CamPos[0] + (CamPos2[0]-CamPos[0])/(0.15/delta_time), CamPos[1] + (CamPos2[1]-CamPos[1])/(0.15/delta_time)]
    Settings_button_x = [490 + 1280*WindowXscale/WindowScale2, 490 + 1280*WindowXscale/WindowScale2, 490 + 1280*WindowXscale/WindowScale2, 490 + 1280*WindowXscale/WindowScale2, 490 + 1280*WindowXscale/WindowScale2, 490 + 1280*WindowXscale/WindowScale2, 490 + 1280*WindowXscale/WindowScale2]
    if (rl.get_music_time_played(music1) >= rl.get_music_time_length(music1)-.03) and musicplays2 == 0:
        musicplays2 = 1
    if musicplays >= 0.03:
        rl.stop_music_stream(music1)
        rl.play_music_stream(music2)
        musicplays2 = -1
        musicplays = 0
    musicplays += delta_time*musicplays2*speedmusic
    checkenemyded("wait")
rl.unload_music_stream(music1)
rl.unload_music_stream(music2)
rl.close_audio_device()
# Quit Pygame
pygame.quit()