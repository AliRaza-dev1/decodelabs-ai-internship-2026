# Project 3: AI Recommendation Logic

## Overview
A content-based filtering recommendation system that matches a user's skills to the most relevant tech job roles using TF-IDF vectorization and Cosine Similarity.

## Language
Python 3

## Libraries Used
scikit-learn

## How To Run
python tech_stack_recommender.py

## What It Does
- Takes minimum 3 skill inputs from the user
- Converts skills and job role descriptions into TF-IDF vectors
- Calculates Cosine Similarity between user profile and each job role
- Sorts results by similarity score in descending order
- Displays Top 3 most relevant job roles with match percentage

## Key Concepts
- Content-Based Filtering: Matches user profile directly to item attributes without needing other users data
- TF-IDF: Penalizes common generic words and rewards specific unique skills for better matching
- Cosine Similarity: Measures angle between vectors not distance so it is not affected by vector size
- Cold Start Solution: Asking minimum 3 inputs ensures enough data density for accurate matching
- 4 Step Pipeline: Ingestion, Scoring, Sorting, Filtering

## Job Roles Covered
AI Engineer, Data Scientist, Data Analyst, Backend Developer, Frontend Developer, Full Stack Developer, DevOps Engineer, Cloud Architect, Cybersecurity Analyst, Mobile Developer, Database Administrator, NLP Engineer

## Internship
DecodeLabs AI Internship | Batch 2026
