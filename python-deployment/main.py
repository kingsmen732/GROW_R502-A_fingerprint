import time
import serial
import adafruit_fingerprint

# Change this to the correct serial port
# Ensure the correct COM port is used (e.g., "COM3" or "/dev/ttyUSB0" on Linux/Mac)
uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

# State for toggling something like a relay
relay_state = False

def get_num_input(prompt="Enter ID (1-127): "):
    while True:
        try:
            val = int(input(prompt))
            if 1 <= val <= 127:
                return val
            else:
                print("ID must be between 1 and 127.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def enroll_fingerprint(location):
    print("Place finger on sensor...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Image taken")

    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        print("Failed to convert image")
        return False

    print("Remove finger...")
    time.sleep(2)
    while finger.get_image() != adafruit_fingerprint.NOFINGER:
        pass

    print("Place the same finger again...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Image taken")

    if finger.image_2_tz(2) != adafruit_fingerprint.OK:
        print("Failed to convert second image")
        return False

    if finger.create_model() != adafruit_fingerprint.OK:
        print("Fingerprints did not match")
        return False

    if finger.store_model(location) == adafruit_fingerprint.OK:
        print("Fingerprint stored successfully at ID", location)
        return True
    else:
        print("Failed to store fingerprint")
        return False

def verify_fingerprint():
    global relay_state

    print("Waiting for finger...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Image taken")

    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        print("Could not convert image to template")
        return

    if finger.finger_search() != adafruit_fingerprint.OK:
        print("No match found.")
        return

    # If match found
    print("Found ID #{} with confidence {}".format(finger.finger_id, finger.confidence))

    # Toggle "relay"
    relay_state = not relay_state
    if relay_state:
        print("Relay ON")
        # You could trigger a real GPIO or output signal here
    else:
        print("Relay OFF")

def list_fingerprints():
    print("Listing all stored fingerprints:")
    for i in range(1, finger.library_size + 1):
        if finger.load_model(i) == adafruit_fingerprint.OK:
            print(f"Fingerprint ID {i} is stored.")
    
def delete_fingerprint(location):
    """Delete a fingerprint from the sensor."""
    if finger.delete_model(location) == adafruit_fingerprint.OK:
        print(f"Fingerprint ID {location} deleted successfully.")
    else:
        print(f"Failed to delete fingerprint ID {location}.")

def main():
    print("Fingerprint Sensor Control")
    if finger.verify_password():
        print("Sensor detected successfully.")
        print("Could not detect fingerprint sensor. Please check the wiring and serial port.")
        print("Could not detect fingerprint sensor.")
        return

    print(f"Sensor Info: Capacity: {finger.library_size}, Security Level: {finger.security_level}")

    while True:
        mode = input("\nChoose mode: [1] Enroll  [2] Verify  [3] List All  [4] Delete  [q] Quit : ").strip().lower()
        if mode == "1":
            id = get_num_input()
            enroll_fingerprint(id)
        elif mode == "2":
            verify_fingerprint()
        elif mode == "3":
            list_fingerprints()
        elif mode == "4":
            id = get_num_input("Enter ID to delete (1-127): ")
            delete_fingerprint(id)
        elif mode == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, 4, or q.")

if __name__ == "__main__":
    main()
