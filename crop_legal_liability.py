from PIL import Image
import os

src_path = r'C:\Users\getsu\.gemini\antigravity-ide\brain\407fb5b4-ac85-444c-b2c6-6e2d4382d2c2\media__1785563311022.png'
out_dir = r'static/images/grouped_icons'
os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_path).convert('RGBA')
w, h = img.size
print(f"Source Image Dimension: {w} x {h}")

# The image contains a single centered card
# Icon is in the upper part of the card
y0 = int(h * 0.15)
y1 = int(h * 0.65)
x0 = int(w * 0.30)
x1 = int(w * 0.70)

cropped = img.crop((x0, y0, x1, y1))
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

bbox = cropped.getbbox()
if bbox:
    cropped = cropped.crop(bbox)

save_path = os.path.join(out_dir, 'legal_liability_insurance.png')
cropped.save(save_path, 'PNG')
print(f"Saved clean object: {save_path} size: {cropped.size}")
