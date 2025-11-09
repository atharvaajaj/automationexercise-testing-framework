import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
import os
from pathlib import Path
import pytest

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# ---------- CLI option ----------
def pytest_addoption(parser):
    parser.addoption(
        "--screenshots",
        action="store",
        default="failed",  # choose: failed | all | none
        help="Screenshot policy: failed (default), all, or none",
    )

# ---------- hook to capture screenshots ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Save screenshots according to --screenshots policy and attach to pytest-html if available.
    Expects a fixture named `driver`.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when != "call":
        return

    policy = item.config.getoption("--screenshots") or "failed"
    want = (policy == "all") or (policy == "failed" and rep.failed)
    if not want:
        return

    driver = item.funcargs.get("driver", None)
    if not driver:
        return

    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    base = item.nodeid.replace("/", "_").replace("\\", "_").replace("::", "__")
    status = "passed" if rep.passed else "failed"
    png_path = screenshots_dir / f"{base}__{status}.png"

    try:
        driver.save_screenshot(str(png_path))
        print(f"\n📸 Screenshot saved: {png_path}")
    except Exception as e:
        print(f"\n⚠️ Could not save screenshot: {e}")
        return

    plugin = item.config.pluginmanager.getplugin("html")
    if plugin:
        extra = getattr(rep, "extra", [])
        try:
            img_bytes = png_path.read_bytes()
            extra.append(plugin.extras.image(img_bytes, mime_type="image/png"))
        except Exception:
            extra.append(plugin.extras.url(png_path.as_posix()))
        rep.extra = extra


import pytest
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to get the report object
    outcome = yield
    rep = outcome.get_result()

    # Only capture screenshot for failed tests
    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, "driver", None)
        if driver is not None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = f"screenshots/{screenshot_name}"
            driver.save_screenshot(screenshot_path)
            # Attach to HTML report
            if hasattr(item.config, "_html"):
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                rep.extra = extra

# Register pytest-html for extra screenshots
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

# conftest.py
import os
from pathlib import Path
from datetime import datetime
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots for ALL tests (passed + failed) and embed in pytest-html."""
    outcome = yield
    rep = outcome.get_result()

    # only after test body runs
    if rep.when != "call":
        return

    # get driver fixture (must be named 'driver')
    driver = item.funcargs.get("driver")
    if not driver:
        return

    # prepare path
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    # safe filename based on nodeid
    nodeid_safe = item.nodeid.replace("/", "_").replace("\\", "_").replace("::", "__")
    status = "passed" if rep.passed else "failed"
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    png_path = screenshots_dir / f"{nodeid_safe}__{status}__{ts}.png"

    try:
        driver.save_screenshot(str(png_path))
        print(f"📸 Screenshot saved: {png_path}")
    except Exception as e:
        print(f"⚠️ Could not save screenshot: {e}")
        return

    # attach to pytest-html if present
    plugin = item.config.pluginmanager.getplugin("html")
    if plugin:
        extra = getattr(rep, "extra", [])
        try:
            # embed image bytes so it appears inline (works with --self-contained-html)
            img_bytes = png_path.read_bytes()
            extra.append(plugin.extras.image(img_bytes, mime_type="image/png"))
        except Exception:
            # fallback: just link to the file
            extra.append(plugin.extras.url(png_path.as_posix()))
        rep.extra = extra
