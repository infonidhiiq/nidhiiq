from PIL import Image
import os

src_path = r'C:\Users\getsu\.gemini\antigravity-ide\brain\407fb5b4-ac85-444c-b2c6-6e2d4382d2c2\media__1785562994849.png'
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
        # Remove card white/off-white background (#f8fafc / #f5f7fa / white)
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
    ('home_insurance.png', 0),
    ('industrial_all_risk_insurance.png', 1),
    ('goods_in_transit_insurance.png', 2),
]

# Tighter y range focused purely on 3D icon
y0 = int(h * 0.15)
y1 = int(h * 0.65)

for name, col in items:
    col_w = w / 3.0
    x0 = int(col * col_w + col_w * 0.05)
    x1 = int((col + 1) * col_w - col_w * 0.05)
    
    save_path = os.path.join(out_dir, name)
    clean_and_save((x0, y0, x1, y1), save_path)

print("Extraction of 3 marine & property insurance cards completed successfully!")
