from api import get_completion
from prompt_generator import PromptGenerator


class WritingAgent:
    def __init__(
        self,
        api_key,
        n_initial_drafts=3,
        n_dialogue_turns=3,
        model="gpt-3.5-turbo",
        language="de",
    ):
        self.api_key = api_key
        self.n_initial_drafts = n_initial_drafts
        self.n_dialogue_turns = n_dialogue_turns
        self.model = model
        self.language = language
        self.PromptGenerator = None

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
            text_goals (List[str], optional): The goals of the text. Defaults to None.
            text_criteria (List[str], optional): The criteria of the text. Defaults to None.

        Returns:
            str: The generated text.
        """
        self.PromptGenerator = PromptGenerator(
            self.language, text_type, text_length, factual_content
        )

        initial_drafts = self._generate_initial_drafts(self.n_initial_drafts)

        revised_draft = self._discuss(initial_drafts)

        return True

    def _generate_initial_drafts(self, n):
        """
        Generate initial drafts for the text.

        Args:
            n_initial_drafts (int): The number of initial drafts to generate.

        Returns:
            List[str]: A list of n initial drafts.
        """
        prompt, system_message = self.PromptGenerator.initial_prompt()

        return get_completion(
            prompt, system_message, self.api_key, n=n, model=self.model
        )

    def _discuss(self, initial_drafts):
        """ """
