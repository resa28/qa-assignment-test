# SauceDemo Automation

A test automation framework built with **Katalon Studio** for end-to-end testing of the [SauceDemo](https://www.saucedemo.com/) e-commerce application.

## Overview

This project implements **Page Object Model (POM)** principles to automate login functionality testing across multiple scenarios including successful authentication, failed login attempts, and UI validation.

## Test Scenarios

| Scenario | Description |
|----------|-------------|
| Valid Login | Verifies successful authentication with products page |
| Invalid Credentials | Validates error message display |
| UI Verification | Confirms dashboard, menu, and product elements |
| ENTER Key Login | Tests form submission via keyboard |

## Project Structure

```
SauceDemo_Automation/
├── Test Cases/         # Test case definitions (.tc)
├── Scripts/            # Groovy implementation logic
├── Object Repository/  # Page objects with XPath selectors
├── Data Files/         # Test data references (Excel)
└── Profiles/           # Execution profiles
```

## Page Objects

| Element | Locator |
|---------|---------|
| Username | `//input[@id='user-name']` |
| Password | `//input[@id='password']` |
| Login Button | `//input[@id='login-button']` |
| Products Label | `//span[text()='Products']` |
| Error Message | `//h3[@data-test='error']` |

## Execution

### Via Katalon Studio GUI
```
File → Open Project → Select Project Directory
Test Cases → SauceDemo → TC_Login_All_Scenarios → Run
```

### Via Command Line
```bash
kataloc -noSplash -runMode=console \
  -projectPath=$(pwd)/SauceDemo_Automation.prj \
  -testCasePath="Test Cases/SauceDemo/TC_Login_All_Scenarios" \
  -browserType=Chrome
```

### Via Gradle
```bash
gradle katalonExecute
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Katalon Studio 10.3.2 |
| Language | Groovy (Java 17) |
| Engine | Selenium WebDriver |
| Locators | XPath |
| Build | Gradle with Katalon Plugin |
