# 🚀 Como Iniciar o Jupyter Corretamente

## Problema: Erros 404 - Arquivos não encontrados

Isso acontece quando o Jupyter é iniciado do diretório errado.

## ✅ Solução: Iniciar do Diretório Correto

### Opção 1: Via Terminal (Recomendado)

1. **Abra o PowerShell ou Terminal**

2. **Navegue até o diretório do projeto:**
   ```powershell
   cd c:\Users\thiag\Downloads\python-bruno
   ```

3. **Inicie o Jupyter Lab:**
   ```powershell
   jupyter lab
   ```

4. **Ou inicie o Jupyter Notebook:**
   ```powershell
   jupyter notebook
   ```

### Opção 2: Reiniciar o Jupyter Atual

1. **Pare o Jupyter atual:**
   - No terminal onde está rodando, pressione `Ctrl + C`
   - Ou feche a janela do terminal

2. **Navegue até o diretório correto:**
   ```powershell
   cd c:\Users\thiag\Downloads\python-bruno
   ```

3. **Inicie novamente:**
   ```powershell
   jupyter lab
   ```

## 📁 Estrutura Correta

O Jupyter deve ser iniciado do diretório raiz do projeto:

```
python-bruno/
├── data/
├── notebooks/          ← Os notebooks estão aqui
├── models/
├── submissions/
└── requirements.txt
```

Quando você iniciar o Jupyter deste diretório, você verá:
- `notebooks/01_eda_exploratoria.ipynb`
- `notebooks/02_modelo_e_submissao.ipynb`
- `data/raw/` (com os CSVs)

## 🔍 Verificar se está no diretório correto

No terminal, antes de iniciar o Jupyter, execute:
```powershell
pwd  # ou no PowerShell: Get-Location
```

Deve mostrar: `C:\Users\thiag\Downloads\python-bruno`

## ⚠️ Se ainda der erro

1. Verifique se os arquivos existem:
   ```powershell
   dir notebooks
   ```

2. Verifique o caminho atual:
   ```powershell
   Get-Location
   ```

3. Se necessário, navegue manualmente:
   ```powershell
   cd c:\Users\thiag\Downloads\python-bruno
   jupyter lab
   ```
