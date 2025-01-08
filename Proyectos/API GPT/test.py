from openai import OpenAI


client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
