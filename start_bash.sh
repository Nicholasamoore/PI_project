#!/bin/bash
#connect to a container
echo "Connect to container instance : $1" docker exec -it $1 /bin/bash -c "export TERM=xterm; exec bash"
