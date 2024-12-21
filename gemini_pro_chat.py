from typing import Optional, List
from dataclasses import dataclass
import requests
import json

class ResponseError(Exception):
    """Custom exception for handling API response errors."""
    def __init__(self, status_code: int, message: str):
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code
        self.message = message

@dataclass
class ChatMessage:
    """Represents a single message in the chat."""
    role: str
    content: str

class GeminiProChatModel:
    """Handles chat interactions with the Gemini Pro API."""
    def __init__(self):
        self.api_url = "https://nexra.aryahcr.cc/api/chat/complements"

    def send_request(self, messages: List[ChatMessage]) -> str:
        """
        Sends a request to the Gemini Pro API and retrieves the response.

        Args:
            messages (List[ChatMessage]): List of chat messages to send.

        Returns:
            str: The final response message.
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "messages": [message.__dict__ for message in messages],
            "markdown": False,
            "stream": True,
            "model": "gemini-pro",
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers, stream=True)
            if response.status_code != 200:
                raise ResponseError(response.status_code, response.text)

            # Process response stream
            for chunk in response.iter_lines(decode_unicode=True, chunk_size=1024):
                chunk_data = json.loads(chunk)
                if chunk_data.get('finish') in {True, "true"}:
                    return chunk_data.get('message', "")
            return "No complete message received."
        except requests.exceptions.RequestException as e:
            raise ResponseError(-1, str(e)) from e

    def get_response(self, query: str, system_prompt: Optional[str] = "You are a helpful assistant.") -> str:
        """
        Sends a query to the chat model and retrieves the response.

        Args:
            query (str): The user's query.
            system_prompt (Optional[str]): The system's initial prompt.

        Returns:
            str: The response from the chat model.
        """
        messages = [
            ChatMessage(role="system", content=system_prompt),
            ChatMessage(role="user", content=query),
        ]
        return self.send_request(messages)

# Example usage
if __name__ == "__main__":
    try:
        model = GeminiProChatModel()
        user_query = "What is your name?"
        response = model.get_response(query=user_query)
        print(response)
    except ResponseError as e:
        print(f"Error: {e}")
