Pi Project
==========
.. note::
    Group Members: John Bradshaw, Michael Scales, Matthew Wiederaenders, Nicholas Moore
    
    Our report is a sphinx project located in the docs.

**To view report:**

Clone the repo and navigate to *docs/build/html/index.html*

Contributions:

* John: Sphinx, Git, project research
* Matt: Docker, Bash, Pi setup for remote access
* Mike: Google Transcription API, Docker Python Container, File System Mapping
* Nick: Python

|
|	\pi_project
|	/
|	\|--bin
|		\--scribe.py
|	\|--lib
|		\--AudioTranscription.py
|		\--read.py
|	\|--src
|		\--facory.py
|	\|--test
|		\--wav_file_examples.wav
|		\--transcribed_wav_files.txt
|	\|--secret
|		\--XX
|	main.py
|	README.rst
|	push.sh
|

Dependencies
------------
|	'requirements.txt'
|	SpeechRecognition==3.6.1
|	argparse==1.2.1
|	## FIXME: could not find svn URL in \dependency_links for this package:
|	distribute==0.6.24dev-r0
|	google-api-python-client==1.6.2
|	httplib2==0.10.3
|	oauth2client==4.0.0
|	pyasn1==0.2.3
|	pyasn1-modules==0.0.8
|	rsa==3.4.2
|	six==1.10.0
|	uritemplate==3.0.0
|	virtualenv==1.7.1.2
|	wsgiref==0.1.2
|   #Python Version: 2.7

Discussion
**********
|
| 	Docker:
|	Use a dockerfile to create an image of a container to run a python application.
|	The python container needs flac as an audio codec for converting the incoming wav files.
|	In order to ease downloading python modules we also included pip.
|	Using pip we install SpeechRecognition and google's cloud speech api.
|	Some attempt was made into cloning the git repo in the dockerfile, but efforts to coordinate placing the ssh files into the docker image are in development.
|
|	Python:
|	Our entry point into this application starts in main.py. Main sets the environment variables for the rest of our application and sends the incoming wav files to scribe.
|	Scribe sends the wav file to AudioTranscription. The incoming wav file is sent to google's cloud service where it crunches the data.
|	The returned data is read into a text file. This step is repeated for additional wav files.
|	The txt file(s) is/are pushed up to our github where the world can see what we said in the wav file(s).
|
|	Record Wav File/Push to GitHub:
|	Execute shell 'record_wav_to_git.sh' to record wav file from local machine after cloning the repo. Default is to record for 5 seconds but length of recording may be changed by typing 'record_wav_to_git.sh 10' to record for 10, or any integer value. Langer recordings though are larger and take more time to process. A 20 second recording is several MBs. The script will automatically ensure the repo is up to date on the local machine, record a wav file, and then push that wav file to /pi_project/test/ using a timestamp and naming convention to ensure unique file names.
