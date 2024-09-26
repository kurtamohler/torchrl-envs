from mlagents_envs.environment import UnityEnvironment

print('Please click the play button in the Unity editor')
env = UnityEnvironment()
print('Running')
env.reset()

def print_specs(env):
    print('behavior_specs:')
    for behavior_name, behavior_spec in env.behavior_specs.items():
        print(f'  behavior_name: {behavior_name}')

        for idx, observation_spec in enumerate(behavior_spec.observation_specs):
            print(f'    observation_spec[{idx}]:')
            name = observation_spec.name
            shape = observation_spec.shape
            dimension_property = observation_spec.dimension_property
            observation_type = observation_spec.observation_type
            print(f'      name: {name}')
            print(f'      shape: {shape}')
            print(f'      dimension_property: {dimension_property}')
            print(f'      observation_type: {observation_type}')

        action_spec = behavior_spec.action_spec
        is_continuous = action_spec.is_continuous()
        continuous_size = action_spec.continuous_size
        is_discrete = action_spec.is_discrete()
        discrete_branches = action_spec.discrete_branches
        print(f'    action_spec: {action_spec}')
        print(f'      is_continuous: {is_continuous}')
        print(f'      continuous_size: {continuous_size}')
        print(f'      is_discrete: {is_discrete}')
        print(f'      discrete_branches: {discrete_branches}')

def print_steps(env):
    print('current steps:')
    for behavior_name, behavior_spec in env.behavior_specs.items():
        print(f'  behavior_name: {behavior_name}')

        for idx, step_type in enumerate(['decision', 'terminal']):
            print(f'    {step_type} step:')
            step = env.get_steps(behavior_name)[idx]
            agent_id = step.agent_id
            group_id = step.group_id
            observation_shapes = [ob.shape for ob in step.obs]
            reward = step.reward
            group_reward = step.group_reward

            print(f'      agent_id: {agent_id}')
            print(f'      group_id: {group_id}')
            print(f'      observation_shapes: {observation_shapes}')
            print(f'      reward: {reward}')
            print(f'      group_reward: {group_reward}')

            if idx == 0:
                action_mask = step.action_mask
                if action_mask:
                    action_mask_shapes = [mask.shape for mask in action_mask]
                    print(f'      action_mask_shapes: {action_mask_shapes}')
                else:
                    print(f'      action_mask: {action_mask}')


print_specs(env)
print_steps(env)

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
