from PIL import Image
import os

img_path = r'C:\Users\getsu\.gemini\antigravity-ide\brain\5d251d22-57d8-46ee-aaed-501257e323af\media__1784895020374.png'
out_dir = r'static/images/pb_exact_tiles'
os.makedirs(out_dir, exist_ok=True)

img = Image.open(img_path)
width, height = img.size
print(f"Screenshot size: {width} x {height}")

# The grid section in screenshot is roughly the lower 60% of the image
# Bounding box for 7x2 grid
# Y range for Row 1: y ~ 50% to 75%
# Y range for Row 2: y ~ 75% to 100%

# Let's calculate precise coordinates
grid_x0 = int(width * 0.02)
grid_x1 = int(width * 0.98)
grid_width = grid_x1 - grid_x0
col_w = grid_width / 7.0

row1_y0 = int(height * 0.50)
row1_y1 = int(height * 0.74)

row2_y0 = int(height * 0.74)
row2_y1 = int(height * 0.98)

# Row 1 (7 items)
for c in range(7):
    x0 = int(grid_x0 + c * col_w)
    x1 = int(grid_x0 + (c + 1) * col_w)
    crop_img = img.crop((x0, row1_y0, x1, row1_y1))
    crop_img.save(os.path.join(out_dir, f'pb_r1_c{c+1}.png'))

# Row 2 (7 items)
for c in range(7):
    x0 = int(grid_x0 + c * col_w)
    x1 = int(grid_x0 + (c + 1) * col_w)
    crop_img = img.crop((x0, row2_y0, x1, row2_y1))
    crop_img.save(os.path.join(out_dir, f'pb_r2_c{c+1}.png'))

print("Cropped 14 PB exact grid items!")
