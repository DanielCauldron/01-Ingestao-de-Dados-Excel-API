# Ingestão de Dados (Excel + API)

Este projeto tem como objetivo automatizar a extração, transformação e armazenamento de dados provenientes de arquivos Excel baixados via API, convertendo-os para o formato CSV para facilitar análises e manipulação dos dados.

## Funcionalidades

- Download automático de arquivos Excel via API
- Conversão de arquivos Excel (.xlsx) para CSV
- Organização dos dados em pastas (`raw` e `processed`)
- Scripts modulares para extração e transformação

## Estrutura de Pastas

```
extract/              # Scripts de extração de dados
transform/            # Scripts de transformação de dados
dados/raw/            # Arquivos originais baixados
dados/processed/      # Arquivos processados (CSV)
```

## Como Usar

1. **Instale as dependências**
   ```sh
   pip install pandas requests
   ```

2. **Configure variáveis de ambiente**  
   (Se necessário, crie um arquivo `.env` com as chaves da API ou URLs.)

3. **Execute a extração dos dados**
   ```sh
   python extract/extrair_dados.py
   ```

4. **Transforme os dados**
   ```sh
   python transform/extracty.py
   ```

## Exemplo

- **Input:** Arquivo Excel baixado da API
- **Output:** Arquivo CSV salvo em `dados/processed/`

## Requisitos

- Python 3.x
- pandas
- requests

## Autor

Daniel Caldeirão  
dfcaldeirao@gmail.com

## Licença
