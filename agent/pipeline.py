from agent.steps.extract import extract
from agent.steps.analyze import analyze
from agent.steps.decide import decide

def run():
    data = extract()
    insight = analyze(data)
    return decide(insight)
