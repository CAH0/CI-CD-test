from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

def correctloginTest(driver,login, password):
    try :
        driver.find_element(By.ID, "username").send_keys(f"{login}")
        driver.find_element(By.NAME, "password").send_keys(f"{password}")

        driver.find_element(By.CLASS_NAME, "radius").click()

        wait = WebDriverWait(driver, 1)
        message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        assert "You logged into a secure area!" in message.text

        driver.find_element(By.CLASS_NAME, "button.secondary.radius").click()
        message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        assert "You logged out of the secure area!" in message.text
        return True
    except Exception as e:
        print("correctloginTest", "FAIL", f"Тест упал с ошибкой")
        print(f"   ✗ Ошибка: {e}")
        return False

def uncorrectloginTest(driver, login, password):
    try:
        driver.find_element(By.ID, "username").send_keys(f"{login}")
        driver.find_element(By.NAME, "password").send_keys(f"{password}")

        driver.find_element(By.CLASS_NAME, "radius").click()

        wait = WebDriverWait(driver, 1)
        message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        assert "Your username is invalid!" in message.text
        return True
    except Exception as e:
        print("correctloginTest", "FAIL", f"Тест упал с ошибкой")
        print(f"   ✗ Ошибка: {e}")
        return False

def uncorrectPasswordTest(driver ,login, password):
    try:
        driver.find_element(By.ID, "username").send_keys(f"{login}")
        driver.find_element(By.NAME, "password").send_keys(f"{password}")

        driver.find_element(By.CLASS_NAME, "radius").click()

        wait = WebDriverWait(driver, 1)
        message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        assert "Your password is invalid!" in message.text
        return True
    except Exception as e:
        print("correctloginTest", "FAIL", f"Тест упал с ошибкой")
        print(f"   ✗ Ошибка: {e}")
        return False



correctloginTest(driver, "tomsmith", "SuperSecretPassword!")
uncorrectloginTest(driver, "tomsmith1", "SuperSecretPassword!")
uncorrectPasswordTest(driver, "tomsmith", "SuperSecretPassword!1")

test_results = []
test_results.append(("correctloginTest", correctloginTest(driver, "tomsmith", "SuperSecretPassword!")))
test_results.append(("uncorrectloginTest", uncorrectloginTest(driver, "tomsmith", "SuperSecretPassword!")))
test_results.append(("uncorrectPasswordTest", uncorrectPasswordTest(driver, "tomsmith", "SuperSecretPassword!1")))
print("\n📋 Детализация:")
for test_name, result in test_results:
    status = "✅ PASS" if result else "❌ FAIL"
    print(f"   {status} - {test_name}")