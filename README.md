# Yahboom Raspberry Pi Line-Following Robot

## Overview

This repository contains materials for setting up and running a Yahboom Raspberry Pi line-following robot:

- **Slides**: A PowerPoint deck detailing how to connect to the robot via PuTTY.
- **Documentation**: PDF guides explaining the business logic, code structure, and usage.
- **Code**: The Python script that implements the line-following behavior.

---

## Repository Structure

```plaintext
├── slides/
│   └── Yahboom_Pi_Putty_Connection.pptx    # PuTTY connection tutorial slides
├── docs/
│   ├── line_following_documentation.pdf   #  PDF documentation
├── code/
│   └── line_following.py                  # Main Python line-following script
├── img/
│   └── imges                 # Images and assets (wiring diagrams, screenshots)
└── README.md                              # This file
```

---

## Requirements

- **Hardware**: Yahboom Raspberry Pi Robot Kit with motors, IR sensors, start button.
- **Software**:
  - Python 3
  - RPi.GPIO library (`pip install RPi.GPIO`)
  - `python-pptx` for slide generation (if modifying slides) (`pip install python-pptx`)
  - `reportlab` for PDF generation (if regenerating docs) (`pip install reportlab`)
  - PuTTY (Windows) or any SSH client


---

## Usage

### 1. Slides

Open `slides/Yahboom_Pi_Putty_Connection.pptx` in PowerPoint or a compatible viewer to see step-by-step instructions for connecting via PuTTY.

### 2. Documentation

Open the PDF files in the `docs/` folder for detailed explanations of the code, hardware pin mapping, and control logic.

### 3. Code

1. Wire your robot kit according to the pin mapping in the documentation.
2. Copy `code/line_following.py` to your Raspberry Pi.
3. Install dependencies:
   ```bash
   pip install RPi.GPIO
   ```
4. Run the script with root privileges:
   ```bash
   sudo python3 line_following.py
   ```
5. Press the start button to begin line following.


---

## Authors

- Abdulahdy Abas Abdullah
- Hussein Mohammed Ali

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
