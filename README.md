# RAG Ollama

A minimal, fully local **Retrieval-Augmented Generation (RAG)** chatbot built with Python, NumPy and [Ollama](https://ollama.com). It answers questions about **RideMachan** (a sample Sri Lankan vehicle rental marketplace) using a Markdown knowledge base in `docs/`.

No vector database or LLM framework is used: embeddings are kept in memory as a NumPy array and retrieval is plain cosine similarity, so the whole pipeline is easy to read in a single file.

## How it works

1. **Load:** reads every `docs/*.md` file.
2. **Chunk:** strips the YAML front matter and splits each file on `##` headings. The page's `#` title is prepended to every chunk (e.g. `About RideMachan > ## What is RideMachan?`) so each chunk keeps its context.
3. **Embed:** sends all chunks to Ollama's `/api/embed` endpoint using `nomic-embed-text`.
4. **Retrieve:** embeds your question and picks the top 3 chunks by cosine similarity.
5. **Generate:** sends those chunks plus your question to `qwen3:4b-instruct` via `/api/chat`, with instructions to answer only from the context (or reply "I don't know").

## Project structure

```
.
├── docs/                        # Knowledge base (RAG source)
│   ├── 01-about-ridemachan.md
│   ├── ...
│   ├── 10-admin-operations.md
│   └── ridemachan-kb/README.md  # Describes the knowledge base files
├── src/rag_ollama/
│   ├── __init__.py
│   └── rag.py                   # The RAG pipeline and interactive chat loop
├── pyproject.toml
└── uv.lock
```

## Prerequisites

- **[uv](https://docs.astral.sh/uv/)** for Python and dependency management
- **[Ollama](https://ollama.com/download)** installed and running locally
- Roughly 3–4 GB of free disk space for the two models

You don't need to install Python yourself: the project requires Python 3.14, and uv downloads it automatically if it's missing.

## Setup

### 1. Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# or with Homebrew
brew install uv
```

### 2. Install and start Ollama

Download Ollama from [ollama.com/download](https://ollama.com/download) (or `brew install ollama`), then make sure the server is running:

```bash
ollama serve
```

The desktop app starts the server automatically. Either way, it listens on `http://localhost:11434`.

### 3. Pull the models

```bash
ollama pull nomic-embed-text
ollama pull qwen3:4b-instruct
```

### 4. Clone the repo and install dependencies

```bash
git clone <your-repo-url> rag-ollama
cd rag-ollama
uv sync
```

`uv sync` creates a `.venv/` folder, installs the pinned Python version if needed, and installs everything listed in `uv.lock`.

## Running

Run the script **from the project root** (it reads `docs/` using a relative path):

```bash
uv run python src/rag_ollama/rag.py
```

Example session:

```
Embedded <N> chunks into 768-dimensional vectors.

Ask (type 'exit' to quit): What happens if I cancel a booking 24 hours before pick-up?

Answer:
...

Ask (type 'exit' to quit): exit
```

Type `exit` or `quit` to stop.

> **Note:** the `rag-ollama` console script in `pyproject.toml` currently points to the placeholder `main()` in `__init__.py`, which only prints a greeting. Use the command above to start the chatbot.

## Configuration

These settings are at the top of `src/rag_ollama/rag.py`:

| Variable      | Default                  | Purpose                              |
|---------------|--------------------------|--------------------------------------|
| `OLLAMA_URL`  | `http://localhost:11434` | Where the Ollama server is running   |
| `EMBED_MODEL` | `nomic-embed-text`       | Model used to embed chunks and questions |
| `CHAT_MODEL`  | `qwen3:4b-instruct`      | Model used to generate answers       |

To retrieve more or fewer chunks per question, change `k` in `retrieve(question, k=3)`.

If you switch to a different model, pull it with `ollama pull <model>` first.

## Using your own documents

Replace or add Markdown files in `docs/` (only top-level `*.md` files are loaded). For the best results:

- Start each file with a `# Title`.
- Break content into `##` sections that each make sense on their own.
- Optional YAML front matter (`--- ... ---`) at the top is stripped automatically.

Chunks are re-embedded every time the script starts, so changes are picked up on the next run.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `Ollama API error: ... Connection refused` | Ollama isn't running. Start it with `ollama serve` or open the Ollama app. |
| `Ollama API error: 404 ...` / `model not found` | The model isn't pulled. Run the `ollama pull` commands above. |
| `No Markdown document sections found in the docs folder.` | You're not running from the project root, or `docs/` is empty. `cd` to the repo root and try again. |
| Requests time out | The first call loads the model into memory and can be slow on low-RAM machines. Try again, or switch to a smaller chat model. |

## About the sample data

The RideMachan prices, fees, policies and time limits in `docs/` are **sample content** for development and testing. See `docs/ridemachan-kb/README.md` for details on each file.
