def test_pipeline_runs():
    from agent.pipeline import run
    assert run() == "decision made"
