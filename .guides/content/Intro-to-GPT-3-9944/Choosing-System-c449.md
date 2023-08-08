Lets try creating a system message that sets the context of the AI as a collaborative programming assistant with expertise in Python. The user messages represent two team members, Alice and Bob, with distinct questions related to Python decorators.

First step in our code we are going to get our libraries and API keys.

```Python
import os
import openai
import secret
openai.api_key=secret.api_key
```
{try it!}(python3 temp.py)

To make visualizing easier, we are going to create a variable named `message` that will store our prompt. 
```python
message=[{"role": "system", "content": "You are a collaborative programming assistant with expertise in Python."},
        {"role": "user", "content": "Alice: I'm having trouble understanding how to use Python decorators. Can you explain them to me?"},
        {"role": "user", "content": "Bob: I think I understand decorators, but I could use some help with a specific example. Can you provide one?"}
    ]
```
{try it!}(python3 temp.py 2)




After we are going to make our API call and set it equal to `response`. We will use slicing with our print statement in order to better see the information that the response generates.
``` python
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages= message
)
print(response['choices'][0]['message']['content'].strip())
```
{try it!}(python3 temp.py 3)

 {Check It!|assessment}(multiple-choice-4166878991)

 