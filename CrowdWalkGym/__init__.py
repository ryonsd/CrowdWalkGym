from gym.envs.registration import register

register(
    id="two-routes-v0",
    entry_point="CrowdWalkGym.envs.TwoRoutes:TwoRoutesEnv"
)