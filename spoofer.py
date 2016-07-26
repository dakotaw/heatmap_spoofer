#!/usr/local/ python

from git import Repo
from datetime import datetime
from random import normalvariate as randnorm
import wikipedia
import os

def get_random_page():
	"""Return a random wikipedia page as a wikipedia object. """
	return wikipedia.page(wikipedia.random())

def write_page(page, output_file='heatmap_spoofer/output.md'):
	"""Write a wikipedia page's title and summary in markdown.
	   Returns output file name."""
	with open(output_file, 'w') as f:
		f.write('## {}\n\n'.format(page.title.encode('utf-8')))
		try:
			f.write(page.summary.encode('utf-8'))
		except wikipedia.exceptions.DisambiguationError:
			f.write('Disambiguation page, cannot summarize.')

	return output_file

def main():

	repo = Repo(os.path.dirname(os.path.abspath(__file__)))

	# Choose how many commits for the day.
	num_commits = int(randnorm(2.5, 1.25))
	print 'Running {} commits.'.format(num_commits)

	while num_commits > 0:

		# Get a random page from Wikipedia and write it to a markdown file. 
		random_page = get_random_page()
		outfile = write_page(random_page)
		
		repo.git.add(outfile)
		commit_message = 'Commiting article on {}.'.format(random_page.title.encode(
			'utf-8'))
		print commit_message
		repo.git.commit(m=commit_message)
		repo.git.push()

		num_commits -= 1

if __name__ == '__main__':
	main()