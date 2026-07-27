# 🗺️ Roadmap do Projeto

## Fase 1-3: Setup ✅ (CONCLUÍDA)
- [x] Instalar Git, Python 3.11, VS Code, FFmpeg
- [x] Criar conta no GitHub
- [x] Criar repositório inicial
- [x] Estruturar pastas do projeto
- [x] Primeiro commit
- [x] Hello World funcionando

**Status**: Pronto para usar!

---

## Fase 4-6: Gerenciamento de Projetos 🔄 (PRÓXIMA)

### Fase 4: Criar um Projeto
- [ ] Sistema de prompt interativo
- [ ] Validação de entrada do usuário
- [ ] Criar pasta do projeto automaticamente
- [ ] Salvar metadados do projeto

```bash
python app.py
# Digite o título: A Herdeira da Espada
# Projeto criado em: projects/A_Herdeira_da_Espada/
```

### Fase 5: Gerar Roteiro
- [ ] Integrar modelo de linguagem (LLM)
- [ ] Escolher entre API (OpenAI) ou modelo local (Mistral)
- [ ] Gerar `roteiro.txt`
- [ ] Salvar estrutura do roteiro

```
Título: A Herdeira da Espada
↓
roteiro.txt (estrutura narrativa completa)
```

### Fase 6: Dividir Roteiro em Cenas
- [ ] Parser de cenas automático
- [ ] Validação de estrutura
- [ ] Gerar arquivos individuais

```
cena_001.txt (descrição + diálogos)
cena_002.txt
cena_003.txt
```

---

## Fase 7-9: Geração de Imagens e Vídeos 🎨 (TERCEIRA ETAPA)

### Fase 7: Gerar Prompts Descritivos
- [ ] Converter cada cena em prompt detalhado
- [ ] Adicionar contexto visual e emocional
- [ ] Validar qualidade dos prompts

```
Cena: Uma guerreira sobe uma montanha.
↓
Prompt: Ultra realistic female warrior climbing snowy mountain, 
cinematic lighting, 4k, professional photography...
```

### Fase 8: Gerar Imagens
- [ ] Integrar Flux ou SDXL
- [ ] Gerenciar requisições de GPU
- [ ] Cache de imagens
- [ ] Salvar em alta resolução

```
001.png
002.png
003.png
```

### Fase 9: Gerar Vídeos
- [ ] Integrar modelo de vídeo (Wan 2.2 / CogVideoX / Hunyuan)
- [ ] Converter imagens em vídeos curtos (2-5 segundos)
- [ ] Controlar qualidade e codec

```
001.mp4 (2 segundos)
002.mp4 (3 segundos)
003.mp4 (2.5 segundos)
```

---

## Fase 10-12: Áudio e Legendas 🔊 (QUARTA ETAPA)

### Fase 10: Gerar Narração
- [ ] Integrar TTS (Text-to-Speech)
- [ ] Suporte a múltiplos idiomas
- [ ] Escolher vozes e velocidade
- [ ] Sincronização com cenas

```
Roteiro + voz selecionada → voz.mp3
```

### Fase 11: Gerar Legendas
- [ ] Converter áudio em texto (Speech-to-Text) ou usar roteiro
- [ ] Gerar arquivo SRT
- [ ] Posicionar legendas na tela

```
legenda.srt (formatado para vídeo)
```

### Fase 12: Montagem Automática com FFmpeg
- [ ] Orquestrar FFmpeg
- [ ] Combinar vídeos + áudio + legendas
- [ ] Adicionar efeitos de transição
- [ ] Exportar em múltiplos formatos

```
Vídeos + Áudio + Legendas → video_final.mp4
```

---

## Fase 13-15: Interface e Evolução 🚀 (QUINTA ETAPA)

### Fase 13: Interface Web com Streamlit
- [ ] Criar dashboard interativo
- [ ] Input: Título, idioma, duração, estilo
- [ ] Botão "GERAR VÍDEO"
- [ ] Barra de progresso
- [ ] Preview em tempo real

```
┌─────────────────────────────┐
│  GERADOR DE VÍDEOS IA       │
├─────────────────────────────┤
│ Título: [_______________]   │
│ Idioma: [Português ▼]       │
│ Duração: [30s ▼]            │
│ Estilo: [Épico ▼]           │
│                             │
│     [ GERAR VÍDEO ]         │
└─────────────────────────────┘
```

### Fase 14: Publicar no GitHub
- [ ] Documentação completa
- [ ] Exemplos de uso
- [ ] Contributing guidelines
- [ ] License (MIT)

```
Meu-Gerador-de-Videos-IA/
├── app.py
├── generator.py
├── image_generator.py
├── video_generator.py
├── voice_generator.py
├── subtitle_generator.py
├── editor.py
├── config.py
├── requirements.txt
├── README.md
└── ...
```

### Fase 15: Evoluções e Melhorias 🎯
- [ ] Geração automática de thumbnails
- [ ] Descrição otimizada para YouTube
- [ ] Tags automáticas por IA
- [ ] Narração em múltiplos idiomas
- [ ] **Upload automático para YouTube** (via API)
- [ ] Geração em lote (múltiplos vídeos)
- [ ] Histórico de projetos
- [ ] Análise de performance
- [ ] Sistema de templates
- [ ] Efeitos de transição avançados

---

## 📊 Timeline Sugerida

| Semana | Fase | Objetivo |
|--------|------|----------|
| 1 | 1-3 | Git, Python, estrutura ✅ |
| 2 | 4-6 | Interface e roteiros |
| 3 | 7-9 | Imagens e vídeos |
| 4 | 10-12 | Áudio, legendas, montagem |
| 5 | 13 | Interface web |
| 6 | 14-15 | Publicação e melhorias |

---

## 🔗 Dependências Externas

- **FFmpeg**: Edição de vídeo
- **Modelos HuggingFace**: Imagens, vídeos, áudio, texto
- **CUDA** (opcional): Aceleração de GPU

---

## 💡 Notas

- Cada fase é independente e pode ser ajustada
- Podemos pular fases ou reordená-las conforme necessário
- O projeto será sempre open-source no GitHub
- Feedback e melhorias são bem-vindas em cada etapa
