from bluetooth import *
import paho.mqtt.client as mqtt
import time

## 1: open, 0: close

# MQTT CALLBACK #
def on_message(client, userdata, message):
	encoded = message.payload
	if encoded == b'open':
		client_socket.send('1')
		client.publish("crown/state/doorlock", 'opened')
		print("DOORLOCK OPENED")
		time.sleep(3)
		client_socket.send('0')
		client.publish("crown/state/doorlock", 'close')
		print("DOORLOCK CLOSED")

# MQTT CONNECT #
client = mqtt.Client("doorlock")
broker_address = "192.168.0.40"
client.connect(broker_address, 1883)
print("MQTT CONNECTED !!!")

# BLUETOOTH SOCKET CONNECT #
client_socket = BluetoothSocket( RFCOMM )
client_socket.connect(("00:18:E4:0A:00:01", 1))
print("BLUETOOTH CONNECTED !!!")

client.subscribe("crown/doorlock")
client.subscribe("crown/app/doorlock")
client.on_message = on_message
client.loop_forever()
