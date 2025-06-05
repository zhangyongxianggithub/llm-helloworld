import whisper

from openai_base import client

model = whisper.load_model("base")


def transcribe(file):
    print(file)
    transcription = whisper.transcribe(model=model, audio=file)
    return transcription["text"]


def ask_chatgpt(messages):
    response = client.chat.completions.create(model="gpt-4", messages=messages)
    return response.choices[0].message.content


prompts = {
    "START": "Classify the intent of the next input. Is it: WRITE_EMAIL, QUESTION, OTHER? Only answer one word",
    "QUESTION": "If you can answer the question: ANSWER, if you need more information: MORE, if you cannot answer: OTHER. Only answer one word.",
    "ANSWER": "Now answer the question",
    "MORE": "Now ask for more information",
    "OTHER": "Now tell me you cannot answer the question or do the action",
    "WRITE_EMAIL": "If the subject or recipient or message is missing, answer 'MORE'. Else if you have all the information, answer 'ACTION_WRITE_EMAIL| subject:subject, recipient:recipient, message:message'.",
}

actions = {
    "ACTION_WRITE_EMAIL": "The mail has been sent. Now tell me the action is done in natural language.",
}


def do_action(action):
    print("Doing action:", action)
    return "I did the action " + action


def discussion(messages, last_step):
    # 调用OpenAI API获取下一个状态
    answer = ask_chatgpt(messages)
    print("Answer: ", answer, "last step: ", last_step)
    if answer in prompts.keys():
        messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": prompts[answer]})
        return discussion(messages, answer)
    elif answer in actions.keys():
        return do_action(answer)
    else:
        if last_step != "MORE":
            messages = []
        last_step = "END"
        return answer


def start(user_input):
    messages = [
        {
            "role": "user",
            "content": prompts["START"],
        },
        {"role": "user", "content": user_input},
    ]
    return discussion(messages, "START")


def start_chat(file):
    input = transcribe(file)
    print("audio text: " + input)
    return start(input)


if __name__ == "__main__":
    import gradio as gr

    gr.Interface(
        fn=start_chat,
        live=True,
        inputs=gr.Audio(sources=["microphone"], type="filepath"),
        outputs="text",
    ).launch()
