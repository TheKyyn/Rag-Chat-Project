from chat_service import ChatService

def main():
    chat_service = ChatService()
    
    test_question = "Quelle est la différence entre Python et JavaScript?"
    
    print("Test avec température = 0.7:")
    responses = chat_service.get_comparison(test_question)
    print("\nRéponse standard:")
    print(responses["standard"])
    print("\nRéponse avec RAG:")
    print(responses["rag"])
    
    print("\nTest avec température = 0.2:")
    chat_service.update_temperature(0.2)
    responses = chat_service.get_comparison(test_question)
    print("\nRéponse standard:")
    print(responses["standard"])
    print("\nRéponse avec RAG:")
    print(responses["rag"])

if __name__ == "__main__":
    main()
