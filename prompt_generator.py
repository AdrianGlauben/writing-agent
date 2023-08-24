class PromptGenerator:
    def __init__(self, language, text_type, text_length, factual_content):
        self.language = language
        self.text_type = text_type
        self.text_length = text_length
        self.factual_content = factual_content

    def initial_prompt(self):
        if self.language == "de":
            system_message = (
                "Versetze dich in die Lage eines Beratungsteams, "
                + "das dafür zuständig ist, qualitativ hochwertige und professionelle "
                + "Texte für große und erfolgreiche Unternehmen zu schreiben."
            )
            prompt = (
                f"Du wurdest vom Unternehmen gebeten, ein {self.text_type} zu schreiben. "
                + f"Der Text soll ca. {self.text_length} Wörter umfassen. "
                + f"Das Unternehmen hat dir folgende faktische Informationen zur Verfügung gestellt:\n "
                + f"{self.factual_content}. "
                + "Reflektiere zunächst die Aufgabenstellung und erarbeite einen Plan zur Lösung der Aufgabe. "
                + f"Reflektiere dabei insbesondere die Anforderungen an ein herausragendes {self.text_type}. "
                + "Führe danach den Plan aus und schreibe den Text Schritt für Schritt."
            )
        return prompt, system_message
