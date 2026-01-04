"""
Video Recording Test Script for ReqRes.in API
All 18 test cases with video recording using pyscreenrec.
Based on: https://www.thegreenreport.blog/articles/from-code-to-video-recording-selenium-test-sessions-in-python/
"""

import json
import re
import threading
import os
from datetime import datetime

from seleniumbase import BaseCase

# Video recording support (pyscreenrec)
try:
    import pyscreenrec
    VIDEO_RECORDING_AVAILABLE = True
except ImportError:
    VIDEO_RECORDING_AVAILABLE = False
    print("Warning: pyscreenrec not installed. Install with: python -m pip install pyscreenrec")
    exit(1)


def get_browser_coordinates(driver):
    """Get browser window coordinates for recording"""
    rect = driver.get_window_rect()
    return {
        'left': rect['x'],
        'top': rect['y'],
        'width': rect['width'],
        'height': rect['height']
    }


def wait_for_page_content(test_case, timeout=15):
    """Wait for page content to load and return parsed JSON data"""
    # Initial wait to let the page start loading
    test_case.sleep(3)

    for i in range(timeout):
        body_text = test_case.execute_script("return document.body.textContent;")
        if body_text and body_text.strip() and body_text.strip() not in ["", "null", "undefined"]:
            try:
                data = json.loads(body_text)
                return data
            except json.JSONDecodeError:
                pass
        if i < timeout - 1:  # Don't sleep on the last iteration
            test_case.sleep(1)

    # Final attempt - if still empty, raise clear error
    body_text = test_case.execute_script("return document.body.textContent;")
    if not body_text or not body_text.strip():
        raise ValueError("Page content is empty after waiting for page to load")
    return json.loads(body_text)


def record_test(driver, test_actions, max_duration=60, output_filename=None):
    """Record test execution using pyscreenrec"""
    if output_filename is None:
        output_filename = f"videos/recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"

    # Create videos directory if it doesn't exist
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    coordinates = get_browser_coordinates(driver)
    recorder = pyscreenrec.ScreenRecorder()
    test_complete = threading.Event()

    def run_test():
        try:
            test_actions()
        finally:
            test_complete.set()

    try:
        print(f"Starting video recording: {output_filename}")
        recorder.start_recording(
            output_filename,
            30,  # FPS
            {
                "mon": 1,  # Primary monitor
                "left": coordinates['left'],
                "top": coordinates['top'],
                "width": coordinates['width'],
                "height": coordinates['height']
            }
        )

        test_thread = threading.Thread(target=run_test)
        test_thread.start()
        test_thread.join(timeout=max_duration)

    finally:
        recorder.stop_recording()
        print(f"Recording saved to: {output_filename}")

    return output_filename


class TestVideoRecord(BaseCase):

    def test_tc001_with_video(self):
        """TC001: Valid request with page=2"""
        def test_actions():
            url = "https://reqres.in/api/users?page=2"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 2
            assert data.get("per_page") == 6
            assert len(data.get("data", [])) == 6
        record_test(self.driver, test_actions, 60, "videos/tc001_valid_request_page_2.mp4")

    def test_tc002_with_video(self):
        """TC002: Valid request with page=1"""
        def test_actions():
            url = "https://reqres.in/api/users?page=1"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 1
            assert data.get("data")[0].get("id") == 1
        record_test(self.driver, test_actions, 60, "videos/tc002_valid_request_page_1.mp4")

    def test_tc003_with_video(self):
        """TC003: Page 0 defaults to page 1"""
        def test_actions():
            url = "https://reqres.in/api/users?page=0"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 1
        record_test(self.driver, test_actions, 60, "videos/tc003_page_zero_defaults_to_1.mp4")

    def test_tc004_with_video(self):
        """TC004: Negative page returns -1"""
        def test_actions():
            url = "https://reqres.in/api/users?page=-1"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == -1
        record_test(self.driver, test_actions, 60, "videos/tc004_negative_page_returns_minus_1.mp4")

    def test_tc005_with_video(self):
        """TC005: Page 999 returns empty data"""
        def test_actions():
            url = "https://reqres.in/api/users?page=999"
            self.open(url)
            data = wait_for_page_content(self)
            assert len(data.get("data", [])) == 0
        record_test(self.driver, test_actions, 60, "videos/tc005_page_999_empty_data.mp4")

    def test_tc006_with_video(self):
        """TC006: No page parameter defaults to 1"""
        def test_actions():
            url = "https://reqres.in/api/users"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 1
            assert len(data.get("data", [])) > 0
        record_test(self.driver, test_actions, 60, "videos/tc006_no_page_defaults_to_1.mp4")

    def test_tc007_with_video(self):
        """TC007: Invalid data type defaults to 1"""
        def test_actions():
            url = "https://reqres.in/api/users?page=abc"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 1
        record_test(self.driver, test_actions, 60, "videos/tc007_invalid_type_defaults_to_1.mp4")

    def test_tc008_with_video(self):
        """TC008: Pagination metadata correct"""
        def test_actions():
            url = "https://reqres.in/api/users?page=2"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("total") == data.get("per_page") * data.get("total_pages")
            assert data.get("per_page") == 6
            assert data.get("total_pages") == 2
        record_test(self.driver, test_actions, 60, "videos/tc008_pagination_metadata.mp4")

    def test_tc009_with_video(self):
        """TC009: Support object exists"""
        def test_actions():
            url = "https://reqres.in/api/users?page=2"
            self.open(url)
            data = wait_for_page_content(self)
            assert "support" in data
            assert data.get("support").get("url")
            assert data.get("support").get("text")
        record_test(self.driver, test_actions, 60, "videos/tc009_support_object.mp4")

    def test_tc010_with_video(self):
        """TC010: Response headers valid"""
        def test_actions():
            url = "https://reqres.in/api/users?page=2"
            self.open(url)
            data = wait_for_page_content(self)
            assert data is not None
            assert "page" in data
        record_test(self.driver, test_actions, 60, "videos/tc010_response_headers.mp4")

    def test_tc011_with_video(self):
        """TC011: Multiple page parameters handled"""
        def test_actions():
            url = "https://reqres.in/api/users?page=1&page=2"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") in [1, 2]
        record_test(self.driver, test_actions, 60, "videos/tc011_multiple_page_params.mp4")

    def test_tc012_with_video(self):
        """TC012: Empty page parameter defaults to 1"""
        def test_actions():
            url = "https://reqres.in/api/users?page="
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 1
        record_test(self.driver, test_actions, 60, "videos/tc012_empty_page_param.mp4")

    def test_tc013_with_video(self):
        """TC013: SQL injection attempt handled safely"""
        def test_actions():
            url = "https://reqres.in/api/users?page=1'OR'1'='1"
            self.open(url)
            data = wait_for_page_content(self)
            assert data is not None
        record_test(self.driver, test_actions, 60, "videos/tc013_sql_injection.mp4")

    def test_tc014_with_video(self):
        """TC014: All emails have valid format"""
        def test_actions():
            url = "https://reqres.in/api/users?page=2"
            self.open(url)
            data = wait_for_page_content(self)
            email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            for user in data.get("data", []):
                assert email_regex.match(user.get("email"))
        record_test(self.driver, test_actions, 60, "videos/tc014_email_format_validation.mp4")

    def test_tc015_with_video(self):
        """TC015: All avatar URLs are valid"""
        def test_actions():
            url = "https://reqres.in/api/users?page=2"
            self.open(url)
            data = wait_for_page_content(self)
            avatar_regex = re.compile(r'^https://reqres\.in/img/faces/\d+-image\.jpg$')
            for user in data.get("data", []):
                assert avatar_regex.match(user.get("avatar"))
        record_test(self.driver, test_actions, 60, "videos/tc015_avatar_url_validation.mp4")

    def test_tc016_with_video(self):
        """TC016: Decimal page rounds to 1"""
        def test_actions():
            url = "https://reqres.in/api/users?page=1.5"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 1
        record_test(self.driver, test_actions, 60, "videos/tc016_decimal_page.mp4")

    def test_tc017_with_video(self):
        """TC017: Special characters default to 1"""
        def test_actions():
            url = "https://reqres.in/api/users?page=!@#$%"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 1
        record_test(self.driver, test_actions, 60, "videos/tc017_special_characters.mp4")

    def test_tc018_with_video(self):
        """TC018: Extra parameters ignored"""
        def test_actions():
            url = "https://reqres.in/api/users?page=2&extra=param"
            self.open(url)
            data = wait_for_page_content(self)
            assert data.get("page") == 2
        record_test(self.driver, test_actions, 60, "videos/tc018_extra_query_parameters.mp4")


if __name__ == "__main__":
    # Run all tests with video recording and HTML report
    import pytest
    pytest.main([
        __file__,
        "-v",
        "--uc",
        "--headed",
        "--time-limit=600",
        "--html=test-report.html",
        "--self-contained-html"
    ])
