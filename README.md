# Octoprint Status Indicator for blink(1)

Show Octoprint status through the blink(1) USB RGB LED light, written in Python originally, with Bash on the side.

![python](https://img.shields.io/badge/-Python-blue?style=flat-square&logo=python&logoColor=white) ![bash](https://img.shields.io/badge/-Bash-green?style=flat-square&logo=gnu-bash&logoColor=white)


## Resources

- Blink(1) info [here](https://blink1.thingm.com/)

- Blink(1) official Python repo [here:](https://github.com/todbot/blink1-python)

- If you want to write it in Bash, the command line program blink1-tool can be found [here](https://github.com/todbot/blink1#blink1-tool)

- The github page for the blink(1) is [here](https://github.com/todbot/blink1)  


## Requirements
- 3D Printer (tested on Creality Ender 3 Pro)
- Raspberry Pi 
    - Python 3 
    - [Octoprint](https://octoprint.org/) (tested on version 1.4.2)
    - [OctoRest](https://github.com/dougbrion/OctoRest)
    - [Octoprint-cli](https://github.com/UserBlackBox/octoprint-cli)


## Setup (bash)
1. Clone the octoprint-cli repo, and setup with the requirements
`pip3 install -r requirements.txt'

2. Install the octoprint-cli package

3. Test bash script to make sure it's running 

4. Send up as cron job. 


## Setup (python) - TBD