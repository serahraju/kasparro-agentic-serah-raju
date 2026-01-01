from abc import ABC, abstractmethod
from typing import Dict, Any

class Agent(ABC):
    """
    Base class for all agents.
    Agents decide autonomously whether they should run based on shared state.
    """

    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def can_run(self, state: Dict[str, Any]) -> bool:
        """
        Decide if this agent should run based on current state.
        """
        ...

    @abstractmethod
    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute agent logic and mutate shared state.
        """
        ...
