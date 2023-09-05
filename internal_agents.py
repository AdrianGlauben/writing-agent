from api import get_completion


class Reflector:
    def __init__(self, api_key, model, prompt_generator):
        self.api_key = api_key
        self.model = model
        self.prompt_generator = prompt_generator

    def reflect(self, drafts):
        prompt, system_message = self.prompt_generator.reflector_prompt(drafts)

        return get_completion(prompt, system_message, self.api_key, model=self.model)


class Resolver:
    def __init__(self, api_key, model, prompt_generator):
        self.api_key = api_key
        self.model = model
        self.prompt_generator = prompt_generator

    def resolve(self, reflection, drafts):
        prompt, system_message = self.prompt_generator.resolver_prompt(
            reflection, drafts
        )

        return get_completion(prompt, system_message, self.api_key, model=self.model)
