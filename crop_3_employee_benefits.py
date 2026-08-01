from PIL import Image
import os

src_path = r'C:\Users\getsu\.gemini\antigravity-ide\brain\5172a4af-da51-498c-a973-b382c231447d\media__1785562562439.png'
out_dir = r'static/images/grouped_icons'
os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_path).convert('RGBA')
w, h = img.size
print(f"Source Image Dimension: {w} x {h}")

def clean_and_save(crop_box, save_path):
    cropped = img.crop(crop_box)
    pixels = list(cropped.getdata())
    
    newData = []
    for px in pixels:
        r, g, b = px[0], px[1], px[2]
        a = px[3] if len(px) > 3 else 255
        # Remove card white/off-white background
        if r >= 235 and g >= 235 and b >= 238:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((r, g, b, a))
            
    cropped.putdata(newData)
    
    # Crop bounding box to tightly fit the 3D illustration object
    bbox = cropped.getbbox()
    if bbox:
        cropped = cropped.crop(bbox)
        
    cropped.save(save_path, 'PNG')
    print(f"Saved clean object: {save_path} size: {cropped.size}")

items = [
    ('group_health_topup_plan.png', 0),
    ('group_gratuity_insurance.png', 1),
    ('group_education_assistance.png', 2),
]

# Tighter y range focused purely on 3D icon
y0 = int(h * 0.20)
y1 = int(h * 0.65)

for name, col in items:
    col_w = w / 3.0
    x0 = int(col * col_w + col_w * 0.08)
    x1 = int((col + 1) * col_w - col_w * 0.08)
    
    save_path = os.path.join(out_dir, name)
    clean_and_save((x0, y0, x1, y1), save_path)

print("Extraction of 3 employee benefit cards completed successfully!")
