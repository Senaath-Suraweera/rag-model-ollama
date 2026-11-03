
import requests as rq
import re
import numpy as np
from pathlib import Path

# --------------------------------------------------
# Configuration
# --------------------------------------------------

OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen3:4b-instruct"


def embed(texts: list[str]) -> np.ndarray:

    r = rq.post(
        f"{OLLAMA_URL}/api/embed",
        json={
            "model": EMBED_MODEL,
            "input": texts
        },
        timeout=120
    )

    r.raise_for_status()

    return np.array(r.json()["embeddings"], dtype=np.float32)


def ask_llm(prompt: str) -> str:

    r = rq.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": CHAT_MODEL,
            "stream": False,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        timeout=120
    )

    r.raise_for_status()

    return r.json()["message"]["content"]



chunks = []

docs_path = Path("docs")

for file in docs_path.glob("*.md"):

    text = file.read_text(encoding="utf-8")

    text = re.sub(
        r"\A---\s*\n.*?\n---\s*\n",
        "",
        text,
        flags=re.DOTALL
    )

    title_match = re.search(r"^# (.+)", text, re.M)

    title = title_match.group(1) if title_match else file.stem

    if title_match:
        text = text[:title_match.start()] + text[title_match.end():]

    sections = re.split(r"\n(?=## )", text)

    for section in sections:

        section = section.strip()

        if section:
            chunks.append(f"{title} > {section}")


if not chunks:
    raise ValueError("No Markdown document sections found in the docs folder.")


chunk_vectors = embed(chunks)

print(
    f"Embedded {len(chunks)} chunks into "
    f"{chunk_vectors.shape[1]}-dimensional vectors."
)


def retrieve(question: str, k: int = 3):

    q = embed([question])[0]

    chunk_norms = np.linalg.norm(chunk_vectors, axis=1)
    q_norm = np.linalg.norm(q)

    if q_norm == 0:
        raise ValueError("Query embedding has zero magnitude.")

    scores = (
        chunk_vectors @ q
        / (chunk_norms * q_norm + 1e-10)
    )

    top_indices = np.argsort(scores)[::-1][:k]

    return [chunks[i] for i in top_indices]

while True:

    question = input("\nAsk (type 'exit' to quit): ").strip()

    if question.lower() in ["exit", "quit"]:
        break

    if not question:
        continue

    try:

        # Retrieve relevant context
        context = "\n\n".join(retrieve(question))

        # Construct prompt
        prompt = f"""
Answer the question based only on the provided context.

If the answer is not contained within the context,
respond with "I don't know".

Context:
{context}

Question:
{question}
"""

        # Generate response
        response = ask_llm(prompt)

        print("\nAnswer:")
        print(response)

    except rq.exceptions.RequestException as e:
        print(f"\nOllama API error: {e}")

    except Exception as e:
        print(f"\nError: {e}")
