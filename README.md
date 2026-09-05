# Holosen Chatbot

An asynchronous AI-powered Telegram chatbot built with Python and [aiogram](https://aiogram.dev/). The bot uses OpenAI to generate conversational responses and keeps a short, in-memory conversation history for each user.

## Features

- Asynchronous Telegram message handling
- AI-generated responses powered by OpenAI
- Separate short-term conversation history for each Telegram user
- Persian welcome message for the `/start` command
- Optional DeepSeek integration through the Hugging Face inference router
- Simple, modular structure for handlers and AI services

## Project Structure

```text
holosen_chatbot/
├── bot.py                 # Application entry point
├── config.py              # Bot and API configuration
├── handler/
│   ├── command.py         # /start command handler
│   ├── chat.py            # Text message handler
│   └── router.py          # Handler registration
└── service/
    ├── openai.py          # OpenAI integration and conversation history
    └── deepseek.py        # Optional DeepSeek integration via Hugging Face
```

## Requirements

- Python 3.11 or newer
- A Telegram bot token from [BotFather](https://t.me/BotFather)
- An [OpenAI API key](https://platform.openai.com/api-keys)
- A [Hugging Face access token](https://huggingface.co/settings/tokens) if you want to use the optional DeepSeek service

The project is currently tested with:

- Python 3.14
- aiogram 3.30
- openai 3.3

## Installation

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/badrnezhad/Telegram-ChatBot.git
   cd holosen-chatbot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows:

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Open `config.py` and replace the placeholder values with your credentials:

```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
HF_TOKEN = "YOUR_HUGGING_FACE_TOKEN"
```

> **Security warning:** Never commit real bot tokens or API keys to GitHub. For production use, load secrets from environment variables or a local `.env` file excluded by `.gitignore`. If a real key has already been committed or shared, revoke it and create a new one immediately.

## Usage

Start the bot with:

```bash
python bot.py
```

Then open your bot in Telegram:

1. Send `/start` to receive the welcome message.
2. Send any text message.
3. The bot forwards the conversation context to OpenAI and replies with the generated answer.

Stop the bot by pressing `Ctrl+C` in the terminal.

## How It Works

The application starts an aiogram dispatcher using long polling. Command handlers process Telegram commands, while the chat handler forwards text messages to the OpenAI service. Recent messages are stored in memory by Telegram user ID and included in later requests to preserve short-term context.

The in-memory history is cleared whenever the application restarts. A database or cache such as Redis can be added if persistent conversation history is required.

The DeepSeek service is included as an alternative integration, but the current chat handler uses OpenAI by default. To switch providers, update the function called in `handler/chat.py`.

## Notes for Production

- Move all credentials to environment variables.
- Add error handling for Telegram and AI API failures.
- Use persistent storage if conversation history must survive restarts.
- Add logging, rate limiting, and user access controls as needed.
- Run the bot with a process manager or container for automatic restarts.

## License

No license has been added yet. Add a `LICENSE` file before distributing or accepting contributions to the project.
