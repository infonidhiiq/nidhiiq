from PIL import Image
import os

src_path = r'C:\Users\getsu\.gemini\antigravity-ide\brain\aaa67ff6-7e44-43ad-a675-0e8ed565aa35\media__1785735765681.png'
out_dir = r'static/images/grouped_icons'
os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_path).convert('RGBA')
w, h = img.size
print(f"Source Image Dimension: {w} x {h}")

items = [
    # Row 0
    ("free_term_life.png", 0, 0),
    ("term_plans_rop.png", 0, 1),
    ("term_insurance_women.png", 0, 2),
    ("term_life_self_employed.png", 0, 3),
    ("term_life_nri_global.png", 0, 4),
    ("home_loan_insurance.png", 0, 5),
    ("dollar_term_plan.png", 0, 6),
    # Row 1
    ("term_insurance_diabetic.png", 1, 0),
    ("term_insurance_non_smokers.png", 1, 1),
    ("term_insurance_doctors.png", 1, 2),
    ("term_insurance_salaried.png", 1, 3),
    ("term_plan_critical_illness.png", 1, 4),
    ("family_protection_plan.png", 1, 5),
    ("instant_online_term_plan.png", 1, 6),
]

def clean_and_save(crop_box, save_path):
    cropped = img.crop(crop_box)
    
    # Process transparency
    # Convert pixels that are light/white background to transparent
    newData = []
    for px in cropped.getdata():
        r, g, b, a = px[0], px[1], px[2], px[3]
        # Any white or near-white background pixel
        if r >= 240 and g >= 240 and b >= 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((r, g, b, a))
            
    cropped.putdata(newData)
    
    # Bounding box crop around non-transparent pixels
    bbox = cropped.getbbox()
    if bbox:
        cropped = cropped.crop(bbox)
        
    cropped.save(save_path, 'PNG')
    print(f"Saved: {os.path.basename(save_path):<32} size: {cropped.size}")

col_w = w / 7.0

for name, row, col in items:
    x0 = int(col * col_w + 6)
    x1 = int((col + 1) * col_w - 6)
    
    if row == 0:
        y0 = 38
        y1 = 160
    else:
        y0 = 246
        y1 = 372
        
    save_path = os.path.join(out_dir, name)
    clean_and_save((x0, y0, x1, y1), save_path)

print("Extraction completed!")
