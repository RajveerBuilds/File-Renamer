# 🧠 File Renamer Automation Script (Interactive Version)

A simple *Python automation script* that automatically renames all files in a chosen folder while keeping their original file extensions.  
This version is *interactive*, meaning you just enter the folder path when you run it — no code editing needed.

---

## 🚀 Features
- Renames all files in any selected folder
- Keeps original file extensions (.txt, .jpg, .pdf, etc.)
- Skips subfolders and hidden files
- Asks before performing any renaming (safe confirmation)
- Simple, clean console interface with user prompts
- No external libraries required

---

## 🧩 How It Works
The script uses Python’s built-in **os** module to:
1. Ask you to enter a folder path
2. Check if the folder exists and list all files inside it
3. Split each filename into name and extension
4. Rename each file sequentially (e.g., renamed_0.txt, renamed_1.pdf, etc.)
5. Show progress and confirmation for every renamed file

---

## 🧰 Technologies Used
- *Language:* Python 3  
- *Libraries:* os (built-in, no installation needed)

---

## 🧪 How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/RajveerBuilds/File-Renamer.git

---

## 🧠 Example Output 
- File Renamer Automation Script
This script renames all files in a folder while keeping their extensions.

👉 Enter the full folder path: C:\Users\Rajveer\Desktop\testfolder

Found files in 'C:\Users\Rajveer\Desktop\testfolder':
1. notes.pdf
2. photo.txt
3. video.jpg

Proceed with renaming? (y/n): y
notes.pdf -> renamed_0.pdf
photo.txt -> renamed_1.txt
video.jpg -> renamed_2.jpg

✅ All files renamed successfully!

---

## 🧠 Future Improvements
- Add undo feature
- Build a GUI version

---

## 👨‍💻 Author
*Rajveer Jaiswal*  
First-year Software Engineering student at NIAT Jaipur  
Learning automation, AI, and real-world software development.