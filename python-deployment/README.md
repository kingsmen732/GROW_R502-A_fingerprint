
# Grow-R502-A Fingerprint Sensor Control

This Python script provides a command-line interface to interact with a fingerprint sensor using the `adafruit_fingerprint` library. It allows you to enroll, verify, list, and delete fingerprints stored on the sensor.

## Features

- **Enroll Fingerprint**: Add a new fingerprint to the sensor's memory.
- **Verify Fingerprint**: Match a fingerprint against stored fingerprints and toggle a relay state.
- **List Fingerprints**: Display all stored fingerprints.
- **Delete Fingerprint**: Remove a fingerprint from the sensor's memory.

## Requirements

- Python 3.x
- `adafruit_fingerprint` library
- `pyserial` library
- A compatible fingerprint sensor (e.g., Adafruit Fingerprint Sensor)
- Correctly configured serial port (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux/Mac)

## Installation

1. Install the required Python libraries:
    ```Bash
    #unwanted library which confuses
    pip uninstall adafruit-fingerprint adafruit-circuitpython-fingerprint
    # install only required lib
    pip install adafruit-circuitpython-fingerprint # required library 
    ```

2. Connect the fingerprint sensor to your system and note the serial port (e.g., `/dev/ttyUSB0`).

3. Update the `uart` variable in the script to match your serial port:
    ```python
    uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
    ```

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to interact with the fingerprint sensor.

### Modes

- **Enroll**: Add a new fingerprint to the sensor.
  - Enter an ID (1-127) for the fingerprint.
  - Follow the prompts to place and remove your finger.

- **Verify**: Match a fingerprint against stored fingerprints.
  - Place your finger on the sensor.
  - If a match is found, the relay state toggles (ON/OFF).

- **List All**: Display all stored fingerprints.

- **Delete**: Remove a fingerprint from the sensor.
  - Enter the ID (1-127) of the fingerprint to delete.

- **Quit**: Exit the program.

## Functions

### `get_num_input(prompt)`
Prompts the user for a numeric input within a specific range.

### `enroll_fingerprint(location)`
Enrolls a new fingerprint at the specified location (ID).

### `verify_fingerprint()`
Verifies a fingerprint against stored fingerprints and toggles the relay state.

### `list_fingerprints()`
Lists all stored fingerprints in the sensor's memory.

### `delete_fingerprint(location)`
Deletes a fingerprint from the specified location (ID).

### `main()`
The main function that provides the command-line interface.

## Notes

- Ensure the sensor is connected to the correct serial port.
- The relay state toggling is simulated in the script. You can replace it with actual GPIO control for hardware integration.

## Troubleshooting

- If the sensor is not detected, check the wiring and serial port configuration.
- Ensure the `adafruit_fingerprint` library is installed and up-to-date.

## License

This script is provided as-is for educational purposes. Modify it as needed for your specific use case.
