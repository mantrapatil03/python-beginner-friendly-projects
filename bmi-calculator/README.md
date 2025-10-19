<h1 align="center"> BMI Calculator (Python)</h1>

<p align="center">
A simple yet effective <b>Python command-line application</b> that calculates your <b>Body Mass Index (BMI)</b>   
and categorizes your health status based on your input weight and height.  
Perfect for beginners learning input handling and conditional logic in Python!
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Platform-Terminal%2FCMD-orange?style=for-the-badge&logo=windowsterminal"></a>
  <a href="https://github.com/mantrapatil03/python-beginner-friendly-projects"><img src="https://img.shields.io/github/stars/mantrapatil03/python-beginner-friendly-projects?style=for-the-badge&logo=github"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative"></a>
</p>

---

##  Features

✅ **BMI Calculation** – Computes BMI using standard formula:  
> BMI = weight (kg) / height² (m²)

 **Health Categories:**
| Category | BMI Range |
|-----------|------------|
| Underweight | < 18.5 |
| Normal weight | 18.5 – 24.9 |
| Overweight | 25.0 – 29.9 |
| Obesity | ≥ 30.0 |

> **Error Handling** – Prevents crashes for invalid inputs or zero height.  
>**User-Friendly Interface** – Simple prompts and clean output.

---

##  Example Demo
```
$ python bmi_calculator.py

⚖️ BMI Calculator

Enter your weight in kilograms: 70
Enter your height in meters: 1.75

Your BMI is: 22.86
Category: Normal weight
```

---

##  Installation & Setup

### 1️⃣ Prerequisites  
Ensure you have **Python 3.x** installed:  
```bash
python --version
```
2️⃣ Clone the Repository
```
git clone https://github.com/mantrapatil03/python-beginner-friendly-projects.git
```
3️⃣ Navigate to the BMI Calculator folder
```
cd python-beginner-friendly-projects/bmi-calculator
```
4️⃣ Run the Script
```
python bmi_calculator.py
```

### How It Works
- Takes user input for weight (kg) and height (m)
- Computes BMI with the formula:
```
bmi = weight / (height ** 2)
```
- Displays the BMI value (rounded to 2 decimals)
- Categorizes result into:
    1. Underweight
    2. Normal weight
    3. Overweight
    4. Obesity

##  Future Roadmap
| Feature                 |   Status  | Description                      |
| ----------------------- | :-------: | -------------------------------- |
|  Save results to file |  Planned | Store BMI history in text/CSV    |
|  Health tips          |  Planned | Show fitness advice per category |
|  GUI version          |  Planned | Build a Tkinter-based interface  |
|  Web version          |  Planned | Create a Flask-based BMI web app |

##  Contributing

Contributions are welcome! 🎉
To contribute:
- Fork this repo
- Create a new branch (feature/your-feature)
- Commit changes
- Push and open a PR

## Author
**Mantra Patil**

💼 LinkedIn: https://www.linkedin.com/in/mantrapatil25

✉️ techmantrapatil@gmail.com


<h3 align="center">⭐ If you found this project helpful, don’t forget to star the repo! ⭐</h3> <p align="center"> <img src="https://img.shields.io/badge/Keep%20Coding%20%26%20Stay%20Healthy!-Python-blue?style=for-the-badge&logo=python"> </p>
