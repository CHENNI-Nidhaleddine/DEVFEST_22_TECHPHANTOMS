<!-- PROJECT LOGO -->
<br />
<p align="center">
<a href="https://imgbb.com/"><img src="https://i.ibb.co/5GN9Ctj/logo.png" alt="logo" border="0"></a>
<h3 align="center">Eldery Fall Detection</h3>

  <p align="center">
This Repository is for the model proposed by Tech Phantoms Team during the devfest22
    <br />
    <br />
We augment human pose estimation
(openpifpaf library) by support for multi-camera and multi-person tracking and a long short-term memory (LSTM)
neural network to predict two classes: “Fall” or “No Fall”. From the poses, we extract five temporal and spatial
features which are processed by an LSTM classifier.
<p align="center">
<img src="examples/savio demo.gif" width="420" />
</p>

## Setup

```shell script
pip install -r requirements.txt
```

## Usage
```shell script
python3 index.py
```
