import swarmnode

from .fixtures import prepare_and_teardown  # noqa: F401


def test_agent_builder_job(prepare_and_teardown):
    data = prepare_and_teardown

    jobs = swarmnode.AgentBuilderJob.list(agent_id=data["agent_id"])
    assert jobs.total_count == 1
    assert jobs.results[0].id == data["agent_builder_job_id"]

    job = swarmnode.AgentBuilderJob.retrieve(data["agent_builder_job_id"])
    assert job.id == data["agent_builder_job_id"]


def test_build(prepare_and_teardown):
    data = prepare_and_teardown

    builds = swarmnode.Build.list(agent_builder_job_id=data["agent_builder_job_id"])
    assert builds.total_count == 1
    assert builds.results[0].id == data["build_id"]

    build = swarmnode.Build.retrieve(data["build_id"])
    assert build.id == data["build_id"]


def test_execution(prepare_and_teardown):
    data = prepare_and_teardown

    executions = swarmnode.Execution.list(agent_id=data["agent_id"])
    assert len(executions.results) == 1
    assert executions.results[0].id == data["execution_id"]

    execution = swarmnode.Execution.retrieve(data["execution_id"])
    assert execution.id == data["execution_id"]


def test_agent_executor_job(prepare_and_teardown):
    data = prepare_and_teardown

    swarmnode.AgentExecutorJob.create(agent_id=data["agent_id"], payload={"foo": "bar"})

    jobs = swarmnode.AgentExecutorJob.list(agent_id=data["agent_id"])
    assert len(jobs.results) == 2

    job = swarmnode.AgentExecutorJob.retrieve(data["agent_executor_job_id"])
    assert job.id == data["agent_executor_job_id"]


def test_agent(prepare_and_teardown):
    data = prepare_and_teardown

    agent = swarmnode.Agent.create(
        name="testagent2",
        script="def main():\n    print('hello world')\n",
        requirements="requests",
        env_vars="FOO=BAR",
        python_version="3.9",
        store_id=data["store_id"],
    )
    assert swarmnode.Agent.update(agent.id, name="updated").name == "updated"
    assert swarmnode.Agent.list().total_count == 2
    assert swarmnode.Agent.retrieve(agent.id).id == agent.id
    swarmnode.Agent.delete(agent.id)
    assert swarmnode.Agent.list().total_count == 1


def test_execute_agent(prepare_and_teardown):
    data = prepare_and_teardown

    agent = swarmnode.Agent.retrieve(data["agent_id"])

    execution = agent.execute()
    assert type(execution) is swarmnode.Execution

    agent_executor_job = agent.execute(wait=False)
    assert type(agent_executor_job) is swarmnode.AgentExecutorJob


def test_agent_executor_cron_job(prepare_and_teardown):
    data = prepare_and_teardown

    cron_job = swarmnode.AgentExecutorCronJob.create(
        agent_id=data["agent_id"], name="test", expression="* * * * *"
    )
    assert cron_job.status == "running"
    assert (
        swarmnode.AgentExecutorCronJob.update(cron_job.id, status="suspended").status
        == "suspended"
    )
    assert (
        swarmnode.AgentExecutorCronJob.list(agent_id=data["agent_id"]).total_count == 1
    )
    assert swarmnode.AgentExecutorCronJob.retrieve(cron_job.id).id == cron_job.id
    swarmnode.AgentExecutorCronJob.delete(cron_job.id)
    assert (
        swarmnode.AgentExecutorCronJob.list(agent_id=data["agent_id"]).total_count == 0
    )


def test_store():
    store = swarmnode.Store.create("test")
    assert swarmnode.Store.update(store.id, name="updated").name == "updated"
    assert swarmnode.Store.list().total_count == 2
    assert swarmnode.Store.retrieve(store.id).id == store.id
    swarmnode.Store.delete(store.id)
    assert swarmnode.Store.list().total_count == 1
