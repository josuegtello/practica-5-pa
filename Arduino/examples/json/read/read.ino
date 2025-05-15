#include <ArduinoJson.h>
class Json{
    public:
        DynamicJsonDocument parse(const String& payload){
            // Calcular el tamaño necesario para el documento JSON
            const size_t capacity = JSON_OBJECT_SIZE(10) + payload.length();
            DynamicJsonDocument doc(capacity);

            // Deserializar el String JSON (parsear)
            DeserializationError error = deserializeJson(doc, payload);
            // Verificar si hubo un error en la deserialización
            if (error) {
                Serial.print(F("Error al deserializar el JSON: "));
                Serial.println(error.c_str());
                // Retornamos un documento vacío en caso de error
                return DynamicJsonDocument(0);
            }
            return doc;
        }
        String stringify(const DynamicJsonDocument& doc) {
            // Calculamos el tamaño necesario para el JSON serializado
            size_t jsonSize = measureJson(doc);
             // Creamos un buffer del tamaño exacto necesario
            String json_string;
            json_string.reserve(jsonSize);
            // Serializamos el objeto JSON directamente a la String
            serializeJson(doc, json_string);

            return json_string;
        }
};

Json JSON;

void setup(){
    Serial.begin(115200);
    Serial.println("Inicializando Placa");
    Serial.println("Leyendo un JSON string");
    String json = "{\"nombre\":\"Ramses\", \"edad\":25}";
    DynamicJsonDocument response = JSON.parse(json);
    String nombre=response["nombre"];
    int edad=response["edad"];
    Serial.println("Respuesta");
    Serial.print("Nombre:");
    Serial.print(nombre);
    Serial.print("Edad:");
    Serial.println(edad);
}

void loop(){

}


