from dotenv import load_dotenv
load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello from rag-langgraph!")
    print(app.invoke(input={"question":"what is agent memory?"}))
