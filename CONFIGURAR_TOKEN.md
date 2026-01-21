# 🔑 Como Configurar o Token do Kaggle

Você já tem o token de API do Kaggle! Aqui estão as formas de configurá-lo:

## Token que você possui:
```
KGAT_d90232b7269fedf44271f65b01a6e973
```

## Opção 1: Variável de Ambiente (Recomendado - PowerShell)

No PowerShell, execute:

```powershell
$env:KAGGLE_API_TOKEN='KGAT_d90232b7269fedf44271f65b01a6e973'
```

**Para tornar permanente** (válido apenas na sessão atual):
- A variável será válida apenas enquanto o PowerShell estiver aberto
- Para tornar permanente, adicione ao seu perfil do PowerShell

**Para tornar permanente no PowerShell:**
```powershell
# Adicionar ao perfil do PowerShell
Add-Content $PROFILE "`n`$env:KAGGLE_API_TOKEN='KGAT_d90232b7269fedf44271f65b01a6e973'"
```

## Opção 2: Arquivo kaggle.json (Permanente)

1. Crie o diretório (se não existir):
   ```powershell
   New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.kaggle"
   ```

2. Crie o arquivo `kaggle.json`:
   ```powershell
   @"
   {
     "username": "brunorosabarba",
     "key": "KGAT_d90232b7269fedf44271f65b01a6e973"
   }
   "@ | Out-File -FilePath "$env:USERPROFILE\.kaggle\kaggle.json" -Encoding utf8
   ```

3. Configure as permissões (importante para segurança):
   ```powershell
   icacls "$env:USERPROFILE\.kaggle\kaggle.json" /inheritance:r
   icacls "$env:USERPROFILE\.kaggle\kaggle.json" /grant:r "$env:USERNAME:(R)"
   ```

## Opção 3: Configurar no Script Python

Você também pode definir a variável de ambiente diretamente no script antes de executar:

```python
import os
os.environ['KAGGLE_API_TOKEN'] = 'KGAT_d90232b7269fedf44271f65b01a6e973'
```

## ✅ Verificar se está funcionando

Após configurar, teste com:

```powershell
kaggle competitions list
```

Se funcionar, você está pronto para baixar os dados!

## 🚀 Próximo Passo

Depois de configurar o token, execute:

```powershell
python download_data.py
```
