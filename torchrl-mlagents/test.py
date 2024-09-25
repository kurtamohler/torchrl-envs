from mlagents_envs.environment import UnityEnvironment

print('Please click the play button in the Unity editor')
env = UnityEnvironment()
print('Running')
env.reset()

try:
    while True:
        for behavior_name, behavior_spec in env.behavior_specs.items():
            action_spec = behavior_spec.action_spec
            observation_spec = behavior_spec.observation_specs
            decision_steps = env.get_steps(behavior_name)[0]
            n_agents = decision_steps.agent_id.size
            action_mask = decision_steps.action_mask
            actions = action_spec.random_action(n_agents)
            # Non-action can also be chosen with:
            #  actions = action_spec.empty_action(n_agents)
            env.set_actions(behavior_name, actions)

        env.step()

finally:
    env.close()
