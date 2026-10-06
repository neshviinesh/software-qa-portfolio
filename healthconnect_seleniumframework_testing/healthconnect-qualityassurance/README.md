# HealthConnect QA Automation Framework

An end-to-end (E2E) automated testing framework for the HealthConnect telehealth platform. Built with Python, Selenium WebDriver, and Pytest, this framework is engineered to test complex multiplayer workflows, including live WebRTC video consultations and dynamic React rendering.

## 🚀 Key Features

* **Dual-Driver WebRTC Testing:** Simulates simultaneous real-time interactions between Doctor and Patient sessions using a custom `dual_driver` Pytest fixture.
* **Media Stream Spoofing:** Bypasses hardware permissions to inject synthetic video/audio feeds using Chrome flags (`--use-fake-ui-for-media-stream`, `--use-fake-device-for-media-stream`).
* **Page Object Model (POM):** Centralized UI locators and methods for high maintainability and reduced code duplication.
* **Data-Driven Testing (DDT):** Leverages `@pytest.mark.parametrize` to execute exhaustive positive and negative validation matrices (e.g., login flows) within a single test block.
* **Intelligent Synchronization:** Implements explicit `WebDriverWait` strategies to handle React race conditions and asynchronous DOM updates.
* **Automated Visual Reporting:** Automatically generates self-contained HTML execution reports and embeds Base64 screenshots of the browser state upon test failure.
* **Parallel Execution:** Configured for multi-core test execution via `pytest-xdist` to drastically reduce suite execution time.

## 📁 Project Structure

```text
healthconnect-qualityassurance/
├── pages/                      # Page Object Model classes
│   ├── base_page.py            # Core Selenium wrapper methods
│   ├── login_page.py           # Authentication UI locators
│   └── doctor_dashboard_page.py# Dashboard locators
├── tests/                      # Pytest test suites
│   ├── test_webrtc_consultation.py # Multiplayer video E2E flow
│   ├── test_login_scenarios.py     # Parameterized negative login tests
│   └── test_doctor_schedule.py     # Profile & scheduling tests
├── config.py                   # Centralized environment variables & credentials
├── conftest.py                 # Pytest fixtures, browser setup, & reporting hooks
├── .gitignore                  # Git exclusion rules
└── README.md                   # Project documentation

```
## 🛠️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/healthconnect-qa.git
cd healthconnect-qa
```

2. **Install dependencies:**
Ensure you have Python 3.x installed, then run:
```bash
pip install selenium pytest pytest-html pytest-xdist
```

3. **Configure Environment Variables:**
Update the `config.py` file with your local or staging environment URLs and test credentials:
```python
# config.py
BASE_URL = "http://localhost:3000"
DOCTOR_EMAIL = "your_test_doctor@email.com"
PATIENT_EMAIL = "your_test_patient@email.com"
```

## 💻 Test Execution Commands

Run these commands in your terminal from the root directory of the project.

**Run the entire test suite:**
```bash
pytest tests/ -v
```

**Run a specific test file (e.g., the WebRTC flow):**
```bash
pytest tests/test_webrtc_consultation.py -v
```

**Run tests in parallel (cuts execution time in half):**
```bash
pytest tests/ -v -n auto
```

**Generate an HTML Test Report:**
```bash
pytest tests/ -v --html=report.html --self-contained-html
```

## 🧪 WebRTC Test Architecture

Testing the video consultation room requires two independent browser instances to negotiate a P2P connection via Cloudflare TURN servers. 

The `conftest.py` handles this by yielding a dictionary of independent WebDriver sessions:
```python
def test_webrtc_video_consultation(dual_driver):
    doctor = dual_driver["doctor"]
    patient = dual_driver["patient"]
    # ... navigation and validation logic
```
The framework injects synthetic green-screen video feeds into both browsers and utilizes JavaScript injection (`execute_script`) to query the HTML5 `<video>` element's `readyState` to assert that remote media frames are successfully rendering across the network.