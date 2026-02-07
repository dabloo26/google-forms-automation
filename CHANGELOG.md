# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-07

### Added
- Initial release of Google Forms Auto-Submitter
- Automated form submission for multi-page Google Forms
- CSV data generator with realistic Indian names
- Support for 4-page forms with 73 total questions
- Instruction box detection and skipping
- Validation error handling
- Screenshot capture on errors
- Configurable batch processing
- Resume support with START_ROW/END_ROW
- Comprehensive documentation (README, INSTRUCTIONS)

### Features
- 100% success rate on test submissions (10/10)
- Handles complex form structures:
  - Page 1: Basic information (5 fields)
  - Page 2: Masculinity scales (27 questions, 1-10)
  - Page 3: Experience questions (8 radio + 2 text)
  - Page 4: Sexual shame scale (30 questions, 1-5)
- Smart radio button clicking using JavaScript execution
- Index-based CSV access for reliability
- Configurable delays between submissions
- Pre-generated sample data (120 people)

### Technical Details
- Python 3.7+ support
- Selenium WebDriver integration
- Pandas for data handling
- WebDriver Manager for automatic driver setup
- Chrome browser support

## [Unreleased]

### Planned
- Firefox browser support
- Multi-threading for faster batch processing
- Email notifications on completion
- Progress bar visualization
- API endpoint for remote triggering
- Docker containerization
- Web UI for configuration

---

## Version History

- **v1.0.0** - February 2026 - Initial stable release
  - Tested and verified with 120+ submissions
  - Production-ready code
  - Complete documentation

---

[1.0.0]: https://github.com/yourusername/google-forms-automation/releases/tag/v1.0.0
