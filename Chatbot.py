from ai import call_gpt

def main():
# Welcome banner using simple text art
print("====================================")
print("🤖 Welcome to Amazing ChatBot! 🤖")
print("====================================")
print("Type 'exit' at any time to leave the chat.\n")

# This loop keeps the chatbot running continuously  
while True:  
    print("👤 You: ", end="")  
    user_input = input()  
      
    # Check if the user wants to quit  
    if user_input.lower() == 'exit':  
        print("\n🤖 Amazing ChatBot: Thank you and hope to see you again :) ! 👋")  
        break  
          
    print("⚙️  Processing...")  
      
    # Crafting the prompt for GPT  
    prompt = (  
        f"Find out the information about {user_input} and answer like a chatbot. "  
        f"End your response with a friendly variation of 'If you have any more questions, feel free to ask!'"  
    )  
      
    response = call_gpt(prompt)  
      
    # Print the response with some spacing  
    print(f"\n🤖 Amazing ChatBot:\n{response}")  
    print("-" * 40) # Simple visual separator

if __name__ == "__main__":
    main()
