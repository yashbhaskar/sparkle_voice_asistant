# **Intelligent Personal Assistant with Facial Recognition and Voice Commands**

![Project Overview](images/project_overview.png)  
*Figure 1: Project Overview*

---

## 🌟 **Overview**
This project integrates **facial recognition**, **voice commands**, and **system automation** to create a hands-free **personal assistant**. It provides an interactive and secure way to perform tasks like web searches, system control, and real-time updates.

---

## ✨ **Features**
1. **Facial Recognition**  
   - Secure access using the `face_recognition` library.
   - Matches live webcam footage with pre-saved images.

2. **Voice Command Processing**  
   - Uses `speech_recognition` for listening and `pyttsx3` for responding.
   - Executes tasks like system operations and web searches.

3. **Task Automation**  
   - Automates tasks such as shutting down, restarting, taking screenshots, and more.

4. **Real-Time Updates**  
   - Provides real-time updates like date, time, and weather conditions.

5. **Interactive Utilities**  
   - Volume control, media playback, and notifications.

---

## 🛠️ **Tech Stack**
- **Programming Language:** Python
- **Libraries Used:**
  - `face_recognition` - Facial recognition.
  - `speech_recognition` - Voice command processing.
  - `pyttsx3` - Text-to-speech.
  - `pyautogui` - System automation.
  - `cv2` - Image processing.
  - `webbrowser` - Web integration.

---

## 📂 **Project Structure**
```plaintext
📦 Project Directory
├── main.py                  # Main script
├── images/                  # Directory for images
│   ├── project_overview.png # Overview image
│   └── assistant_demo.png   # Demo image
├── requirements.txt         # Dependencies
└── README.md                # Readme file
