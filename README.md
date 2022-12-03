<!-- PROJECT LOGO -->
<br />
<p align="center">
<a href="https://imgbb.com/"><img src="https://i.ibb.co/5GN9Ctj/logo.png" alt="logo" border="0"></a>
<h3 align="center">Eldery Fall Detection</h3>

  <p align="center">
This Repository is for the model proposed by Tech Phantoms Team during the devfest22
    <br />
    <br />
Falls that are not detected in time are a major health risk for the elderly. With today's home automation or smart sensors, in 6 out of 7 falls, someone is only there after 5 minutes to help the client. In addition, healthcare personnel are inundated with false alarms.


## Solution
To get rid of the previous problems at a lower cost, we developed a new monitoring system, based on a computer vision model that uses Mediapipe to detect landmarks and then, based on these landmarks and other mathematical formulas, predict whether or not there is a fall with an estimate of the most damaged body part.
<p align="center">
<img src="examples/savio demo.gif" width="620" />
</p>

## Setup
```shell script
pip install -r requirements.txt
```

## Usage
```shell script
python3 index.py
```
## Team members
<li>Ayoub Khenfouf</li>
<li>Hanad Nada</li>
<li>Bendaho Sarra</li>
<li>Belkacemi Meriem</li>
<li>Chenni Nidhal Eddine</li>
