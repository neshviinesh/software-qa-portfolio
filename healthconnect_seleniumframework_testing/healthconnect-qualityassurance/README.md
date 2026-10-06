# 🏥 HealthConnect: End-to-End QA Automation Framework

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

## 📌 Project Overview
A robust, scalable E2E test automation framework engineered to validate the core user journeys of **HealthConnect**—a cloud-native telehealth web application built with React, WebRTC, and Supabase. 

This framework is designed for high reliability in modern, state-heavy dynamic web environments, specifically tackling complex automation challenges like native component bypassing and React DOM state injection.

## 🚀 Key Framework Features
* **Page Object Model (POM) Architecture:** Strict separation of test logic from page-specific element locators and interaction methods, ensuring high maintainability and code reuse.
* **React State Injection & DOM Manipulation:** Utilizes custom JavaScript execution within Selenium to forcefully trigger React `onChange` and `onInput` event listeners, bypassing restrictive native browser elements (e.g., Chrome date pickers) for deterministic test execution.
* **Parallel Test Execution:** Configured with `pytest-xdist` to run test suites concurrently across multiple workers, drastically reducing CI/CD pipeline execution time.
* **Dynamic Wait Strategies:** Implementation of explicit `WebDriverWait` conditions to handle dynamic React rendering and async API fetches without relying on fragile hard-coded sleep methods.
* **Automated Evidence Generation:** Integrated with `pytest-html` to automatically generate rich HTML execution reports with embedded screenshots upon test failure.

## 🛠️ Technology Stack
* **Language:** Python 3.14
* **Browser Automation:** Selenium WebDriver
* **Test Runner:** Pytest
* **Parallelization:** Pytest-Xdist
* **Reporting:** Pytest-HTML

## 📂 Framework Architecture
```text
01-HealthConnect-QA/
│
├── pages/                  # Page Object classes (UI locators & methods)
│   ├── base_page.py        # Core WebDriver interactions and explicit waits
│   ├── login_page.py       # Authentication flows
│   └── calendar_page.py    # Appointment scheduling & React date injection
│
├── tests/                  # Pytest execution scripts
│   ├── conftest.py         # WebDriver initialization and Pytest hooks
│   └── test_patient_booking.py # E2E patient scheduling journey
│
├── assets/                 # Test execution evidence and documentation
│   └── report.pdf          
│
└── pytest.ini              # Framework configuration and CLI flags
```

## 🧪 Core E2E Scenarios Validated
**Patient Appointment Booking Flow:**
1. Secure patient authentication and consent verification.
2. Dashboard navigation and dynamic Doctor List rendering.
3. Doctor profile validation and calendar access.
4. **Complex UI Interaction:** Date injection via JS to bypass native OS pickers, fetching available time slots.
5. Exact time slot selection and booking confirmation via dynamic XPaths.

## 📊 Test Execution & Reporting
This framework automatically captures the DOM state and screenshots at the exact moment of failure for rapid debugging.

**Visual Proof of Execution:**
> 📄 [Download the full PDF Test Execution Report](./assets/report.pdf)

