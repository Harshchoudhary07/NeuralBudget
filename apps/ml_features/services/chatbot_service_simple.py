"""
Simplified chatbot service using direct Gemini API (no langchain/FAISS)
This version is optimized for free hosting with minimal dependencies.
"""
import os
import logging
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_chatbot_response(user_id: str, message: str) -> str:
    """
    Simple chatbot using Gemini without RAG.
    For free hosting - no vector store, just direct LLM calls.
    """
    try:
        # Import here to avoid circular imports
        from apps.common_utils.firebase_service import get_transactions
        
        # Get user's recent transactions
        expenses = get_transactions(user_id, "expenses")
        incomes = get_transactions(user_id, "incomes")
        
        # Build context from transactions
        context_parts = ["Here is the user's financial data:\n"]
        
        if incomes:
            context_parts.append("INCOMES:")
            for inc in incomes[:20]:  # Limit to recent 20
                context_parts.append(
                    f"- {inc.get('source', 'Unknown')}: ₹{inc.get('amount', 0)} "
                    f"on {inc.get('date', 'Unknown')} ({inc.get('status', 'Unknown')})"
                )
        
        if expenses:
            context_parts.append("\nEXPENSES:")
            for exp in expenses[:20]:  # Limit to recent 20
                context_parts.append(
                    f"- {exp.get('name', 'Unknown')} ({exp.get('category', 'Other')}): "
                    f"₹{exp.get('amount', 0)} on {exp.get('date', 'Unknown')} "
                    f"({exp.get('status', 'Unknown')})"
                )
        
        context = "\n".join(context_parts)
        
        # Create prompt
        prompt = f"""You are Neural Budget, a helpful financial assistant.

{context}

User Question: {message}

Instructions:
- Answer based ONLY on the data provided above
- Use Indian Rupees (₹) for amounts
- Be concise and helpful
- If the data doesn't contain the answer, say so

Answer:"""
        
        # Call Gemini
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        return response.text.strip()
        
    except Exception as e:
        logger.error(f"Error in chatbot: {e}")
        return "Sorry, I encountered an error. Please try again later."


if __name__ == '__main__':
    # Test
    test_user = "PZWaO69zDjfivyIwPX4wi1KK6Pp2"
    test_query = "How much income do I have this month?"
    
    print(f"Q: {test_query}")
    response = get_chatbot_response(test_user, test_query)
    print(f"A: {response}")
