# 🔍 Image Similarity Search

This Python project scans all images on selected drives and finds the ones that visually match a reference image using perceptual hashing.

## 📂 Project Structure

- `main.py`: Main script to search for similar images.
- `matched_images/`: Output folder where similar images are copied.
- `reference image`: The image you specify when running the script.

## 🚀 Features
- Supports `.jpg`, `.jpeg`, and `.png` formats.
- Detects images visually similar to the reference image.
- Automatically copies matched results to a dedicated folder.
- Handles transparency and RGBA images.
- Interactive input for choosing the reference image at runtime.


## 🛠️ Usage
1. Place your reference image in the same folder as `main.py`.
2. Open terminal and run:
   ```bash
   python main.py
When prompted, enter the file name of your reference image (e.g., sample.png).

The script will search for visually similar images in C:\ and D:\.

Matching images will be copied into a new folder: matched_images.


⚙️ Configuration
You can modify the following variables in main.py:
search_directories = ["C:\\", "D:\\"]
allowed_ext = ['.jpg', '.jpeg', '.png']
MAX_DISTANCE = 10
MAX_RESULTS = 10


🧰 Requirements
Install required packages:
pip install pillow imagehash tqdm


📝 License
This project is open-source and free to use for personal or educational purposes.
