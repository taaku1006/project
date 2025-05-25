from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class LLMChatService:
    def __init__(self, model_name="elyza3"):
        # LLMの初期化
        self.llm = OllamaLLM(model=model_name, base_url="http://ollama:11434")
        self.memory = ConversationBufferMemory(memory_key="history",return_messages=True)
        template = """あなたは親切で知識豊富なAIであり、日本語だけで回答します。
絶対に中国語では答えないでください。以下は会話履歴です：
{history}
ユーザー: {input}
AI（日本語）:"""

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

    def chat(self, user_input: str) -> str:
        # メッセージを送信し、LLMの返答を返す
        return self.chain.run(user_input)

    #会話履歴をメモリに復元
    def load_history_from_records(self, message_records):

        self.memory.clear()

        for record in message_records:
            if record["sender_type"] == "user":
                self.memory.chat_memory.add_user_message(record["content"])
            elif record["sender_type"] == "ai":
                self.memory.chat_memory.add_ai_message(record["content"])
