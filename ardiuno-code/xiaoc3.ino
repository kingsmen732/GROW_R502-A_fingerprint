#include <Adafruit_Fingerprint.h>
#include <HardwareSerial.h>

HardwareSerial mySerial(1); // Use UART1

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

void setup()
{
  Serial.begin(115200);
  while (!Serial);
  delay(100);
  Serial.println("\n\nAdafruit Fingerprint Sensor Test");

  // Initialize UART1
  mySerial.begin(57600, SERIAL_8N1, D6, D7); // D6: RX, D7: TX

  if (finger.verifyPassword()) {
    Serial.println("Found fingerprint sensor!");
  } else {
    Serial.println("Did not find fingerprint sensor :(");
    while (1) { delay(1); }
  }

  // Additional setup code...
}

void loop()
{
  // Your loop code...
}
