#define BLYNK_TEMPLATE_ID "TMPL2yx1PllLf"
#define BLYNK_TEMPLATE_NAME "Sistema de Maceta"
#define BLYNK_AUTH_TOKEN "GwQJiB-WDTRKg5tneK2WwmPOLvEDh6Z7"

//Include the library files
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <NewPing.h>
#include <NoDelay.h>

#define sensor 33
#define relay 4

const int DISTANCIA_ALERTA = 30;

const long TIEMPO_TAREA = 500;


// Configuramos los pines del sensor Trigger y Echo
const int PinTrig = 5;
const int PinEcho = 18;

noDelay pausa(TIEMPO_TAREA);

// Crea una instancia de la clase NewPing
NewPing sonar(PinTrig, PinEcho, DISTANCIA_ALERTA);

//Initialize the LCD display
LiquidCrystal_I2C lcd(0x27, 16, 2);

BlynkTimer timer;

// Enter your Auth token
char auth[] = "GwQJiB-WDTRKg5tneK2WwmPOLvEDh6Z7";

//Enter your WIFI SSID and password
char ssid[] = "plantita";
char pass[] = "12345678";

int obtenDistancia();

void setup() {
  // Debug console
  Serial.begin(115200);
  Serial.print("aaaaaa");

  // Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);
  // lcd.init();
  // lcd.backlight();
  pinMode(relay, OUTPUT);
  digitalWrite(relay, HIGH);
  // Ponemos el pin Trig en modo salida
  pinMode(PinTrig, OUTPUT);
  // Ponemos el pin Echo en modo entrada
  pinMode(PinEcho, INPUT);


  // lcd.setCursor(1, 0);
  // lcd.print("System Loading");
  // for (int a = 0; a <= 15; a++) {
  //   lcd.setCursor(a, 1);
  //   lcd.print(".");
  //   delay(200);
  // }
  // lcd.clear();
}

void medirNivelAgua() {
  // Obtiene la mediana de 5 mediciones del tiempo de viaje del
  // sonido entre el sensor y el objeto
  int uS = sonar.ping_median();
  // Calcular la distancia a la que se encuentra el objeto
  int distancia = sonar.convert_cm(uS);
  //if(distancia==DISTANCIA_ALERTA){
  // Serial.print("Rellenar tanque");
  //}
  Serial.println(distancia);
  Serial.print("< Echo");
  digitalWrite(relay, HIGH);
}

//Get the ultrasonic sensor values
void soilMoisture() {
  int value = analogRead(sensor);
  value = map(value, 0, 4095, 0, 100);
  value = (value - 100) * -1;
  // Blynk.virtualWrite(V0, value);
  Serial.println(value);
  Serial.print("< agua");
  digitalWrite(relay, LOW);
}

//Get the button value
BLYNK_WRITE(V1) {
  bool Relay = param.asInt();
  if (Relay == 1) {
    digitalWrite(relay, LOW);
    // lcd.setCursor(0, 1);
    // lcd.print("Motor is ON ");
  } else {
    digitalWrite(relay, HIGH);
    lcd.setCursor(0, 1);
    lcd.print("Motor is OFF");
  }
}

void loop() {
  if (pausa.update()) {
    soilMoisture();
  } else {
    medirNivelAgua();
  }


  // Blynk.run();  //Run the Blynk library

  // delay(5000);
}