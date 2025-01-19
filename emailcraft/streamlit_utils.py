
class StreamlitInterface:
    def __init__(self, workflow):
        self.workflow = workflow

    def stream_response(self, user_input, tone_option, summarize_option, placeholder):
        full_response = ''
        for chunk, _ in self.workflow.stream(
            {"email_message": user_input, "tone_option": tone_option, "summarize_option": summarize_option},
            {"configurable": {"thread_id": "abc789"}},
            stream_mode="messages",
        ):
            full_response += chunk.content
            placeholder.markdown(full_response.strip())
