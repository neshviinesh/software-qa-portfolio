import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config
from pytest_html import extras

def _get_chrome_options():
    """Helper function to centralize browser configuration."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # for WebRTC - bypasses camera/mic prompts by injecting fake stream
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--use-fake-device-for-media-stream")

    return chrome_options


@pytest.fixture(scope="function")
def driver():
    """Standard fixture for single-player tests."""
    driver = webdriver.Chrome(options=_get_chrome_options())
    driver.implicitly_wait(Config.IMPLICIT_WAIT)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def dual_driver():
    """Spins up TWO independent Chrome instances for multiplayer WebRTC testing."""
    options = _get_chrome_options()

    # 1. initialize doctor browser
    doctor_driver = webdriver.Chrome(options=options)
    doctor_driver.implicitly_wait(Config.IMPLICIT_WAIT)

    # 2. initialize patient browser
    patient_driver = webdriver.Chrome(options=options)
    patient_driver.implicitly_wait(Config.IMPLICIT_WAIT)

    # yield both drivers
    yield {
        "doctor": doctor_driver,
        "patient": patient_driver
    }

    # 3. teardown both patinet and doctor
    doctor_driver.quit()
    patient_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Intercepts test failures and attaches screenshots to the HTML report."""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # Only trigger if the test actually fails during the execution phase
    if report.when == "call" and report.failed:

        # 1. to handle standard single-player tests
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_base64()
            extra.append(extras.image(screenshot, "Screenshot"))

        # 2. to handle multiplayer webrtc tests
        dual_driver = item.funcargs.get("dual_driver")
        if dual_driver:
            doc_img = dual_driver["doctor"].get_screenshot_as_base64()
            pat_img = dual_driver["patient"].get_screenshot_as_base64()
            extra.append(extras.image(doc_img, "Doctor's View"))
            extra.append(extras.image(pat_img, "Patient's View"))

        report.extra = extra