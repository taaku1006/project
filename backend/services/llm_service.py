from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class LLMChatService:
    def __init__(self, model_name="llama3"):
        # Docker Composeのサービス名 'ollama' で接続
        self.llm = OllamaLLM(model=model_name, base_url="http://ollama:11434")
        self.memory = ConversationBufferMemory(memory_key="history",return_messages=True)
        template = """あなたは会話を日本語で回答します。
以下はこれまでの会話です。
{history}
ユーザー: {input}
AI（日本語で回答）:"""

        self.prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=template
        )

        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            verbose=True,
            memory=self.memory
        )

        #self.chain = ConversationChain(llm=self.llm, memory=self.memory)

    def chat(self, user_input: str) -> str:
        # メッセージを送信し、LLMの返答を返す
        return self.chain.run(user_input)
