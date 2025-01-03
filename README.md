# Ally


Ally is an interactive social media agent built using [SwarmNode](https://github.com/swarmnode-ai) framework

Follow Ally: [Ally_SNAI](https://x.com/ally_snai)

## Documentation

Full documentation of the SDK is available at [https://swarmnode.ai/docs/sdk/introduction](https://swarmnode.ai/docs/sdk/introduction). You may also want to check out the [REST API Reference](https://swarmnode.ai/docs/api/v1/introduction).

## Installation

You can install the SDK via `pip`:

```bash
pip install swarmnode
```

## Usage

Once installed, you can use it to make requests.

### Create an Agent

```python
import swarmnode

swarmnode.api_key = "YOUR_API_KEY"

agent = swarmnode.Agent.create(
    name="My Agent",
    script="def main(request, store):\n    return request.payload",
    requirements="requests==2.31.0\npandas==2.1.4",
    env_vars="FOO=bar\nBAZ=qux",
    python_version="3.11",
    store_id="b553e996-6556-42dd-8990-ddb7ef2142f6",
)
```

### Execute an Agent

```python
import swarmnode

swarmnode.api_key = "YOUR_API_KEY"

agent = swarmnode.Agent.retrieve(id="15d19ca3-26f1-4adb-9cea-3955b73d9b4e")

execution = agent.execute(payload={"key": "value"})
```

### Create a Cron Job

```python
import swarmnode

swarmnode.api_key = "YOUR_API_KEY"

cron_job = swarmnode.AgentExecutorCronJob.create(
    agent_id="15d19ca3-26f1-4adb-9cea-3955b73d9b4e",
    name="My cron job",
    expression="* * * * *",
)
```

### Stream Executions from a Cron Job

```python
import swarmnode

swarmnode.api_key = "YOUR_API_KEY"

cron_job = swarmnode.AgentExecutorCronJob.retrieve(id="f3384d13-7a32-4abe-9c10-964ca17413b7")

for execution in cron_job.stream():
    # Every time a new execution is created, it will be printed.
    print(execution)
```

These are only a few examples of what you can do with the SDK. Refer to the [full documentation](https://swarmnode.ai/docs/sdk/introduction) to learn more about the SDK.
