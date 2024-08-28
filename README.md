# A* solver

Here we a a simple implementation of a A* puzzle solver
It uses distance to goal based heuristc and Dikjstra algorithm to find the optimal way the fastest as possible.

### Install dependencies
```bash
pip install -r requirements.txt
```
## Run pygame  view
```bash
python main.py
```
You can write on obstacles_map in main the obstacles matrix using method set_obstacles.
By default obstacles are randomly generated.
OBS: code may fail if it's impossible to find a way

