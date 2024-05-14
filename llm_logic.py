from secret_key import secret_key_1
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
import regex as re


os.environ['OPENAI_API_KEY'] = secret_key_1
llm = OpenAI(temperature=0.6)

memory = ConversationBufferWindowMemory(k=3)

convo = ConversationChain(
    llm = llm,
    memory = memory
    )


def generate_quiz(category, team):
    

    que_prompt = PromptTemplate(
        input_variables = ['category_input', 'team_input'],
        template = "Generate a quiz for category: {category_input} and team: {team_input}. Do not add any other thing, it should simply be just a question"
    )
    # que_chain = LLMChain(llm=llm, prompt=que_prompt, output_key='question')

    que_prompt.format(category_input=category,team_input=team)

    theme = """
    I want you to help me making a quiz game. following in this conversation, I will provide you a category and a team,
    I want you to generate a quiz for that category and team of Indian Premier League. Here, for the first response,
    I only want you to give question or quiz, not any option or hint untill asked for. And for quiz, I want you to be unique,
    quizes should not repeat itself. 

    Then in the next prompt, I will ask for 4 options for the same. Here I only want you to return
    options in following manner:
    A)
    B)
    C)
    D)

    And for the last prompt I will try to answer the quiz then you can verify it.

"""
    convo.run(theme)

    quiz = convo.run(que_prompt.format(category_input=category,team_input=team))

    pattern = r':(.*?\?)'
    matches = re.findall(pattern, quiz, re.DOTALL)
    if matches:
        for match in matches:
            quiz = match.strip()


    return {
        "quiz": quiz
    }

def generate_options():
    options = convo.run('Provide option for the above questions.')
    return {
        'options' : options
    }
    
def check_ans(answer):
    resoponse = convo.run(f"answer is {answer}")
    return {
        'response': resoponse
    }



