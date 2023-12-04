#define BLYNK_TEMPLATE_ID "TMPL2yx1PllLf"
#define BLYNK_TEMPLATE_NAME "Sistema de Maceta"
#define BLYNK_AUTH_TOKEN "GwQJiB-WDTRKg5tneK2WwmPOLvEDh6Z7"

//Include the library files
#include <Wire.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <NewPing.h>
#include <NoDelay.h>

#define sensor 33
#define relay 4
#define trig 5
#define echo 18


BlynkTimer timer;

const int DISTANCIA_ALERTA = 30;
const long TIEMPO_TAREA = 500;

// Configuramos los pines del sensor Trigger y Echo
noDelay pausa(TIEMPO_TAREA);

// Crea una instancia de la clase NewPing
NewPing sonar(trig, echo, DISTANCIA_ALERTA);

// Enter your Auth token
char auth[] = "GwQJiB-WDTRKg5tneK2WwmPOLvEDh6Z7";

//Enter your WIFI SSID and password
char ssid[] = "INFINITUMA39E_2.4";
char pass[] = "DA6EqvGDK8";

int obtenDistancia();

void setup() {
  // Debug console
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);

  pinMode(relay, OUTPUT);
  digitalWrite(relay, HIGH);
  // Ponemos el pin Trig en modo salida
  pinMode(trig, OUTPUT);
  // Ponemos el pin Echo en modo entrada
  pinMode(echo, INPUT);

timer.setInterval(1000L, medirNivelAgua);

}

//Get the ultrasonic sensor values
void soilMoisture() {
  int value = analogRead(sensor);
  value = map(value, 0, 4095, 0, 100);
  value = (value - 100) * -1;
  Blynk.virtualWrite(V0, value);
  Serial.println(value);
}

void medirNivelAgua() {
  // Obtiene la mediana de 5 mediciones del tiempo de viaje del
  // sonido entre el sensor y el objeto
  int uS = sonar.ping_median();
  // Calcular la distancia a la que se encuentra el objeto
  int distancia = sonar.convert_cm(uS);
  if(distancia<=DISTANCIA_ALERTA){
    //Blynk.email("carmen.hernandez240210@potros.itson.edu.mx","Alerta","Tanque de agua bajo");
    Blynk.logEvent("alerta_agua","El contenedor de agua, se esta quedando vacío!!! Rellénalo pronto :)");
  Serial.print("Rellenar tanque");
  }
  Blynk.virtualWrite(V2, distancia);
  Serial.println(distancia);
  Serial.print("< Echo");
}

//Get the button value
BLYNK_WRITE(V1) {
  bool Relay = param.asInt();
  if (Relay == 1) {
    digitalWrite(relay, LOW);
  } else {
    digitalWrite(relay, HIGH);
  }
}

void loop() {
  soilMoisture();
  medirNivelAgua();
  Blynk.run();//Run the Blynk library
  timer.run();
  //delay(200);

}
