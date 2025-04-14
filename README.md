
---

# Language Agnostic Visualization Web Application

## Overview

This project is a **Language-Agnostic Visualization Web Application** that allows users to input **Python or R scripts** to dynamically generate and display **static, interactive, or 3D visualizations** in the browser. It uses an Angular 19 frontend and a Flask backend to securely execute code and render the resulting visual outputs.

### Key Features

- Select between **Python** and **R** as the scripting language.
- Input and execute custom visualization scripts.
- Supports:
  - Static plots (e.g., matplotlib, base R)
  - Interactive plots (e.g., plotly)
  - 3D visualizations (e.g., plotly.surface in Python and R)
- Displays the output visualization (image or HTML) directly on the web page.

---

## Tech Stack

### Frontend: Angular 19

- **Standalone Components** (no traditional NgModules)
- Language selector dropdown
- Code input textarea
- Visualization rendered using `<iframe>` or `<img>`


### Backend: Flask (Python)

- Handles code execution securely
- Uses `subprocess` to run scripts in isolated temp folders
- Supports both `.py` and `.R` file executions
- Static and interactive outputs (HTML or PNG) are served via a public endpoint
- CORS enabled for frontend-backend communication

---

##  Libraries Used

### Python:
- `matplotlib` (static)
- `plotly.express` (interactive)
- `plotly.graph_objects` (3D)

### R:
- `base` plotting (`plot`, `png`) for static
- `plotly` + `htmlwidgets` for interactive & 3D
- `ggplot2` for layered plotting

---

## Sample Visualizations Tested

| Type       | Language | Library        | Description                      |
|------------|----------|----------------|----------------------------------|
| Static     | Python   | matplotlib     | Line plot                        |
| Interactive| Python   | plotly.express | Bar chart                        |
| 3D         | Python   | plotly.graph_objects | Surface plot               |
| Static     | R        | base + png     | Cars dataset                     |
| Interactive| R        | plotly + ggplot2 | Scatter/Bar + Interactivity    |
| 3D         | R        | plotly         | 3D surface using `outer()`       |

---

## Issues & Fixes

### 1. **CORS Errors**
- Issue: Angular frontend couldn’t communicate with Flask backend.
- Fix: Enabled `CORS(app)` using `flask_cors`.

### 2. **`plotly` ModuleNotFound in Flask**
- Issue: Backend couldn’t find `plotly` during execution.
- Fix: Ensured it was installed inside the virtual environment used by Flask.

### 3. **R packages missing**
- Issue: Errors from `rglwidget`, `htmlwidgets`, etc.
- Fix: Installed missing R packages globally using `install.packages()`.

### 4. **Interactive R output not rendering due to Pandoc**
- Issue: `saveWidget(..., selfcontained=TRUE)` failed.
- Fix: Installed **Pandoc** and added it to system PATH.

---

## 🎥 Demo Recording

Link: https://youtu.be/6b86C-YnAbo

---
