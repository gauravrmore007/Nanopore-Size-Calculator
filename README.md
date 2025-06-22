# 🔬 Nanopore Size Calculator

This tool calculates the **length and base diameter of a conical nanopore** based on conductivity, conductance, tip diameter, and cone angle.  
Built using **Flask** (Python), it helps researchers and students visualize nanopore geometry easily.

---

## 💡 What It Does

- Takes user inputs: conductivity, conductance, tip diameter, cone angle
- Calculates:
  - Length of the nanopore
  - Base diameter of the cone
- Shows results in a simple HTML page

---

## 🧠 Formula Used

\[
L = \frac{d}{2 \cdot \tan(\theta / 2)} \\
D = \sqrt{ \frac{4 \cdot L \cdot G}{\pi \cdot \sigma \cdot d} }
\]

---

## 🛠️ Tech Stack

- Python (Flask)
- HTML + CSS (Jinja Templates)
- Math module

---

## 📁 Folder Structure
├── app.py # Flask app with core logic
├── requirements.txt # Python packages
├── templates/
│ └── result.html # Output page
├── static/
│ └── style.css # Styling
├── Procfile # (For deployment)
└── README.md # This file


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py

Visit: http://localhost:5000

📬 Contact
Gaurav More
📧 more.56@buckeyemail.osu.edu
🔗 LinkedIn
