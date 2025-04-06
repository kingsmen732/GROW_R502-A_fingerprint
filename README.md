# GROW R502-A Fingerprint Rust and Python 


This project provides a Rust-based implementation for managing a fingerprint sensor using the `serialport` crate. It enables users to enroll, verify, list, and delete fingerprints stored on the sensor. Communication with the sensor is achieved over a serial connection using a custom packet-based protocol.

## Features

- **Enroll Fingerprint**: Capture and store a fingerprint in the sensor's memory under a specified ID.
- **Verify Fingerprint**: Match a fingerprint against stored templates to identify the user.
- **List Fingerprints**: Retrieve and display all stored fingerprint IDs.
- **Delete Fingerprint**: Remove a fingerprint from the sensor's memory by ID.

## How It Works

### Communication Protocol

The program communicates with the fingerprint sensor using a packet-based protocol:
- Each packet includes a header, module address, packet identifier, payload length, payload, and checksum.
- The `send_packet` function handles packet creation, sending, and response parsing.

### Key Functions

- **`send_packet`**: Constructs and sends a command packet to the sensor, then reads the response.
- **`enroll_fingerprint`**: Guides the user through the process of enrolling a fingerprint in two stages (capturing and matching).
- **`verify_fingerprint`**: Captures a fingerprint and searches for a match in the stored templates.
- **`list_fingerprints`**: Queries the sensor for all stored fingerprint IDs.
- **`delete_fingerprint`**: Deletes a fingerprint template by its ID.

### Main Program Flow

1. The program connects to the fingerprint sensor via a serial port (default: `ttyUSB0` at 57600 baud).
2. It presents a menu to the user with options to enroll, verify, list, or delete fingerprints.
3. Based on the user's choice, the corresponding function is executed.

## Usage

### Setup

1. Ensure the fingerprint sensor is connected to the correct serial port.
2. Update the `port_name` variable in the `main` function if necessary.

### Run the Program

1. Compile and run the program using Cargo:
    ```bash
    cargo run
    ```

2. Interact with the menu:
    - **[1] Enroll**: Enter an ID (1-127) to store a new fingerprint.
    - **[2] Verify**: Place a finger on the sensor to verify against stored fingerprints.
    - **[3] List**: View all stored fingerprint IDs.
    - **[4] Delete**: Enter an ID to delete a stored fingerprint.
    - **[q] Quit**: Exit the program.

### Example Output

```plaintext
[1] Enroll Fingerprint
[2] Verify Fingerprint
[3] List Fingerprints
[4] Delete Fingerprint
[q] Quit
Enter your choice:
```

## Dependencies

- **Rust**: Ensure you have Rust installed. [Install Rust](https://www.rust-lang.org/tools/install)
- **`serialport` crate**: Used for serial communication with the fingerprint sensor.

## Notes

- The program assumes the fingerprint sensor uses a packet-based protocol compatible with the implementation.
- Adjust the serial port name and baud rate as needed for your setup.
- The sensor supports up to 128 fingerprint templates.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Getting Started

1. Install [Rust](https://www.rust-lang.org/tools/install) if you haven't already.
2. Clone this repository:
     ```bash
     git clone <repository-url>
     cd GROW_R502-A_fingerprint_rust
     ```
3. Build the project:
     ```bash
     cargo build
     ```
4. Run the project:
     ```bash
     cargo run
     ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
