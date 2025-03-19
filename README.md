# DESAFIO 🕹️ Improve This Game 🕹️

### Universidade Federal Rural de Pernambuco  
**Departamento de Estatística e Informática**  
**Bacharelado em Sistemas de Informação**  
**Disciplina: Princípios de Programação**

---

# **DESAFIO: Melhoria do Jogo de Personagens - POO em Python**

## **Descrição do Desafio**

Este repositório contém um de um jogo de personagens que precisou ser aprimorado. O objetivo era aplicar conceitos de **Programação Orientada a Objetos (POO)**, **listas**, **dicionários** e **estruturas de repetição e decisão** para tornar o jogo mais interativo e dinâmico.

## **Objetivo da Atividade**

Nós alunos deviamos melhorar o código existente, que possuia as classes `Personagem` e `Vilao`, mas faltava a inclusão da classe `Heroi`. Além disso, os métodos implementados eram muito básicos e não proporcionavam uma interação interessante com o usuário. Tivemos que usar nossa criatividade e habilidades para aprimorar o código e o deixar mais interessante

## **Tarefas a serem realizadas**

1. **Criar a classe `Heroi`**, que deve herdar de `Personagem`, assim como `Vilao`. Essa classe deve ter características e métodos próprios.
2. **Reestruturar os métodos das classes** para que realizem ações mais complexas e significativas, como ataques, defesa e uso de habilidades.
3. **Criar um sistema de interação entre heróis e vilões**, adicionando diálogos e eventos durante o jogo.
4. **Utilizar listas e dicionários** para armazenar informações dos personagens, como status, habilidades e itens.
5. **Implementar estruturas de repetição e decisão** para gerenciar batalhas e eventos no jogo.
6. **Melhorar a interface textual do jogo**, exibindo mensagens mais interativas para o jogador.
7. **Garantir que o código esteja modularizado**, permitindo fácil manutenção e expansão do jogo.

## **Requisitos Técnicos**

✅ Todos os personagens (heróis e vilões) devem ter atributos como `nome`, `vida`, `ataque` e `defesa`.

✅ A classe `Heroi` deve herdar de `Personagem` e possuir métodos próprios (`ataque_final`).

✅ Criar um método `dialogar()` para interações entre personagens, tornando o jogo mais envolvente.

✅ Implementar batalhas entre heróis e vilões utilizando estruturas de repetição e decisão.

✅ Usar **listas** para armazenar diferentes heróis e vilões, e **dicionários** para guardar seus atributos.

✅ Melhorar a exibição de mensagens e interações para tornar a jogabilidade mais interessante.

✅ Criar um sistema de registro de ações para acompanhar o histórico dos eventos do jogo.

## **Arquivos do Projeto**

O projeto contém os seguintes arquivos:

- `personagem.py` - Define a classe base `Personagem`
- `vilao.py` - Define a classe `Vilao`, que herda de `Personagem`
- `heroi.py` - Define a classe `Heroi`, que também herda de `Personagem`
- `main.py` - Arquivo principal para rodar o jogo e testar as interações
- `registro.py` - Define a classe `Registro`, que define o registro das ações do jogo
- `ataques.py` - Define a classe `Luta`, que herda de `Vilão`, `Heroi` e `Personagem` e define a batalha entre os personagens

## **Como Executar o Código**

1. Clone este repositório:
   ```sh
   git clone https://github.com/claramferraz/melhorias-jogo.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd melhorias-jogo
   ```
3. Execute o jogo:
   ```sh
   python main.py
   ```

---

🚀 Espero que se divirta com o jogo!

