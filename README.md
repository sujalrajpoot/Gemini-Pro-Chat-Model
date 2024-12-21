# Gemini Pro Chat Model 🤖✨

Welcome to the **Gemini Pro Chat Model** project! This Python-based library allows you to interact with the **Gemini Pro** API for chat-based queries. Whether you're looking to create a chatbot or integrate AI-powered conversations into your project, this is your go-to solution. 🚀

### Key Features:
- 💬 Seamlessly interact with the Gemini Pro API.
- 📈 Stream real-time responses.
- ✨ Supports Markdown formatting for rich content.
- 🛠️ Easily configurable for different models and system prompts.

## ⚙️ How It Works

1. **Initialization**:
   The `GeminiProChatModel` class is initialized with the API URL, and by default, it is configured to interact with the Gemini Pro API.

2. **Sending Messages**:
   The `send_request` method is used to send a list of `ChatMessage` objects, each containing a `role` and `content`. You can specify whether the response should be in Markdown format and if you want to stream the response.

3. **Receiving Responses**:
   The model listens for responses from the API. If streaming is enabled, it will fetch the message chunk-by-chunk and return when the response is complete.

4. **Error Handling**:
   The custom `ResponseError` exception is raised in case of any API response issues, ensuring better error management.

## 🔧 How to Use

### Requirements

- Python 3.x
- `requests` library: You can install it using `pip install requests`.

### Example Usage

```python
from gemini_pro_chat import GeminiProChatModel, ChatMessage

# Initialize the model
model = GeminiProChatModel()

# Define your user query
user_query = "What is your name?"

# Get the response from the model
response = model.get_response(query=user_query)

# Print the response
print(response)
```

## Parameters:
- messages: A list of ChatMessage objects.

## API Response Codes

| **Code** | **Error**                 | **Description**                                             |
|----------|---------------------------|-------------------------------------------------------------|
| 400      | BAD_REQUEST               | Not all parameters have been entered correctly             |
| 500      | INTERNAL_SERVER_ERROR     | The server has experienced failures                        |
| 200      | Success                   | The API worked without issues                              |

## 💡 How It Can Help Users
This project is perfect for developers looking to:

- Build conversational agents or chatbots with advanced AI.
- Integrate real-time responses into applications.
- Experiment with AI models using an easy-to-use API interface.
---

## ⚖️ Disclaimer
**Remember**: This code is for educational purposes only. Use responsibly and ethically. Use responsibly and respect API limitations! 🚀

---

Created with ❤️ by **Sujal Rajpoot**

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact
For questions or support, please open an issue or reach out to the maintainer.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
