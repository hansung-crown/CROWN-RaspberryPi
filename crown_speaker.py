import paho.mqtt.client as mqtt
import os

# MQTT CALLBACK #
def on_message(client, userdata, message):
	encoded = message.payload
	print(encoded)
	if encoded == b'success':
		client.publish("crown/state/speaker", 'Ididit')
		os.system("sudo omxplayer success.wav")
		print("SUCCESS")
	elif encoded == b'fail':
		client.publish("crown/state/speaker", 'Ididit')
		os.system("sudo omxplayer fail.wav")
		print("FAIL")
	elif encoded == b'start':
		client.publish("crown/state/speaker", 'end')
		os.system("sudo omxplayer fail.wav")
		print("FAIL")

# MQTT CONNECT #
client = mqtt.Client("speaker")
broker_address = "192.168.0.40"
client.connect(broker_address, 1883)
print("MQTT CONNECTED !!!")

client.subscribe("crown/speaker")
client.subscribe("crown/app/speaker")
client.on_message = on_message
client.loop_forever()
