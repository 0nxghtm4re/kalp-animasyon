import tkinter as tk
import math
import random
import time

# ==========================================================
# 20 Dilde "Seni Seviyorum" - Alttan Üste Dolan Kalp
# ==========================================================

LOVE_TEXTS = [
    "I love you",
    "Te amo",
    "Je t'aime",
    "Ich liebe dich",
    "Ti amo",
    "Seni seviyorum",
    "Wo ai ni",
    "Aishiteru",
    "Saranghae",
    "Ya tebya lyublyu",
    "Eu te amo",
    "Ana bahebik",
    "Mahal kita",
    "Aku cinta kamu",
    "S'agapo",
    "Volim te",
    "Miluji te",
    "Kocham cie",
    "Te iubesc",
    "Ani ohev otach"
]

EXTENDED_TEXTS = LOVE_TEXTS * 25
random.shuffle(EXTENDED_TEXTS)

class HeartBottomToTop:
    def __init__(self, root):
        self.root = root
        self.root.title("I love you in 20 languages")
        self.root.configure(bg="black")
        self.width = 900
        self.height = 800
        self.center_x = self.width // 2
        self.center_y = self.height // 2 + 20
        
        self.canvas = tk.Canvas(
            root, 
            width=self.width, 
            height=self.height, 
            bg="black", 
            highlightthickness=0
        )
        self.canvas.pack()

        self.scale = 22
        self.points = []
        self.text_items = []
        self.index = 0
        
        self.colors = ["#ff0000", "#ff1a1a", "#ff3333", "#cc0000", "#ff4d4d", "#e60000"]
        
        self.generate_fill_points()
        self.animate()

    def heart_equation(self, t):
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        return x, y

    def is_inside_heart(self, x, y):
        nx = x / 16.0
        ny = y / 13.0
        return (nx**2 + ny**2 - 1)**3 - nx**2 * ny**3 < 0.05

    def generate_fill_points(self):
        points = []
        attempts = 0
        while len(points) < 500 and attempts < 15000:
            attempts += 1
            r = random.random()
            theta = random.uniform(0, 2 * math.pi)
            radius = r * 16
            x = radius * math.cos(theta)
            y = radius * math.sin(theta) * 1.1
            y = y + random.uniform(-1, 1)
            
            if self.is_inside_heart(x, y):
                points.append((x, y))

        # === EN ÖNEMLİ KISIM: Alttan üste sıralama ===
        # y değeri en küçük olan kalp ucunun en altıdır
        # Bu yüzden y'ye göre sıralıyoruz
        points.sort(key=lambda p: p[1])

        self.points = points

    def get_position_on_canvas(self, x, y):
        s = self.scale
        cx = x * s + self.center_x
        cy = -y * s + self.center_y
        return cx, cy

    def draw_single_text(self):
        if self.index >= len(self.points):
            return False

        x, y = self.points[self.index]
        cx, cy = self.get_position_on_canvas(x, y)
        
        text = EXTENDED_TEXTS[self.index % len(EXTENDED_TEXTS)]
        
        dist = math.sqrt(x*x + y*y)
        if dist < 5:
            font_size = random.randint(11, 14)
            font_weight = "bold"
        else:
            font_size = random.randint(8, 11)
            font_weight = "normal"

        color = random.choice(self.colors)
        
        # gölge
        self.canvas.create_text(
            cx+1, cy+1, 
            text=text, 
            fill="#330000", 
            font=("Consolas", font_size, font_weight)
        )
        
        item = self.canvas.create_text(
            cx, cy, 
            text=text, 
            fill=color, 
            font=("Consolas", font_size, font_weight)
        )
        
        self.text_items.append(item)
        self.index += 1
        return True

    def animate(self):
        # Yavaş yavaş yazsın diye batch küçük
        batch = 2
        
        for _ in range(batch):
            if not self.draw_single_text():
                break

        if self.index < len(self.points):
            self.root.after(35, self.animate)
        else:
            # Bittiğinde sabit kalsın
            print("Kalp doldu!")

def main():
    root = tk.Tk()
    root.geometry("900x800+100+20")
    app = HeartBottomToTop(root)

    def on_close():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
    main()
