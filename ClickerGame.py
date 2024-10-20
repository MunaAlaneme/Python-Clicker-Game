# Credits!!!
# Google Bard - Help
# OpenAI ChatGPT - Help
# Microsoft Bing AI Chat Copilot - Help
# (YT) Clear Code - Particle System
# jay3332 - Number Abbreviation
# Cryptogrounds / Considera Core

import pygame
import random
from decimal import *
import math
import sys
import time
import os
import numpy as np
import svg
import datetime
import pickle
import json

GameFPS = 60

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
                pygame.draw.circle(screen, pygame.Color('White'), particle[0], particle[1]*WindowScale2)
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

def abbreviate(number, suffixes, decimals, greaterthan, rounda):
    if number < greaterthan:
        if rounda:
            return round(number)
        else:
            return round(number*(10**decimals))/(10**decimals)
    if fexp(Decimal(number)) < 10002 * 3 and fexp(Decimal(number)) > -1:
        if suffixes == "l":
            return (str(round(fman(Decimal(number)) * (10**(fexp(Decimal(number))%3)) * (10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3)-decimals)))) / 10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals)) + LongSuffixes[Decimal.__floor__(Decimal(fexp(Decimal(number))/3))+0])
        elif suffixes == "s":
            return (str(round(fman(Decimal(number)) * (10**(fexp(Decimal(number))%3)) * (10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals))) / 10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals)) + ShortSuffixes[Decimal.__floor__(Decimal(fexp(Decimal(number))/3))+0])
    elif Decimal.__abs__(Decimal(fexp(Decimal(number)))) < 10**6:
        return (str(round(fman(Decimal(number)), decimals)) + "e" + str(fexp(Decimal(number))))
    elif Decimal.__abs__(Decimal(fexp(Decimal(number)))) < 10**10002 * 3:
        if suffixes == "l":
            return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)*3), 3)) + LongSuffixes[Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)+0])
        elif suffixes == "s":
            return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)*3), 3)) + ShortSuffixes[Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)+0])
    else:
        return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number))))))), 3)) + "e" + Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))))

# Screen and clock
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Clicker Game")
clock = pygame.time.Clock()

particle1 = ParticlePrinciple()

PARTICLE_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(PARTICLE_EVENT, 20)

# Font
font = pygame.font.Font("./assets/fonts/Lato/Lato-Bold.ttf", 24)

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
upgrades = [
    {"num": 1,
    "name": "+1 Per Click",
    "cost": Decimal(0),
    "startcost": Decimal(40/1.1),
    "costcoefficient": Decimal(1.1),
    "bought": Decimal(1)},
    {"num": 2,
    "name": "Auto Clicker +0.1",
    "cost": Decimal(0),
    "startcost": Decimal(80),
    "costcoefficient": Decimal(1.1),
    "bought": Decimal(0)},
    {"num": 3,
    "name": "Auto Click Rate +0.1",
    "cost": Decimal(0),
    "startcost": Decimal(500),
    "costcoefficient": Decimal(1.1),
    "bought": Decimal(0)},
    {"num": 4,
    "name": "Double Clicks (X2)",
    "cost": Decimal(0),
    "startcost": Decimal(10000),
    "costcoefficient": Decimal(7),
    "bought": Decimal(0)},
    {"num": 5,
    "name": "Auto Clicker +1",
    "cost": Decimal(0),
    "startcost": Decimal(1200),
    "costcoefficient": Decimal(1.07),
    "bought": Decimal(0)},
    {"num": 6,
    "name": "Double Click Rate (X2)",
    "cost": Decimal(0),
    "startcost": Decimal(35000),
    "costcoefficient": Decimal(9),
    "bought": Decimal(0)},
    {"num": 7,
    "name": "Auto Clicker +10",
    "cost": Decimal(0),
    "startcost": Decimal(18000),
    "costcoefficient": Decimal(1.07),
    "bought": Decimal(0)},
    {"num": 8,
    "name": "+10 Per Click",
    "cost": Decimal(0),
    "startcost": Decimal(1000),
    "costcoefficient": Decimal(1.06),
    "bought": Decimal(0)},
    {"num": 9,
    "name": "Triple Click Rate (X3)",
    "cost": Decimal(0),
    "startcost": Decimal(500000),
    "costcoefficient": Decimal(15),
    "bought": Decimal(0)},
    {"num": 10,
    "name": "+1% CPS per click",
    "cost": Decimal(0),
    "startcost": Decimal(1000000),
    "costcoefficient": Decimal(5),
    "bought": Decimal(0)},
]
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
    "value": Decimal(0),
    "percent": True,
    "round": True,
    "holdable": True,
    "held": False,
    "min": Decimal(0),
    "max": Decimal(100)},
    {"num": 3,
    "name": "Bulk Buy",
    "value": "X1",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
    {"num": 4,
    "name": "OCD Buy",
    "value": "OFF",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
    {"num": 5,
    "name": "Save Game",
    "value": "",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
    {"num": 6,
    "name": "Load Game",
    "value": "",
    "percent": False,
    "round": False,
    "holdable": False,
    "held": False,
    "min": "",
    "max": ""},
]
Settings_buttons = []
Settings_button_width = [300, 300, 300, 300, 300, 300]
Settings_button_height = [50, 50, 50, 50, 50, 50]
Settings_button_x = [960, 960, 960, 960, 960, 960]
Settings_button_y = [70, 140, 210, 280, 350, 420, 490]
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
Settings_Button_Y_scroll = 0
Settings_Button_Y_scroll_vel = 0
# Clicker button
clicker_button_image = pygame.image.load("./assets/img/copilot.png").convert_alpha()
# clicker_button_rect = clicker_button_image.get_rect(center=(screen_width // 2, screen_height // 2))
arrow_down_img1 = pygame.image.load("./assets/img/Arrow1-c.png").convert_alpha()
arrow_up_img1 = pygame.image.load("./assets/img/Arrow1-d.png").convert_alpha()

# Upgrade button setup
for i, upgrade in enumerate(upgrades):
    x = upgrade_button_x[i]
    y = screen_height - upgrade_button_height[i] - 20
    upgrade_buttons.append(pygame.Rect(x, y, upgrade_button_width[i], upgrade_button_height[i]))
for i, setting in enumerate(Settings):
    Settings_buttons.append(pygame.Rect(Settings_button_x[i], Settings_button_y[i], Settings_button_width[i], Settings_button_height[i]))


# Game loop
running = True
frames = 0
scale_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scale_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target_scale_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target_scale_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
start_time = time.time()
delta_time = 0.000001
game_time = -0.000001
GameFPS = 1/delta_time
bulkbuy = 1
gems = Decimal(0)
upgradeableButtons = True
SettingsButtonsFixed = True
upbuttempvar1 = 0
def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

pygame.mixer.init()
pygamemixermusic = 1
def PlayMusic(musNum):
    global pygamemixermusic
    pygamemixermusic = 1
    if musNum == 1:
        pygamemixermusic = 0.25
        pygame.mixer.music.load("./assets/audio/Debug Menu Unused   Paper Mario  The Thousand Year Door.wav")
    elif musNum == 2:
        pygamemixermusic = 1
        pygame.mixer.music.load("./assets/audio/SpongeBob SquarePants OST - Dombummel (LQ).wav")
    elif musNum == 3:
        pygamemixermusic = 0.7
        pygame.mixer.music.load("./assets/audio/Kevin MacLeod - Hep Cats.mp3")
    elif musNum == 4:
        pygamemixermusic = 1
        pygame.mixer.music.load("./assets/audio/(Object Break) Kevin MacLeod - Padanaya Blokov - loop.wav")
    pygame.mixer.music.set_volume(Decimal(pygamemixermusic))
    pygame.mixer.music.play(loops=-1)
PlayMusic(random.randint(1,4))
if SettingsButtonsFixed:
    pygame.mixer.music.set_volume(Decimal(pygamemixermusic) * (Settings[1]["value"] / 100))

click_sound = pygame.mixer.Sound("./assets/audio/Click mouse - Fugitive Simulator - The-Nick-of-Time.wav")
hover_sound = pygame.mixer.Sound("./assets/audio/251389__deadsillyrabbit__button_hover-wav.wav")
upgrade_sound = pygame.mixer.Sound("./assets/audio/Upgrade SOund 0001.wav")

Hovering_Buttons = [0,0,0,0,0,0,0,0,0,0]
def save_game():
    with open('./save/gamesaveSettings.txt', 'w') as file1:
        file1.write(str(Settings))
    with open('./save/gamesaveUpgrades.txt', 'w') as file2:
        file2.write(str(upgrades))
    with open('./save/gamesaveGems.txt', 'w') as file3:
        file3.write(str(gems))
    with open('./save/gamesaveScore.txt', 'w') as file4:
        file4.write(str(score))
def load_game():
    global Settings, upgrades, gems, score, upgradeableButtons, SettingsButtonsFixed
    upgradeableButtons = False
    SettingsButtonsFixed = False
    with open('./save/gamesaveSettings.txt', 'r') as file5:
        leng = len(file5.read())
        Settings = file5.read()
    with open('./save/gamesaveUpgrades.txt', 'r') as file6:
        leng = len(file6.read())
        upgrades = file6.read()
    with open('./save/gamesaveGems.txt', 'r') as file7:
        gems = Decimal(file7.read())
    with open('./save/gamesaveScore.txt', 'r') as file8:
        score = Decimal(file8.read())
while running:
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
        if mos_x > WindowWidth/1.1:
            Upgrade_Button_X_scroll_vel -= 60*delta_time
        elif mos_x < WindowWidth - WindowWidth/1.1:
            Upgrade_Button_X_scroll_vel += 60*delta_time
    if mos_y > WindowHeight*0.35 and mos_x > WindowWidth*.75 and mos_y < WindowHeight*0.5:
        Settings_Button_Y_scroll_vel -= 60*delta_time
    elif mos_y < WindowHeight*0.1 and mos_x > WindowWidth*.75:
        Settings_Button_Y_scroll_vel += 60*delta_time

    Upgrade_Button_X_scroll = constrain(Upgrade_Button_X_scroll+Upgrade_Button_X_scroll_vel, screen_width*-2.5, 0)
    Upgrade_Button_X_scroll_vel /= 1.1
    for i, upgrade in enumerate(upgrades):
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
    Settings_Button_Y_scroll = constrain(Settings_Button_Y_scroll+Settings_Button_Y_scroll_vel, screen_height*-.45, screen_height*0.05)
    Settings_Button_Y_scroll_vel /= 1.1
    for i, setting in enumerate(Settings):
        x = Settings_button_x[i]
        y = Settings_button_y[i] + Settings_Button_Y_scroll + Settings_Button_Y_scroll_vel
        Settings_buttons[i] = pygame.Rect(x*WindowScale2, y*WindowYscale, Settings_button_width[i]*WindowScale2, Settings_button_height[i]*WindowScale2)
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
    x_inside = [0,0,0,0,0,0,0,0,0,0]
    y_inside = [0,0,0,0,0,0,0,0,0,0]
    button_rect_x = [(WindowWidth/1) // 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    button_rect_y = [((WindowHeight/1) // 2) + (math.sin(game_time*5)) * 30 * WindowScale2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # clicker_button_rect = clicker_button_image.get_rect(center=(scale_x[0], scale_y[0]))
    mos_x, mos_y = pygame.mouse.get_pos()
    target_scale_x[0] = 500
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
                target_scale_x[0] = 550
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        target_scale_x[0] = 450
                        scale_x[0] = constrain(scale_x[0]-40, 200, math.inf)
                        score += Decimal(click_value)*Decimal(random.uniform(0.95, 1.05))*Decimal(click_value_multi)*Decimal(gemboost) + Decimal(cps_to_cpc)*Decimal(auto_click_value)*Decimal(auto_click_rate)*Decimal(gemboost)
                        click_sound.play()
                        for i in range(10):
                            particle1.add_particles(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, random.randrange(-180, 180), 4)
            elif button_i == 1:
                pass
        else:
            Hovering_Buttons[button_i] = 0
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for i, button in enumerate(upgrade_buttons):
            if button.collidepoint(pygame.mouse.get_pos()):
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
        for i, button in enumerate(Settings_buttons):
            if button.collidepoint(pygame.mouse.get_pos()):
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
        if event.type == pygame.MOUSEBUTTONUP:
            if SettingsButtonsFixed:
                for i, button in enumerate(Settings_buttons):
                    Settings[i]["held"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(upgrade_buttons):
                if button.collidepoint(event.pos):
                    UpgradeTargetButtonColorRed[i] = 150
                    UpgradeTargetButtonColorGreen[i] = 75
                    UpgradeTargetButtonColorBlue[i] = 0
                    UpgradeTargetButtonOutlineColorRed[i] = 0
                    UpgradeTargetButtonOutlineColorGreen[i] = 128
                    UpgradeTargetButtonOutlineColorBlue[i] = 255
                    if Decimal(score) >= Decimal(upgrades[i]["cost"]) and upgradeableButtons and SettingsButtonsFixed:
                        if bulkbuy == "Max":
                            buy00001 = Decimal(calcmax())
                        elif Settings[3]["value"] == "ON":
                            buy00001 = Decimal(upgrades[i]["bought"]) - Decimal(upgrades[i]["bought"]) % Decimal(bulkbuy) + Decimal(bulkbuy) - Decimal(upgrades[i]["bought"])
                        else: buy00001 = Decimal(bulkbuy)
                        score -= Decimal(upgrades[i]["cost"])
                        upgrades[i]["bought"] += Decimal(buy00001)
                        upgrade_sound.stop()
                        upgrade_sound.play()
                        click_sound.play()
            for i, button in enumerate(Settings_buttons):
                if button.collidepoint(event.pos):
                    if SettingsButtonsFixed:
                        click_sound.play()
                        SettingsTargetButtonColorRed[i] = 150
                        SettingsTargetButtonColorGreen[i] = 75
                        SettingsTargetButtonColorBlue[i] = 0
                        SettingsTargetButtonOutlineColorRed[i] = 0
                        SettingsTargetButtonOutlineColorGreen[i] = 128
                        SettingsTargetButtonOutlineColorBlue[i] = 255
                        Settings[i]["held"] = True
                        if i == 2:
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
                        if i == 3:
                            if Settings[3]["value"] == "OFF":
                                Settings[3]["value"] = "ON"
                            elif Settings[3]["value"] == "ON":
                                Settings[3]["value"] = "OFF"
                        if i == 4:
                            save_game()
                        if i == 5:
                            load_game()
    scale_x[0] += (target_scale_x[0]-scale_x[0])/(0.15/delta_time)
    scale_y[0] = scale_x[0]
    smalclicrimg = pygame.transform.scale(clicker_button_image, (constrain(scale_x[0]*WindowScale2, 1, math.inf), constrain(scale_y[0]*WindowScale2, 1, math.inf)))
    realarrowdownimg1 = pygame.transform.scale(arrow_down_img1, (32 * WindowScale2, 32 * WindowScale2))
    realarrowupimg1 = pygame.transform.scale(arrow_up_img1, (32 * WindowScale2, 32 * WindowScale2))
    # Update auto click
    if upgradeableButtons:
        click_value = Decimal(upgrades[0]["bought"]) + (Decimal(upgrades[7]["bought"])*Decimal(10))
        auto_click_value = (Decimal(upgrades[1]["bought"])*Decimal(0.1)) + Decimal(upgrades[4]["bought"]) + (Decimal(upgrades[6]["bought"])*Decimal(10))
        cps_to_cpc = (Decimal(upgrades[9]["bought"])*Decimal(0.01))
        auto_click_rate = (Decimal(upgrades[2]["bought"])*Decimal(0.1)) * (Decimal(2)**Decimal(upgrades[5]["bought"])) * (Decimal(3)**Decimal(upgrades[8]["bought"]))
        click_value_multi = (Decimal(2)**Decimal(upgrades[3]["bought"]))
        score += Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(delta_time) * Decimal(gemboost)


    # Draw screen
    screen.fill((30, 30, 30))
    screen.blit(smalclicrimg, (button_rect_x[0]-(scale_x[0]/2)*WindowScale2, button_rect_y[0]-(scale_y[0]/2)*WindowScale2))
    # Draw text
    font = pygame.font.Font("./assets/fonts/Lato/Lato-Bold.ttf", int(24*WindowScale2))
    def draw_text(text, font, color, x, y, align):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "left":
            screen.blit(text_surface, (x, y))
        elif align == "center":
            text_rect.center = (x, y)
            screen.blit(text_surface, text_rect)
    draw_text(f"Clicks: {abbreviate(score, "s", 3, 100000, False)}", font, WHITE, 10*WindowScale2, 10*WindowScale2, "left")
    draw_text(f"Clicks Per Click: {abbreviate(click_value + cps_to_cpc*auto_click_value*auto_click_rate, "s", 3, 100000, False)}", font, WHITE, 10*WindowScale2, 40*WindowScale2, "left")
    draw_text(f"Click Value Multiplier: x{abbreviate(click_value_multi, "s", 3, 100000, False)}", font, WHITE, 10*WindowScale2, 70*WindowScale2, "left")
    draw_text(f"Clicks Per Second: {abbreviate(auto_click_value, "s", 3, 100000, False)}/s", font, WHITE, 10*WindowScale2, 100*WindowScale2, "left")
    if delta_time > 0:
        draw_text(f"FPS: {Decimal(1/delta_time):.2f}", font, WHITE, 10*WindowScale2, 130*WindowScale2, "left")
    else:
        draw_text(f"FPS: INFINITY", font, WHITE, 10*WindowScale2, 130*WindowScale2, "left")
    draw_text(f"Seconds Per Second: {abbreviate(auto_click_rate, "s", 3, 1000, False)}/s", font, WHITE, 10*WindowScale2, 160*WindowScale2, "left")
    draw_text(f"Gems: {abbreviate(gems, "s", 3, 100000, True)}, {abbreviate(Decimal(gemboost), "s", 3, 100000, False)}x boost", font, WHITE, 10*WindowScale2, 190*WindowScale2, "left")
    draw_text(f"Total Clicks Per Second: {abbreviate(auto_click_value * auto_click_rate, "s", 3, 1000, False)}/s", font, WHITE, 10*WindowScale2, 220*WindowScale2, "left")
    draw_text(f"Total Clicks Per Click: {abbreviate((click_value*click_value_multi + cps_to_cpc*auto_click_value*auto_click_rate)*gemboost, "s", 3, 100000, False)}", font, WHITE, 10*WindowScale2, 250*WindowScale2, "left")

    # Draw upgrade buttons
    if SettingsButtonsFixed:
        for i, button in enumerate(Settings_buttons):
            setx = Settings_button_x[i]
            sety = constrain(Settings_button_y[i] + Settings_Button_Y_scroll + Settings_Button_Y_scroll_vel, screen_height*-0.04, screen_height*0.5)
            if isinstance(Settings[i]["value"], Decimal):
                if Settings[i]["held"] and Settings[i]["holdable"]:
                    if mos_x/WindowXscale <= setx + Settings_button_width[i]/2:
                        Settings[i]["value"] -= Decimal(20*delta_time)
                    if mos_x/WindowXscale >= setx + Settings_button_width[i]/2:
                        Settings[i]["value"] += Decimal(20*delta_time)
                Settings[i]["value"] = constrain(Decimal(Settings[i]["value"]), Decimal(Settings[i]["min"]), Decimal(Settings[i]["max"]))
            if not bulkbuy == "Max": Settings[2]["value"] = "X" + str(bulkbuy)
            else: Settings[2]["value"] = "Max"
            Settings_buttons[i] = pygame.Rect(setx*WindowXscale, sety*WindowYscale, Settings_button_width[i]*WindowXscale, Settings_button_height[i]*WindowScale2)
            pygame.draw.rect(screen, (SettingsButtonOutlineColorRed[i], SettingsButtonOutlineColorGreen[i], SettingsButtonOutlineColorBlue[i]), (setx*WindowXscale - 5*WindowScale2, sety*WindowYscale - 5*WindowScale2, Settings_button_width[i]*WindowXscale + 10*WindowScale2, Settings_button_height[i]*WindowScale2 + 10*WindowScale2), 30)
            pygame.draw.rect(screen, (SettingsButtonColorRed[i], SettingsButtonColorGreen[i], SettingsButtonColorBlue[i]), (setx*WindowXscale, sety*WindowYscale, Settings_button_width[i]*WindowXscale, Settings_button_height[i]*WindowScale2))
            if Settings[i]["round"]:
                if Settings[i]["percent"]:
                    draw_text(f"{Settings[i]['name']} - {Decimal(round(Settings[i]['value']))}%", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + Settings_button_height[i]*WindowScale2/2, "center")
                else:
                    draw_text(f"{Settings[i]['name']} - {Decimal(round(Settings[i]['value']))}", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + Settings_button_height[i]*WindowScale2/2, "center")
            elif Settings[i]["percent"]:
                draw_text(f"{Settings[i]['name']} - {Decimal(Settings[i]['value'])}%", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + Settings_button_height[i]*WindowScale2/2, "center")
            elif Settings[i]['value'] != "":
                draw_text(f"{Settings[i]['name']} - {Settings[i]['value']}", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + Settings_button_height[i]*WindowScale2/2, "center")
            else:
                draw_text(f"{Settings[i]['name']}", font, WHITE, setx*WindowXscale + Settings_button_width[i]*WindowXscale/2, sety*WindowYscale + Settings_button_height[i]*WindowScale2/2, "center")
    pygame.draw.rect(screen, (30, 30, 30), (900*WindowXscale, WindowHeight*0.35, 380*WindowXscale, WindowHeight*1))
    pygame.draw.rect(screen, (30, 30, 30), (900*WindowXscale, WindowHeight*0.0, 380*WindowXscale, WindowHeight*0.1))
    draw_text(f"Options", pygame.font.Font("./assets/fonts/Lato/Lato-Bold.ttf", int(36*WindowScale2)), WHITE, 1110*WindowXscale, 18 * WindowYscale, "center")
    draw_text(f"Upgrades", pygame.font.Font("./assets/fonts/Lato/Lato-Bold.ttf", int(36*WindowScale2)), WHITE, 30*WindowXscale, 540 * WindowYscale, "left")
    if upgradeableButtons and SettingsButtonsFixed:
        for i, button in enumerate(upgrade_buttons):
            def calcmax():
                return constrain(Decimal.__floor__( Decimal.log10( (Decimal(score) * (Decimal(upgrades[i]["costcoefficient"]) - 1)) / Decimal(upgrades[i]["startcost"] * (Decimal(upgrades[i]["costcoefficient"]) ** Decimal(upgrades[i]["bought"]))) + 1) / Decimal.log10(Decimal(upgrades[i]["costcoefficient"]))), Decimal(1), math.inf)
            if bulkbuy == "Max":
                upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(calcmax()) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
            elif Settings[3]["value"] == "ON":
                upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(Decimal(upgrades[i]["bought"]) - Decimal(upgrades[i]["bought"]) % Decimal(bulkbuy) + Decimal(bulkbuy) - Decimal(upgrades[i]["bought"])) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
            else:
                upgrades[i]["cost"] = Decimal(upgrades[i]["startcost"]) * (((Decimal(upgrades[i]["costcoefficient"])**Decimal(upgrades[i]["bought"])) * (Decimal(upgrades[i]["costcoefficient"])**Decimal(bulkbuy) - Decimal(1))) / (Decimal(upgrades[i]["costcoefficient"])-Decimal(1)))
            upgx = upgrade_button_x[i] + Upgrade_Button_X_scroll + Upgrade_Button_X_scroll_vel
            upgy = (screen_height - upgrade_button_height[i]) - 20
            upgrade_buttons[i] = pygame.Rect(upgx*WindowScale2, upgy*WindowYscale, upgrade_button_width[i]*WindowScale2, upgrade_button_height[i]*WindowScale2)
            pygame.draw.rect(screen, (UpgradeButtonColorRed[i], UpgradeButtonColorGreen[i], UpgradeButtonColorBlue[i]), (upgx*WindowScale2 - 5*WindowScale2, upgy*WindowYscale - 40*WindowScale2, 200*WindowScale2, upgrade_button_height[i]*WindowScale2 - 15*WindowScale2), 30)
            pygame.draw.rect(screen, (UpgradeButtonOutlineColorRed[i], UpgradeButtonOutlineColorGreen[i], UpgradeButtonOutlineColorBlue[i]), (upgx*WindowScale2 - 5*WindowScale2, upgy*WindowYscale - 5*WindowScale2, upgrade_button_width[i]*WindowScale2 + 10*WindowScale2, upgrade_button_height[i]*WindowScale2 + 10*WindowScale2), 30)
            pygame.draw.rect(screen, (UpgradeButtonColorRed[i], UpgradeButtonColorGreen[i], UpgradeButtonColorBlue[i]), button)
            draw_text(f"{upgrades[i]['name']} - {abbreviate(upgrades[i]['cost'], "s", 3, 10000, False)}", font, WHITE, upgx*WindowScale2 + upgrade_button_width[i]*WindowScale2/2, upgy*WindowYscale + upgrade_button_height[i]*WindowScale2/2, "center")
            if bulkbuy == "Max":
                draw_text(f"{abbreviate(upgrades[i]["bought"], "s", 3, 100000, True)} + Max ({Decimal(calcmax())})", font, WHITE, upgx*WindowScale2, upgy*WindowYscale - 38*WindowScale2, "left")
            elif Settings[3]["value"] == "ON":
                draw_text(f"{abbreviate(upgrades[i]["bought"], "s", 3, 100000, True)} + {Decimal(upgrades[i]["bought"]) - Decimal(upgrades[i]["bought"]) % Decimal(bulkbuy) + Decimal(bulkbuy) - Decimal(upgrades[i]["bought"])}", font, WHITE, upgx*WindowScale2, upgy*WindowYscale - 38*WindowScale2, "left")
            else:
                draw_text(f"{abbreviate(upgrades[i]["bought"], "s", 3, 100000, True)} + {bulkbuy}", font, WHITE, upgx*WindowScale2, upgy*WindowYscale - 38*WindowScale2, "left")
    def distance_to(ax, ay, bx, by):
        return math.sqrt((ax - bx)**2 + (ay - by)**2)
    realarrowdownimg1.set_alpha(200 - distance_to(mos_x, mos_y, 1100*WindowXscale, 252*WindowYscale))
    screen.blit(realarrowdownimg1, (1100*WindowXscale, 252*WindowYscale))
    realarrowupimg1.set_alpha(200 - distance_to(mos_x, mos_y, 1100*WindowXscale, 36*WindowYscale))
    screen.blit(realarrowupimg1, (1100*WindowXscale, 36*WindowYscale))

    if SettingsButtonsFixed:
        pygame.mixer.music.set_volume(Decimal(pygamemixermusic) * (Settings[1]["value"] / 100))
        upgrade_sound.set_volume(Settings[0]["value"]/100)
        hover_sound.set_volume(Settings[0]["value"]/100)
        click_sound.set_volume(Settings[0]["value"]/100)

    # Update display
    particle1.emit()
    pygame.display.flip()
    pygame.display.update()
    if upgradeableButtons == False:
        upbuttempvar1 += delta_time
    else:
        upbuttempvar1 = 0
    if upbuttempvar1 >= 0.25:
        upgradeableButtons = False
        print(upgrades)

    #SettingsButtonsFixed = True
    #clock.tick(24)

# Quit Pygame
pygame.quit()
