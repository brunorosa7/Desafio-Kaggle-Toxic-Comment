"""
Script para baixar dados da competição Kaggle: Jigsaw Toxic Comment Classification Challenge
"""

import os
import sys
import subprocess
import zipfile
from pathlib import Path

# Configurar encoding para Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


def verificar_kaggle_cli():
    """Verifica se o Kaggle CLI está instalado e configurado"""
    try:
        result = subprocess.run(
            ['kaggle', '--version'],
            capture_output=True,
            text=True,
            check=True
        )
        print("[OK] Kaggle CLI encontrado")
        
        # Verificar se há token configurado
        token_env = os.environ.get('KAGGLE_API_TOKEN')
        kaggle_file = Path.home() / '.kaggle' / 'kaggle.json'
        
        if token_env:
            print("[OK] Token de API encontrado na variável de ambiente")
            return True
        elif kaggle_file.exists():
            print("[OK] Arquivo kaggle.json encontrado")
            # Verificar se o arquivo está válido
            try:
                import json
                with open(kaggle_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    if 'username' in config and 'key' in config:
                        print(f"  Username: {config['username']}")
                        print(f"  Token: {config['key'][:20]}...")
                        return True
                    else:
                        print("[AVISO] Arquivo kaggle.json está incompleto")
                        print("  Deve conter: {\"username\":\"...\",\"key\":\"...\"}")
                        return False
            except json.JSONDecodeError:
                print("[AVISO] Arquivo kaggle.json está com formato inválido")
                return False
            except Exception as e:
                print(f"[AVISO] Erro ao ler kaggle.json: {e}")
                return False
        else:
            print("[AVISO] Token de API não configurado")
            print("\nConfigure o token usando uma das opções:")
            print("\nOpção 1 - Variável de ambiente (PowerShell):")
            print("  $env:KAGGLE_API_TOKEN='seu_token_aqui'")
            print("\nOpção 2 - Arquivo kaggle.json:")
            print(f"  Crie o arquivo: {kaggle_file}")
            print("  Com o conteúdo: {\"username\":\"seu_usuario\",\"key\":\"seu_token\"}")
            return False  # Não continua sem token
            
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[ERRO] Kaggle CLI não encontrado")
        print("\nPara instalar o Kaggle CLI, execute:")
        print("  pip install kaggle")
        print("\nDepois, configure suas credenciais:")
        print("  1. Acesse: https://www.kaggle.com/account")
        print("  2. Vá em 'API' e clique em 'Create New Token'")
        print("  3. Configure via variável de ambiente ou arquivo kaggle.json")
        return False


def criar_estrutura_diretorios():
    """Cria a estrutura de diretórios necessária"""
    dirs = ['data', 'data/raw', 'data/processed', 'models', 'notebooks']
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"[OK] Diretório criado/verificado: {dir_path}")


def testar_autenticacao():
    """Testa se a autenticação do Kaggle está funcionando"""
    print("\n[TESTE] Testando autenticação...")
    try:
        result = subprocess.run(
            ['kaggle', 'competitions', 'list'],
            capture_output=True,
            text=True,
            check=True,
            timeout=30
        )
        print("[OK] Autenticação OK")
        return True
    except subprocess.TimeoutExpired:
        print("[ERRO] Timeout ao testar autenticação")
        return False
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Erro na autenticação:")
        print(f"  stdout: {e.stdout}")
        print(f"  stderr: {e.stderr}")
        print(f"  Código de retorno: {e.returncode}")
        return False
    except Exception as e:
        print(f"[ERRO] Erro inesperado: {e}")
        return False


def baixar_dados():
    """Baixa os dados da competição usando o Kaggle CLI"""
    competicao = "jigsaw-toxic-comment-classification-challenge"
    diretorio_destino = "data/raw"
    
    print(f"\n[DOWNLOAD] Baixando dados da competição: {competicao}")
    print(f"[DESTINO] Destino: {diretorio_destino}")
    
    try:
        comando = [
            'kaggle',
            'competitions',
            'download',
            '-c',
            competicao,
            '-p',
            diretorio_destino
        ]
        
        print(f"Executando: {' '.join(comando)}")
        
        result = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            check=True,
            timeout=300  # 5 minutos de timeout
        )
        
        # Mostrar saída se houver
        if result.stdout:
            print(f"Saída: {result.stdout}")
        
        print("[OK] Download concluído com sucesso!")
        return True
        
    except subprocess.TimeoutExpired:
        print("[ERRO] Timeout ao baixar dados (pode estar demorando muito)")
        return False
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Erro ao baixar dados:")
        print(f"  Código de retorno: {e.returncode}")
        if e.stdout:
            print(f"  stdout: {e.stdout}")
        if e.stderr:
            print(f"  stderr: {e.stderr}")
        
        # Verificar erros comuns
        if "403" in str(e.stderr) or "Forbidden" in str(e.stderr):
            print("\n[AVISO] Erro 403: Verifique se você aceitou os termos da competição no Kaggle")
            print("  Acesse: https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/rules")
        elif "404" in str(e.stderr) or "Not Found" in str(e.stderr):
            print("\n[AVISO] Erro 404: Verifique se o nome da competição está correto")
        elif "401" in str(e.stderr) or "Unauthorized" in str(e.stderr):
            print("\n[AVISO] Erro 401: Problema de autenticação. Verifique seu token")
        
        return False
    except Exception as e:
        print(f"[ERRO] Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        return False


def descompactar_arquivos():
    """Descompacta todos os arquivos ZIP na pasta data/raw"""
    diretorio_raw = Path("data/raw")
    arquivos_zip = list(diretorio_raw.glob("*.zip"))
    
    if not arquivos_zip:
        print("[AVISO] Nenhum arquivo ZIP encontrado em data/raw")
        return False
    
    print(f"\n[UNZIP] Descompactando {len(arquivos_zip)} arquivo(s)...")
    
    for arquivo_zip in arquivos_zip:
        try:
            print(f"  Descompactando: {arquivo_zip.name}")
            with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
                zip_ref.extractall(diretorio_raw)
            print(f"  [OK] {arquivo_zip.name} descompactado")
        except zipfile.BadZipFile:
            print(f"  [ERRO] {arquivo_zip.name} não é um arquivo ZIP válido")
        except Exception as e:
            print(f"  [ERRO] Erro ao descompactar {arquivo_zip.name}: {e}")
    
    return True


def listar_arquivos_baixados():
    """Lista os arquivos CSV baixados"""
    diretorio_raw = Path("data/raw")
    arquivos_csv = list(diretorio_raw.glob("*.csv"))
    
    if arquivos_csv:
        print("\n[ARQUIVOS] Arquivos CSV disponíveis:")
        for arquivo in arquivos_csv:
            tamanho_mb = arquivo.stat().st_size / (1024 * 1024)
            print(f"  • {arquivo.name} ({tamanho_mb:.2f} MB)")
    else:
        print("\n[AVISO] Nenhum arquivo CSV encontrado")


def main():
    """Função principal"""
    print("=" * 60)
    print("Kaggle: Jigsaw Toxic Comment Classification Challenge")
    print("Script de Download de Dados")
    print("=" * 60)
    
    # Verificar Kaggle CLI
    if not verificar_kaggle_cli():
        return
    
    # Criar estrutura de diretórios
    print("\n[DIRETORIOS] Criando estrutura de diretórios...")
    criar_estrutura_diretorios()
    
    # Testar autenticação
    if not testar_autenticacao():
        print("\n[AVISO] A autenticação falhou. Verifique seu token antes de continuar.")
        resposta = input("Deseja continuar mesmo assim? (s/n): ").strip().lower()
        if resposta != 's':
            return
    
    # Baixar dados
    if not baixar_dados():
        return
    
    # Descompactar arquivos
    if not descompactar_arquivos():
        return
    
    # Listar arquivos baixados
    listar_arquivos_baixados()
    
    print("\n" + "=" * 60)
    print("[SUCESSO] Processo concluído com sucesso!")
    print("=" * 60)
    print("\nPróximos passos:")
    print("  1. Explore os dados em data/raw/")
    print("  2. Crie notebooks de análise em notebooks/")
    print("  3. Desenvolva seus modelos e salve em models/")


if __name__ == "__main__":
    main()
