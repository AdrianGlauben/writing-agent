from api import get_completion
from prompt_generator import PromptGenerator
from internal_agents import Reflector, Resolver


class WritingAgent:
    def __init__(
        self,
        api_key,
        n_initial_drafts=1,
        model="gpt-3.5-turbo",
        language="de",
    ):
        self.api_key = api_key
        self.n_initial_drafts = n_initial_drafts
        self.model = model
        self.language = language
        self.prompt_generator = None
        self.initial_drafts = None
        self.reflection = None
        self.resolution = None

    def write_text(
        self,
        text_type,
        text_length,
        factual_content,
    ):
        """
        Write a text of a given type.

        Args:
            text_type (str): The type of text to write.
            factual_content (str): The factual content of the text.
            text_length (int): The length of the text in words.

        Returns:
            str: The generated text.
        """
        self.prompt_generator = PromptGenerator(
            self.language, text_type, text_length, factual_content
        )
        reflector = Reflector(self.api_key, self.model, self.prompt_generator)
        resolver = Resolver(self.api_key, self.model, self.prompt_generator)

        self.initial_drafts = self._generate_initial_drafts(self.n_initial_drafts)
        self.reflection = reflector.reflect(self.initial_drafts)
        self.resolution = resolver.resolve(self.reflection, self.initial_drafts)

        return self.resolution[0]

    def _generate_initial_drafts(self, n):
        """
        Generate initial drafts for the text.

        Args:
            n_initial_drafts (int): The number of initial drafts to generate.

        Returns:
            List[str]: A list of n initial drafts.
        """
        prompt, system_message = self.prompt_generator.initial_prompt()

        return get_completion(
            prompt, system_message, self.api_key, n=n, model=self.model
        )
