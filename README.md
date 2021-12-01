# P8-Humedad

## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta práctica es tener la primera toma de contacto con el sensor de humedad.

En este ejercicio hacemos un programa que encendera un led verde cuando el programa se esté ejecutando, y un led rojo cuando no se detecte
suficiente agua. Se han subido dos programas. Uno que no usa hilos, y otro que si. Se recomienda usar el de hilos ya que es mas rápido,
eficiente y permite al procesador dedicarse a procesos mas importantes si es necesario y finalizar el programa de forma correcta.

**Aclaración:**
Aunque al cerrar el programa que usa hilos con control+c salen varios errores por el terminal, el funcionamiento y finalizacion del mismo
es correcto ya que se nos indica que el programa a cerrado correctamente. Estos warnings se deben a que el hilo es eliminado de forma
un poco abrupta, pero está bien.

**El esquema de es igual que el facilitado en el enunciado a diferencia de lo que se puede intuir de**

```python
   
   #GPIO Mode (BOARD / BCM)
   GPIO.setmode(GPIO.BCM)

   sensorHumedad = 16
   ledVerde=20
   ledRojo=21
```

Si quieres ver un video de demostracion del programa, pulsa [aqui](https://drive.google.com/file/d/1CtN3hMUaAqXXbgcD6rmA94BVnNn1w9FZ/view?usp=sharing).

Para hacer que el programa se ejecute al arrancar tu raspberrey tambien haz lo siguiente:
1)ejecuta en un terminal: chmod +x programaseleccionado.
2)ejecuta en un terminal sudo crontab -e.
3)edita el fichero y escribe: python3 rutaabsolutadetufichero.
4)reinicia tu raspbery y ya lo tendrias.

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
