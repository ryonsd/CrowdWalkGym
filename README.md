# CrowdWalkGym
API for reinforcement learning, and crowd movement simulation environments.
CrowdWalk, a multi-agent pedestrian flow simulator, is used for representing crowd movements.

![overview](images/overview.png)

# Environments
| ![two_routes](images/two_routes.gif)          | ![moji](images/moji.gif) |
| ----------------------------------------- | ------------------------------------- |
| Two routes | Real map (moji port) |

When you try learning on "moji" environment, I recommend to use "moji_small" from the perspective of calculation time.
"moji" represents a real map and a generation of pedestrians, but it takes a long time to calculate a congestion degree from all pedestrian locations.
"moji_small" is a low-fidelity version of "moji", and the routes width and number of pedestrians are 1/10.
Its reduction makes the calculation time is shorter, 1 episode is 1 min.
If you test your algorithm tentatively, using "two_routes" is best because 1 episode is 12 seconds.

```
python dqn.py --env_name two_routes
```

# Examples
The result of learning route guidance with DQN that minimizes congestion degree in "two_routes" and "moji" environment.

| ![result](images/result_two_routes.png)          | ![result](images/result_moji.png) |
| ----------------------------------------- | ------------------------------------- |
| Two routes | Real map (moji port) |



