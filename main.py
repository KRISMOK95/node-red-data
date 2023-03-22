import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

# Send data from Python to Node-red
publish.single("academics/IoT", "I am Ka Long here", hostname="test.mosquitto.org")



# Define the callback function that will be called when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {str(message.payload.decode('utf-8'))}")

# Set up the MQTT client and connect to the broker
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)

# Set up the callback function to be called when a message is received
client.on_message = on_message

# Subscribe to the "academics/IoT" topic
client.subscribe("academics/IoT")

# Start the MQTT client loop to listen for incoming messages
client.loop_forever()

print("Done")