import pywhatkit as kit
import pyautogui
import time

# Ask user for choice
x = input("1.spam messages\n2.text\n3.image\n")
choice = input("Send to: 1. Phone Number 2. Group? ")

# Function to simulate sending the message multiple times after opening WhatsApp Web once
def send_multiple_messages(repeat_count, delay_between_messages, message):
    for i in range(repeat_count):
        pyautogui.typewrite(message)  # Type the message
        pyautogui.press('enter')  # Press Enter to send the message
        print(f"Message {i+1} sent.")
        time.sleep(delay_between_messages)  # Wait before sending the next message

# Sending to phone number
if x == "1":
    # Number of times to send the message and delay between each
    repeat_count = int(input("Enter how many msgs you want to spam! "))  # Number of messages to send
    delay_between_messages = int(input("Enter the delay between the msgs (in seconds): "))  # Delay between messages

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

# Function to send a single WhatsApp message
def send_text_message(phonenumber, message, hour, minute):
    try:
        # Schedule message for the specified time
        kit.sendwhatmsg(phonenumber, message, hour, minute)
        print("Message scheduled successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to send a message to a group
def send_text_message_group(group_id, message, hour, minute):
    try:
        # Schedule message for the specified time
        kit.sendwhatmsg_to_group(group_id, message, hour, minute)
        print("Message scheduled successfully to group.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Text message option
if x == "2":
    hour = int(input("Enter the hour (24-hour format): "))
    minute = int(input("Enter the minute: "))
    message = input("Enter your message: ")

    # Sending to phone number
    if choice == "1":
        phonenumber = input("Enter the phone number (with country code): ")
        send_text_message(phonenumber, message, hour, minute)

    # Sending to group
    elif choice == "2":
        group_id = input("Enter your group id: ")
        send_text_message_group(group_id, message, hour, minute)
    else:
        print("Invalid choice. Please choose either 1 or 2.")

# Image sending option
if x == "3":
    image_path = input("Enter the full path of the image (including the extension): ")  # Get the image file path
    caption = input("Enter the caption for the image (optional): ")  # Caption for the image (optional)

    # Sending to phone number
    if choice == "1":
        phonenumber = input("Enter the phone number (with country code): ")
        try:
            kit.sendwhats_image(phonenumber, image_path, caption)  # Send image with optional caption
            print("Image sent successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Sending to group
    elif choice == "2":
        group_id = input("Enter your group id: ")
        try:
            kit.sendwhats_image(group_id, image_path, caption, True)  # Send image to group with optional caption
            print("Image sent successfully to group.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid choice. Please choose either 1 or 2.")