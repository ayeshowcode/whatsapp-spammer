import pywhatkit as kit
import pyautogui
import time

# Ask user for choice
choice = input("Send to: 1. Phone Number 2. Group? ")

# Number of times to send the message and delay between each
repeat_count = int(input("Enter how many msgs you want to spam! "))  # Number of messages to send
delay_between_messages = int(input("Enter the delay between the msgs (in seconds): "))  # Delay between messages

# Function to simulate sending the message multiple times after opening WhatsApp Web once
def send_multiple_messages(repeat_count, delay_between_messages, message):
    for i in range(repeat_count):
        pyautogui.typewrite(message)  # Type the message
        pyautogui.press('enter')  # Press Enter to send the message
        print(f"Message {i+1} sent.")
        time.sleep(delay_between_messages)  # Wait before sending the next message

# Sending to phone number
if choice == "1":
    phonenumber = input("Enter the phone number (with country code): ")
    try:
        msg = input("Enter message: ")
        # Open WhatsApp Web once
        kit.sendwhatmsg_instantly(phonenumber, msg, 15, False, 2)  # Set `close_tab=False` to keep the tab open
        time.sleep(10)  # Wait for WhatsApp Web to load
        # Send the message multiple times
        send_multiple_messages(repeat_count, delay_between_messages, msg)
    except Exception as e:
        print(f"An error occurred: {e}")

# Sending to group
elif choice == "2":
    group_id = input("Enter your group id: ")
    try:
        msgg = input("Enter message: ")
        # Open WhatsApp Web once
        kit.sendwhatmsg_to_group_instantly(group_id, msgg, 15, False, 2)  # Set `close_tab=False` to keep the tab open
        time.sleep(10)  # Wait for WhatsApp Web to load
        # Send the message multiple times
        send_multiple_messages(repeat_count, delay_between_messages, msgg)
    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print("Invalid choice. Please choose either 1 or 2.")