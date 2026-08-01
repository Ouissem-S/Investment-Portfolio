# Investment Portfolio API

A REST API for tracking investment holdings (stocks, ETFs, crypto), built with FastAPI. Users can add holdings and view their portfolio. Built with a clean, layered architecture where each part of the code has a single responsibility.

## Architecture

The project is organised into layers, each with one job. A request flows downward through them:

**request → routes → services → data**

| Folder / File | Responsibility                                                                       |
| ------------- | ------------------------------------------------------------------------------------ |
| `routes/`     | The web layer — defines API endpoints and handles HTTP requests                      |
| `services/`   | The business logic — performs operations like generating an id and storing a holding |
| `schemas/`    | The data models — defines what a holding looks like and validates input              |
| `data/`       | The storage layer — an in-memory list for now (to be replaced with a database)       |
| `main.py`     | The entry point — creates the app and connects the route files                       |

Each layer only depends on the layers below it, so storage can later be swapped for a real database without changing the rest of the code.

## Tech Stack

- **Python**
- **FastAPI** — web framework
- **Pydantic** — data validation
- **Uvicorn** — server

## Getting Started

Run the development server from the project root:

```bash
uvicorn main:app --reload
```

Then open the interactive API docs in your browser:
http://127.0.0.1:8000/docs

## Endpoints

| Method | Path        | Description         |
| ------ | ----------- | ------------------- |
| `GET`  | `/holdings` | Return all holdings |
| `POST` | `/holdings` | Add a new holding   |

## Roadmap

- [ ] Update and delete holdings (full CRUD)
- [ ] Add a transactions feature
- [ ] Replace in-memory storage with a database
- [ ] Add authentication and user accounts
