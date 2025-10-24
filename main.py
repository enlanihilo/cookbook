import sys
import time
import json
import random
import os
import requests
from playwright.sync_api import sync_playwright, Page, TimeoutError

# =========================
# Apps Script Configuration
# =========================
# !!! CẢNH BÁO BẢO MẬT: Không nên để URL trực tiếp trong code nếu repository là công khai.
# Sử dụng GitHub Secrets là phương pháp an toàn hơn.
APPS_SCRIPT_WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbwVZI2SnEfkNaCQZyxsJGEF_RwxXgeZdJ8P18YdueiZEzPak0f7a2kDFmbMnCBdQsIhqw/exec'

def send_data_to_apps_script(new_username, password, new_2fa_secret, email, result_message):
    """Sends data to the Google Apps Script Web App."""
    if not APPS_SCRIPT_WEB_APP_URL:
        print("Lỗi: URL của Apps Script không được cấu hình.")
        return False
        
    payload = {
        'new_username': new_username,
        'password': password,
        'new_2fa_secret': new_2fa_secret,
        'email': email,
        'result': result_message
    }
    headers = {'Content-Type': 'application/json'}
    try:
        print(f"Đang gửi dữ liệu tới Apps Script Web App.")
        response = requests.post(APPS_SCRIPT_WEB_APP_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status() 
        print(f"Apps Script phản hồi: {response.text}")
        response_json = response.json()
        if response_json.get('status') == 'error':
            print(f"Lỗi từ Apps Script: {response_json.get('message')}")
            return False
        return True
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi gửi dữ liệu đến Apps Script: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"Lỗi giải mã JSON từ Apps Script: {e}. Phản hồi: {response.text}")
        return False

# =========================
# Automation Class
# =========================
class AutomationRunner:
    def __init__(self, account_string):
        self.account_string = account_string
        self.logs = []
        # Các thông tin tài khoản được trích xuất
        self.new_username = "N/A"
        self.current_username = "N/A"
        self.password = "N/A"
        self.initial_2fa_secret = "N/A" 
        self.new_2fa_secret = "N/A" 
        self.email = "N/A"

    def log(self, message):
        """Prints a message and adds it to the log list."""
        print(message)
        self.logs.append(message)

    def wait_a_bit(self, min_s=2.0, max_s=4.0):
        time.sleep(random.uniform(min_s, max_s))

    def type_slow(self, page: Page, selector: str, text: str):
        locator = page.locator(selector)
        locator.wait_for(state="visible", timeout=30000)
        try:
            locator.click()
        except Exception:
            pass
        locator.fill("")
        self.wait_a_bit(0.3, 0.7)
        for ch in text:
            locator.type(ch, delay=random.uniform(90, 180))
        self.wait_a_bit(0.4, 0.9)

    def safe_click_locator(self, locator):
        locator.first.wait_for(state="visible", timeout=30000)
        try:
            locator.first.scroll_into_view_if_needed()
        except Exception:
            pass
        t0 = time.time()
        while time.time() - t0 < 10:
            try:
                if locator.first.is_enabled():
                    break
            except Exception:
                pass
            time.sleep(0.2)
        self.wait_a_bit(0.3, 0.8)
        locator.first.click()
        self.wait_a_bit(0.6, 1.2)
        
    def safe_click_selector(self, page: Page, selector: str):
        loc = page.locator(selector)
        self.safe_click_locator(loc)

    def click_sign_in(self, page: Page) -> bool:
        candidates = [
            '''form[action="/session"] button:has-text("Sign in")''',
            '''form[action="/session"] input[type="submit"][value="Sign in"]''',
            '''button:has-text("Sign in")''',
            '''input[type="submit"][value="Sign in"]''',
        ]
        for sel in candidates:
            loc = page.locator(sel)
            try:
                if loc.count() > 0 and loc.first.is_visible():
                    self.safe_click_locator(loc)
                    return True
            except Exception:
                continue
        try:
            btn = page.get_by_role("button", name="Sign in", exact=True)
            self.safe_click_locator(btn)
            return True
        except Exception:
            return False

    def run(self):
        result_message = ""
        try:
            def get_totp(page: Page, secret: str) -> str:
                self.log(f"Getting 2FA code for secret: {secret[:5]}...")
                p = page.context.new_page()
                p.goto(f"https://2fa.live/tok/{secret}", wait_until="domcontentloaded", timeout=20000)
                data = json.loads(p.inner_text("body"))
                p.close()
                token = data.get("token")
                self.log(f"Got 2FA code: {token}")
                return token

            # Parse input string
            parts = [x.strip() for x in self.account_string.split("|")]
            if len(parts) < 5: 
                raise Exception("Incorrect format. Must be: newusername|currentusername|password|2fa_secret|email")
            
            self.new_username, self.current_username, self.password, self.initial_2fa_secret, self.email = parts

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
                page = context.new_page()

                # ... (phần còn lại của logic automation giữ nguyên)
                self.log("Opening login page...")
                page.goto("https://github.com/login", wait_until="domcontentloaded", timeout=50000)
                self.type_slow(page, '''input[name="login"]''', self.current_username)
                self.type_slow(page, '''input[name="password"]''', self.password)
                self.log('Clicking "Sign in"...')
                if not self.click_sign_in(page):
                    raise Exception('Could not find "Sign in" button.')
                self.wait_a_bit(1.0, 2.0)

                # Wait for 2FA page, if it appears
                try:
                    page.wait_for_url("**/sessions/two-factor/app**", timeout=60000)
                    code = get_totp(page, self.initial_2fa_secret)
                    if not code:
                        raise Exception("Could not get 2FA code.")
                    self.type_slow(page, '''input[placeholder="XXXXXX"], input[name="app_otp"]''', code)
                    self.wait_a_bit(0.6, 1.2)
                except TimeoutError:
                    self.log("2FA page did not appear, proceeding with login (possibly already logged in or no 2FA).")


                self.log("Waiting for next page (dashboard or verification)...")
                dashboard_selector = "header[role='banner']"
                skip_button_selector = "button:has-text('skip 2FA verification'), button:has-text('Skip for now')"
                final_selector = f"{dashboard_selector}, {skip_button_selector}"
                page.wait_for_selector(final_selector, timeout=60000)
                skip_locator = page.locator(skip_button_selector)
                try:
                    if skip_locator.first.is_visible(timeout=5000):
                        self.log("Device verification page detected. Clicking skip button...")
                        self.safe_click_locator(skip_locator)
                    else:
                        self.log("Login successful, on dashboard.")
                except Exception:
                    self.log("Login successful, on dashboard (skip button not visible).")
                self.wait_a_bit()

                self.log("Opening /settings/admin...")
                page.goto("https://github.com/settings/admin", wait_until="domcontentloaded", timeout=60000)
                page.wait_for_selector("turbo-frame#settings-frame", timeout=60000)
                self.wait_a_bit(0.8, 1.5)

                self.log('Clicking "Change username"...')
                self.safe_click_selector(page, "turbo-frame#settings-frame #dialog-show-rename-warning-dialog")
                page.wait_for_selector("dialog#rename-warning-dialog[open]", timeout=40000)
                self.wait_a_bit()

                self.log('Clicking "I understand, let’s change my username"...')
                self.safe_click_selector(page, "dialog#rename-warning-dialog button[data-show-dialog-id='rename-form-dialog']")
                page.wait_for_selector("dialog#rename-form-dialog[open]", timeout=40000)
                self.wait_a_bit()

                self.log("Entering new username...")
                self.type_slow(page, "dialog#rename-form-dialog input#login", self.new_username)
                page.keyboard.press("Tab")
                self.wait_a_bit(1.2, 2.0)

                self.log('Clicking "Change my username" (1st attempt)...')
                submit_sel = "dialog#rename-form-dialog button[type='submit']"
                self.safe_click_selector(page, submit_sel)

                self.log("Waiting for result after 1st click...")
                rename_success = False
                end_time = time.time() + 80
                while time.time() < end_time:
                    if page.locator("text='Your account has been renamed'").first.is_visible():
                        self.log("Success: 'Your account has been renamed' appeared.")
                        rename_success = True
                        break
                    is_available_locator = page.locator("dialog#rename-form-dialog :text('is available')")
                    if is_available_locator.first.is_visible(timeout=1000):
                        self.log("'is available' appeared. Clicking 'Change my username' a 2nd time.")
                        self.safe_click_selector(page, submit_sel)
                        page.wait_for_selector("text='Your account has been renamed'", timeout=70000)
                        rename_success = True
                        break
                    error_locator = page.locator("dialog#rename-form-dialog .flash.flash-error")
                    if error_locator.first.is_visible(timeout=1000):
                        error_text = error_locator.first.inner_text()
                        raise Exception(f"Error from GitHub on name change: {error_text}")
                    time.sleep(0.5)

                if not rename_success:
                     raise Exception("Could not confirm successful rename.")
                self.wait_a_bit()
                
                self.log("--- Starting 2FA reset ---")
                self.log("Navigating to security settings...")
                page.goto("https://github.com/settings/security", wait_until="domcontentloaded", timeout=60000)

                self.log("Clicking 'Edit' for Authenticator app...")
                edit_button_selector = "#two-factor-summary > div:nth-child(2) > div > div.d-flex.width-full > form > button"
                self.safe_click_selector(page, edit_button_selector)
                
                self.log("Waiting for config page and clicking 'setup key'...")
                setup_key_button_selector = "#dialog-show-two-factor-setup-verification-mashed-secret"
                page.wait_for_selector(setup_key_button_selector, timeout=40000)
                self.safe_click_selector(page, setup_key_button_selector)

                self.log("Waiting for new secret key dialog...")
                secret_key_dialog_selector = "dialog#two-factor-setup-verification-mashed-secret[open]"
                page.wait_for_selector(secret_key_dialog_selector, timeout=30000)

                self.log("Getting new 2FA secret string...")
                new_2fa_secret_element = page.locator(f"{secret_key_dialog_selector} [data-target='two-factor-setup-verification.mashedSecret']").first
                self.new_2fa_secret = new_2fa_secret_element.inner_text().strip()

                if not self.new_2fa_secret:
                    raise Exception("Could not get new 2FA secret string.")
                self.log(f"Got new secret: {self.new_2fa_secret}")
                
                new_code = get_totp(page, self.new_2fa_secret)
                if not new_code:
                    raise Exception("Could not get 6-digit code from 2FA.live.")

                self.log("Closing secret key dialog...")
                close_button_selector = "button[data-close-dialog-id='two-factor-setup-verification-mashed-secret']"
                self.safe_click_selector(page, close_button_selector)
                self.wait_a_bit(0.5, 1.0)

                self.log("Entering 6-digit code for verification...")
                verify_input_selector = "input[data-target='two-factor-configure-otp-factor.appOtpInput']"
                self.type_slow(page, verify_input_selector, new_code)
                
                self.log("Waiting for confirmation icon (green checkmark)...")
                page.wait_for_selector("[data-target='two-factor-configure-otp-factor.otpVerifySuccess']:not([hidden])", timeout=30000)
                self.log("Confirmation icon appeared.")
                self.wait_a_bit(0.5, 1.0)

                self.log("Clicking 'Save' to save 2FA changes...")
                save_button_selector = "button[data-target='two-factor-configure-otp-factor.saveButton']"
                self.safe_click_selector(page, save_button_selector)

                self.log("Waiting for page reload and final confirmation...")
                page.wait_for_selector("text='Authenticator app successfully reconfigured.'", timeout=40000)
                self.log("Successfully reconfigured Authenticator app!")

                result_message = "SUCCESS" 

        except TimeoutError as e:
            result_message = f"ERROR: TIMEOUT - A page or element took too long to load. Details: {e}"
        except Exception as e:
            result_message = f"ERROR: {e}"
        finally:
            print("\n--- SCRIPT FINISHED ---")
            print(f"Final Result: {result_message}")
            send_data_to_apps_script(
                self.new_username, 
                self.password, 
                self.new_2fa_secret, 
                self.email, 
                result_message
            )


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 2:
        print("Usage: python main.py \"newusername|currentusername|password|2fa_secret|email\"")
        sys.exit(1)
    
    account_details = sys.argv[1]
    runner = AutomationRunner(account_details)
    runner.run()
