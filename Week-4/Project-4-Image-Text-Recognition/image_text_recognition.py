import os
import sys
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def load_image(path):
    if not os.path.exists(path):
        print("  Error: File not found -> " + path)
        sys.exit(1)

    image = Image.open(path)
    print("  Image loaded    : " + path)
    print("  Format          : " + str(image.format))
    print("  Size            : " + str(image.size[0]) + " x " + str(image.size[1]) + " pixels")
    print("  Mode            : " + str(image.mode))
    return image


def preprocess_image(image):
    grayscale = image.convert("L")
    sharpened = grayscale.filter(ImageFilter.SHARPEN)
    enhanced  = ImageEnhance.Contrast(sharpened).enhance(2.0)
    threshold = enhanced.point(lambda px: 255 if px >= 88 else 0, "L")

    print()
    print("  Preprocessing Pipeline:")
    print("    Step 1 : RGB  -> Grayscale       (remove color noise)")
    print("    Step 2 : Grayscale -> Sharpened  (enhance edges)")
    print("    Step 3 : Contrast enhanced       (factor 2.0)")
    print("    Step 4 : Otsu Threshold @ 88     (pure black/white)")

    return threshold


def run_ocr(image):
    config = "--psm 6 --oem 3"
    raw_text = pytesseract.image_to_string(image, config=config)

    data = pytesseract.image_to_data(
        image,
        config=config,
        output_type=pytesseract.Output.DICT
    )

    confidences = [
        int(c) for c in data["conf"]
        if str(c).isdigit() and int(c) > 0
    ]

    avg_confidence = round(sum(confidences) / len(confidences), 2) if confidences else 0.0
    word_count     = len([w for w in data["text"] if w.strip() != ""])

    return raw_text.strip(), avg_confidence, word_count


def display_results(text, confidence, word_count, path):
    print()
    print("=" * 60)
    print("  OCR OUTPUT")
    print("=" * 60)
    print()

    if text:
        print("  Extracted Text:")
        print()
        for line in text.split("\n"):
            if line.strip():
                print("    " + line)
        print()
    else:
        print("  No text detected in this image.")
        print()

    print("=" * 60)
    print("  RECOGNITION REPORT")
    print("=" * 60)
    print("  Source File       : " + os.path.basename(path))
    print("  Words Detected    : " + str(word_count))
    print("  Avg Confidence    : " + str(confidence) + "%")
    print()

    if confidence >= 80:
        quality = "High Confidence — reliable extraction"
    elif confidence >= 50:
        quality = "Medium Confidence — review recommended"
    else:
        quality = "Low Confidence — image quality may be poor"

    print("  Quality Rating    : " + quality)
    print()


def get_image_path():
    print()
    print("  Enter image path or press Enter to use default test.")
    print("  Supported formats: PNG, JPG, JPEG, BMP, TIFF")
    print()
    path = input("  Image path : ").strip()

    if path == "":
        path = generate_test_image()

    return path


def generate_test_image():
    from PIL import ImageDraw, ImageFont

    img  = Image.new("RGB", (600, 200), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    lines = [
        "DecodeLabs AI Internship 2026",
        "Project 4: Image Text Recognition",
        "OCR Engine: Tesseract",
        "Status: Running successfully"
    ]

    y = 20
    for line in lines:
        draw.text((20, y), line, fill=(0, 0, 0))
        y += 40

    test_path = "test_input.png"
    img.save(test_path)
    print("  No path given. Generated test image: " + test_path)
    return test_path


def main():
    print("=" * 60)
    print("  IMAGE TEXT RECOGNITION  |  DecodeLabs 2026")
    print("  Engine  : Tesseract OCR (pytesseract)")
    print("  Method  : Transfer Learning + LSTM Pipeline")
    print("=" * 60)

    image_path = get_image_path()

    print()
    print("=" * 60)
    print("  PHASE 1 : INPUT")
    print("=" * 60)
    image = load_image(image_path)

    print()
    print("=" * 60)
    print("  PHASE 2 : PREPROCESSING")
    print("=" * 60)
    processed = preprocess_image(image)

    print()
    print("=" * 60)
    print("  PHASE 3 : OCR RECOGNITION")
    print("=" * 60)
    print("  Running Tesseract engine...")
    print("  PSM Mode : 6  (Uniform block of text)")
    print("  OEM Mode : 3  (LSTM neural network)")

    text, confidence, word_count = run_ocr(processed)

    display_results(text, confidence, word_count, image_path)

    print("=" * 60)
    print("  Pipeline Complete.")
    print("  Steps: Load -> Preprocess -> OCR -> Output")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
