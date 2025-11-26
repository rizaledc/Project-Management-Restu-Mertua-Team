import pygame
import paho.mqtt.client as mqtt
import sys
import time

BROKER = "broker.hivemq.com"
TOPIC = "restumertua/automind/control/rizal_fix_99"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Controller_Laptop")
print("Menghubungkan ke Broker...")
try:
    client.connect(BROKER, 1883, 60)
    print("TERHUBUNG! Siap mengendalikan.")
except:
    print("Gagal koneksi internet. Cek WiFi Anda.")

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("CONTROLLER (Klik Disini)")

font = pygame.font.SysFont(None, 24)
last_cmd = ""

def kirim(cmd):
    global last_cmd
    if cmd != last_cmd:
        client.publish(TOPIC, cmd)
        print(f"Mengirim: {cmd}")
        last_cmd = cmd

print("Klik jendela 'CONTROLLER' yang muncul, lalu tekan Panah Keyboard.")

running = True
while running:
    screen.fill((50, 50, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    status_text = "STOP"
    if keys[pygame.K_UP]:
        kirim("MAJU")
        status_text = "MAJU"
    elif keys[pygame.K_DOWN]:
        kirim("MUNDUR")
        status_text = "MUNDUR"
    elif keys[pygame.K_LEFT]:
        kirim("KIRI")
        status_text = "KIRI"
    elif keys[pygame.K_RIGHT]:
        kirim("KANAN")
        status_text = "KANAN"
    else:
        kirim("STOP") 

    txt = font.render(f"Kirim: {status_text}", True, (0, 255, 0))
    screen.blit(txt, (20, 80))
    txt2 = font.render("Fokus/Klik jendela ini untuk mengontrol!", True, (200, 200, 200))
    screen.blit(txt2, (20, 20))

    pygame.display.flip()
    time.sleep(0.05) 

pygame.quit()