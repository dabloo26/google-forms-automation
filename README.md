# 🤖 Google Forms Auto-Submitter

> Automated form submission tool for Google Forms using Selenium WebDriver with 100% success rate

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: Python](https://img.shields.io/badge/code%20style-python-blue.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/dabloo26/google-forms-automation/graphs/commit-activity)

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [How It Works](#-how-it-works)
- [Performance](#-performance)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- 🎯 **100% Success Rate** - Tested with 120 submissions
- 🚀 **Automated Submission** - Handles multi-page forms automatically
- 📊 **CSV Data Generator** - Creates realistic test data with Indian names
- 🛡️ **Error Handling** - Built-in validation and retry mechanisms
- 📸 **Debug Screenshots** - Automatically saves screenshots on errors
- ⚡ **Configurable** - Easy to adjust delays, batch sizes, and data
- 🔄 **Resume Support** - Continue from where you stopped
- 📝 **Comprehensive Logging** - Track every submission attempt

## 🎥 Demo

![Terminal Output](screenshots/terminal_output.png)

```bash
$ python3 google_form_complete.py

======================================================================
SUBMISSION #119: Karan Singh
======================================================================

📄 PAGE 1: Basic Info
  ✓ All fields filled
  ✓ Clicked Next!

📄 PAGE 2: Masculinity Scales (1-10)
  ✅ Filled 27/27 scales
  ✓ Clicked Next!

📄 PAGE 3: Experience Questions
  ✅ Completed 11/11 items
  ✓ Clicked Next!

📄 PAGE 4: Self-Assessment (1-5)
  ✅ Filled 30/30 scales

✅ Ready to submit...
  ✓ Form submitted!

🎉 SUCCESS #119!

⏳ Waiting 7.8s...
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- Internet connection

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/dabloo26/google-forms-automation.git
cd google-forms-automation

# Install required packages
pip install -r requirements.txt
```

## ⚡ Quick Start

### Option 1: Use Pre-Generated Data

```bash
# Run with included sample data (120 people)
python3 google_form_complete.py
```

### Option 2: Generate Custom Data

```bash
# Generate new data
python3 generate_form_data.py

# Enter desired number of responses
How many responses to generate? (default 100): 200

# Run the submitter
python3 google_form_complete.py
```

## 📖 Usage

### Basic Usage

```python
# Process all rows in CSV
START_ROW = 0
END_ROW = len(df)
```

### Process Specific Range

```python
# Process rows 1-50
START_ROW = 0
END_ROW = 50

# Process rows 51-100
START_ROW = 50
END_ROW = 100
```

### Adjust Submission Speed

```python
# Slower (safer for large batches)
delay = random.uniform(10, 15)

# Faster (may trigger rate limits)
delay = random.uniform(3, 5)
```

## 📁 Project Structure

```
google-forms-automation/
│
├── google_form_complete.py       # Main automation script
├── generate_form_data.py          # CSV data generator
├── FormResponses_120_People.csv   # Sample data (120 people)
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── INSTRUCTIONS.md                # Detailed documentation
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
│
├── screenshots/                   # Project screenshots
│   └── terminal_output.png
│
└── examples/                      # Example outputs
    └── sample_output.txt
```

## ⚙️ Configuration

### Update CSV Path

```python
# In google_form_complete.py
csv_path = 'FormResponses_120_People.csv'  # Relative path (recommended)
```

### Change Rows to Process

```python
START_ROW = 0    # First row (0-indexed)
END_ROW = 120    # Last row
```

### Adjust Delays

```python
delay = random.uniform(5, 8)  # Seconds between submissions
```

## 🔧 How It Works

The form has 4 pages with 73 total questions:

| Page | Questions | Type | Total |
|------|-----------|------|-------|
| 1 | Basic Info | Text + Radio | 5 |
| 2 | Masculinity Scales | 1-10 Scale | 27 |
| 3 | Experience Questions | Radio + Text | 11 |
| 4 | Sexual Shame Scale | 1-5 Scale | 30 |

### Key Features

- **Instruction Box Detection** - Automatically skips non-question elements on Pages 2, 3, and 4
- **Index-Based CSV Access** - Reliable data mapping using column indices
- **Smart Clicking** - Uses JavaScript execution for reliable radio button selection
- **Validation Handling** - Checks for errors and saves debug screenshots

## 📊 Performance

| Batch Size | Time | Recommendation |
|------------|------|----------------|
| 10 | 3-4 min | ✅ Quick test |
| 50 | 17-20 min | ✅ Small batch |
| 100 | 35-40 min | ⚠️ Monitor closely |
| 120 | 42-45 min | ⚠️ Full dataset |

**Average:** ~20-25 seconds per submission (including 5-8 second delays)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Selenium WebDriver](https://www.selenium.dev/)
- Data handling with [Pandas](https://pandas.pydata.org/)
- Developed for research in social sciences

## 📞 Contact

**Abhyansh Anand**

- GitHub: [@dabloo26](https://github.com/dabloo26)
- Email: abhyanshsri@gmail.com

## ⭐ Support

If this project helped you, please give it a ⭐ star!

---

**Note:** This tool is intended for legitimate research and testing purposes. Always ensure you have permission to submit data to any form you're automating.
