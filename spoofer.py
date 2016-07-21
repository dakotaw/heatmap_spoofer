#!/usr/local/python

from git import Repo
from os import getcwd
from datetime import datetime
from random import normalvariate as randnorm
import random_wiki

# Set repo to current directory.
repo = Repo(getcwd())

# We want between 0 - 10 commits, but want to weight it on the lighter side;
# maybe slightly more realistic this way?
num_commits = int(randnorm(2.5, 1.25))

while num_commits > 0:

	# Get a random page from Wikipedia and write it to a markdown file. 
	random_page = random_wiki.get_random_page()
	outfile = random_wiki.write_page(random_page)
	
	repo.git.add(outfile)
	repo.git.commit(m='Commiting article on {}.'.format(random_page.title.encode(
		'utf-8')))
	repo.git.push()

	num_commits -= 1