from langchain_openai import ChatOpenAI


class AIModel:
    def __init__(self, api_key: str, model_name: str = "gpt-4o-mini", temperature: float = 0):
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature
        self.model = ChatOpenAI(openai_api_key=api_key, model=model_name, temperature=temperature)

    def invoke(self, messages):
        return self.model.invoke(messages)
