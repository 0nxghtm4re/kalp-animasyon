import tkinter as tk
import math
import random

# 20 dil
LOVE = [
    "I love you", "Te amo", "Je t'aime", "Ich liebe dich", "Ti amo",
    "Seni seviyorum", "Wo ai ni", "Aishiteru", "Saranghae", "Ya tebya lyublyu",
    "Eu te amo", "Ana bahebik", "Mahal kita", "Aku cinta kamu", "S'agapo",
    "Volim te", "Miluji te", "Kocham cie", "Te iubesc", "Ani ohev otach"
]

root = tk.Tk()
root.configure(bg="black")
root.geometry("900x800")
canvas = tk.Canvas(root, width=900, height=800, bg="black", highlightthickness=0)
canvas.pack()

# Ayarlar
center_x = 450
center_y = 420
scale = 22
colors = ["#ff0000", "#ff1a1a", "#ff3333", "#e60000", "#ff4d4d"]

def is_inside(x, y):
    nx = x / 16.0
    ny = y / 13.0
    return (nx**2 + ny**2 - 1)**3 - nx**2 * ny**3 < 0.05

# Noktaları oluştur
points = []
while len(points) < 450:
    r = random.random() * 16
    theta = random.uniform(0, 2*math.pi)
    x = r * math.cos(theta)
    y = r * math.sin(theta) * 1.1
    if is_inside(x, y):
        points.append((x, y))

# ALTTAN ÜSTE SIRALA - en alttan başlasın
points.sort(key=lambda p: p[1])

# Direkt çiz
for i, (x, y) in enumerate(points):
    cx = x * scale + center_x
    cy = -y * scale + center_y
    text = random.choice(LOVE)
    color = random.choice(colors)
    
    if abs(x) < 4 and abs(y) < 4:
        size = random.randint(11, 13)
    else:
        size = random.randint(8, 11)

    # gölge
    canvas.create_text(cx+1, cy+1, text=text, fill="#330000", font=("Consolas", size, "bold"))
    canvas.create_text(cx, cy, text=text, fill=color, font=("Consolas", size, "bold"))

root.mainloop()
