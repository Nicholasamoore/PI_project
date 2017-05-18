from sys import argv
from os import path, sys, environ


from bin.scribe import main


if __name__ == '__main__':
	print('my directory is')
	print(path.dirname(path.abspath(__file__)))
	environ['GOOGLE_APPLICATION_CREDENTIALS'] = "{}/secret/audio transcription-259fc609e0f1.json".format(path.dirname(path.abspath(__file__)))
	# environ['GIT_SSH_COMMAND'] = ssh_cmd
	sys.path.append(path.dirname(path.abspath(__file__)))
	main(*argv[1:])

