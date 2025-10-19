<h1 align="center"> Advanced To-Do List Application (Python)</h1>

<p align="center">
  A modern, interactive, and beginner-friendly <b>Command-Line To-Do List App</b> written in <b>Python</b> .  
  Manage your daily tasks efficiently — add, view, complete, and delete tasks — all from your terminal!  
  Built with scalability, simplicity, and future upgrades in mind. 
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python"></a>
  <a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/Editor-VS%20Code-0078D4?style=for-the-badge&logo=visualstudiocode&logoColor=white"></a>
  <a href="https://github.com/mantrapatil03/python-beginner-friendly-projects/stargazers"><img src="https://img.shields.io/github/stars/mantrapatil03/python-beginner-friendly-projects?style=for-the-badge&logo=github"></a>
  <a href="https://github.com/mantrapatil03/python-beginner-friendly-projects/network/members"><img src="https://img.shields.io/github/forks/mantrapatil03/python-beginner-friendly-projects?style=for-the-badge&logo=git"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white"></a>
  <a href="#"><img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge&logo=github"></a>
</p>

---

##  Key Features

-  **View All Tasks** – Instantly see all your tasks with status icons (`[✔]` or `[✗]`)  
-  **Add Tasks** – Add unlimited tasks dynamically  
-  **Mark as Completed** – Update task progress easily  
-  **Delete Tasks** – Remove finished or unnecessary items  
-  **Auto Save (Upcoming)** – Persist tasks in a local `.json` or `.csv` file  
-  **Priority Levels (Upcoming)** – Assign high/medium/low importance tags  
-  **Due Date Tracking (Upcoming)** – Stay ahead of deadlines  
-  **Colorful UI** – Optional color themes for a better CLI experience  
-  **Exit Gracefully** – Clean shutdown and data handling  

---

##  Tech Stack

| Technology | Purpose |
|-------------|----------|
| **Python 3** | Core logic and CLI |
| **os & sys modules** | Handle input/output and screen clearing |
| **JSON / CSV (future)** | Data persistence |
| **Colorama (optional)** | Add color to CLI output |

---

##  Installation & Setup

###  Prerequisites
Make sure you have **Python 3.10+** installed:
```bash
python --version
```

## Run the Application
```
# Clone the repository
git clone https://github.com/mantrapatil03/python-beginner-friendly-projects.git

# Navigate to the To-Do List project
cd python-beginner-friendly-projects/todo-list

# Run the app
python todo.py
```

> ptional: Install `colorama` for colored terminal output
> ```
> pip install colorama
> ```

###  Example Demo
```
✅ To-Do List Menu
─────────────────────────────
1. View Tasks
2. Add Task
3. Mark Task as Completed
4. Delete Task
5. Exit
─────────────────────────────
Choose an option: 2
Enter task description: Build Python To-Do App
📌 Task added successfully!

✅ To-Do List Menu
Choose an option: 1

Your Tasks:
1. [✗] Build Python To-Do App
```
###  Example Code Snippet
```
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def show_tasks():
    if not tasks:
        print("🕳️ No tasks yet!")
    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["completed"] else "✗"
        print(f"{i}. [{status}] {t['task']}")
```

##  Future Roadmap
| Feature                  | Status         | Description                      |
| ------------------------ | -------------- | -------------------------------- |
|  File storage (JSON)   |  In Progress | Save and load tasks persistently |
| Task count summary    |  Done         | Shows total & completed tasks    |
|  Due dates & priorities |  Planned     | Add deadlines and importance     |
|  GUI (Tkinter)         |  Planned     | Simple desktop interface         |
|  Flask/Django web app  |  Planned     | Full-stack upgrade               |



###  Contributing

Contributions are always welcome
- Fork the repo
- Create a new branch:
      ```
      git checkout -b feature/your-feature
      ```
- Commit & Push your changes
- Open a Pull Request
> Please follow Python’s PEP8 guidelines and include meaningful commit messages.

##  Author
**Mantra Patil**

💼 LinkedIn: https://www.linkedin.com/in/mantrapatil25

✉️ techmantrapatil@gmail.com

<h3 align="center">🌟 Thanks for checking out my Advanced To-Do List project! 🌟</h3> <p align="center"> If you found this useful, please give it a ⭐ on GitHub — it helps a lot! <br><br> <img src="https://img.shields.io/badge/Keep%20Building-Build%20with%20Python-orange?style=for-the-badge&logo=python"> </p>

<p align="center"> <img src="https://img.shields.io/badge/Made%20With-Python3-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/Platform-Cross%20Platform-brightgreen?style=for-the-badge&logo=windows"> <img src="https://img.shields.io/badge/Status-Active%20Development-orange?style=for-the-badge&logo=githubactions"> <img src="https://img.shields.io/badge/Code%20Style-PEP8-blueviolet?style=for-the-badge&logo=python"> </p>

