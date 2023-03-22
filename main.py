import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import ast
import time

# create global valuable
received_data = None

# Send data from Python to Node-red
publish.single("academics/IoT", "I am Ka Long here", hostname="test.mosquitto.org")



# Define the callback function that will be called when a message is received
'''
def on_message(client, userdata, message):
    print(f"Received message: {str(message.payload.decode('utf-8'))}")
'''
def on_message(client, userdata, message):
    payload_str = message.payload.decode('utf-8')
    payload_dict = ast.literal_eval(payload_str)
    data = payload_dict["data"]
    print(f"Received message data: {data}")
    print(f"Data type: {type(data)}")
    received_data = data

    circulating_fluid_discharge_temperature = received_data[0]
    circulating_fluid_discharge_pressure = received_data[2]
    electric_resistivity_and_conductivity_circulating_fluid = received_data[3]
    status_flag = received_data[4]
    alarm_flag_1 = received_data[5]
    alarm_flag_2 = received_data[6]
    alarm_flag_3 = received_data[7]
    status_flag_2 = received_data[9]
    circulating_fluid_set_temperature = received_data[11]
    ####### status flag ##########
    print(f" main: {received_data}")


    STATUS_FLAG_BIT_MEANING = {
        0: "Run flag",
        1: "Operation stop alarm flag",
        2: "Operation continued alarm flag",
        4: "Press Unit flag",
        5: "Remote status flag",
        9: "Completion of preparation (TEMP READY) flag",
        10: "Temperature unit flag",
        11: "Run timer flag",
        12: "Stop timer flag",
        13: "Reset after power failure flag",
        14: "Anti-freezing flag",
        15: "Automatic fluid filling flag",
    }

    # Extract the value of each bit and print the corresponding status
    for bit, meaning in STATUS_FLAG_BIT_MEANING.items():
        bit_value = (status_flag >> bit) & 1
        print(f"{meaning}: {bit_value}")

    time.sleep(2)
    status_flag =received_data[5]

    STATUS_FLAG_BIT_MEANING = {
        0: "Run flag",
        1: "Operation stop alarm flag",
        2: "Operation continued alarm flag",
        4: "Press Unit flag",
        5: "Remote status flag",
        9: "Completion of preparation (TEMP READY) flag",
        10: "Temperature unit flag",
        11: "Run timer flag",
        12: "Stop timer flag",
        13: "Reset after power failure flag",
        14: "Anti-freezing flag",
        15: "Automatic fluid filling flag",
    }

    # Extract the value of each bit and print the corresponding status
    for bit, meaning in STATUS_FLAG_BIT_MEANING.items():
        bit_value = (status_flag >> bit) & 1
        print(f"{meaning}: {bit_value}")


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