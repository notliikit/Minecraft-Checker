# Minecraft Checker

This Python script is designed to check Minecraft usernames using the Mojang API. The script can take either a single username or a list of usernames and, optionally, a list of proxies to check the validity of these usernames.

## Usage

1. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Script:**
    ```bash
    python checker.py
    ```

    The script will prompt the user for an option and the required file paths, then proceed to check the usernames using the Mojang API.

3. **File Structure:**

   - If you only want to check a single username, add the username to the `usernames.txt` file.

   - If you want to use proxies for checking, also add the proxy addresses to the `proxies.txt` file.

4. **View the Results:**

   After running the script, it will display the list of valid usernames.

## Options

1. **Check Only Username:**
    - Performs checks only on usernames.

2. **Check Username with Proxy:**
    - Performs checks on usernames using randomly selected proxies.

## Warning

Use this script responsibly and avoid unauthorized or unlawful checking of usernames. It is important to respect Mojang's terms of service.

---

**Note:** This script is written for educational purposes, and any responsibility arising from its use rests with the user.
