## Play tic-tac-toe in PowerPoint

Inspired by this tweet: https://twitter.com/buildsghost/status/1399971984541249538

The presentation has around 6,000 slides representing every possible game state (and some impossible ones, since I didn't check for wins or ties). You play by clicking on the squares, which are hyperlinks to other slides.

https://user-images.githubusercontent.com/8890878/120588727-ab22d780-c405-11eb-8d27-b615f131951c.mp4

## I don't want to clone a repo and run a python script just to play a terrible gimmicky game of tic-tac-toe!
Fair enough. I've converted it to a [Google Slides presentation](https://docs.google.com/presentation/d/1_uKyq2WGYqu_SmXR-XBeGp5swDvSZzj_ovHLKV2NU68/edit?usp=sharing), which you can play by clicking "Present" on the top right corner. It'll take a minute to load.

## I *do* want to clone a repo and run a python script just to play a terrible gimmicky game of tic-tac-toe!
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python generate_powerpoint.py
```
