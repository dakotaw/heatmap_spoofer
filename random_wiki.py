#!/usr/local/python

import wikipedia

def get_random_page():
	"""Return a random wikipedia page as a wikipedia object. """
	return wikipedia.page(wikipedia.random())

def write_page(page, output_file='output.md'):
	"""Write a wikipedia page's title and summary in markdown."""
	with open(output_file, 'w') as f:
		f.write('## {}\n\n'.format(page.title.encode('utf-8')))
		f.write(page.summary.encode('utf-8'))