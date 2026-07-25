from PIL import Image
import os

img_path = r'C:\Users\getsu\.gemini\antigravity-ide\brain\dd16231a-b085-4ca7-8335-3779d92ea6ad\media__1784975219660.png'
out_dir = r'static/images/new_14_tiles'
os.makedirs(out_dir, exist_ok=True)

img = Image.open(img_path)
w, h = img.size
print(f"Uploaded Image size: {w} x {h}")

# The image is 1024 x 512
# Let's find exact coordinates of the 2 rows x 7 cols grid
# Row 1: y approx 60 to 240
# Row 2: y approx 250 to 430

# Let's define column positions
# 7 columns across 1024 width
# Let's measure card boxes:
# Card width: ~128px, gap: ~14px
# Left margin: ~16px, Right margin: ~16px

cards = [
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

# Grid parameters estimation
margin_x = 16
gap_x = 14
card_w = (w - 2 * margin_x - 6 * gap_x) / 7.0

row1_y0, row1_y1 = 62, 238
row2_y0, row2_y1 = 254, 430

for name, r, c in cards:
    x0 = int(margin_x + c * (card_w + gap_x))
    x1 = int(x0 + card_w)
    y0 = row1_y0 if r == 0 else row2_y0
    y1 = row1_y1 if r == 0 else row2_y1
    
    cropped = img.crop((x0, y0, x1, y1))
    save_path = os.path.join(out_dir, f"{name}.png")
    cropped.save(save_path)
    print(f"Saved {name}.png box: ({x0}, {y0}, {x1}, {y1}) size: {cropped.size}")
