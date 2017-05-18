# To use Gitpython:
# pip install gitpython

import sys
from datetime import datetime
from os import getcwd
from os.path import dirname, abspath
from sys import argv
# from git import Repo


def read(inc_text):
	
	ts = datetime.today().now().time()
	textFile = "/{lvl_back}/test/{timestamp}_transcription.txt".format(lvl_back=dirname(dirname(abspath(__file__))),
										 timestamp=ts)
	print('test stuff')
	print(getcwd())
	print(textFile)
	print(dirname(abspath(__file__)))

	# Open file	
	with open(textFile, mode="wb") as f:
		f.seek(0)
		f.write(inc_text)

	# Push and commit to GitHub
	# repo = Repo('.git')
	# file_list = [textFile] # Text file location
	# commit_message = 'Test push'
	# repo.index.add(file_list)
	# repo.index.commit(commit_message)
	# origin = repo.remote('origin')
	# origin.push()

	# I need to figure out a way to automatically push without prompting for user/pass

if __name__ == "__main__":
	read(argv[1])


