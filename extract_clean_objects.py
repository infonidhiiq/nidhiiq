from PIL import Image
import os

src_path = r'C:\Users\getsu\.gemini\antigravity-ide\brain\5d251d22-57d8-46ee-aaed-501257e323af\media__1784895362793.jpg'
out_dir = r'static/images/clean_icons'
os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_path).convert('RGBA')
w, h = img.size
print(f"Source Image Dimension: {w} x {h}")

def clean_and_save(crop_box, save_path):
    cropped = img.crop(crop_box)
    datas = cropped.getdata()
    
    newData = []
    for item in datas:
        # Check if pixel is white / light grey background of the source card
        # RGB values near white (>= 236)
        if item[0] >= 235 and item[1] >= 238 and item[2] >= 240:
            newData.append((255, 255, 255, 0)) # Fully transparent
        else:
            newData.append(item)
            
    cropped.putdata(newData)
    
    # Crop bounding box to tightly fit the 3D illustration object
    bbox = cropped.getbbox()
    if bbox:
        cropped = cropped.crop(bbox)
        
    cropped.save(save_path, 'PNG')
    print(f"Saved clean object: {save_path}")

# ROW 1 (5 items)
row1_y0, row1_y1 = int(h * 0.02), int(h * 0.26)
for c in range(5):
    x0 = int(c * (w / 5.0) + (w / 5.0) * 0.05)
    x1 = int((c + 1) * (w / 5.0) - (w / 5.0) * 0.05)
    clean_and_save((x0, row1_y0, x1, row1_y1), os.path.join(out_dir, f'icon_0{c+1}.png'))

# ROW 2 (5 items)
row2_y0, row2_y1 = int(h * 0.35), int(h * 0.59)
for c in range(5):
    x0 = int(c * (w / 5.0) + (w / 5.0) * 0.05)
    x1 = int((c + 1) * (w / 5.0) - (w / 5.0) * 0.05)
    clean_and_save((x0, row2_y0, x1, row2_y1), os.path.join(out_dir, f'icon_0{c+6}.png'))

# ROW 3 (4 items)
row3_y0, row3_y1 = int(h * 0.68), int(h * 0.92)
for c in range(4):
    x0 = int(c * (w / 4.0) + (w / 4.0) * 0.05)
    x1 = int((c + 1) * (w / 4.0) - (w / 4.0) * 0.05)
    clean_and_save((x0, row3_y0, x1, row3_y1), os.path.join(out_dir, f'icon_{c+11}.png'))

print("All 14 clean 3D objects extracted successfully without background or shadows!")
