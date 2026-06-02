# Project 4: Image Text Recognition

## Overview
A basic OCR (Optical Character Recognition) system that extracts text from images using the Tesseract engine and pytesseract Python wrapper.

## Language
Python 3

## Libraries Used
pytesseract, pillow

## Requirements
Tesseract OCR engine must be installed separately from https://github.com/UB-Mannheim/tesseract/wiki

## How To Run
python image_text_recognition.py

## What It Does
- Loads an image from a given path or generates a test image automatically
- Preprocesses the image through a 4 step pipeline
- Runs Tesseract OCR engine to extract text
- Displays extracted text with confidence score and word count

## Preprocessing Pipeline
- Step 1: RGB to Grayscale to remove color noise
- Step 2: Sharpen filter to enhance text edges
- Step 3: Contrast enhancement with factor 2.0
- Step 4: Otsu Thresholding at value 88 to convert to pure black and white

## Key Concepts
- Transfer Learning: Uses Tesseract which is pre-trained on millions of images so no training needed
- Otsu Thresholding: Forces every pixel to pure black or white for cleaner text recognition
- Confidence Score: The model's own probability assessment of how accurately it read each character
- PSM Mode 6: Treats image as a uniform block of text for best results
- OEM Mode 3: Uses LSTM neural network for character recognition

## Internship
DecodeLabs AI Internship | Batch 2026
