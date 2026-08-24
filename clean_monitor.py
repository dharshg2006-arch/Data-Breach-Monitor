import requests

def check_email_breach(email):
    print("Checking status for: " + email + "...\n")
    url = "https://leakcheck.io" + email
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("success") and data.get("sources"):
                    print("[ALERT] This email was found in leaks!")
                    for source in data["sources"]:
                        print(" - " + str(source.get('name')))
                else:
                    print("[SUCCESS] No known public breaches found.")
            except ValueError:
                print("[WARNING] The API returned non-JSON text.")
                print("Raw Response:", response.text[:200])
        else:
            print("Error. Status Code: " + str(response.status_code))
    except Exception as e:
        print("An error occurred: " + str(e))

check_email_breach("test@example.com")