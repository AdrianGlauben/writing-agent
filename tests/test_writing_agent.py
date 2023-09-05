from writing_agent import WritingAgent
from prompt_generator import PromptGenerator
import os

api_key = os.environ.get("OPENAI_API_KEY")
n_initial_drafts = 5
model = "gpt-3.5-turbo"
language = "de"
writing_agent = WritingAgent(api_key, n_initial_drafts, model, language)

text_type = "Missionstatement"
text_length = "100"
factual_content = "Unternehmensname: Deutsche Bank Research Unternehmenstätigkeit Erstellung Unabhängiger volkswirtschaftliche Analysen Verfolgung der relevanten Entwicklungen auf den Finanzmärkten Unternehmenswerte: Qualitativ hochwertig Innovativ Unabhängig Unternehmensziel: Bereichern der offentlichen diskussion in ökonomischen, finanzpolitischen, arbeitsmarkt und sozialpolitischen themen Analysen sollen Investoren bei Anlegeentscheidungen unterstützen"


def test_generate_initial_drafts():
    writing_agent.prompt_generator = PromptGenerator(
        language, text_type, text_length, factual_content
    )
    initial_drafts = writing_agent._generate_initial_drafts(n_initial_drafts)
    print(initial_drafts[0])

    assert isinstance(initial_drafts, list)
    assert len(initial_drafts) == n_initial_drafts
    assert isinstance(initial_drafts[0], str)


def test_write_text():
    resolution = writing_agent.write_text(text_type, text_length, factual_content)
    print(resolution)

    assert isinstance(resolution, str)
    assert len(resolution) > 0
