# ReqRes.in API Automation Tests

API automation tests for `https://reqres.in/api/users` using **SeleniumBase** with undetected Chrome Driver to bypass Cloudflare protection.

## Overview

This project demonstrates automated API testing for the reqres.in `GET /api/users` endpoint with Cloudflare bypass using SeleniumBase's undetected-chromedriver mode. Includes video recording capability using pyscreenrec.

## The Problem

Cloudflare actively blocks automated browser testing tools (Playwright, Selenium, Puppeteer) with "Just a moment..." challenge pages. Traditional stealth plugins are often detected.

## The Solution: SeleniumBase

**SeleniumBase** uses `undetected-chromedriver` which:
- Patches Chrome to avoid bot detection
- Mimics real browser fingerprint
- Bypasses Cloudflare challenges automatically
- No manual session capture required

## Project Structure

```
reqres-api-tests/
├── test_record_video.py    # All 18 test cases with video recording
├── pytest.ini              # Pytest configuration
├── manual-test-cases.md    # Test documentation
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.11+
- Chrome/Chromium browser

### Install Dependencies

```bash
python -m pip install seleniumbase pytest pyscreenrec
```

SeleniumBase will automatically download the required ChromeDriver on first run.

**pyscreenrec** is used for video recording test sessions.

## Running Tests

### Run All Tests with Video + HTML Report

```bash
python test_record_video.py
```

This runs all 18 tests with:
- Video recording (saved to `videos/` folder)
- HTML report (saved to `test-report.html`)
- Browser visible in headed mode

### Run Specific Test

```bash
# Run TC001 only with video
python -m pytest test_record_video.py::TestVideoRecord::test_tc001_with_video -v --uc --headed
```

**Video Recording Features:**
- Runs all 18 test cases with video recording
- Saves videos to `videos/` folder with descriptive names
- Generates HTML report (test-report.html)
- Displays browser window during recording
- No environment variables needed (works on Windows, Linux, Mac)

## Command Options

| Flag | Description |
|------|-------------|
| `--uc` | Enable undetected-chromedriver mode (bypasses Cloudflare) |
| `--headed` | Show browser window (required for video recording) |
| `--html=report.html` | Generate HTML report |
| `--self-contained-html` | Create self-contained HTML report |
| `--screenshots` | Capture screenshots on test failure |
| `-v` | Verbose output |

## Test Coverage

| Category | Tests | Description |
|----------|-------|-------------|
| Valid Requests | 2 | TC001, TC002 - Normal page requests |
| Invalid Pages | 5 | TC003-TC007 - Zero, negative, large, invalid inputs |
| Metadata | 4 | TC008-TC010 - Pagination, support, headers |
| Edge Cases | 7 | TC011-TC017 - Multiple params, SQL injection, special chars |
| Data Validation | 2 | TC014-TC015 - Email, avatar validation |
| Extra Params | 1 | TC018 - Extra query parameters |

**Total: 18 test cases (100% pass rate)**

## Test Results Summary

| Test Case | Status | Description |
|-----------|--------|-------------|
| TC001 | ✅ PASSED | Valid request with page=2 |
| TC002 | ✅ PASSED | Valid request with page=1 |
| TC003 | ✅ PASSED | Page 0 defaults to page 1 |
| TC004 | ✅ PASSED | Negative page returns -1 |
| TC005 | ✅ PASSED | Page 999 returns empty data |
| TC006 | ✅ PASSED | No page parameter defaults to 1 |
| TC007 | ✅ PASSED | Invalid data type defaults to 1 |
| TC008 | ✅ PASSED | Pagination metadata correct |
| TC009 | ✅ PASSED | Support object exists |
| TC010 | ✅ PASSED | Response headers valid |
| TC011 | ✅ PASSED | Multiple page parameters handled |
| TC012 | ✅ PASSED | Empty page parameter defaults to 1 |
| TC013 | ✅ PASSED | SQL injection attempt handled safely |
| TC014 | ✅ PASSED | All emails have valid format |
| TC015 | ✅ PASSED | All avatar URLs are valid |
| TC016 | ✅ PASSED | Decimal page rounds to 1 |
| TC017 | ✅ PASSED | Special characters default to 1 |
| TC018 | ✅ PASSED | Extra parameters ignored |

## API Behavior Notes

| Input | API Response |
|-------|--------------|
| `page=0` | Defaults to page 1 |
| `page=-1` | Returns -1 |
| `page=999` | Returns empty data array |
| `page=abc` | Defaults to page 1 |
| `page=1.5` | Rounds to page 1 |
| `page=!@#$%` | Defaults to page 1 |
| No page param | Defaults to page 1 |

## Configuration

### pytest.ini

```ini
[pytest]
python_files = test_*.py
python_classes = Test*
python_functions = test_*

addopts = -v --strict-markers
console_output_style = classic

markers =
    skip: Skip test
    slow: Mark test as slow
```

## Troubleshooting

### "ChromeDriver not found" error

SeleniumBase will automatically download ChromeDriver on first run. If it fails:

```bash
sbase install chromedriver
```

### Cloudflare still blocking

The `--uc` flag enables undetected-chromedriver mode which should bypass Cloudflare. If still blocked:

1. Make sure you're using the latest SeleniumBase: `pip install -U seleniumbase`
2. Try running with `--headed` to see what's happening
3. Check if Cloudflare has changed their protection

### Tests timing out

Increase timeout in test or run specific tests:

```bash
# Run single test with time limit
python -m pytest test_record_video.py::TestVideoRecord::test_tc001_with_video -v --uc --headed --time-limit=60
```

## References

- [SeleniumBase Documentation](https://seleniumbase.com/)
- [Undetected Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
- [Pytest HTML Reports](https://pytest-html.readthedocs.io/)
- [Video Recording in Python - The Green Report](https://www.thegreenreport.blog/articles/from-code-to-video-recording-selenium-test-sessions-in-python/from-code-to-video-recording-selenium-test-sessions-in-python.html)
- [ReqRes.in API](https://reqres.in/)

## License

MIT
