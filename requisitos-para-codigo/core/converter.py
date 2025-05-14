import ollama
from typing import Optional
from .prompts import SYSTEM_PROMPT, GREETINGS, ERROR_MESSAGES

class BusinessRuleConverter:
    def __init__(self, model: str = "mistral"):
        self.model = model
    
    def convert(self, business_rule: str) -> str:
        business_rule = business_rule.strip().lower()
        
        if not business_rule:
            return ERROR_MESSAGES["empty"]
            
        if business_rule in GREETINGS:
            return GREETINGS[business_rule]
        
        if any(keyword in business_rule for keyword in ["?", "como", "quando", "onde", "porque"]):
            return ERROR_MESSAGES["out_of_scope"]
        
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": business_rule}
                ]
            )
            return response['message']['content']
        except Exception as e:
            return f"# Erro: {str(e)}\n# Verifique se o Ollama está rodando"