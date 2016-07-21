#!/usr/local/python

from git import Repo
from os import getcwd
from random import randint
import random_wiki

repo = Repo(getwcd())

# We want between 0 - 10 commits, but want to weight it on the lighter side;
# maybe slightly more realistic this way?
num_commits = randint(0, 5)

while num_commits:

	# Get a random page from Wikipedia and write it to a markdown file. 
	random_page = random_wiki.get_random_page()
	random_wiki.write_page(random_page)
	repo.git.commit(m='message')

	num_commits -= 1