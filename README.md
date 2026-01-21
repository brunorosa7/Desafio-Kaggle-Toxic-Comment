# Jigsaw Toxic Comment Classification Challenge

Projeto para resolver o desafio de classificação de comentários tóxicos do Kaggle.

## 📋 Descrição

Este projeto visa desenvolver modelos de machine learning para identificar e classificar comentários tóxicos em diferentes categorias:
- `toxic`
- `severe_toxic`
- `obscene`
- `threat`
- `insult`
- `identity_hate`

## 🚀 Como começar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar credenciais do Kaggle

Você já possui o token de API! Veja o arquivo `CONFIGURAR_TOKEN.md` para instruções detalhadas.

**Forma rápida (PowerShell):**
```powershell
$env:KAGGLE_API_TOKEN='KGAT_d90232b7269fedf44271f65b01a6e973'
```

Ou configure via arquivo `kaggle.json` (veja `CONFIGURAR_TOKEN.md` para detalhes).

### 3. Baixar os dados

```bash
python download_data.py
```

O script irá:
- Verificar se o Kaggle CLI está instalado
- Criar a estrutura de diretórios
- Baixar os dados da competição
- Descompactar os arquivos automaticamente

## 📁 Estrutura do Projeto

```
python-bruno/
├── data/
│   ├── raw/          # Dados originais baixados
│   └── processed/    # Dados pré-processados
├── models/           # Modelos treinados
├── notebooks/        # Jupyter notebooks de análise
├── download_data.py  # Script para baixar dados
├── requirements.txt  # Dependências do projeto
└── README.md        # Este arquivo
```

## 📊 Dados

Após o download, você terá os seguintes arquivos em `data/raw/`:

- `train.csv` - Conjunto de treinamento com comentários e rótulos
- `test.csv` - Conjunto de teste para previsões
- `test_labels.csv` - Rótulos do conjunto de teste (adicionado após o encerramento)
- `sample_submission.csv` - Formato de exemplo para submissão

## 🔧 Próximos Passos

1. Análise Exploratória de Dados (EDA)
2. Pré-processamento de texto
3. Feature engineering
4. Treinamento de modelos
5. Avaliação e otimização
6. Submissão das previsões
