import os
import shutil
from PIL import Image
import imagehash
from tqdm import tqdm

image_name = input("أدخل اسم الصورة المرجعية (مثال: image.png): ").strip()
target_image_path = os.path.join(os.getcwd(), image_name)

if not os.path.isfile(target_image_path):
    print(f"لم يتم العثور على الصورة: {target_image_path}")
    exit(1)

search_directories = ["C:\\", "D:\\"]
allowed_ext = ['.jpg', '.jpeg', '.png']
MAX_DISTANCE = 10
MAX_RESULTS = 10

def load_image_with_alpha(path):
    img = Image.open(path)
    if img.mode == 'RGBA':
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        return background
    return img.convert("RGB")

target_img = load_image_with_alpha(target_image_path)
target_hash = imagehash.phash(target_img)

output_folder = os.path.join(os.getcwd(), "matched_images")
os.makedirs(output_folder, exist_ok=True)

all_image_paths = []
for directory in search_directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in allowed_ext:
                all_image_paths.append(os.path.join(root, file))

similar_images = []
for path in tqdm(all_image_paths, desc="Searching for similar images"):
    try:
        img = load_image_with_alpha(path)
        img_hash = imagehash.phash(img)
        distance = abs(target_hash - img_hash)
        if distance <= MAX_DISTANCE:
            similar_images.append((path, distance))
            shutil.copy(path, output_folder)
            if len(similar_images) >= MAX_RESULTS:
                break
    except Exception:
        continue

print("\nالصور المطابقة:")
for path, distance in sorted(similar_images, key=lambda x: x[1]):
    print(f"{path} | Distance: {distance}")
