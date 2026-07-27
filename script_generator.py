"""
Script Generator Module - Generates video scripts using LLM
Implements Fase 5: Script Generation
Supports OpenAI API and local models (Mistral, LLaMA, etc)
"""

import os
from pathlib import Path
from config import PROJECTS_DIR, MODELS, OPENAI_API_KEY, HUGGINGFACE_API_KEY


class ScriptGenerator:
    """Generates video scripts from titles/prompts"""

    def __init__(self, provider="huggingface", model="mistral"):
        """
        Initialize script generator
        
        Args:
            provider: "openai" or "huggingface"
            model: Model name (e.g., "gpt-4", "mistral-7b")
        """
        self.provider = provider
        self.model = model
        self.model_config = MODELS.get("llm", {})

    def generate_script(self, title, duration=300, style="épico"):
        """
        Generate a complete video script
        
        Args:
            title: Video title/topic
            duration: Approximate duration in seconds
            style: "épico", "dramático", "comédia", "educativo", etc
            
        Returns:
            Generated script text
        """
        prompt = self._build_prompt(title, duration, style)
        
        if self.provider == "openai":
            return self._generate_openai(prompt)
        elif self.provider == "huggingface":
            return self._generate_huggingface(prompt)
        else:
            return self._generate_local(prompt)

    def _build_prompt(self, title, duration, style):
        """Build the prompt for the LLM"""
        num_scenes = max(3, duration // 60)  # ~1 minute per scene
        
        prompt = f"""Gere um roteiro de vídeo com as seguintes especificações:

Título: {title}
Duração: ~{duration} segundos
Estilo: {style}
Número de cenas: {num_scenes}

Formato do roteiro (IMPORTANTE - use exatamente este formato):
- Comece com uma introdução impactante
- Cada cena deve usar este formato:
  [CENA N] - Título da Cena
  DESCRIÇÃO: (descrição visual detalhada)
  NARRAÇÃO: (texto a ser narrado)
  DURAÇÃO: (tempo em segundos)
  
- Termine com uma conclusão/call-to-action

Crie um roteiro envolvente e bem estruturado. Use exatamente o formato acima para cada cena.
"""
        return prompt

    def _generate_openai(self, prompt):
        """Generate script using OpenAI API"""
        try:
            import openai
            openai.api_key = OPENAI_API_KEY
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Você é um roteirista profissional de vídeos."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"❌ Erro ao gerar script com OpenAI: {e}")
            return None

    def _generate_huggingface(self, prompt):
        """Generate script using HuggingFace API"""
        try:
            from transformers import pipeline
            
            print(f"⏳ Gerando script com {self.model}...")
            generator = pipeline(
                "text-generation",
                model=f"mistralai/{self.model}",
                token=HUGGINGFACE_API_KEY
            )
            
            result = generator(prompt, max_length=1000, do_sample=True)
            return result[0]["generated_text"]
        except Exception as e:
            print(f"❌ Erro ao gerar script com HuggingFace: {e}")
            return None

    def _generate_local(self, prompt):
        """Generate script using local model"""
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            
            print(f"⏳ Carregando modelo local: {self.model}...")
            tokenizer = AutoTokenizer.from_pretrained(self.model)
            model = AutoModelForCausalLM.from_pretrained(self.model)
            
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(**inputs, max_length=1000, temperature=0.7)
            
            return tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            print(f"❌ Erro ao gerar script localmente: {e}")
            return None

    def save_script(self, project_name, script, filename="roteiro.txt"):
        """Save script to project directory"""
        project_path = PROJECTS_DIR / project_name
        script_file = project_path / filename
        
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script)
        
        print(f"✅ Roteiro salvo: {script_file}")
        return str(script_file)
