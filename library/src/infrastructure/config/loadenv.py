import os

def load_env(file_path='.env'):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo {file_path} não encontrado.")

    with open(file_path, 'r') as env_file:
        lines = env_file.readlines()

        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line and not cleaned_line.startswith('#'):
                key_value = cleaned_line.split('=', 1)
                if len(key_value) == 2:
                    key, value = key_value
                    cleaned_value = value.strip('\'"')
                    os.environ[key] = cleaned_value

print(load_env)
# Exemplo de uso:
# load_env()  # Isso carrega o arquivo .env padrão na raiz





# CRIAR FUNÇÂO PARA CARREGAMENTO DAS VARIAVEIS DE AMBIENTE

# LER informaçoes do arquivo de variaveis de ambiente