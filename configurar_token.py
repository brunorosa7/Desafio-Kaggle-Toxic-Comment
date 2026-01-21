"""
Script auxiliar para configurar o token do Kaggle
"""

import os
import json
from pathlib import Path


def configurar_via_arquivo():
    """Configura o token via arquivo kaggle.json"""
    token = "KGAT_d90232b7269fedf44271f65b01a6e973"
    username = "brunorosabarba"
    
    kaggle_dir = Path.home() / '.kaggle'
    kaggle_file = kaggle_dir / 'kaggle.json'
    
    # Criar diretório se não existir
    kaggle_dir.mkdir(exist_ok=True)
    
    # Criar arquivo kaggle.json
    config = {
        "username": username,
        "key": token
    }
    
    with open(kaggle_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    
    print(f"✓ Token configurado em: {kaggle_file}")
    print(f"✓ Username: {username}")
    print(f"✓ Token: {token[:20]}...")
    
    # Configurar permissões no Windows (se disponível)
    try:
        import subprocess
        # Remove herança de permissões
        subprocess.run(
            ['icacls', str(kaggle_file), '/inheritance:r'],
            capture_output=True,
            check=False
        )
        # Concede apenas leitura para o usuário atual
        usuario = os.environ.get('USERNAME', '')
        subprocess.run(
            ['icacls', str(kaggle_file), f'/grant:r', f'{usuario}:(R)'],
            capture_output=True,
            check=False
        )
        print("✓ Permissões de segurança configuradas")
    except Exception as e:
        print(f"⚠ Não foi possível configurar permissões: {e}")
        print("  Configure manualmente se necessário")
    
    return True


def configurar_via_variavel_ambiente():
    """Mostra como configurar via variável de ambiente"""
    token = "KGAT_d90232b7269fedf44271f65b01a6e973"
    
    print("\n" + "=" * 60)
    print("Configuração via Variável de Ambiente")
    print("=" * 60)
    print("\nNo PowerShell, execute:")
    print(f"  $env:KAGGLE_API_TOKEN='{token}'")
    print("\nOu no CMD:")
    print(f"  set KAGGLE_API_TOKEN={token}")
    print("\n⚠ Nota: Esta configuração é válida apenas na sessão atual")
    print("   Para tornar permanente, adicione ao perfil do PowerShell")


def main():
    """Função principal"""
    print("=" * 60)
    print("Configuração do Token do Kaggle")
    print("=" * 60)
    
    print("\nEscolha o método de configuração:")
    print("  1. Arquivo kaggle.json (permanente)")
    print("  2. Variável de ambiente (mostrar instruções)")
    print("  3. Ambos")
    
    escolha = input("\nDigite sua escolha (1, 2 ou 3): ").strip()
    
    if escolha == "1":
        configurar_via_arquivo()
    elif escolha == "2":
        configurar_via_variavel_ambiente()
    elif escolha == "3":
        configurar_via_arquivo()
        configurar_via_variavel_ambiente()
    else:
        print("Opção inválida. Configurando via arquivo por padrão...")
        configurar_via_arquivo()
    
    print("\n" + "=" * 60)
    print("✅ Configuração concluída!")
    print("=" * 60)
    print("\nPróximo passo: Execute 'python download_data.py'")


if __name__ == "__main__":
    main()
