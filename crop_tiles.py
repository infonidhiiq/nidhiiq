from PIL import Image
import os

img_path = r'static/images/pb_icons_grid.jpg'
out_dir = r'static/images/tiles'
os.makedirs(out_dir, exist_ok=True)

img = Image.open(img_path)
width, height = img.size
print(f"Original image size: {width} x {height}")

# Grid coordinates calculation:
# Row 1 (5 cols): 0 to 33.3% height
# Row 2 (5 cols): 33.3% to 66.6% height
# Row 3 (4 cols): 66.6% to 100% height

row1_y0, row1_y1 = 0, int(height * 0.33)
row2_y0, row2_y1 = int(height * 0.33), int(height * 0.66)
row3_y0, row3_y1 = int(height * 0.66), height

# Row 1 (5 items)
for c in range(5):
    x0 = int(c * (width / 5))
    x1 = int((c + 1) * (width / 5))
    crop_img = img.crop((x0, row1_y0, x1, row1_y1))
    crop_img.save(os.path.join(out_dir, f'tile_r1_c{c+1}.png'))

# Row 2 (5 items)
for c in range(5):
    x0 = int(c * (width / 5))
    x1 = int((c + 1) * (width / 5))
    crop_img = img.crop((x0, row2_y0, x1, row2_y1))
    crop_img.save(os.path.join(out_dir, f'tile_r2_c{c+1}.png'))

# Row 3 (4 items)
for c in range(4):
    x0 = int(c * (width / 4))
    x1 = int((c + 1) * (width / 4))
    crop_img = img.crop((x0, row3_y0, x1, row3_y1))
    crop_img.save(os.path.join(out_dir, f'tile_r3_c{c+1}.png'))

print("All 14 tiles extracted successfully!")
