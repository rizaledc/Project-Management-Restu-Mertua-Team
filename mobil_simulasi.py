import pygame
import paho.mqtt.client as mqtt
import sys

BROKER = "broker.hivemq.com"
TOPIC = "restumertua/automind/control/rizal_fix_99"
current_command = "STOP"

def on_message(client, userdata, msg):
    global current_command
    try:
        current_command = msg.payload.decode()
        print(f"Pesan Masuk: {current_command}")
    except:
        pass

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Mobil_Virtual")
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)
client.loop_start()

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mobil AutoMind")
clock = pygame.time.Clock()

x, y = 200, 200
speed = 3

while True:
    screen.fill((20, 20, 20)) # Layar Hitam
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    if current_command == "MAJU": y -= speed
    elif current_command == "MUNDUR": y += speed
    elif current_command == "KIRI": x -= speed
    elif current_command == "KANAN": x += speed

    if x < 0: x = 0
    if x > 360: x = 360
    if y < 0: y = 0
    if y > 340: y = 340

    pygame.draw.rect(screen, (200, 50, 50), (x, y, 40, 60))
    pygame.draw.rect(screen, (255, 255, 0), (x+5, y, 10, 5))
    pygame.draw.rect(screen, (255, 255, 0), (x+25, y, 10, 5))

    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Status: {current_command}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)