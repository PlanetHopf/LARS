import time
import requests

# URL for the Chrome DevTools Protocol HTTP Interface
url = 'http://localhost:9222/json'

# Retrieve the list of available targets (tabs)
response = requests.get(url)
targets = response.json()

# Find the target (tab) you want to interact with
target_id = None
for target in targets:
    if target['url'] == 'https://www.progress-knight-multiplayer.net/':  # Target the correct URL
        target_id = target['id']
        break

if target_id is None:
    print("Target tab not found. Make sure Chrome is running and the target URL is open.")
    exit()

# Click on the element every second for one minute
start_time = time.time()
while time.time() - start_time < 60:  # Run for one minute
    try:
        # Execute JavaScript to click on the element
        click_url = f'http://localhost:9222/session/{target_id}/execute'
        click_script = {"script": "document.querySelector('div[aria-label=\"Click to fish\"]').click();"}
        response = requests.post(click_url, json=click_script)
        response.raise_for_status()  # Raise exception if request failed

        print("Element clicked successfully.")
    except Exception as e:
        print(f"Error clicking element: {e}")

    time.sleep(1)  # Wait for one second before clicking again
