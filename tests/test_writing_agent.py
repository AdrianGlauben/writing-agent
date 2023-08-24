from writing_agent import WritingAgent
from prompt_generator import PromptGenerator
import os


def test_generate_initial_drafts():
    api_key = os.environ.get("OPENAI_API_KEY")
    n_initial_drafts = 1
    n_dialogue_turns = 3
    model = "gpt-3.5-turbo"
    language = "de"
    writing_agent = WritingAgent(
        api_key, n_initial_drafts, n_dialogue_turns, model, language
    )

    text_type = "Missionstatement"
    text_length = "100"
    factual_content = "Unternehmensname: Deutsche Bank Research Unternehmenstätigkeit Erstellung Unabhängiger volkswirtschaftliche Analysen Verfolgung der relevanten Entwicklungen auf den Finanzmärkten Unternehmenswerte: Qualitativ hochwertig Innovativ Unabhängig Unternehmensziel: Bereichern der offentlichen diskussion in ökonomischen, finanzpolitischen, arbeitsmarkt und sozialpolitischen themen Analysen sollen Investoren bei Anlegeentscheidungen unterstützen"

    writing_agent.PromptGenerator = PromptGenerator(
        language, text_type, text_length, factual_content
    )
    initial_drafts = writing_agent._generate_initial_drafts(n_initial_drafts)

    assert isinstance(initial_drafts, list)
    assert len(initial_drafts) == n_initial_drafts
    assert isinstance(initial_drafts[0], str)
