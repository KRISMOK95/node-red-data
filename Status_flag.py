from main import received_data
def process_received_data():
    global received_data  # Use the global variable
    if received_data is not None:
        # Do something with the received data
        print(f"Received data: {received_data}")
    else:
        print("No data received yet")

print(received_data)

status_flag = [0, 0, 0, 0, 32, 0][4]  # example value, replace with your own

# Define the meaning of each bit
BIT_MEANING = {
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
for bit, meaning in BIT_MEANING.items():
    bit_value = (status_flag >> bit) & 1
    print(f"{meaning}: {bit_value}")
