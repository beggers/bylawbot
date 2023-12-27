# TODO use Chroma for faster RAG.
# import chromadb
from openai import OpenAI

import os

# Squelch warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"

APIKEY = open(".apikey").read().strip()
print("APIKEY:", APIKEY)
COLLECTION_NAME = "bylaws"
DIVIDER = "============================================================================"
FULL_BYLAWS = open("bylaws.txt").read().split("\n")
INTRODUCTION = """Hello, I am the bylaw bot. I am an artificial intelligence \
whose purpose is to \
help humans understand the bylaws of their apartment buildings. I can answer \
questions about the bylaws, or I can help you find the bylaw you are looking \
for."""
OPENAI_CLIENT = OpenAI(api_key=APIKEY)
SYSTEM_PROMPT = """
You are an artificial intelligence whose purpose is to help humans understand \
the bylaws of their apartment buildings. Please use the following context to \
aid you in generating your response. Wherever possible, cite the specific \
bylaw that you are referencing.

Context:
{context}

Prompt:
{prompt}
"""


def main():
    print_with_dividers(INTRODUCTION)

    # client = chromadb.PersistentClient()
    # collection_names = [c.name for c in client.list_collections()]
    # if COLLECTION_NAME not in collection_names:
    #     create_and_populate_collection(client)

    # collection = client.get_collection(COLLECTION_NAME)

    semantic_search_mode = True
    while True:
        prompt = input('Enter a question or set mode ("f" or "s"): ')
        if prompt == "f":
            print("======== Switching to full bylaw document search mode")
            semantic_search_mode = True
            continue
        elif prompt == "r":
            print("======== Switching to semantic search mode")
            semantic_search_mode = True
            continue

        context = get_context(prompt, semantic_search_mode)
        prompt = SYSTEM_PROMPT.format(context=context, prompt=prompt)
        response = generate_response(prompt)
        print_with_dividers(response)


def print_with_dividers(text):
    print("\n" + DIVIDER)
    print(text)
    print(DIVIDER + "\n")


# def create_and_populate_collection(client):
#     print("======== Embeddings collection not found. Creating collection...")
#     collection = client.create_collection(COLLECTION_NAME)
#     embed_bylaws(collection)


# def embed_bylaws(collection):
#     pass


def get_context(prompt, semantic_search_mode):
    return FULL_BYLAWS


def generate_response(prompt):
    choices = OPENAI_CLIENT.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4-1106-preview",
    )
    return choices.choices[0].message.content


if __name__ == "__main__":
    main()
