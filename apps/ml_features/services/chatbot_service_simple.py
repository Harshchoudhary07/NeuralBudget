"""
Ultra-minimal chatbot using Gemini REST API (no SDK dependencies)
Optimized for free hosting with absolute minimal dependencies.
"""
import os
import logging
import json
from dotenv import load_dotenv
import requests

# Load environment
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

def call_gemini_api(prompt: str) -> str:
    """Call Gemini API directly using REST"""
    try:
        headers = {
            "Content-Type": "application/json"
        }
        
        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 512
            }
        }
        
        url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
        
    except Exception as e:
        logger.error(f"Gemini API error: {e}")
        raise

def get_chatbot_response(user_id: str, message: str) -> str:
    """
    Simple chatbot using Gemini REST API.
    For free hosting - no vector store, just direct API calls.
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
        
        # Call Gemini REST API
        response_text = call_gemini_api(prompt)
        return response_text.strip()
        
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
