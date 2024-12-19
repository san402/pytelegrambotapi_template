# Telegram Bot Template using PyTelegramBotAPI (TeleBot)

This repository provides a starting point for building Telegram bots with [PyTelegramBotAPI (TeleBot)](https://github.com/eternnoir/pyTelegramBotAPI). It includes a basic project structure, Docker configuration, and MongoDB integration for user data persistence.

## Features

- **Clean Project Structure:**  
  Organized codebase to streamline development:
  - `app.py`: Main bot logic and handlers.
  - `models.py`: Data models (Pydantic-based) and user management logic.
  - `Dockerfile` & `docker-compose.yml`: Containerization setup and environment configuration.

- **MongoDB Integration:**  
  Easily store and retrieve user information using MongoDB. The `User` class in `models.py` manages database interactions for easy user state persistence.

- **User Data Sanitization:**  
  Inputs from Telegram users are sanitized to ensure data integrity and security.

- **Inline & Reply Keyboards:**  
  Helper functions `gen_inline_markup` and `gen_reply_markup` are provided to quickly create user-friendly navigation within the chat interface.

## Prerequisites

- **Docker & Docker Compose:**  
  Make sure you have Docker and Docker Compose installed.  
  [Install Docker](https://docs.docker.com/get-docker/)  
  [Install Docker Compose](https://docs.docker.com/compose/install/)

- **Telegram Bot Token:**  
  Create a bot via [BotFather](https://core.telegram.org/bots#6-botfather) and obtain your bot token.

- **MongoDB Connection Details:**  
  By default, `docker-compose.yml` sets up a MongoDB service. Environment variables in `.env` can be adjusted for your database configurations.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/san402/pytelegrambotapi_template
   cd pytelegrambotapi_template
