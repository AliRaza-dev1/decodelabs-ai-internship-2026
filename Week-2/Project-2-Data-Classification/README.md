# Project 1: Rule-Based AI Chatbot

## Overview
A rule-based AI chatbot named ARIA that responds to user inputs using dictionary-based keyword matching and control flow logic.

## Language
Python 3

## Libraries Used
datetime, random

## How To Run
python aria_chatbot.py

## What It Does
- Takes user input and sanitizes it
- Matches input against a dictionary of keywords
- Returns a response from the matched category
- Runs in a continuous loop until user types exit

## Key Concepts
- Dictionary is used instead of if-elif for O(1) fast lookup
- Input sanitization using .lower().strip()
- Random responses so bot does not repeat itself
- Continuous while loop with clean exit command

## Internship
DecodeLabs AI Internship | Batch 2026
