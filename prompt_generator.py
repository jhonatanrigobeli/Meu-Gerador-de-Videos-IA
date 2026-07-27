"""
Prompt Generator Module - Converts scenes into detailed image prompts
"""

from pathlib import Path
from config import PROJECTS_DIR


class PromptGenerator:
    """Generates detailed image prompts from scenes"""

    def __init__(self):
        self.style_templates = {
            "épico": "ultra realistic, cinematic, epic, grand scale, dramatic lighting",
            "dramático": "dramatic, emotional, intense, high contrast, moody",
            "comédia": "colorful, vibrant, fun, playful, bright lighting",
            "educativo": "clear, professional, well-lit, clean background, informative",
            "horror": "dark, ominous, eerie, scary, ominous lighting",
            "fantasia": "magical, mystical, fantasy art, detailed, intricate",
        }

    def generate_prompt(self, scene, style="épico", quality="4k"):
        """
        Generate image prompt from scene
        
        Args:
            scene: Scene dictionary with description
            style: Visual style
            quality: Image quality (4k, 8k, etc)
            
        Returns:
            Detailed prompt for image generation
        """
        style_base = self.style_templates.get(style, "professional")
        
        prompt = f"""{scene['description']}

Professional art, {style_base}, {quality} quality, 
cinematic composition, professional photography, 
color graded, highly detailed, sharp focus,
beautiful lighting, best quality, masterpiece"""
        
        return prompt

    def generate_prompts_batch(self, project_name, scenes, style="épico"):
        """
        Generate prompts for all scenes
        
        Args:
            project_name: Project name
            scenes: List of scenes
            style: Visual style for all scenes
            
        Returns:
            List of generated prompts
        """
        prompts = []
        project_path = PROJECTS_DIR / project_name
        prompts_dir = project_path / "prompts"
        prompts_dir.mkdir(parents=True, exist_ok=True)
        
        for scene in scenes:
            prompt = self.generate_prompt(scene, style)
            prompts.append({
                "scene_number": scene['number'],
                "scene_title": scene['title'],
                "prompt": prompt
            })
            
            # Save individual prompt file
            filename = f"prompt_{scene['number']:03d}.txt"
            filepath = prompts_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"[CENA {scene['number']}] - {scene['title']}\n\n")
                f.write(prompt)
            
            print(f"✅ Prompt gerado: {filename}")
        
        return prompts

    def load_prompts(self, project_name):
        """Load generated prompts from project"""
        project_path = PROJECTS_DIR / project_name
        prompts_dir = project_path / "prompts"
        
        if not prompts_dir.exists():
            return []
        
        prompts = []
        prompt_files = sorted(prompts_dir.glob("prompt_*.txt"))
        
        for prompt_file in prompt_files:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            prompts.append(content)
        
        return prompts

    def enhance_prompt(self, base_prompt, additional_details=""):
        """
        Enhance prompt with additional details
        
        Args:
            base_prompt: Base prompt text
            additional_details: Extra details to add
            
        Returns:
            Enhanced prompt
        """
        enhanced = base_prompt
        
        if additional_details:
            enhanced += f", {additional_details}"
        
        # Add quality indicators
        enhanced += ", trending on artstation, highly detailed, sharp focus"
        
        return enhanced
