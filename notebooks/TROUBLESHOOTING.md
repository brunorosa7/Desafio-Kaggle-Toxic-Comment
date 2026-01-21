# 🔧 Guia de Troubleshooting - Jupyter Notebook

## Problema: Células não executam ou ficam travadas

### 1. Verificar se o Kernel está conectado

**Sintoma:** Células mostram `[*]` e não completam

**Solução:**
- Olhe no canto superior direito do notebook
- Deve aparecer "Python 3 (ipykernel)" ou similar
- Se aparecer "No Kernel" ou "Connecting...", clique e selecione um kernel

### 2. Reiniciar o Kernel

**Sintoma:** Células travadas, não respondem

**Solução:**
- Menu: `Kernel` → `Restart Kernel`
- Ou: `Kernel` → `Restart Kernel and Clear All Outputs`
- Depois execute as células novamente

### 3. Verificar se os dados existem

**Sintoma:** Erro ao carregar arquivos CSV

**Solução:**
Execute esta célula de teste:

```python
from pathlib import Path
import os

# Verificar caminho atual
print("Diretório atual:", os.getcwd())

# Verificar se os arquivos existem
data_dir = Path('../data/raw')
print(f"\nCaminho dos dados: {data_dir.absolute()}")

arquivos = list(data_dir.glob('*.csv'))
print(f"\nArquivos CSV encontrados: {len(arquivos)}")
for arquivo in arquivos:
    print(f"  - {arquivo.name} ({arquivo.stat().st_size / (1024*1024):.2f} MB)")
```

### 4. Células demorando muito

**Sintoma:** Célula mostra `[*]` por muito tempo

**Causa:** Arquivos grandes (train.csv tem ~68MB)

**Solução:**
- Aguarde! O carregamento pode levar 10-30 segundos
- Verifique se há mensagens de erro no output
- Se travar completamente, reinicie o kernel

### 5. Erro de caminho

**Sintoma:** `FileNotFoundError` ao carregar dados

**Solução:**
- Certifique-se de que está executando do diretório correto
- O notebook deve estar em `notebooks/`
- Os dados devem estar em `data/raw/`

### 6. Verificar se as bibliotecas estão instaladas

**Sintoma:** `ModuleNotFoundError`

**Solução:**
Execute no terminal:
```bash
pip install pandas numpy matplotlib seaborn
```

### 7. Executar célula por célula

**Recomendação:**
- Execute uma célula por vez
- Aguarde cada uma completar antes de executar a próxima
- Verifique se há erros antes de continuar

## Comandos úteis no JupyterLab

- **Interromper execução:** `Kernel` → `Interrupt Kernel` (ou botão ⏹️)
- **Reiniciar kernel:** `Kernel` → `Restart Kernel`
- **Limpar outputs:** `Edit` → `Clear All Outputs`
- **Executar todas:** `Run` → `Run All Cells`

## Verificar status do kernel

- Canto superior direito: mostra o kernel ativo
- Se estiver "Busy", o kernel está processando
- Se estiver "Idle", está pronto para executar
