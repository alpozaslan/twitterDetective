def login(driver, username, password, login_url):
    print("Login page is loading...")
    driver.get(login_url)
    print("Login page is loaded.")
    print("Logging in...")