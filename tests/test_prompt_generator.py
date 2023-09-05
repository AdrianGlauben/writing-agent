from prompt_generator import PromptGenerator

prompt_generator = PromptGenerator(
    "de",
    "Missionstatement",
    "100",
    "Unternehmensname: Deutsche Bank Research Unternehmenstätigkeit Erstellung Unabhängiger volkswirtschaftliche Analysen Verfolgung der relevanten Entwicklungen auf den Finanzmärkten Unternehmenswerte: Qualitativ hochwertig Innovativ Unabhängig Unternehmensziel: Bereichern der offentlichen diskussion in ökonomischen, finanzpolitischen, arbeitsmarkt und sozialpolitischen themen Analysen sollen Investoren bei Anlegeentscheidungen unterstützen",
)


def test_initial_prompt():
    prompt, system_message = prompt_generator.initial_prompt()
    print(prompt)
    assert isinstance(prompt, str)
    assert isinstance(system_message, str)
    assert len(prompt) > 0
    assert len(system_message) > 0


def test_reflector_prompt():
    drafts = ["Entwurf 1", "Entwurf 2", "Entwurf 3"]
    prompt, system_message = prompt_generator.reflector_prompt(drafts)
    print(prompt)
    assert isinstance(prompt, str)
    assert isinstance(system_message, str)
    assert len(prompt) > 0
    assert len(system_message) > 0


def test_resolver_prompt():
    reflection = "Reflektion"
    drafts = ["Entwurf 1", "Entwurf 2", "Entwurf 3"]
    prompt, system_message = prompt_generator.resolver_prompt(reflection, drafts)
    print(prompt)
    assert isinstance(prompt, str)
    assert isinstance(system_message, str)
    assert len(prompt) > 0
    assert len(system_message) > 0
