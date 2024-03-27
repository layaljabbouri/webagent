from selenium import webdriver
import time

# Set up WebDriver for Firefox
driver = webdriver.Firefox()

# Define the URL of the page to refresh
page_url = "http://localhost:5020/get-messages"

# Navigate to the page
driver.get(page_url)
try:
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    # alert.dismiss()  # Dismiss the alert
except:
    pass  # No alert present

cookie = {'name': 'FLAG', 'value': 'CSCTF{Y0U_JU3S7_R37R3!V3D_4N07H3R_H!DD3N_FL4G}'}
driver.add_cookie(cookie)
# print(driver.get_cookies())

# Function to fetch and display messages as HTML
def fetch_and_display_messages():
    # Refresh the page to ensure we get the latest messages
    driver.refresh()

    # Wait for the page to load
    time.sleep(2)


    

# Loop to refresh the page and display messages every 30 seconds
while True:
    try:
        # Call the function to fetch and display messages
        fetch_and_display_messages()
        cookies = driver.get_cookies()
        # print(cookies)


        # Wait for a moment
        time.sleep(30)

    except KeyboardInterrupt:
        break

# Close the WebDriver
driver.quit()
