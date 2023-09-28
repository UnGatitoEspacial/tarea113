import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/gatop/Downloads"

# Clase Event Hanlder 
class FileEventHandler(FileSystemEventHandler):
    
    #1_on_created
    def on_created(self, event):
        print(f"¡Oye {event.src_path} ha sido creado!")

    #2_on_deleted
    def on_deleted(self, event):
        print(f"¡Lo siento! ¡Alguien borró!{event.src_path}")

    #3_on_modified
    def on_modified(self, event):
        print(f"¡Hola! {event.src_path} ha sido modificado")
    
    #4_on_moved
    def on_moved(self, event):
        print(f"Alguien movió {event.src_path} a {event.dest_path}")        


# Inicia clase Event Handler 
event_handler = FileEventHandler()

# Inicia Observer
observer = Observer()

# Programa the Observer
observer.schedule(event_handler, from_dir, recursive=True)


#Comienza el Observer
observer.start()


#5 Escribe una excepción para keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt: 
    print("¡detenido!")
    observer.stop()


