LB3-MQTT-Python-Twitter
=======================

Die nachfolgende Dokumentation basiert auf einer Projektarbeit, für das Modul 242, an der Technischen Berufsschule Zürich, von Kabashi Aris, Funhoff Thomas und Frunz Kevin.

Idee und Ziele
--------------

![](images/idee.png)

- - -

Anpassungen mbed
----------------

![](images/mbed.png)

- - -

MQTT - Twitter Bridge (Python)
------------------------------

![](images/twitter.png)

- - -

IFTTT
-----

![](images/ifttt.png)

MQTT - IFTTT Bridge
- - -

![](images/webhook.png)

Konfiguration IFTTT
- - -

Umsetzung
---------

Raspberry Pi als MQTT Broker und Gateway zu IFTT aufsetzen:
* [Mosquitto](https://mosquitto.org/) und Python installieren
* `sendmail.py` und `sendtweet.py` anpassen und starten
    
IoTKit als MQTT Publisher aufsetzen:
* [MQTTPublish](https://os.mbed.com/teams/IoTKitV3/code/MQTTPublish/) in Online Compiler importierten
* Variable `hostname` und `port` auf Raspberry Pi anpassen.  
    

