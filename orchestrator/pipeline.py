from orchestrator.graph import OrchestrationGraph
from agents.product_parser_agent import ProductParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.content_agent import ContentLogicAgent
from agents.template_agent import TemplateAgent

def build_pipeline() -> OrchestrationGraph:
    graph = OrchestrationGraph()
    graph.add_agent(ProductParserAgent())
    graph.add_agent(QuestionGenerationAgent())
    graph.add_agent(ContentLogicAgent())
    graph.add_agent(TemplateAgent())
    return graph
