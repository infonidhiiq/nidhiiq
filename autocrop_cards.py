from PIL import Image
import os

img_path = r'C:\Users\getsu\.gemini\antigravity-ide\brain\dd16231a-b085-4ca7-8335-3779d92ea6ad\media__1784975219660.png'
out_dir = r'static/images/new_14_tiles'
os.makedirs(out_dir, exist_ok=True)

img = Image.open(img_path).convert("RGB")
w, h = img.size

card_info = [
    # Row 1
    ("term_life_insurance", 0, 0),
    ("health_insurance", 0, 1),
    ("investment_plans", 0, 2),
    ("motor_insurance", 0, 3),
    ("term_plans", 0, 4),
    ("guaranteed_return_plans", 0, 5),
    ("child_savings_plans", 0, 6),
    # Row 2
    ("family_health_insurance", 1, 0),
    ("travel_insurance", 1, 1),
    ("retirement_plans", 1, 2),
    ("employee_group_health_insurance", 1, 3),
    ("home_insurance", 1, 4),
    ("family_office", 1, 5),
    ("real_estate", 1, 6),
]

for name, r, c in card_info:
    search_x0 = int(c * (w / 7.0))
    search_x1 = int((c + 1) * (w / 7.0))
    search_y0 = int(0 if r == 0 else h / 2.0)
    search_y1 = int(h / 2.0 if r == 0 else h)
    
    crop_search = img.crop((search_x0, search_y0, search_x1, search_y1))
    
    # Find bounding box of non-white pixels
    # Background color is roughly RGB (255, 255, 255)
    sw, sh = crop_search.size
    min_x, max_x = sw, 0
    min_y, max_y = sh, 0
    
    pixels = crop_search.load()
    for y in range(sh):
        for x in range(sw):
            r_val, g_val, b_val = pixels[x, y]
            # If not white/near white background
            if r_val < 250 or g_val < 250 or b_val < 250:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    real_x0 = search_x0 + max(0, min_x - 1)
    real_y0 = search_y0 + max(0, min_y - 1)
    real_x1 = search_x0 + min(sw, max_x + 2)
    real_y1 = search_y0 + min(sh, max_y + 2)
    
    card_img = img.crop((real_x0, real_y0, real_x1, real_y1))
    save_path = os.path.join(out_dir, f"{name}.png")
    card_img.save(save_path)
    print(f"Cropped {name}: box=({real_x0}, {real_y0}, {real_x1}, {real_y1}), size={card_img.size}")

print("All 14 cards autocropped precisely!")
