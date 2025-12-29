# PedTriage

A minimal full-stack Django + Hotwire web app demonstrating a parent-facing symptom checker that uses an LLM to provide safe, guideline-informed triage recommendations for common pediatric issues.

## Project Overview

This is a demo project built to showcase full-stack skills for future job applications. It features user authentication, a multi-step symptom input form, LLM integration for triage suggestions, and dynamic UI updates. The app emphasizes pragmatic, safe healthcare tech without providing actual medical advice.

## Features

- **User Authentication**: Simple signup/login for parents, with optional child profiles.
- **Symptom Input**: Multi-step form for child age, primary complaints, and additional details.
- **LLM Triage**: Integrates an LLM via OpenRouter (using a free model, e.g., deepseek/deepseek-chat-v3-0324:free) to generate urgency levels and reasoning based on standard guidelines.
- **Results Display**: Dynamic output with urgency badges and disclaimers.
- **Admin Panel**: Manage symptom options via Django admin.

## Tech Stack

- Django (backend, auth, forms, views)
- Hotwire (Turbo + Stimulus) for dynamic UI
- SQLite (or PostgreSQL for production)
- LLM API: OpenRouter (configurable with free models)
- Deployment: Github Actions to VPS

## Setup and Installation

1. Clone the repo: `git clone https://github.com/theEricDevelops/PedTriage.git`
2. Create a virtual environment: `python -m venv venv` and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment variables (e.g., in `.env`):
   - `SECRET_KEY=your_django_secret`
   - `OPENROUTER_API_KEY=your_api_key_here` (Sign up for a free account at openrouter.ai to get an API key)
   - `LLM_MODEL=deepseek/deepseek-chat-v3-0324:free` (or another free model)
   - Use SQLite (default Django database)
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Start the server: `python manage.py runserver`

## Usage

- Register as a parent user.
- Fill out the symptom form for a child.
- Submit to get AI-generated triage suggestions.
- Always heed the disclaimer: This is a demo and not real medical advice.

## Development Notes

- Forms use Turbo Frames for real-time updates.
- LLM prompts are conservative and include guardrails.
- Uses OpenRouter for LLM access with free models to keep costs zero for portfolio/demo purposes.
- Keep scope small; no production features like history tracking.

## Why This Project?

Built to align with pediatric telehealth roles (e.g., Blueberry Pediatrics), demonstrating AI integration, risk flagging, and a clean Django/Hotwire stack.

## License

MIT License. Feel free to use and modify for personal/demo purposes.