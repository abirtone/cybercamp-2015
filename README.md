Cybercamp 2015
==============


![Logo](https://raw.githubusercontent.com/abirtone/cybercamp-2015/master/banner.png)

*url_bruteforcer: Descubridor de directorios en URLs por fuerza bruta*


Qué es Cybercamp 2015
----------------------

Este repositorio contiene los códigos de ejemplo y los enlaces de la charla impartida por nuestro compañero [Daniel García (cr0hn) - @ggdaniel](https://www.linkedin.com/in/garciagarciadaniel) en el Cybercamp 2015:

**Python, hacking y sec-tools desde las trincheras**

Slides | http://www.slideshare.net/cr0hn/cybercamp-2015-python-hacking-y-sectools-desde-las-trincheras
---- | -----------------------------------------------------------------------------------------------
Video [es] | https://www.youtube.com/watch?v=LD6qw4TnQPI
Video [en] | https://www.youtube.com/watch?v=eqxpuSzI0RQ

Índice
------

Este repositorio contiene los siguientes códigos de ejemplo:

+ cyberscan: scanner de puertos usando la metodología OMSTD y el motor de creación STB para crear herramientas escalables y mantenibles.
+ python-nmap: convertidor de ficheros XML de nmap en ficheros JSON.
+ url-bruteforcer: herramienta, basada en STB y OMSTD, capaz de hacer un descubrimiento por fuerza bruta de URLs, basado en diccionarios, con la capacidad de distinguir de manera inteligente las páginas de error con el fin de filtrar falsos positivos e incrementar el ratio de acierto.
+ single-files:
   + arp_flood.py: implementación del ataque ARP flood con Scapy.
   + demo-fuzzing.py: ejemplo de un ataque de fuzzing usando Scapy y paquetes ICMP.
   + dhcp_starvation.py: implementación de ataque DHCP starvation con Scapy. Capaz de agotar el poll de IPs en servidores DHCP mal configurados.
   + port-scanner.py: simple escaneador de puertos mono-hilo con Scapy.
   + port-scanner-multithread.py: simple escaneador de puertos multi-hilo con Scapy.
   + dns_collect.py: analizador de tráfico de red, capaz de extraer todas las consultas DNS realizadas en una LAN.

Referencias
-----------

+ STB: Generador de herramientas de seguridad escalables y mantenibles - https://github.com/abirtone/STB
+ OMSTD: Metodología de creación de herramientas de seguridad - http://omstd.readthedocs.org
