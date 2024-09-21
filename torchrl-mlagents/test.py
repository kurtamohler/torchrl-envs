from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.envs.unity_aec_env import UnityAECEnv
from mlagents_envs.envs.unity_parallel_env import UnityParallelEnv
from pettingzoo.test import api_test, parallel_api_test

print('Please click the play button in the Unity editor')
env_unity = UnityEnvironment()
print('Running')


env = UnityParallelEnv(env_unity)

try:
  while True:
    parallel_api_test(env)

finally:
  env_unity.close()