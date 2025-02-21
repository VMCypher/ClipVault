# 🎬 ClipVault - YouTube Video Downloader 📥

**ClipVault** is a simple and intuitive application for **downloading YouTube videos** directly to your PC. Developed in **Python** with **KivyMD**, it offers a modern and user-friendly interface. 🚀

## ✨ Features
- ✅ **Download MP4 videos** in resolutions **4K, 1440p, 1080p, 720p, and 480p**
- ✅ **Automatically saves to the user's "Downloads" folder**
- ✅ **Clean and responsive interface made with KivyMD**
- ✅ **Compatible with Windows** (installable version via Inno Setup)

## 📌 How to Use
1️⃣ **Copy the YouTube video link**  
2️⃣ **Paste it into the URL field**  
3️⃣ **Select the desired resolution**  
4️⃣ **Click "Download MP4" and wait!**  

## 🛠 Technologies Used
- 🔹 **Python 3**
- 🔹 **Kivy & KivyMD** (Graphical interface)
- 🔹 **yt-dlp** (Video downloading)
- 🔹 **PyInstaller & Inno Setup** (Executable and installer creation)

## 🔽 Download and Installation
Download the latest version of **ClipVault** from the [Releases](https://github.com/VMCypher/ClipVault/releases) tab.

### 📥 Installation
1. Download the `ClipVault_Setup.exe` installer from the Releases tab.
2. Run the installer and follow the instructions.
3. After installation, open **ClipVault** and start downloading your videos!

## 🛠 Creating Executables
To generate the standalone `.exe` file, use the following commands:

```sh
# Generate a single-file executable
pyinstaller --noconsole --windowed --onefile --icon="assets/icon.ico" --hidden-import=kivymd ClipVault.py

# Generate an executable with dependencies in a separate folder
pyinstaller --noconsole --windowed --icon="assets/icon.ico" --hidden-import=kivymd ClipVault.py
```

To create the **installer** using Inno Setup, follow these steps:
1. Open **Inno Setup Compiler**.
2. Load the `ClipVault.iss` script.
3. Compile to generate `ClipVault_Setup.exe`.

### 🎨 Interface
![ClipVault Interface](https://github.com/VMCypher/ClipVault/blob/main/screenshot/interface.png)


## 🤝 Contributing
If you want to contribute with improvements, open an **issue** or submit a **pull request**! 
![Discord](https://img.shields.io/badge/Discord-vmcypher-7289DA?style=for-the-badge&logo=discord)

## 📢 Follow and contribute on GitHub!
🔗 [https://github.com/VMCypher/ClipVault](https://github.com/VMCypher/ClipVault)


