# Sistema de Gerenciamento de Restaurantes

## Descrição

Este projeto é um sistema de gerenciamento de restaurantes que permite a criação de restaurantes, adição de pratos ao cardápio, registro de avaliações de clientes e gerenciamento de informações de clientes. O sistema é construído utilizando **Python** e **FastAPI**, proporcionando uma API RESTful para interação.

## Funcionalidades

- **Gerenciamento de Restaurantes**: Criar, listar e alterar o estado (ativo/desativado) dos restaurantes.
- **Gerenciamento de Pratos**: Adicionar pratos ao cardápio de cada restaurante.
- **Avaliações**: Registrar e listar avaliações feitas por clientes, além do cálculo da média das avaliações.
- **Gerenciamento de Clientes**: Cadastrar, buscar e listar clientes.

## Estrutura do Código

O código está organizado em classes que representam as principais entidades do sistema:

- **Restaurante**: Representa um restaurante, com métodos para adicionar pratos e registrar pedidos.
- **SistemaAvaliacoes**: Gerencia as avaliações dos restaurantes, permitindo registrar e listar avaliações, além de calcular a média das notas.
- **SistemaClientes**: Gerencia os clientes, permitindo cadastrar, buscar e listar clientes.

## Instalação

Para executar este projeto, você precisará ter o **Python** instalado em sua máquina. Siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/cristoferrxan/Restaurante-2.0.git
   cd Restaurante-2.0
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install fastapi uvicorn
   ```

## Uso

Para iniciar o servidor, execute o seguinte comando:

```bash
uvicorn main:app --reload
```

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Endpoints

### Criar Restaurante
**POST** `/criar_restaurante/`
```json
{
  "nome": "Nome do Restaurante",
  "categoria": "Categoria do Restaurante"
}
```

### Adicionar Prato
**POST** `/adicionar_prato/`
```json
{
  "nome_restaurante": "Nome do Restaurante",
  "nome_prato": "Nome do Prato",
  "preco": 10.0
}
```

### Registrar Avaliação
**POST** `/registrar_avaliacao/`
```json
{
  "restaurante": "Nome do Restaurante",
  "cliente": "Nome do Cliente",
  "nota": 5,
  "comentario": "Ótimo!"
}
```

### Listar Avaliações
**GET** `/listar_avaliacoes/`
**Query Params:** `restaurante=Nome do Restaurante`

### Calcular Média de Avaliações
**GET** `/calcular_media_avaliacoes/`
**Query Params:** `restaurante=Nome do Restaurante`

### Cadastrar Cliente
**POST** `/cadastrar_cliente/`
```json
{
  "nome": "Nome do Cliente",
  "idade": 30,
  "telefone": "11999999999",
  "email": "cliente@email.com"
}
```

### Listar Clientes
**GET** `/listar_clientes/`

### Buscar Cliente
**GET** `/buscar_cliente/`
**Query Params:** `email=cliente@email.com`

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b feature/nome-da-sua-feature
   ```
3. Faça suas alterações e commit:
   ```bash
   git commit -m "Adicionando nova feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nome-da-sua-feature
   ```
5. Abra um **Pull Request**.

## Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, fique à vontade para entrar em contato.

Agradecemos por usar o **Sistema de Gerenciamento de Restaurantes**!



