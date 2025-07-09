from openai import OpenAI
from rag import get_results
client = OpenAI()

query = input(">>")
context = get_results(query)
query_with_context = f"Answer the following question: {query}\n\nContext: {context}"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that provides short answers (1-2 sentences) based strictly on the given context. Do not make up information or use external knowledge."
        },
        {
            "role": "user", 
            "content": query_with_context
        }
    ],
)

print(response.choices[0].message.content)