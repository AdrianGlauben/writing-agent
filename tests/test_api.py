import api
import os


def test_get_completion():
    prompt = "Test"
    system_message = "Test"
    api_key = os.environ.get("OPENAI_API_KEY")
    n = 2
    model = "gpt-3.5-turbo"

    completion = api.get_completion(
        prompt, system_message, api_key, n, model, max_tokens=2
    )
    print(completion)

    assert isinstance(completion, list)
    assert len(completion) == n
    assert isinstance(completion[0], str)
