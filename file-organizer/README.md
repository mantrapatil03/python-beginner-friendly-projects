<h1 align="center"> File Organizer Script (Python)</h1>

<p align="center">
A smart and lightweight <b>Python automation script</b> that automatically <b>organizes your files</b> into categorized subfolders based on their extensions.  
Say goodbye to messy "Downloads" folders — everything gets sorted neatly in seconds! 
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Automation-Script-green?style=for-the-badge&logo=autohotkey"></a>
  <a href="#"><img src="https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20MacOS-orange?style=for-the-badge&logo=linux"></a>
  <a href="https://github.com/mantrapatil03/python-beginner-friendly-projects"><img src="https://img.shields.io/github/stars/mantrapatil03/python-beginner-friendly-projects?style=for-the-badge&logo=github"></a>
</p>

---

## How It Works

1️⃣ You input the **folder path** you want to organize.  
2️⃣ The script scans all files (ignoring subfolders).  
3️⃣ It creates subfolders based on file types and **moves** files accordingly:  

| Category | File Extensions |
|-----------|----------------|
|  **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff` |
|  **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx` |
|  **Audio** | `.mp3`, `.wav`, `.aac`, `.flac` |
|  **Videos** | `.mp4`, `.mov`, `.avi`, `.mkv` |
|  **Archives** | `.zip`, `.rar`, `.tar`, `.gz`, `.7z` |
|  **Scripts** | `.py`, `.js`, `.html`, `.css`, `.sh`, `.bat` |
|  **Others** | Any unrecognized file type |

 Files with unknown or uncommon extensions are moved into an **“Others”** folder.  

---

##  Usage Guide

### 1️⃣ Clone this repository:
```bash
git clone https://github.com/mantrapatil03/python-beginner-friendly-projects.git
cd python-beginner-friendly-projects/file-organizer
```
### 2️⃣ Run the script:
```
python file_organizer.py
```
3️⃣ Enter your target folder path:
```
Enter the path of the folder to organize: /home/user/Downloads
```
✅ Done! Your files will now be automatically categorized into subfolders.

## Example Output
Before:
```javascript
Downloads/
├── photo1.jpg
├── song.mp3
├── document.pdf
├── script.py
```

After:
```arduino
Downloads/
├── Images/
│   └── photo1.jpg
├── Audio/
│   └── song.mp3
├── Documents/
│   └── document.pdf
├── Scripts/
│   └── script.py
```

### ⚠️ Notes

- This script moves files (does not copy).
- Make sure you have write permissions for the directory.
- Always test on a small sample folder first to verify results.

## Author
**Mantra Patil**

💼 LinkedIn: https://www.linkedin.com/in/mantrapatil25

✉️ techmantrapatil@gmail.com


<h3 align="center">✨ If you found this useful, consider giving it a ⭐ on GitHub! ✨</h3> <p align="center"> <img src="https://img.shields.io/badge/Stay%20Organized%20%26%20Keep%20Coding!-Python-blue?style=for-the-badge&logo=python"> </p>
