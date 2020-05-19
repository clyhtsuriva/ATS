#!/bin/bash

apt install tcpdump

./ATS/automatisation/BDDAuto.sh

./ATS/automatisation/apacheAuto.sh

./ATS/analyse/script.sh
