#!/bin/bash

apt install tcpdump

./ATS-Project/automatisation/BDDAuto.sh

./ATS-Project/automatisation/apacheAuto.sh

./ATS-Project/analyse/script.sh
