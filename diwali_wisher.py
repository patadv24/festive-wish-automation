import csv
import random
import pywhatkit
import time
from messages import MESSAGES

def send_diwali_wishes(contacts_file):
    """
    Reads contacts from a CSV file and sends them a random, generic Diwali wish via WhatsApp.
    """

    try:
        with open(contacts_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header if present

            print("Starting to send Diwali wishes...")
            mode = input("Choose mode (manual/auto): ").lower()

            for row in reader:
                if len(row) < 2:
                    print(f"[SKIP] Invalid row: {row}")
                    continue

                name = row[0].strip()
                phone_number = "+" + row[1].strip()
                generic_message = random.choice(MESSAGES)

                print(f"[INFO] Sending to {name} ({phone_number})...")

                try:
                    pywhatkit.sendwhatmsg_instantly(
                        phone_no=phone_number,
                        message=generic_message,
                        wait_time=10,
                        tab_close=False,
                        close_time=3
                    )

                    if mode == "auto":
                        import pyautogui
                        time.sleep(3)
                        pyautogui.press("enter")
                        print(f"[AUTO] Sent to {name}")
                        time.sleep(3)

                    else:
                        input(f"[MANUAL] Press ENTER to continue to next contact...")

                except Exception as e:
                    print(f"[ERROR] Could not send to {name}: {e}")

            print("\n[SUCCESS] All wishes processed. Happy Diwali!")

    except FileNotFoundError:
        print(f"[ERROR] File '{contacts_file}' not found.")
    except Exception as e:
        print(f"[ERROR] Unexpected issue: {e}")


if __name__ == "__main__":
    send_diwali_wishes('contacts.csv')