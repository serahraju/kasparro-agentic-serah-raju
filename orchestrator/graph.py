from typing import Dict, Any, List
from agents.base import Agent

class OrchestrationGraph:
    """
    Orchestrator that repeatedly scans agents and lets any agent run
    when its can_run(state) is True, until no more progress.
    """

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def run(self, initial_state: Dict[str, Any]) -> Dict[str, Any]:
        state = dict(initial_state)
        progress = True

        while progress:
            progress = False
            for agent in self.agents:
                if agent.can_run(state):
                    state = agent.run(state)
                    progress = True

        return state
