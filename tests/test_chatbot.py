import unittest
from unittest.mock import MagicMock
from basic_chatbot.chatbot import get_response

class TestChatbot(unittest.TestCase):

    def test_get_response(self):
        # Mock the OpenAI client
        mock_openai_client = MagicMock()
        mock_openai_client.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="Test response"))]
        )
        
        response = get_response(mock_openai_client, "Hello")
        self.assertEqual(response, "Test response")

if __name__ == '__main__':
    unittest.main()
