import tkinter as tk
import math
import random
import time

# ==========================================================
# 20 Dilde "Seni Seviyorum" - Atan Kalp Animasyonu
# github.com/0nxghtmr4e/kalp-animasyon
# ==========================================================

LOVE_TEXTS = [
    "I love you",          # İngilizce
    "Te amo",              # İspanyolca
    "Je t'aime",           # Fransızca
    "Ich liebe dich",      # Almanca
    "Ti amo",              # İtalyanca
    "Seni seviyorum",      # Türkçe
    "Wo ai ni",            # Çince
    "Aishiteru",           # Japonca
    "Saranghae",           # Korece
    "Ya tebya lyublyu",    # Rusça
    "Eu te amo",           # Portekizce
    "Ana bahebik",         # Arapça
    "Mahal kita",          # Filipince
    "Aku cinta kamu",      # Endonezce
    "S'agapo",             # Yunanca
    "Volim te",            # Sırpça/Hırvatça
    "Miluji te",           # Çekçe
    "Kocham cie",          # Lehçe
    "Te iubesc",           # Rumence
    "Ani ohev otach"       # İbranice
]

# Tekrar çoğalt kalp dolu görünsün
EXTENDED_TEXTS = LOVE_TEXTS * 25
random.shuffle(EXTENDED_TEXTS)

class BeatingHeart:
    def __init__(self, root):
        self.root = root
        self.root.title("I love you in 20 languages")
        self.root.configure(bg="black")
        self.width = 900
        self.height = 800
        self.center_x = self.width // 2
        self.center_y = self.height // 2 - 20
        
        self.canvas = tk.Canvas(
            root, 
            width=self.width, 
            height=self.height, 
            bg="black", 
            highlightthickness=0
        )
        self.canvas.pack()

        self.scale = 22
        self.beat_scale = 1.0
        self.beat_direction = 1
        self.points = []
        self.text_items = []
        self.index = 0
        
        self.colors = ["#ff0000", "#ff1a1a", "#ff3333", "#cc0000", "#ff4d4d", "#e60000"]
        
        self.generate_heart_outline()
        self.generate_fill_points()
        self.animate()

    def heart_equation(self, t):
        """Klasik kalp formülü"""
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        return x, y

    def is_inside_heart(self, x, y):
        """Nokta kalbin içinde mi?"""
        # Normalize
        nx = x / 16.0
        ny = y / 13.0
        # (x^2 + y^2 -1)^3 - x^2 y^3 < 0
        return (nx**2 + ny**2 - 1)**3 - nx**2 * ny**3 < 0.05

    def generate_heart_outline(self):
        """Kalp dış çizgisi için noktalar"""
        self.outline = []
        for i in range(0, 360, 2):
            t = math.radians(i)
            x, y = self.heart_equation(t)
            self.outline.append((x, y))

    def generate_fill_points(self):
        """Kalp içini dolduracak rastgele noktalar - spiral dağıtım"""
        points = []
        attempts = 0
        while len(points) < 500 and attempts < 10000:
            attempts += 1
            # Daha çok merkeze yakın nokta
            r = random.random()
            theta = random.uniform(0, 2 * math.pi)
            
            # Spiral mantığı
            radius = r * 16
            
            x = radius * math.cos(theta)
            y = radius * math.sin(theta) * 1.1
            
            # Y eksenini biraz yukarı kaydır
            y = y + random.uniform(-1, 1)
            
            if self.is_inside_heart(x, y):
                # Kenara yakın olanları biraz daha çoğalt
                if abs(x) > 5 or y < -2:
                    if random.random() > 0.3:
                        points.append((x, y))
                else:
                    points.append((x, y))

        # Kenar detayları için outline'dan da ekle
        for x, y in self.outline[::3]:
            if random.random() > 0.4:
                points.append((x * 0.95, y * 0.95))

        random.shuffle(points)
        self.points = points

    def get_position_on_canvas(self, x, y):
        """Matematiksel noktayı canvas koordinatına çevir, atma efekti ile"""
        s = self.scale * self.beat_scale
        cx = x * s + self.center_x
        cy = -y * s + self.center_y
        return cx, cy

    def draw_single_text(self):
        """Tek bir 'seni seviyorum' yaz"""
        if self.index >= len(self.points):
            return False

        x, y = self.points[self.index]
        cx, cy = self.get_position_on_canvas(x, y)
        
        text = EXTENDED_TEXTS[self.index % len(EXTENDED_TEXTS)]
        
        # Boyut ve renk rastgele, merkeze yakın olanlar daha büyük
        dist = math.sqrt(x*x + y*y)
        if dist < 5:
            font_size = random.randint(11, 14)
            font_weight = "bold"
        else:
            font_size = random.randint(8, 11)
            font_weight = "normal"

        color = random.choice(self.colors)
        
        # Hafif gölge efekti için 2 kat yaz
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

    def update_beat(self):
        """Kalp atışı efekti"""
        self.beat_scale += 0.008 * self.beat_direction
        
        if self.beat_scale > 1.15:
            self.beat_direction = -1
        elif self.beat_scale < 0.92:
            self.beat_direction = 1

        # Tüm yazıları ölçekle - yeniden çiz
        for i, item in enumerate(self.text_items):
            if i >= len(self.points):
                break
            x, y = self.points[i]
            cx, cy = self.get_position_on_canvas(x, y)
            self.canvas.coords(item, cx, cy)

    def animate(self):
        """Ana animasyon döngüsü"""
        # Başlangıçta hızlı dolum
        batch = 8 if self.index < 200 else 3
        
        for _ in range(batch):
            if not self.draw_single_text():
                break

        self.update_beat()

        # Kalp tamamen dolduysa, atışa devam et
        if self.index < len(self.points):
            self.root.after(25, self.animate)
        else:
            # Sonsuz atış
            self.update_beat()
            self.root.after(30, self.animate_continuous_beat)

    def animate_continuous_beat(self):
        """Dolu kalp sonsuz atıyor"""
        self.update_beat()
        self.root.after(30, self.animate_continuous_beat)

def main():
    root = tk.Tk()
    # Pencereyi ortala
    root.geometry("900x800+100+20")
    app = BeatingHeart(root)
    
    # Kapatma animasyonu
    def on_close():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
    main()
