# Contributing to Google Forms Auto-Submitter

First off, thank you for considering contributing to this project! 🎉

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, CSV data, form URL if possible)
- **Describe the behavior you observed** and what you expected
- **Include screenshots** if relevant
- **Include your environment details** (Python version, OS, Chrome version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any similar features** in other tools

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure your code follows the existing style
4. Update the documentation if needed
5. Write a clear commit message

## Development Setup

```bash
# Clone your fork
git clone https://github.com/dabloo26/google-forms-automation.git
cd google-forms-automation

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make your changes
# Test your changes

# Commit and push
git add .
git commit -m "Description of changes"
git push origin your-branch-name
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Add docstrings to functions

## Testing

Before submitting:

```bash
# Test with small batch (5-10 rows)
START_ROW = 0
END_ROW = 10

# Run the script
python3 google_form_complete.py
```

## Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

## Questions?

Feel free to open an issue with your question or reach out at abhyanshsri@gmail.com

Thank you for contributing! 🚀
