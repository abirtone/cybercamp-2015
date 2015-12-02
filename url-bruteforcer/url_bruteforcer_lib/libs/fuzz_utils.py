# -*- coding: utf-8 -*-

import string
import requests
import logging

from os import getcwd
from random import choice
from urlparse import urljoin
from os.path import join, abspath
from difflib import SequenceMatcher

log = logging.getLogger(__name__)


BASE_PATH = join(abspath(getcwd()),
				 "resources",
				 "fuzzdb-master",
				 "discovery",
				 "predictable-filepaths")


# ----------------------------------------------------------------------
def get_url_content_and_code(url):
	"""
	:return: Devuelve contenido HTTP y el status code
	:rtype: (contenido, status)

	"""

	r = requests.get(url)

	return r.text, r.status_code


# ----------------------------------------------------------------------
def generate_error_page(base_url):
	"""genera una URL de pagina de error y devuelve su contenido"""

	# generate random text
	random_path = ''.join([choice(string.letters + string.digits) for i in range(20)])

	# build url
	random_url = urljoin(base_url, random_path)

	content, code = get_url_content_and_code(random_url)

	return content


# ----------------------------------------------------------------------
def get_matching(url_content_1, url_content_2):
	return SequenceMatcher(None, url_content_1, url_content_2).quick_ratio()


# ----------------------------------------------------------------------
def fuzz(config):
	"""
	Devuelve una lista con las URLs descubiertas.
	"""
	wordlist_file_path = config.wordlist
	target = config.target[0]
	smart = config.smart
	matching_error = config.ratio

	results = []

	# Resolve wordlist
	if ".fuzz.txt" not in wordlist_file_path:
		wordlist_file_path += ".fuzz.txt"

	wordlist_file = join(BASE_PATH, wordlist_file_path)

	# Load wordlist
	wordlist_elements = []
	with open(wordlist_file, "rU") as f:
		for l in f.readlines():
			wordlist_elements.append(l.replace("\r", "").replace("\n", ""))

	# Get error page
	error_page = generate_error_page(target)

	log.critical("[*] Trying to find %s loaded URLs" % len(wordlist_elements))
	# test each URL
	for x in wordlist_elements:

		# build url
		url = urljoin(target, x)

		log.warning("    - Try '%s'" % url)

		# Get content
		content, code = get_url_content_and_code(url)

		# 200?
		if code == 200:

			# Check if is error page
			if smart:
				if get_matching(content, error_page) < matching_error:
					results.append(url)
			else:
				results.append(url)

	return results
