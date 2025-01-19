from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, SystemMessage
from emailcraft.ai_integration import AIModel
from typing_extensions import TypedDict


class EmailState(TypedDict):
    email_message: str
    tone_option: str
    summarize_option: bool


class EmailWorkflow:
    def __init__(self, model: AIModel):
        self.model = model
        self.workflow = StateGraph(EmailState)
        self._configure_workflow()

    def _configure_workflow(self):
        self.workflow.add_node("email_assistant", self.email_assistant)
        self.workflow.add_edge(START, "email_assistant")
        self.workflow.add_edge("email_assistant", END)

    def email_assistant(self, state: EmailState):
        sys_prompt = f"""You are an assistant that helps to create polished emails. 
        Here are the settings: email tone: {state['tone_option']} and summarize option: {state['summarize_option']}."""
        hum_prompt = f"Here is the email message: {state['email_message']}"

        messages = [
            SystemMessage(content=sys_prompt),
            HumanMessage(content=hum_prompt),
        ]
        response = self.model.invoke(messages)
        state["email_message"] = response.content
        return state

    def get_workflow(self):
        return self.workflow.compile()
