# torchrl-mlagents

This environment is for setting up a torchrl development environment of along
with an installation of Unity's ml-agents toolkit.

## Installation

NOTE: These instructions are partially based on the [installation
instructions](https://unity-technologies.github.io/ml-agents/Installation/)
provided by ml-agents, but adapted to work with a torchrl development
environment.

### Install conda env

```bash
conda env create -n torchrl-mlagents -f environment.yml
```

### Activate conda env

```bash
conda activate torchrl-mlagents
```

### Install prerequisites for torchrl and ml-agents

```bash
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
pip3 install tensordict-nightly
```

### Clone and install ml-agents

```bash
cd <some-work-directory>
git clone --branch release_21 https://github.com/Unity-Technologies/ml-agents.git
cd ml-agents
python -m pip install ./ml-agents-envs
python -m pip install ./ml-agents
```

### Confirm that ml-agents was installed properly

```bash
mlagents-learn --help
```

### Clone and install torchrl

```bash
cd <some-work-directory>
git clone git@github.com:pytorch/rl.git torchrl
cd torchrl
pip3 install ninja -U
python setup.py develop
```

### Confirm that torchrl was installed properly

```bash
python -c 'import torchrl; print(torchrl.__version__)'
python test/test_actors.py
```

### Install Unity Hub

Follow these instructions: <https://docs.unity3d.com/hub/manual/InstallHub.html>

## Open a Unity project

We need to open a Unity project to use as a training environment. We can use the
example project included with the `ml-agents` github repo. In Unity Hub, go to
"Projects", click "Add", navigate to the `ml-agents` directory you cloned, click
the `Project` directory, and then click "Open". The Unity project importer will
recommend installing a certain version of the Unity editor.  Select the one it
suggests, and after it's finished installing, open the project you imported.

In the Project explorer, go to `Assets/ML-Agents/Examples/3DBall/Scenes/` and
open the `3DBall` scene.

### Run a pretrained model

Click the play button near the top middle of the Unity editor, and the
simulation should start running with a pre-trained model. There should be 12
blockheads balancing a ball by rotating. Click the play button again to stop.

### Train a new model

Now you can follow the ["Training the
environment"](https://unity-technologies.github.io/ml-agents/Getting-Started/#training-the-environment)
step from the `ml-agents` guide to easily start a new training session.

## Control Unity environment from Python

Open a Unity project that is set up for ML-Agents (like `3DBall`). Make sure the
simulation is not running. Open a Python terminal and run:

```python
>>> import mlagents_envs.environment
>>> env_unity = mlagents_envs.environment.UnityEnvironment()
```

NOTE: Not sure about this yet. Look at
`ml-agents-envs/tests/test_pettingzoo_wrapper.py`.

This last line will hang, waiting for you to click the play button in the Unity
editor. Click the play button and then run:

```python
>>> import mlagents_envs.envs
>>> env_aec = mlagents_envs.envs.unity_aec_env.UnityAECEnv(env_unity)
```

### (Not supported yet) Control Unity environment from TorchRL

```
>>> import torchrl
>>> env = torchrl.envs.PettingZooWrapper(env_aec, use_mask=True)
```