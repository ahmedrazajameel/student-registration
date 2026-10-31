import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

BASE_URL = "http://localhost:8000"

# Global delay between tests (seconds). Tune to taste.
BETWEEN_TESTS_DELAY = 5


class StudentRegistrationTests(unittest.TestCase):

    # Shared browser and results list across all tests
    driver = None
    results = []

    # Runs ONCE before any test
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    # Runs ONCE after all tests finish
    @classmethod
    def tearDownClass(cls):
        time.sleep(3)  # leave the final page visible for a moment
        cls.driver.quit()

    # Runs before EACH test (delay only — no open/close here)
    def setUp(self):
        time.sleep(BETWEEN_TESTS_DELAY)

    # Runs after EACH test (nothing here — browser stays open)
    def tearDown(self):
        pass

    # ---- helper so the summary can list name + result ----
    def _record(self, name, passed):
        StudentRegistrationTests.results.append((name, passed))

    # ================= TEST 1 =================
    def test_01_successful_registration(self):
        try:
            d = self.driver
            d.get(BASE_URL)
            time.sleep(1)

            name_field = d.find_element(By.ID, "name")
            name_field.click()
            for ch in "Alice Tan":
                name_field.send_keys(ch)
                time.sleep(0.1)

            email_field = d.find_element(By.ID, "email")
            email_field.click()
            for ch in "alice@example.com":
                email_field.send_keys(ch)
                time.sleep(0.1)

            Select(d.find_element(By.ID, "course")).select_by_value("ITC402")
            time.sleep(1)

            d.find_element(By.ID, "submit").click()
            time.sleep(1)

            self.assertIn("Registered Students", d.page_source)
            self.assertIn("Alice Tan", d.page_source)
            self._record("test_01_successful_registration", True)
        except Exception:
            self._record("test_01_successful_registration", False)
            raise

    # ================= TEST 2 =================
    def test_02_empty_name(self):
        try:
            d = self.driver
            d.get(BASE_URL)
            time.sleep(1)

            email_field = d.find_element(By.ID, "email")
            email_field.click()
            for ch in "bob@example.com":
                email_field.send_keys(ch)
                time.sleep(0.1)

            Select(d.find_element(By.ID, "course")).select_by_value("ITC401")
            time.sleep(1)

            d.find_element(By.ID, "submit").click()
            time.sleep(1)

            self.assertIn("Name must be at least 3 characters", d.page_source)
            self._record("test_02_empty_name", True)
        except Exception:
            self._record("test_02_empty_name", False)
            raise

    # ================= TEST 3 =================
    def test_03_invalid_email(self):
        try:
            d = self.driver
            d.get(BASE_URL)
            time.sleep(1)

            name_field = d.find_element(By.ID, "name")
            name_field.click()
            for ch in "Charlie":
                name_field.send_keys(ch)
                time.sleep(0.1)

            email_field = d.find_element(By.ID, "email")
            email_field.click()
            for ch in "not-an-email":
                email_field.send_keys(ch)
                time.sleep(0.1)

            Select(d.find_element(By.ID, "course")).select_by_value("ITC403")
            time.sleep(1)

            d.find_element(By.ID, "submit").click()
            time.sleep(1)

            self.assertIn("valid email", d.page_source)
            self._record("test_03_invalid_email", True)
        except Exception:
            self._record("test_03_invalid_email", False)
            raise

        # ================= TEST 4 =================
    def test_04_navigate_to_summary(self):
        try:
            d = self.driver
            d.get(BASE_URL)
            time.sleep(1)

            d.find_element(By.ID, "nav_summary").click()
            time.sleep(1)

            self.assertIn("Registered Students", d.page_source)
            self._record("test_04_navigate_to_summary", True)
        except Exception:
            self._record("test_04_navigate_to_summary", False)
            raise

    # ================= TEST 5 =================
    def test_05_course_dropdown_options(self):
        try:
            d = self.driver
            d.get(BASE_URL)
            time.sleep(1)

            dropdown = Select(d.find_element(By.ID, "course"))
            options = [o.text for o in dropdown.options]
            time.sleep(1)

            self.assertIn("ITC402", options)
            self.assertIn("ITC401", options)
            self.assertIn("ITC403", options)
            self._record("test_05_course_dropdown_options", True)
        except Exception:
            self._record("test_05_course_dropdown_options", False)
            raise

    # ================= TEST 6 =================
    def test_06_navigate_about_page(self):
        try:
            d = self.driver
            d.get(BASE_URL)
            time.sleep(1)

            d.find_element(By.ID, "nav_about").click()
            time.sleep(1)

            self.assertIn("About This Application", d.page_source)
            self._record("test_06_navigate_about_page", True)
        except Exception:
            self._record("test_06_navigate_about_page", False)
            raise


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(StudentRegistrationTests)
    result = runner.run(suite)

    # Custom end-of-run summary
    print("\n" + "=" * 60)
    print("CUSTOM TEST SUMMARY")
    print("=" * 60)
    for name, passed in StudentRegistrationTests.results:
        status = "PASS" if passed else "FAIL"
        print(f"  {status}  {name}")
    print("-" * 60)
    total = len(StudentRegistrationTests.results)
    passed_count = sum(1 for _, p in StudentRegistrationTests.results if p)
    failed_count = total - passed_count
    print(f"  Total: {total}   Passed: {passed_count}   Failed: {failed_count}")
    print("=" * 60)