# -*- coding: utf-8 -*-

from scapy.all import IP, TCP, sr1


def analyze_port(host, port):
	"""
	Funcion que determina el estado de un puerto: Abierto/cerrado

	:param host: target
	:type host: str

	:param port: puerto a comprobar
	:type port: int

	:return: True/False en funcion si el puerto esta abierto/cerrado.
	:rtype: bool
	"""
	res = sr1(IP(dst=host)/TCP(dport=port), verbose=False, timeout=0.2)

	if res is not None and TCP in res:
		if res[TCP].flags == 18:
			return True
	else:
		return False

