from collections import defaultdict
from typing import Dict
from app.config import settings


class ConversationMemory:
    """
    Stores conversation history and session metadata.
    """

    def __init__(self):

        self.sessions: Dict[str, dict] = defaultdict(
            lambda: {
                "messages": [],
                "response_count": 0,
                "lead_popup_shown": False,
            }
        )

    def add_user_message(self, session_id: str, message: str) -> None:
        """
        Add a user message to the conversation history.
        """

        self.sessions[session_id]["messages"].append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_ai_message(self, session_id: str, message: str) -> None:
        """
        Add an AI response to the conversation history.
        """

        self.sessions[session_id]["messages"].append(
            {
                "role": "assistant",
                "content": message,
            }
        )

        # Count every bot response
        self.sessions[session_id]["response_count"] += 1

    def get_history(self, session_id: str):
        """
        Return only the conversation history.
        """

        return self.sessions[session_id]["messages"]

    def get_response_count(self, session_id: str) -> int:
        """
        Return how many responses the chatbot has given.
        """

        return self.sessions[session_id]["response_count"]

    def should_show_lead_popup(self, session_id: str) -> bool:
        """
        Show the lead popup only once after 5 chatbot responses.
        """

        session = self.sessions[session_id]

        if (
            session["response_count"] >= settings.LEAD_POPUP_AFTER
            and not session["lead_popup_shown"]
        ):

            session["lead_popup_shown"] = True
            return True

        return False

    def reset_lead_popup(self, session_id: str) -> None:
        """
        Optional: Reset the popup flag for testing.
        """

        if session_id in self.sessions:
            self.sessions[session_id]["lead_popup_shown"] = False

    def clear_history(self, session_id: str) -> None:
        """
        Delete the entire session.
        """

        if session_id in self.sessions:
            del self.sessions[session_id]

    def get_all_sessions(self):
        """
        Return all active sessions.
        """

        return self.sessions