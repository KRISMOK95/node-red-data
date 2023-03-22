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
    print(f" main: {received_data}")

    ####### status flag ###########

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

    ####### status flag 2 ###########

    STATUS_FLAG_2_BIT_MEANING = {
        0: "Electric resistivity/conductivity setting flag",
        1: "Electric resistivity/conductivity setting flag",
    }

    # Extract the value of each bit and print the corresponding status
    for bit, meaning in STATUS_FLAG_2_BIT_MEANING.items():
        bit_value = (status_flag_2 >> bit) & 1
        print(f"{meaning}: {bit_value}")

    time.sleep(2)

    ################### alarm flag 1 #################

    ALARM_FLAG_1_BIT_MEANING = {
        0: "Low level in tank",
        1: "High circulating fluid discharge temp",
        2: "Circulating fluid discharge temp. rise",
        3: "Circulating fluid discharge temp.",
        4: "High circulating fluid return temp..",
        5: "High circulating fluid discharge pressure",
        6: "Abnormal pump operation",
        7: "Circulating fluid discharge pressure rise",
        8: "Circulating fluid discharge pressure drop",
        9: "High compressor intake temp",
        10: "Low compressor intake temp.",
        11: "Low super heat temperature",
        12: "High compressor discharge pressure",
        14: "Refrigerant circuit pressure (high pressure side) drop",
        15: "Refrigerant circuit pressure (low pressure side) rise",
    }
    # Extract the value of each bit and print the corresponding status
    for bit, meaning in ALARM_FLAG_1_BIT_MEANING.items():
        bit_value = (alarm_flag_1 >> bit) & 1
        print(f"Alarm flag: {meaning} /// {bit_value}")

    time.sleep(2)
    ################### alarm flag 2 #################

    ALARM_FLAG_2_BIT_MEANING = {
        0: "Refrigerant circuit pressure (low pressure side) drop",
        1: "Compressor overload",
        2: "Communication error",
        3: "Memory error",
        4: "DC line fuse cut",
        5: "Circulating fluid discharge temp. sensor failure",
        6: "Circulating fluid return temp. sensor failure",
        7: "Compressor intake temp. sensor failure",
        8: "Circulating fluid discharge pressure sensor failure",
        9: "Compressor discharge pressure sensor failure",
        10: "Compressor intake pressure sensor failure",
        11: "Maintenance of pump",
        12: "Maintenance of fan motor",
        13: "Maintenance of compressor",
        14: "Contact input 1 signal detection alarm",
        15: "Contact input 2 signal detection alarm",
    }
    # Extract the value of each bit and print the corresponding status
    for bit, meaning in ALARM_FLAG_2_BIT_MEANING.items():
        bit_value = (alarm_flag_2 >> bit) & 1
        print(f"Alarm flag: {meaning} /// {bit_value}")
    time.sleep(2)
    ################### alarm flag 2 #################

    ALARM_FLAG_3_BIT_MEANING = {
        0: "Water leakage",
        1: "Electric resistivity/conductivity level rise",
        2: "Electric resistivity/conductivity level drop",
        3: "Electric resistivity/conductivity sensor error",

    }
    # Extract the value of each bit and print the corresponding status
    for bit, meaning in ALARM_FLAG_3_BIT_MEANING.items():
        bit_value = (alarm_flag_3 >> bit) & 1
        print(f"Alarm flag: {meaning} /// {bit_value}")
    time.sleep(2)

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