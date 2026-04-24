# 🎨 Computer Graphics Lab (OpenGL)

This repository contains implementations of **Computer Graphics Lab experiments** using **Python and OpenGL (PyOpenGL)**.

---

## 📁 Project Structure

```
Lab Codes/
│
├── Lab-01/
│   └── Lab01_DDA_Bresenham.py
│
├── Lab-02/
│   └── Lab02_OpenGL_Shapes.py
│
├── Lab-03/
│   └── Lab03_DDA_Bresenham_Circle.py
│
├── Lab-04/
│   └── Lab04_Boundary_Fill.py
│
└── README.md
```

---

## 📚 Lab Experiments

### 🧪 Lab-01

**Implementation of DDA and Bresenham Line Drawing Algorithm**

* Draw two intersecting lines (X shape)
* Algorithms used:

  * DDA
  * Bresenham
* Coordinates:

  * (100,100) → (300,300)
  * (300,100) → (100,300)

---

### 🧪 Lab-02

**Drawing Multiple Objects using OpenGL**

* Create a 600×600 window
* Draw four non-overlapping objects:

  * Green square (bottom-left)
  * Triangle (top-right)
  * Rectangle using two triangles (top-left)
  * Pentagon (bottom-right)

---

### 🧪 Lab-03

**Line Drawing Comparison and Circle Drawing**

#### Task-01:

* Draw two intersecting lines:

  * DDA Algorithm
  * Bresenham Algorithm
* Features:

  * Execution time comparison
  * 3-second delay

#### Task-02:

* Draw circle using Bresenham Algorithm
* Center: (250,250)
* Radius: 10

---

### 🧪 Lab-04

**Stack Based Boundary Filling Algorithm**

* Fill region using stack-based boundary fill
* Features:

  * Click inside → fill
  * Outside click → no fill
  * Boundary detection using color

---

## 🛠️ Technologies Used

* Python
* PyOpenGL
* GLUT

---

## ▶️ How to Run

### Install Dependencies

```
pip install PyOpenGL PyOpenGL_accelerate
```

### Run Programs

## ▶️ How to Run

### Run Lab-01

```bash
python Lab-01/Lab01_DDA_Bresenham.py
```

### Run Lab-02

```bash
python Lab-02/Lab02_OpenGL_Shapes.py
```

### Run Lab-03

```bash
python Lab-03/Lab03_DDA_Bresenham_Circle.py
```

### Run Lab-04

```bash
python Lab-04/Lab04_Boundary_Fill.py
```


---

## 🖥️ Features

* Line Drawing Algorithms (DDA & Bresenham)
* Circle Drawing (Bresenham)
* Shape Rendering using OpenGL
* Execution Time Comparison
* Stack-Based Boundary Fill

---

## 👨‍💻 Author

**Kamrul_43**

---

## 📌 Notes

* All algorithms are implemented manually
* Designed for academic lab submission
* No shortcut libraries used

---

## ⭐ Conclusion

This project demonstrates key computer graphics concepts:

* Line Drawing Algorithms
* Circle Drawing Techniques
* Polygon Rendering
* Region Filling Algorithm

---

⭐ If you find this helpful, give it a star!
