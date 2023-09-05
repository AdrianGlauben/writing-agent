class PromptGenerator:
    def __init__(self, language, text_type, text_length, factual_content):
        self.language = language
        self.text_type = text_type
        self.text_length = text_length
        self.factual_content = factual_content

    def initial_prompt(self):
        if self.language == "de":
            system_message = (
                "Du bist ein professioneller Texter, "
                + "der dafür zuständig ist, qualitativ hochwertige und professionelle "
                + "Texte für große und erfolgreiche Unternehmen zu schreiben."
            )
            prompt = (
                f"Du wurdest vom Unternehmen gebeten, ein {self.text_type} zu schreiben. "
                + f"Der Text soll ca. {self.text_length} Wörter umfassen. "
                + f"Das Unternehmen hat dir folgende faktische Informationen zur Verfügung gestellt:\n "
                + f"{self.factual_content}. \n\n"
                + "Erarbeite einen Plan zur Lösung der Aufgabe. "
                + f"Reflektiere dabei insbesondere die Anforderungen an ein herausragendes {self.text_type}. "
                + "Schreibe anschließend einen ersten Entwurf."
            )
        return prompt, system_message

    def reflector_prompt(self, drafts):
        if self.language == "de":
            system_message = (
                "Du bist ein professioneller Reflektierer, der dafür zuständig ist, "
                + "Entwürfe für Unternehmenstexte korrekturzulesen und Verbesserungsvorschläge zu formulieren. "
                + "Mache lediglich listenartige Vorschläge, aber schreibe keine eigenen Texte."
            )
            prompt = (
                "Du wurdest vom Unternehmen gebeten, mehrere Texte zu reflektieren. "
                + "Die Entwürfe wurden von einem professionellen Texter geschrieben. "
                + "Das Unternehmen erwartet, dass die Entwürfe folgende faktischen Informationen enthalten:\n "
                + f"{self.factual_content}.\n\n"
                + "Entwürfe:\n"
                + "".join(
                    f"Entwurf {index}: \n {item}\n\n"
                    for index, item in enumerate(drafts)
                )
                + "Deine Aufgabe ist es, jeden Entwurf zu bewerten, zu reflektieren und Verbesserungsvorschläge abzugeben. "
                + f"Gehe dabei Schritt für Schritt vor und beachte die speziellen Anforderungen an die Textart ({self.text_type}) und den faktischen Inhalt.\n\n"
            )
        return prompt, system_message

    def resolver_prompt(self, reflection, drafts):
        if self.language == "de":
            system_message = (
                "Du bist ein professioneller Texter, "
                + "der dafür zuständig ist, qualitativ hochwertige und professionelle "
                + "Texte für große und erfolgreiche Unternehmen zu schreiben."
            )
            prompt = (
                f"Du wurdest vom Unternehmen gebeten, den finalen Text ({self.text_type}) zu schreiben. "
                + "Dazu werden dir initiale Entwürfe und Verbesserungsvorschläge zur Verfügung gestellt. "
                + "Das Unternehmen erwartet, dass der finale Text folgende faktischen Informationen enthält:\n "
                + f"{self.factual_content}. \n\n"
                + "Entwürfe:\n"
                + "".join(
                    f"Entwurf {index}: \n {item}\n\n"
                    for index, item in enumerate(drafts)
                )
                + "Verbesserungsvorschläge:\n"
                + f"{reflection}\n\n"
                + "Deine Aufgabe ist es anhand der gegebenen Entwürfe und Verbesserungsvorschläge einen finalen Text zu formulieren. "
                + f"Gehe dabei Schritt für Schritt vor und beachte die speziellen Anforderungen an die Textart ({self.text_type}) und den faktischen Inhalt. "
                + f"Der finale Text soll ca. {self.text_length} Wörter umfassen."
            )

        return prompt, system_message
