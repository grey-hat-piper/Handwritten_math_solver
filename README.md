# Handwritten_math_solver
AI-powered Streamlit app that reads kids’ handwritten math problems, solves them instantly using OCR and SymPy, and promotes quality education (SDG 4)

# 🧮 Handwritten Math Solver

### Empowering Quality Education with AI (SDG 4)

The **Handwritten Math Solver** is a Streamlit-based AI project that helps children learn mathematics by recognizing and solving their handwritten math problems. This initiative contributes to the **United Nations Sustainable Development Goal 4 (Quality Education)** — ensuring inclusive and equitable education for all.

## 🚀 Live Demo
👉 **Try it here:** [Handwritten Math Solver on Streamlit Cloud](https://handwrittenmathsolver.streamlit.app/)


## 🎯 Problem Statement

Many children, especially in under-resourced schools, lack access to personalized learning tools that can adapt to their individual pace. Handwriting remains the most common medium of learning, yet most educational technologies are built around typed text. This creates a gap in accessibility and engagement for early learners.

## 💡 Solution Overview

This project bridges that gap by allowing children to **upload or capture an image of handwritten math expressions**, which the system then **reads and solves instantly**. It combines the power of **computer vision (OCR)** and **symbolic mathematics** to provide real-time feedback — making learning interactive and fun.

## 🧠 Machine Learning Paradigm

This app leverages **Supervised Learning** through a pre-trained **Optical Character Recognition (OCR)** model, implemented via **EasyOCR**. The model identifies handwritten numbers and arithmetic symbols, translating them into text. The recognized expressions are then processed by **SymPy**, a symbolic mathematics library, to compute accurate results safely.

## 🧰 Tech Stack

- **Streamlit** – User interface  
- **EasyOCR** – Handwriting recognition  
- **SymPy** – Mathematical solving  
- **NumPy & Pillow** – Image handling  
- **PyTorch** – Backend for OCR models  

## 🖼️ App in Action

![Handwritten Math Solver Screenshot](/app_screenshot.png)

> The app reads handwritten math like “12 + 7” and returns the result instantly — making math accessible, engaging, and AI-powered.

## 🌍 Impact

By integrating AI into early-stage education, this project supports the SDG 4 goal of **inclusive and equitable quality education**, providing a simple yet powerful way to enhance numeracy and confidence in young learners.

---

### 🚀 Getting Started

```bash
pip install -r requirements.txt
streamlit run app.py
