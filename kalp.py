import tkinter as tk
import math
import random
import time

# 20 farklı dilde seni seviyorum
asklar = [
    "I love you", "Te amo", "Je t'aime", "Ich liebe dich",
    "Ti amo", "Seni seviyorum", "Wo ai ni", "Aishiteru",
    "Saranghae", "Ya tebya lyublyu", "Eu te amo", "Ana bahebik",
    "Mahal kita", "Aku cinta kamu", "S'agapo", "Volim te",
    "Miluji te", "Kocham cie", "Te iubesc", "Ani ohev otach"
]

root = tk.Tk()
root.title("Kalp - 20 Dilde")
root.configure(bg="black")
canvas = tk.Canvas(root, width=800, height=700, bg="black", highlightthickness=0)
canvas.pack()

# Kalp formülü
def kalp_noktasi(t, scale=300):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x * scale/16, -y * scale/16

# Kalp içini dolduracak noktaları oluştur
noktalar = []
for _ in range(600):
    tx = random.uniform(-16, 16)
    ty = random.uniform(-17, 13)
    # Kalp içinde mi kontrolü
    if (tx**2 + ty**2 - 1)**3 - tx**2 * ty**3 <= 0.3:
        x = tx * 18 + 400
        y = -ty * 18 + 320
        noktalar.append((x, y))

random.shuffle(noktalar)

# Animasyonlu yazma
for i, (x, y) in enumerate(noktalar):
    kelime = random.choice(asklar)
    renk = "#ff1a1a" if random.random() > 0.3 else "#ff4d4d"
    size = random.randint(8, 13)
    canvas.create_text(x, y, text=kelime, fill=renk, font=("Arial", size, "bold"))
    if i % 15 == 0:
        root.update()
        time.sleep(0.02)

root.mainloop()
