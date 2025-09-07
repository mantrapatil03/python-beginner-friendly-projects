## 🗂️ File Organizer Script (Python)

A simple Python script to automatically **organize files** in a directory into subfolders based on their file types (extensions).  
No more messy folders — everything is sorted neatly!

---

## ⚙️ How It Works
1. You input the folder path you want to organize.
2. The script scans all files in that directory (ignores subfolders).
3. It moves files into subfolders based on their extensions:
   - **Images** → `.jpg, .jpeg, .png, .gif, .bmp, .tiff`
   - **Documents** → `.pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx`
   - **Audio** → `.mp3, .wav, .aac, .flac`
   - **Videos** → `.mp4, .mov, .avi, .mkv`
   - **Archives** → `.zip, .rar, .tar, .gz, .7z`
   - **Scripts** → `.py, .js, .html, .css, .sh, .bat`
   - **Others** → Any file type not listed above
4. Files with unknown extensions are moved into an **"Others"** folder.

---

## 🚀 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   
2.Run the script:


```python file_organizer.py```

3.Enter the folder path when prompted:

```
Enter the path of the folder to organize: /home/user/Downloads
```
4.Done ✅ Your files will be sorted into subfolders.

## 📌 Example

Before:
```
javascript
Downloads/
├── photo1.jpg
├── song.mp3
├── document.pdf
├── script.py
```

After running the script:
```
arduino
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

## ⚠️ Notes
This script moves files (not copies), so double-check before running it on important directories.

Make sure you have permissions to modify the target folder.

## 🔮 Future Improvements
Add support for more file categories (fonts, executables, etc.).

Option for copying instead of moving files.

GUI version for easier use.

## 👨‍💻 Author
Mantra Patil

Engineering Student | Python Developer (Learning) | Cybersecurity Enthusiast


