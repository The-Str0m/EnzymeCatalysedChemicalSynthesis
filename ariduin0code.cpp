--
const float VOLUME_L = 1.0;   
const float AIR_PUMP_FLOW_LPM = 2.0;  

const int PUMP_PIN = 3;   
const unsigned long PUMP_RUN_TIME_MS = 5000; 


unsigned long aerationPauseMs = 0;
unsigned long previousMillis = 0;
bool isPumpRunning = false;

void setup() {
  Serial.begin(9600);
  pinMode(PUMP_PIN, OUTPUT);
  
  
  aerationPauseMs = pauseMinutes * 60.0 * 1000.0;

  Serial.print("Calculated Aeration Pause Duration (ms): ");
  Serial.println(aerationPauseMs);
  

  startLiquidDose();
}

void loop() {
  unsigned long currentMillis = millis();

  if (isPumpRunning) {
    
    if (currentMillis - previousMillis >= PUMP_RUN_TIME_MS) {
      startAerationPause();
    }
  } else {
    
    if (currentMillis - previousMillis >= aerationPauseMs) {
      startLiquidDose();
    }
  }
}

