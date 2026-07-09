"""
PyTutor – Plataforma Inteligente para Aprendizagem de Python
Projeto de faculdade - Interface completa com CustomTkinter
"""

import customtkinter as ctk
import json
import os
import random
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

CORES = {
    "bg_principal": "#0f1117",
    "bg_sidebar": "#161b27",
    "bg_card": "#1e2535",
    "bg_card2": "#252d3d",
    "verde": "#4ade80",
    "verde_escuro": "#16a34a",
    "azul": "#3b82f6",
    "azul_claro": "#60a5fa",
    "roxo": "#a855f7",
    "amarelo": "#facc15",
    "laranja": "#f97316",
    "texto": "#e2e8f0",
    "texto_sub": "#94a3b8",
    "borda": "#2d3748",
    "erro": "#7f1d1d",
}
# categorias de conteudo
CONTEUDOS = [
    {"id": 1, "titulo": "Variáveis e Tipos", "icone": "📦",
     "descricao": "Em Python, variáveis são usadas para armazenar informações. Cada informação possui um tipo.",
     "explicacao": "Em Python, variáveis são usadas para armazenar informações.\nCada informação possui um tipo.\n\nOs 4 tipos principais são:\n\n  str   → textos          ex: nome = \"João\"\n  int   → inteiros        ex: idade = 18\n  float → decimais        ex: altura = 1.80\n  bool  → verdadeiro/falso ex: estudando = True\n\nExemplos:\n  cidade = \"Brasília\"   # str\n  ano    = 2026          # int\n  peso   = 72.5          # float\n  ativo  = True          # bool",
     "codigo": "nome     = \"João\"    # str\nidade    = 18         # int\naltura   = 1.80      # float\nestudando = True     # bool\n\nprint(nome)\nprint(idade)"},
    
    {"id": 2, "titulo": "Operações Básicas", "icone": "➕",
     "descricao": "Python suporta operações matemáticas e com strings de forma intuitiva.",
     "explicacao": "Python suporta operações matemáticas comuns:\n\n  +  → soma           ex: 5 + 3  = 8\n  -  → subtração      ex: 10 - 4 = 6\n  *  → multiplicação  ex: 3 * 4  = 12\n  /  → divisão        ex: 10 / 2 = 5.0\n  // → divisão inteira ex: 10 // 3 = 3\n  %  → resto          ex: 10 % 3 = 1\n  ** → potência       ex: 2 ** 3 = 8\n\nTambém podemos concatenar strings:\n  \"Olá\" + \" Mundo\"  →  \"Olá Mundo\"",
     "codigo": "a = 10\nb = 3\n\nprint(a + b)   # 13\nprint(a - b)   # 7\nprint(a * b)   # 30\nprint(a / b)   # 3.333...\nprint(a // b)  # 3\nprint(a % b)   # 1\nprint(a ** b)  # 1000"},
    
    {"id": 3, "titulo": "Condicionais", "icone": "🔀",
     "descricao": "Estruturas if/else permitem tomar decisões no programa.",
     "explicacao": "Condicionais permitem que o programa tome decisões:\n\n  if   → se (condição verdadeira)\n  elif → senão se (outra condição)\n  else → senão (nenhuma condição anterior)\n\nOperadores de comparação:\n  ==  igual       !=  diferente\n  >   maior       <   menor\n  >=  maior/igual <=  menor/igual\n\nImportante: Python usa indentação (4 espaços)\npara definir blocos de código!",
     "codigo": "idade = 18\n\nif idade >= 18:\n    print(\"Maior de idade\")\nelif idade >= 16:\n    print(\"Pode votar\")\nelse:\n    print(\"Menor de idade\")"},
    
    {"id": 4, "titulo": "Loops", "icone": "🔁",
     "descricao": "Loops permitem repetir ações múltiplas vezes.",
     "explicacao": "Python possui dois tipos principais de loop:\n\n  for  → repete para cada item de uma sequência\n  while → repete enquanto condição for True\n\nFunções úteis com loops:\n  range(n)      → sequência de 0 até n-1\n  range(a,b)    → sequência de a até b-1\n  break         → sai do loop\n  continue      → pula para a próxima iteração\n\nExemplo de loop for:\n  for i in range(5):\n      print(i)  # 0, 1, 2, 3, 4",
     "codigo": "# Loop for\nfor i in range(5):\n    print(i)\n\n# Loop while\ncontador = 0\nwhile contador < 3:\n    print(contador)\n    contador += 1"},
    
    {"id": 5, "titulo": "Funções", "icone": "⚙️",
     "descricao": "Funções agrupam código reutilizável com def.",
     "explicacao": "Funções são blocos de código reutilizáveis:\n\n  def nome_funcao(parametros):\n      # código\n      return resultado\n\nConceitos importantes:\n  def      → define a função\n  ()       → parâmetros (podem ser vazios)\n  return   → retorna um valor (opcional)\n\nBoas práticas:\n  - Nomes descritivos em minúsculas\n  - Uma função = uma responsabilidade\n  - Adicione docstrings para documentar",
     "codigo": "def saudacao(nome):\n    return f\"Olá, {nome}!\"\n\ndef soma(a, b):\n    return a + b\n\nprint(saudacao(\"João\"))\nprint(soma(3, 5))"},
    
    {"id": 6, "titulo": "Listas", "icone": "📋",
     "descricao": "Listas armazenam múltiplos valores em uma variável.",
     "explicacao": "Listas armazenam coleções de valores:\n\n  lista = [valor1, valor2, valor3]\n\nOperações principais:\n  lista[0]         → acessa o 1º elemento\n  lista.append(x)  → adiciona x ao final\n  lista.remove(x)  → remove o valor x\n  len(lista)       → tamanho da lista\n  lista.sort()     → ordena a lista\n\nÍndices começam em 0!\n  lista[-1]  → último elemento\n  lista[1:3] → do índice 1 ao 2",
     "codigo": "frutas = [\"maçã\", \"banana\", \"uva\"]\n\nprint(frutas[0])      # maçã\nprint(len(frutas))    # 3\n\nfrutas.append(\"manga\")\nprint(frutas)\n\nfor fruta in frutas:\n    print(fruta)"},
]
# exercicios normal, o id define o numero da questao, e o conteudo id define em qual categoria de conteudo a questao vai aparecer, entao se quiser adicionar uma categoria a mais e outra questao é só adicionar uma id maior das q já existe
EXERCICIOS = [
    {"id": 1, "conteudo_id": 1, "pergunta": "Qual tipo armazena textos em Python?",
     "alternativas": ["A) str", "B) bool", "C) int", "D) float"], "correta": 0,
     "explicacao": "O tipo str (string) é usado para armazenar textos.\nExemplo: nome = \"João\"",
     "dica": "Pense no tipo que usamos para armazenar nomes, palavras e frases.", "xp": 20},
    
    {"id": 2, "conteudo_id": 1, "pergunta": "Qual é o tipo de dado do valor  True  em Python?",
     "alternativas": ["A) str", "B) int", "C) bool", "D) float"], "correta": 2,
     "explicacao": "True e False são valores do tipo bool (booleano).\nRepresentam verdadeiro ou falso.",
     "dica": "Este tipo só aceita dois valores: True ou False.", "xp": 20},
    
    {"id": 3, "conteudo_id": 1, "pergunta": "Qual alternativa declara corretamente uma variável inteira?",
     "alternativas": ["A) x = 3.14", "B) x = \"10\"", "C) x = True", "D) x = 42"], "correta": 3,
     "explicacao": "O tipo int armazena números inteiros sem ponto decimal.\nExemplo: x = 42",
     "dica": "Inteiros não têm ponto decimal nem aspas.", "xp": 20},

    {"id": 4, "conteudo_id": 1, "pergunta": "O que retorna o comando  type(\"Olá\")  em Python?",
     "alternativas": ["A) int", "B) <class 'str'>", "C) string", "D) text"], "correta": 1,
     "explicacao": "type() retorna a classe do objeto.\nPara uma string, retorna <class 'str'>",
     "dica": "Use type() para verificar o tipo de qualquer variável.", "xp": 25},

    {"id": 5, "conteudo_id": 1, "pergunta": "Qual é o resultado de  len(\"Python\")  ?",
     "alternativas": ["A) 5", "B) 7", "C) 6", "D) 0"], "correta": 2,
     "explicacao": "len() retorna o comprimento (número de caracteres) de uma string.\n\"Python\" tem 6 caracteres: P-y-t-h-o-n",
     "dica": "Conte os caracteres na palavra.", "xp": 25},
    
    {"id": 6, "conteudo_id": 2, "pergunta": "Qual operador calcula o resto da divisão em Python?",
     "alternativas": ["A) //", "B) **", "C) %", "D) /"], "correta": 2,
     "explicacao": "O operador % retorna o resto de uma divisão.\nExemplo: 10 % 3 = 1",
     "dica": "Este operador é muito usado para verificar se um número é par ou ímpar.", "xp": 25},
    
    {"id": 7, "conteudo_id": 2, "pergunta": "Qual é o resultado de  2 ** 4  em Python?",
     "alternativas": ["A) 8", "B) 16", "C) 6", "D) 24"], "correta": 1,
     "explicacao": "O operador ** é de potenciação.\n2 ** 4 = 2 × 2 × 2 × 2 = 16",
     "dica": "O operador ** eleva o número à potência indicada.", "xp": 25},

    {"id": 8, "conteudo_id": 2, "pergunta": "Qual é o resultado de  10 / 3  em Python?",
     "alternativas": ["A) 3", "B) 3.0", "C) 3.333...", "D) 3.3333333333333335"], "correta": 3,
     "explicacao": "A divisão / retorna um float com a precisão completa.\n10 / 3 = 3.3333333333333335",
     "dica": "Use / para divisão normal e // para divisão inteira.", "xp": 30},

    {"id": 9, "conteudo_id": 2, "pergunta": "Se x = 5, qual é o resultado de  x += 3  ?",
     "alternativas": ["A) 8", "B) 5", "C) 15", "D) 53"], "correta": 0,
     "explicacao": "x += 3 é equivalente a x = x + 3\nSe x = 5, então x = 5 + 3 = 8",
     "dica": "+=, -=, *=, /= são operadores de atribuição composta.", "xp": 30},

    {"id": 10, "conteudo_id": 2, "pergunta": "Qual é o resultado de  \"Olá\" * 3  em Python?",
     "alternativas": ["A) \"OláOláOlá\"", "B) 9", "C) \"Olá3\"", "D) Erro"], "correta": 0,
     "explicacao": "O operador * repete uma string.\n\"Olá\" * 3 = \"OláOláOlá\"",
     "dica": "Você pode repetir strings multiplicando por um número inteiro.", "xp": 30},
    
    {"id": 11, "conteudo_id": 3, "pergunta": "Qual palavra-chave inicia uma condição em Python?",
     "alternativas": ["A) when", "B) case", "C) if", "D) check"], "correta": 2,
     "explicacao": "A palavra-chave if inicia uma estrutura condicional em Python.\nif condição:\n    # código",
     "dica": "É a mesma palavra em inglês que significa 'se'.", "xp": 20},
    
    {"id": 12, "conteudo_id": 3, "pergunta": "O que o operador  ==  verifica?",
     "alternativas": ["A) Atribuição", "B) Igualdade", "C) Diferença", "D) Maior que"], "correta": 1,
     "explicacao": "== verifica se dois valores são iguais.\nEx: 5 == 5 retorna True\n= é usado para atribuição!",
     "dica": "Não confunda com = (um sinal), que é atribuição.", "xp": 20},

    {"id": 13, "conteudo_id": 3, "pergunta": "Qual operador verifica se dois valores são DIFERENTES?",
     "alternativas": ["A) <>", "B) =/=", "C) !=", "D) ~="], "correta": 2,
     "explicacao": "!= verifica se dois valores são diferentes.\nEx: 5 != 3 retorna True",
     "dica": "O símbolo ! significa negação em muitas linguagens.", "xp": 25},

    {"id": 14, "conteudo_id": 3, "pergunta": "O que retorna a expressão  5 > 3 and 10 < 20  ?",
     "alternativas": ["A) True", "B) False", "C) None", "D) Erro"], "correta": 0,
     "explicacao": "5 > 3 é True E 10 < 20 é True\nTrue AND True = True",
     "dica": "and retorna True apenas se AMBAS as condições forem verdadeiras.", "xp": 30},

    {"id": 15, "conteudo_id": 3, "pergunta": "O que retorna  not True  em Python?",
     "alternativas": ["A) True", "B) False", "C) None", "D) not"], "correta": 1,
     "explicacao": "O operador not inverte o valor booleano.\nnot True = False\nnot False = True",
     "dica": "not é a negação lógica.", "xp": 25},

    {"id": 16, "conteudo_id": 3, "pergunta": "Qual é o resultado de  (5 > 3) or (10 < 5)  ?",
     "alternativas": ["A) True", "B) False", "C) None", "D) Erro"], "correta": 0,
     "explicacao": "5 > 3 é True E 10 < 5 é False\nTrue OR False = True\nor retorna True se PELO MENOS UMA condição for verdadeira.",
     "dica": "or é menos rigoroso que and.", "xp": 30},
    
    {"id": 17, "conteudo_id": 4, "pergunta": "Quantas vezes o loop  for i in range(4)  executa?",
     "alternativas": ["A) 3 vezes", "B) 5 vezes", "C) 4 vezes", "D) 0 vezes"], "correta": 2,
     "explicacao": "range(4) gera os valores 0, 1, 2, 3.\nPortanto o loop executa 4 vezes.",
     "dica": "range(n) começa em 0 e vai até n-1.", "xp": 25},
    
    {"id": 18, "conteudo_id": 4, "pergunta": "Qual comando interrompe um loop imediatamente?",
     "alternativas": ["A) stop", "B) exit", "C) continue", "D) break"], "correta": 3,
     "explicacao": "O comando break para o loop imediatamente.\ncontinue pula para a próxima iteração.",
     "dica": "Em inglês, significa 'quebrar' ou 'interromper'.", "xp": 25},

    {"id": 19, "conteudo_id": 4, "pergunta": "O que faz o comando  continue  dentro de um loop?",
     "alternativas": ["A) Para o loop", "B) Pula para a próxima iteração", "C) Reinicia o loop", "D) Retorna um valor"], "correta": 1,
     "explicacao": "continue pula o resto do código e vai para a próxima iteração do loop.",
     "dica": "Útil para pular iterações que não queremos processar.", "xp": 30},

    {"id": 20, "conteudo_id": 4, "pergunta": "Qual é o resultado de  for i in range(2, 5): print(i)  ?",
     "alternativas": ["A) 0 1 2 3 4", "B) 2 3 4", "C) 2 3 4 5", "D) 5"], "correta": 1,
     "explicacao": "range(2, 5) gera 2, 3, 4 (começa em 2 e vai até 4)\nExcluindo o 5!",
     "dica": "range(a, b) vai de a até b-1.", "xp": 30},

    {"id": 21, "conteudo_id": 4, "pergunta": "Qual comando repete enquanto uma condição for verdadeira?",
     "alternativas": ["A) for", "B) while", "C) loop", "D) repeat"], "correta": 1,
     "explicacao": "while repete enquanto uma condição for True.\nfor repete para cada item de uma sequência.",
     "dica": "while é para condições, for é para sequências.", "xp": 30},

    {"id": 22, "conteudo_id": 4, "pergunta": "Qual é o resultado deste código?\ni = 0\nwhile i < 3:\n    print(i)\n    i += 1",
     "alternativas": ["A) 0 1 2", "B) 0 1 2 3", "C) 1 2 3", "D) Loop infinito"], "correta": 0,
     "explicacao": "i começa em 0, imprime 0, depois i=1, imprime 1, depois i=2, imprime 2.\nQuando i=3, a condição é falsa e para.",
     "dica": "Sempre incremente a variável de controle para evitar loops infinitos.", "xp": 35},
    
    {"id": 23, "conteudo_id": 5, "pergunta": "Qual palavra-chave define uma função em Python?",
     "alternativas": ["A) func", "B) function", "C) def", "D) fun"], "correta": 2,
     "explicacao": "A palavra-chave def define uma função em Python.\nExemplo:\ndef minha_funcao():\n    pass",
     "dica": "É uma abreviação de 'define'.", "xp": 20},

    {"id": 24, "conteudo_id": 5, "pergunta": "O que o comando  return  faz em uma função?",
     "alternativas": ["A) Para a função", "B) Retorna um valor", "C) Reinicia a função", "D) Imprime na tela"], "correta": 1,
     "explicacao": "return retorna um valor da função e encerra sua execução.\nSem return, a função retorna None.",
     "dica": "Funções que fazem cálculos devem usar return.", "xp": 25},

    {"id": 25, "conteudo_id": 5, "pergunta": "Qual é o resultado de chamar  len(\"Python\")  ?",
     "alternativas": ["A) Uma função", "B) O número 6", "C) Uma string", "D) Erro"], "correta": 1,
     "explicacao": "len() é uma função built-in que retorna o comprimento.\nlen(\"Python\") = 6",
     "dica": "len() é uma função, não uma variável.", "xp": 25},

    {"id": 26, "conteudo_id": 5, "pergunta": "Se definimos  def soma(a, b):\\n    return a + b  qual é  soma(3, 5)  ?",
     "alternativas": ["A) \"3 5\"", "B) 8", "C) 35", "D) Erro"], "correta": 1,
     "explicacao": "A função soma retorna a + b.\nsoma(3, 5) = 3 + 5 = 8",
     "dica": "Os parâmetros a e b recebem os valores 3 e 5.", "xp": 30},

    {"id": 27, "conteudo_id": 5, "pergunta": "Qual é a diferença entre  parâmetros  e  argumentos  ?",
     "alternativas": ["A) Não há diferença", "B) Parâmetros são na definição, argumentos na chamada", "C) Argumentos são sempre strings", "D) Parâmetros retornam valores"], "correta": 1,
     "explicacao": "Parâmetros: variáveis na definição da função\nArgumentos: valores passados na chamada da função\nExemplo: def func(x):  ← x é parâmetro\nfunc(5)  ← 5 é argumento",
     "dica": "Memorize: Parâmetros = Definição, Argumentos = Chamada.", "xp": 35},

    {"id": 28, "conteudo_id": 5, "pergunta": "O que retorna uma função sem comando return?",
     "alternativas": ["A) 0", "B) \"\"", "C) None", "D) Erro"], "correta": 2,
     "explicacao": "Se uma função não tem return ou chega ao final sem retornar,\nela retorna None por padrão.",
     "dica": "None é o valor padrão em Python.", "xp": 30},
    
    {"id": 29, "conteudo_id": 6, "pergunta": "Como adicionar um elemento ao final de uma lista?",
     "alternativas": ["A) lista.add(x)", "B) lista.insert(x)", "C) lista.append(x)", "D) lista.push(x)"], "correta": 2,
     "explicacao": "O método append() adiciona um elemento ao final da lista.\nExemplo: frutas.append(\"manga\")",
     "dica": "Em inglês, 'append' significa 'acrescentar ao final'.", "xp": 25},
    
    {"id": 30, "conteudo_id": 6, "pergunta": "Qual é o índice do primeiro elemento de uma lista?",
     "alternativas": ["A) 1", "B) -1", "C) 0", "D) None"], "correta": 2,
     "explicacao": "Em Python (e na maioria das linguagens), listas começam no índice 0.\nlista[0] → primeiro elemento",
     "dica": "Programação geralmente começa a contar do zero!", "xp": 20},

    {"id": 31, "conteudo_id": 6, "pergunta": "Se  lista = [1, 2, 3, 4, 5]  qual é  lista[-1]  ?",
     "alternativas": ["A) 1", "B) 5", "C) -1", "D) Erro"], "correta": 1,
     "explicacao": "Índices negativos contam de trás para frente.\nlista[-1] = último elemento = 5",
     "dica": "lista[-2] seria o penúltimo, lista[-3] o antepenúltimo, etc.", "xp": 30},

    {"id": 32, "conteudo_id": 6, "pergunta": "Se  lista = [10, 20, 30, 40]  qual é  lista[1:3]  ?",
     "alternativas": ["A) [20]", "B) [20, 30]", "C) [20, 30, 40]", "D) [10, 20]"], "correta": 1,
     "explicacao": "lista[1:3] retorna elementos do índice 1 até 2 (o 3 é excluído).\nlista[1:3] = [20, 30]",
     "dica": "Slicing: começa no índice da esquerda, termina ANTES do índice da direita.", "xp": 35},

    {"id": 33, "conteudo_id": 6, "pergunta": "O que faz o método  lista.remove(x)  ?",
     "alternativas": ["A) Remove o primeiro x da lista", "B) Remove o último elemento", "C) Remove o índice x", "D) Limpa toda a lista"], "correta": 0,
     "explicacao": "remove(x) remove o PRIMEIRO valor x encontrado.\nSe x não existir, gera erro!",
     "dica": "Use del lista[i] para remover por índice.", "xp": 30},

    {"id": 34, "conteudo_id": 6, "pergunta": "Qual método retorna o índice de um elemento em uma lista?",
     "alternativas": ["A) lista.find(x)", "B) lista.index(x)", "C) lista.get(x)", "D) lista.search(x)"], "correta": 1,
     "explicacao": "lista.index(x) retorna o índice do primeiro x encontrado.\nSe x não existir, gera ValueError!",
     "dica": "Combine com try/except para evitar erros.", "xp": 35},

    {"id": 35, "conteudo_id": 6, "pergunta": "Se  lista = [3, 1, 4, 1, 5]  qual é  lista.count(1)  ?",
     "alternativas": ["A) 1", "B) 2", "C) 3", "D) False"], "correta": 1,
     "explicacao": "count(x) retorna quantas vezes x aparece na lista.\nO número 1 aparece 2 vezes: [3, 1, 4, 1, 5]",
     "dica": "Útil para contar ocorrências de um elemento.", "xp": 35},
]

EXERCICIOS_DIGITACAO = [
    #CATEGORIA 1: VARIÁVEIS E TIPOS
    {"id": 1, "titulo": "Olá, Mundo!", "descricao": "Digite exatamente o código abaixo para imprimir uma mensagem",
     "codigo": 'print("Olá, Mundo!")', "dica": "Use aspas duplas e parênteses", "xp": 30, "categoria": "Variáveis e Tipos"},
    
    {"id": 2, "titulo": "Variáveis simples", "descricao": "Digite o código para criar variáveis",
     "codigo": "nome = \"João\"\nidade = 18", "dica": "Lembre-se de usar = para atribuição", "xp": 30, "categoria": "Variáveis e Tipos"},
    
    {"id": 3, "titulo": "Tipos diferentes", "descricao": "Digite o código com diferentes tipos de dados",
     "codigo": "texto = \"Python\"\nnumero = 42\ndecimal = 3.14\nbooleano = True", "dica": "Combine str, int, float e bool", "xp": 40, "categoria": "Variáveis e Tipos"},

    {"id": 4, "titulo": "Verificar tipo", "descricao": "Digite o código para verificar o tipo de uma variável",
     "codigo": "valor = 100\nprint(type(valor))", "dica": "Use type() para descobrir o tipo", "xp": 35, "categoria": "Variáveis e Tipos"},

    {"id": 5, "titulo": "Conversão de tipos", "descricao": "Digite o código para converter string em número",
     "codigo": "numero_texto = \"123\"\nnumero = int(numero_texto)\nprint(numero)", "dica": "Use int() para converter string para inteiro", "xp": 45, "categoria": "Variáveis e Tipos"},

    #CATEGORIA 2: OPERAÇÕES BÁSICAS
    {"id": 6, "titulo": "Operação matemática", "descricao": "Digite o código para fazer uma soma",
     "codigo": "resultado = 10 + 5\nprint(resultado)", "dica": "A variável resultado armazena o valor", "xp": 40, "categoria": "Operações Básicas"},
    
    {"id": 7, "titulo": "Quatro operações", "descricao": "Digite o código com as quatro operações básicas",
     "codigo": "a = 20\nb = 5\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)", "dica": "Use +, -, *, /", "xp": 50, "categoria": "Operações Básicas"},

    {"id": 8, "titulo": "Operadores especiais", "descricao": "Digite o código com divisão inteira e resto",
     "codigo": "numero = 10\nprint(numero // 3)\nprint(numero % 3)", "dica": "// é divisão inteira, % é resto", "xp": 45, "categoria": "Operações Básicas"},

    {"id": 9, "titulo": "Potência", "descricao": "Digite o código para calcular potência",
     "codigo": "base = 2\nexpoente = 8\nprint(base ** expoente)", "dica": "Use ** para potência", "xp": 40, "categoria": "Operações Básicas"},

    {"id": 10, "titulo": "Operadores compostos", "descricao": "Digite o código com atribuição composta",
     "codigo": "x = 10\nx += 5\nx -= 3\nx *= 2\nprint(x)", "dica": "+=, -=, *= são operadores compostos", "xp": 50, "categoria": "Operações Básicas"},

    #CATEGORIA 3: CONDICIONAIS
    {"id": 11, "titulo": "Condicional simples", "descricao": "Digite o código com if simples",
     "codigo": "idade = 18\nif idade >= 18:\n    print(\"Maior de idade\")", "dica": "Respeite a indentação de 4 espaços", "xp": 50, "categoria": "Condicionais"},

    {"id": 12, "titulo": "If-else", "descricao": "Digite o código com if e else",
     "codigo": "numero = 7\nif numero % 2 == 0:\n    print(\"Par\")\nelse:\n    print(\"Ímpar\")", "dica": "Use else para a condição falsa", "xp": 55, "categoria": "Condicionais"},

    {"id": 13, "titulo": "If-elif-else", "descricao": "Digite o código com múltiplas condições",
     "codigo": "nota = 7\nif nota >= 9:\n    print(\"Excelente\")\nelif nota >= 7:\n    print(\"Bom\")\nelse:\n    print(\"Ruim\")", "dica": "Use elif para outras condições", "xp": 60, "categoria": "Condicionais"},

    {"id": 14, "titulo": "Operadores lógicos", "descricao": "Digite o código com and, or, not",
     "codigo": "idade = 25\ntem_carteira = True\nif idade >= 18 and tem_carteira:\n    print(\"Pode dirigir\")", "dica": "Use and, or, not para lógica booleana", "xp": 60, "categoria": "Condicionais"},

    {"id": 15, "titulo": "Comparações", "descricao": "Digite o código com diferentes comparações",
     "codigo": "a = 10\nb = 5\nprint(a > b)\nprint(a == b)\nprint(a != b)", "dica": "Use >, <, ==, !=, >=, <=", "xp": 50, "categoria": "Condicionais"},

    #CATEGORIA 4: LOOPS
    {"id": 16, "titulo": "Loop for", "descricao": "Digite o código para um loop simples",
     "codigo": "for i in range(5):\n    print(i)", "dica": "Não esqueça da indentação (4 espaços)", "xp": 45, "categoria": "Loops"},

    {"id": 17, "titulo": "For com intervalo", "descricao": "Digite o código com range customizado",
     "codigo": "for i in range(2, 7):\n    print(i)", "dica": "range(inicio, fim) vai de inicio até fim-1", "xp": 50, "categoria": "Loops"},

    {"id": 18, "titulo": "While", "descricao": "Digite o código com loop while",
     "codigo": "contador = 0\nwhile contador < 3:\n    print(contador)\n    contador += 1", "dica": "Sempre incremente para evitar loop infinito", "xp": 55, "categoria": "Loops"},

    {"id": 19, "titulo": "Break e continue", "descricao": "Digite o código com break e continue",
     "codigo": "for i in range(10):\n    if i == 3:\n        continue\n    if i == 7:\n        break\n    print(i)", "dica": "break para, continue pula", "xp": 60, "categoria": "Loops"},

    {"id": 20, "titulo": "For em lista", "descricao": "Digite o código para iterar sobre uma lista",
     "codigo": "frutas = [\"maçã\", \"banana\", \"uva\"]\nfor fruta in frutas:\n    print(fruta)", "dica": "Use for para percorrer listas", "xp": 50, "categoria": "Loops"},

    # CATEGORIA 5: FUNÇÕES
    {"id": 21, "titulo": "Função básica", "descricao": "Digite o código para definir uma função simples",
     "codigo": "def saudacao():\n    print(\"Olá!\")\n\nsaudacao()", "dica": "Use def para definir, depois chame com ()", "xp": 50, "categoria": "Funções"},

    {"id": 22, "titulo": "Função com parâmetro", "descricao": "Digite o código de função com um parâmetro",
     "codigo": "def saudacao(nome):\n    print(f\"Olá, {nome}!\")\n\nsaudacao(\"João\")", "dica": "Use f-string para inserir variáveis", "xp": 55, "categoria": "Funções"},

    {"id": 23, "titulo": "Função com retorno", "descricao": "Digite o código de função que retorna valor",
     "codigo": "def soma(a, b):\n    return a + b\n\nresultado = soma(5, 3)\nprint(resultado)", "dica": "Use return para retornar um valor", "xp": 55, "categoria": "Funções"},

    {"id": 24, "titulo": "Múltiplos parâmetros", "descricao": "Digite o código de função com vários parâmetros",
     "codigo": "def calcular(a, b, operacao):\n    if operacao == \"+\":\n        return a + b\n    elif operacao == \"-\":\n        return a - b\n\nprint(calcular(10, 5, \"+\"))", "dica": "Funções podem ter múltiplos parâmetros", "xp": 65, "categoria": "Funções"},

    {"id": 25, "titulo": "Duas funções", "descricao": "Digite o código com duas funções diferentes",
     "codigo": "def fahrenheit(celsius):\n    return 1.8 * celsius + 32\n\ndef kelvin(celsius):\n    return celsius + 273.15\n\nprint(fahrenheit(0))\nprint(kelvin(0))", "dica": "Combine múltiplas funções", "xp": 65, "categoria": "Funções"},

    # CATEGORIA 6: LISTAS
    {"id": 26, "titulo": "Criar lista", "descricao": "Digite o código para criar uma lista",
     "codigo": "frutas = [\"maçã\", \"banana\", \"uva\"]\nprint(frutas)", "dica": "Use colchetes [] para listas", "xp": 35, "categoria": "Listas"},

    {"id": 27, "titulo": "Acessar elementos", "descricao": "Digite o código para acessar elementos da lista",
     "codigo": "numeros = [10, 20, 30, 40]\nprint(numeros[0])\nprint(numeros[2])\nprint(numeros[-1])", "dica": "Índices começam em 0, -1 é o último", "xp": 45, "categoria": "Listas"},

    {"id": 28, "titulo": "Adicionar elementos", "descricao": "Digite o código para adicionar elementos",
     "codigo": "lista = [1, 2, 3]\nlista.append(4)\nprint(lista)", "dica": "Use append() para adicionar ao final", "xp": 40, "categoria": "Listas"},

    {"id": 29, "titulo": "Remover elementos", "descricao": "Digite o código para remover elementos",
     "codigo": "lista = [1, 2, 3, 4, 5]\nlista.remove(3)\nprint(lista)", "dica": "Use remove() para remover um valor", "xp": 45, "categoria": "Listas"},

    {"id": 30, "titulo": "Slicing", "descricao": "Digite o código para fatiar uma lista",
     "codigo": "numeros = [10, 20, 30, 40, 50]\nprint(numeros[1:4])\nprint(numeros[:3])\nprint(numeros[2:])", "dica": "Use [inicio:fim] para fatiar", "xp": 55, "categoria": "Listas"},

    {"id": 31, "titulo": "Tamanho e índice", "descricao": "Digite o código para usar len() e index()",
     "codigo": "lista = [\"a\", \"b\", \"c\", \"d\"]\nprint(len(lista))\nprint(lista.index(\"c\"))", "dica": "len() retorna tamanho, index() retorna posição", "xp": 50, "categoria": "Listas"},

    {"id": 32, "titulo": "Ordenar lista", "descricao": "Digite o código para ordenar uma lista",
     "codigo": "numeros = [5, 2, 8, 1, 9]\nnumeros.sort()\nprint(numeros)", "dica": "Use sort() para ordenar", "xp": 45, "categoria": "Listas"},
]

DESAFIOS = [
    {"id": 1, "titulo": "Número Pari ou Ímpar", "icone": "🔢", "dificuldade": "Fácil",
     "descricao": "Crie um programa que verifica se um número é par ou ímpar",
     "objetivo": "Use um if/else e o operador %",
     "dica": "Se número % 2 == 0, é par!", "xp": 50},
    
    {"id": 2, "titulo": "Maior de Três", "icone": "📊", "dificuldade": "Fácil",
     "descricao": "Encontre o maior entre 3 números",
     "objetivo": "Use if/elif/else para comparar valores",
     "dica": "Compare os números com > e ==", "xp": 50},
    
    {"id": 3, "titulo": "Tabuada", "icone": "📐", "dificuldade": "Médio",
     "descricao": "Crie uma tabuada de um número",
     "objetivo": "Use um loop for de 1 a 10",
     "dica": "for i in range(1, 11): print(numero * i)", "xp": 75},
    
    {"id": 4, "titulo": "Soma de Lista", "icone": "➕", "dificuldade": "Médio",
     "descricao": "Calcule a soma de todos os números em uma lista",
     "objetivo": "Use um loop for para iterar",
     "dica": "Crie uma variável total e vá adicionando", "xp": 75},
    
    {"id": 5, "titulo": "Contador de Repetição", "icone": "🔄", "dificuldade": "Médio",
     "descricao": "Conte quantas vezes um número aparece em uma lista",
     "objetivo": "Use count() ou um loop com if",
     "dica": "Use lista.count(numero) ou for com comparação", "xp": 75},
    
    {"id": 6, "titulo": "Reverter Lista", "icone": "🔀", "dificuldade": "Médio",
     "descricao": "Inverta a ordem dos elementos de uma lista",
     "objetivo": "Use slicing ou o método reverse()",
     "dica": "lista[::-1] inverte em uma linha!", "xp": 75},
    
    {"id": 7, "titulo": "Fibonacci", "icone": "🌀", "dificuldade": "Difícil",
     "descricao": "Gere uma sequência de Fibonacci até 50",
     "objetivo": "Use um loop while e armazene em uma lista",
     "dica": "Próximo = anterior1 + anterior2", "xp": 100},
    
    {"id": 8, "titulo": "Palíndromo", "icone": "🔍", "dificuldade": "Difícil",
     "descricao": "Verifique se uma palavra é palíndromo",
     "objetivo": "Compare a palavra com seu reverso",
     "dica": "palavra == palavra[::-1]", "xp": 100},
    
    {"id": 9, "titulo": "Fatorial", "icone": "❗", "dificuldade": "Difícil",
     "descricao": "Calcule o fatorial de um número",
     "objetivo": "Use um loop for ou uma função recursiva",
     "dica": "5! = 5 × 4 × 3 × 2 × 1 = 120", "xp": 100},
    
    {"id": 10, "titulo": "Remover Duplicatas", "icone": "🗂️", "dificuldade": "Difícil",
     "descricao": "Remova números duplicados de uma lista",
     "objetivo": "Use um set() ou um loop com if",
     "dica": "set(lista) remove duplicatas automaticamente!", "xp": 100},
]

CONQUISTAS_DEF = [
    {"id": 1, "nome": "Primeiros Passos", "icone": "⭐", "descricao": "Complete seu primeiro exercício", "meta": 1, "tipo": "exercicios", "cor": CORES["amarelo"]},
    {"id": 2, "nome": "Estudioso", "icone": "📚", "descricao": "Estude 3 conteúdos", "meta": 3, "tipo": "conteudos", "cor": CORES["azul"]},
    {"id": 3, "nome": "Praticante", "icone": "🏆", "descricao": "Responda 10 exercícios", "meta": 10, "tipo": "exercicios", "cor": CORES["verde"]},
    {"id": 4, "nome": "Persistente", "icone": "🛡️", "descricao": "Estude 7 dias seguidos", "meta": 7, "tipo": "dias", "cor": CORES["roxo"]},
    {"id": 5, "nome": "Campeão", "icone": "🥇", "descricao": "Complete todos os exercícios", "meta": 35, "tipo": "exercicios", "cor": CORES["laranja"]},
    {"id": 6, "nome": "Mestre Python", "icone": "🐍", "descricao": "Chegue ao nível 10", "meta": 10, "tipo": "nivel", "cor": CORES["roxo"]},
    {"id": 7, "nome": "Expert", "icone": "💎", "descricao": "Complete a trilha completa", "meta": 6, "tipo": "conteudos", "cor": CORES["azul_claro"]},
    {"id": 8, "nome": "Lenda Python", "icone": "👑", "descricao": "Alcance 1000 XP", "meta": 1000, "tipo": "xp", "cor": CORES["amarelo"]},
    {"id": 9, "nome": "Desafiador", "icone": "⚔️", "descricao": "Complete 5 desafios", "meta": 5, "tipo": "desafios", "cor": CORES["laranja"]},
]

XP_POR_NIVEL = 500
ARQUIVO_DADOS = "pytutor_dados.json"

# randomiza a posicao dos exercicios (
def embaralhar_exercicios():
    """Embaralha as alternativas dos exercícios e randomiza a ordem"""
    # Embaralha alternativas de cada exercício
    for ex in EXERCICIOS:
        alternativas = ex["alternativas"][:]
        resposta_correta = ex["alternativas"][ex["correta"]]
        random.shuffle(alternativas)
        ex["alternativas"] = alternativas
        ex["correta"] = alternativas.index(resposta_correta)
    
    # Randomiza a ordem dos exercícios

    random.shuffle(EXERCICIOS)


class DadosUsuario:
    def __init__(self):
        self.nome = "Aluno"
        self.xp = 0
        self.nivel = 1
        self.exercicios_feitos = []
        self.conteudos_vistos = []
        self.desafios_feitos = []
        self.atividade_recente = []
        self.carregar()

    def carregar(self):
        if os.path.exists(ARQUIVO_DADOS):
            try:
                with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                    d = json.load(f)
                    self.nome = d.get("nome", "Aluno")
                    self.xp = d.get("xp", 0)
                    self.nivel = d.get("nivel", 1)
                    self.exercicios_feitos = d.get("exercicios_feitos", [])
                    self.conteudos_vistos = d.get("conteudos_vistos", [])
                    self.desafios_feitos = d.get("desafios_feitos", [])
                    self.atividade_recente = d.get("atividade_recente", [])
            except Exception:
                pass

    def salvar(self):
        dados = {
            "nome": self.nome,
            "xp": self.xp,
            "nivel": self.nivel,
            "exercicios_feitos": self.exercicios_feitos,
            "conteudos_vistos": self.conteudos_vistos,
            "desafios_feitos": self.desafios_feitos,
            "atividade_recente": self.atividade_recente,
        }
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

    def ganhar_xp(self, quantidade, descricao):
        self.xp += quantidade
        if self.xp >= self.nivel * XP_POR_NIVEL:
            self.nivel += 1
        self.atividade_recente.insert(0, {
            "descricao": descricao,
            "xp": quantidade,
            "data": datetime.now().strftime("%d/%m/%Y")
        })
        if len(self.atividade_recente) > 10:
            self.atividade_recente.pop()
        self.salvar()

    def marcar_conteudo(self, conteudo_id):
        if conteudo_id not in self.conteudos_vistos:
            self.conteudos_vistos.append(conteudo_id)
            nome = self._obter_nome_conteudo(conteudo_id)
            self.ganhar_xp(10, f"Iniciou o conteúdo: {nome}")

    def marcar_exercicio(self, exercicio_id, xp):
        if exercicio_id not in self.exercicios_feitos:
            self.exercicios_feitos.append(exercicio_id)
            ex = next((e for e in EXERCICIOS if e["id"] == exercicio_id), None)
            nome = ex["pergunta"][:35] + "..." if ex else f"Exercício {exercicio_id}"
            self.ganhar_xp(xp, f"Respondeu exercício: {nome}")

    def marcar_digitacao(self, exercicio_id, xp):
        if exercicio_id not in self.exercicios_feitos:
            self.exercicios_feitos.append(exercicio_id)
            ex = next((e for e in EXERCICIOS_DIGITACAO if e["id"] == exercicio_id), None)
            nome = ex["titulo"] if ex else f"Digitação {exercicio_id}"
            self.ganhar_xp(xp, f"Completou digitação: {nome}")

    def marcar_desafio(self, desafio_id, xp):
        if desafio_id not in self.desafios_feitos:
            self.desafios_feitos.append(desafio_id)
            des = next((d for d in DESAFIOS if d["id"] == desafio_id), None)
            nome = des["titulo"] if des else f"Desafio {desafio_id}"
            self.ganhar_xp(xp, f"Completou desafio: {nome}")

    def _obter_nome_conteudo(self, cid):
        c = next((c for c in CONTEUDOS if c["id"] == cid), None)
        return c["titulo"] if c else f"Conteúdo {cid}"

    def progresso_conteudo(self, conteudo_id):
        exs = [e for e in EXERCICIOS if e["conteudo_id"] == conteudo_id]
        if not exs:
            return 0
        feitos = sum(1 for e in exs if e["id"] in self.exercicios_feitos)
        return int(feitos / len(exs) * 100)

    def progresso_geral(self):
        total = len(EXERCICIOS) + len(EXERCICIOS_DIGITACAO)
        feitos = len(self.exercicios_feitos)
        return int(feitos / total * 100) if total > 0 else 0

    def conquistas_desbloqueadas(self):
        resultado = []
        for c in CONQUISTAS_DEF:
            if c["tipo"] == "exercicios":
                progresso = len(self.exercicios_feitos)
            elif c["tipo"] == "conteudos":
                progresso = len(self.conteudos_vistos)
            elif c["tipo"] == "nivel":
                progresso = self.nivel
            elif c["tipo"] == "xp":
                progresso = self.xp
            elif c["tipo"] == "desafios":
                progresso = len(self.desafios_feitos)
            else:
                progresso = 0
            desbloqueada = progresso >= c["meta"]
            resultado.append((c, progresso, desbloqueada))
        return resultado

    @property
    def xp_nivel_atual(self):
        return (self.nivel - 1) * XP_POR_NIVEL

    @property
    def xp_proximo_nivel(self):
        return self.nivel * XP_POR_NIVEL

    @property
    def xp_no_nivel(self):
        return self.xp - self.xp_nivel_atual

    @property
    def xp_falta(self):
        return self.xp_proximo_nivel - self.xp_nivel_atual

    @property
    def nivel_nome(self):
        nomes = {1: "Iniciante", 2: "Aprendiz", 3: "Desenvolvedor",
                 4: "Avançado", 5: "Expert", 10: "Mestre Python"}
        return nomes.get(self.nivel, f"Nível {self.nivel}")


def criar_card(parent, **kwargs):
    return ctk.CTkFrame(parent, fg_color=CORES["bg_card"],
                        corner_radius=12, border_width=1,
                        border_color=CORES["borda"], **kwargs)


def criar_label(parent, text, size=13, weight="normal", color=None, **kwargs):
    return ctk.CTkLabel(parent, text=text,
                        font=("Segoe UI", size, weight),
                        text_color=color or CORES["texto"], **kwargs)


def criar_botao(parent, text, height=36, cor=None, **kwargs):
    return ctk.CTkButton(parent, text=text, height=height,
                        fg_color=cor or CORES["azul"],
                        hover_color=CORES["azul_claro"],
                        font=("Segoe UI", 12, "bold"), **kwargs)


class PyTutor(ctk.CTk):
    def __init__(self):
        super().__init__()
        embaralhar_exercicios()
        self.dados = DadosUsuario()
        self.tela_atual = None
        self.exercicio_index = 0
        self.exercicios_sessao = []
        self.resp_selecionada = -1

        self.title("PyTutor – Aprenda Python do Zero ao Avançado")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.configure(fg_color=CORES["bg_principal"])

        self._build_layout()
        self._mostrar_inicio()

    def _build_layout(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, fg_color=CORES["bg_sidebar"],
                                    width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self._build_sidebar()

        self.area = ctk.CTkFrame(self, fg_color=CORES["bg_principal"], corner_radius=0)
        self.area.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.area.grid_columnconfigure(0, weight=1)
        self.area.grid_rowconfigure(0, weight=1)

    def _build_sidebar(self):
        sb = self.sidebar
        
        logo_f = ctk.CTkFrame(sb, fg_color="transparent")
        logo_f.pack(fill="x", padx=16, pady=(20, 4))
        criar_label(logo_f, "PyTutor", 22, "bold").pack(anchor="w")
        criar_label(logo_f, "Aprenda Python do Zero ao Avançado",
                   9, color=CORES["texto_sub"], wraplength=160, justify="left").pack(anchor="w")

        ctk.CTkFrame(sb, fg_color=CORES["borda"], height=1).pack(fill="x", padx=16, pady=12)

        itens = [
            ("🏠", "Início", self._mostrar_inicio),
            ("📚", "Conteúdos", self._mostrar_conteudos),
            ("✏️", "Exercícios", self._mostrar_exercicios_menu),
            ("⚔️", "Desafios", self._mostrar_desafios),
            ("📊", "Progresso", self._mostrar_progresso),
            ("🏆", "Conquistas", self._mostrar_conquistas),
            ("⚙️", "Configurações", self._mostrar_config),
        ]
        self.btns_nav = {}
        for icone, nome, cmd in itens:
            btn = ctk.CTkButton(sb, text=f"  {icone}  {nome}", anchor="w",
                              fg_color="transparent", hover_color=CORES["bg_card"],
                              text_color=CORES["texto_sub"], font=("Segoe UI", 13),
                              height=40, corner_radius=8,
                              command=lambda c=cmd, n=nome: self._nav(n, c))
            btn.pack(fill="x", padx=10, pady=2)
            self.btns_nav[nome] = btn

        ctk.CTkFrame(sb, fg_color="transparent").pack(fill="both", expand=True)
        ctk.CTkFrame(sb, fg_color=CORES["borda"], height=1).pack(fill="x", padx=16, pady=8)

        self.perfil_frame = ctk.CTkFrame(sb, fg_color="transparent")
        self.perfil_frame.pack(fill="x", padx=12, pady=(0, 16))
        self._atualizar_perfil()

    def _atualizar_perfil(self):
        for w in self.perfil_frame.winfo_children():
            w.destroy()
        d = self.dados
        row = ctk.CTkFrame(self.perfil_frame, fg_color="transparent")
        row.pack(fill="x")
        ctk.CTkLabel(row, text="👤", font=("Segoe UI", 24)).pack(side="left", padx=(0, 8))
        col = ctk.CTkFrame(row, fg_color="transparent")
        col.pack(side="left", fill="x", expand=True)
        criar_label(col, d.nome, 12, "bold").pack(anchor="w")
        criar_label(col, f"Nível {d.nivel} - {d.nivel_nome}", 10, color=CORES["texto_sub"]).pack(anchor="w")
        
        pct = d.xp_no_nivel / d.xp_falta if d.xp_falta > 0 else 1
        xp_bg = ctk.CTkFrame(self.perfil_frame, fg_color=CORES["bg_card2"], height=6, corner_radius=3)
        xp_bg.pack(fill="x", pady=(4, 2))
        xp_fill = ctk.CTkFrame(self.perfil_frame, fg_color=CORES["verde"], height=6, corner_radius=3)
        xp_fill.place(in_=xp_bg, relx=0, rely=0, relwidth=min(pct, 1.0), relheight=1)
        criar_label(self.perfil_frame, f"⚡ XP {d.xp} / {d.xp_proximo_nivel}", 10,
                  color=CORES["amarelo"]).pack(anchor="w")

    def _nav(self, nome, cmd):
        for n, b in self.btns_nav.items():
            b.configure(
                fg_color=CORES["azul"] if n == nome else "transparent",
                text_color=CORES["texto"] if n == nome else CORES["texto_sub"]
            )
        cmd()

    def _limpar_area(self):
        for w in self.area.winfo_children():
            w.destroy()
        self.tela_atual = None

    def _scroll_area(self):
        scroll = ctk.CTkScrollableFrame(self.area, fg_color="transparent",
                                        scrollbar_button_color=CORES["bg_card2"])
        scroll.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        scroll.grid_columnconfigure(0, weight=1)
        return scroll

    def _mostrar_inicio(self):
        self._limpar_area()
        self._nav("Início", lambda: None)
        d = self.dados
        scroll = self._scroll_area()

        criar_label(scroll, f"Bem-vindo ao PyTutor! 👋", 22, "bold").grid(
            row=0, column=0, sticky="w", padx=24, pady=(20, 0))
        criar_label(scroll, "Vamos começar sua jornada no Python de forma simples, prática e divertida!",
                   13, color=CORES["texto_sub"]).grid(row=1, column=0, sticky="w", padx=24, pady=(4, 12))

        row1 = ctk.CTkFrame(scroll, fg_color="transparent")
        row1.grid(row=2, column=0, sticky="ew", padx=24, pady=12)
        row1.grid_columnconfigure((0, 1), weight=1)

        card_cont = criar_card(row1)
        card_cont.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        criar_label(card_cont, "Continue aprendendo", 13, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        
        prox = next((c for c in CONTEUDOS if c["id"] not in d.conteudos_vistos), CONTEUDOS[0])
        pct = d.progresso_conteudo(prox["id"])
        row_c = ctk.CTkFrame(card_cont, fg_color="transparent")
        row_c.pack(fill="x", padx=16, pady=4)
        criar_label(row_c, f"{prox['icone']} {prox['titulo']}", 13).pack(side="left")
        criar_label(row_c, f"{pct}%", 11, color=CORES["texto_sub"]).pack(side="right")
        
        bar = ctk.CTkProgressBar(card_cont, height=8, corner_radius=4,
                                fg_color=CORES["bg_card2"], progress_color=CORES["verde"])
        bar.set(pct / 100)
        bar.pack(fill="x", padx=16, pady=(2, 4))
        
        criar_botao(card_cont, "Continuar", 36,
                   command=lambda c=prox: self._abrir_conteudo(c)).pack(fill="x", padx=16, pady=(4, 14))

        card_obj = criar_card(row1)
        card_obj.grid(row=0, column=1, sticky="ew", padx=(8, 0))
        criar_label(card_obj, "Próximo objetivo", 13, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        falta = 3 - (len(d.exercicios_feitos) % 3)
        criar_label(card_obj, "🏆", 32).pack(pady=(8, 4))
        criar_label(card_obj, f"Complete {falta} exercício(s)\npara ganhar 50 XP",
                   12, color=CORES["texto_sub"]).pack(padx=16, pady=(0, 4))
        prog_ex = (3 - falta) / 3
        bar2 = ctk.CTkProgressBar(card_obj, height=8, corner_radius=4,
                                 fg_color=CORES["bg_card2"], progress_color=CORES["amarelo"])
        bar2.set(prog_ex)
        bar2.pack(fill="x", padx=16, pady=(2, 14))

        card_trilha = criar_card(scroll)
        card_trilha.grid(row=3, column=0, sticky="ew", padx=24, pady=6)
        criar_label(card_trilha, "Trilha de aprendizado", 13, "bold").pack(anchor="w", padx=16, pady=(14, 10))
        row_tr = ctk.CTkFrame(card_trilha, fg_color="transparent")
        row_tr.pack(fill="x", padx=16, pady=(0, 14))
        for i, c in enumerate(CONTEUDOS):
            feito = d.progresso_conteudo(c["id"]) >= 100
            ativo = c["id"] == prox["id"]
            cor_bg = CORES["azul"] if ativo else (CORES["verde_escuro"] if feito else CORES["bg_card2"])
            cor_tx = CORES["texto"] if (ativo or feito) else CORES["texto_sub"]
            step = ctk.CTkFrame(row_tr, fg_color="transparent")
            step.pack(side="left", padx=8)
            criar_botao(step, str(i + 1), 42, cor_bg,
                       width=42, command=lambda c=c: self._abrir_conteudo(c)).pack()
            criar_label(step, c["titulo"], 9, color=cor_tx).pack(pady=(4, 0))

        card_dica = criar_card(scroll)
        card_dica.grid(row=4, column=0, sticky="ew", padx=24, pady=(6, 20))
        row_d = ctk.CTkFrame(card_dica, fg_color="transparent")
        row_d.pack(fill="x", padx=16, pady=14)
        criar_label(row_d, "⭐ Dica do dia", 13, "bold").pack(side="left")
        criar_label(row_d, "</>", 12, color=CORES["texto_sub"]).pack(side="right")
        criar_label(card_dica, "Praticar todos os dias é o segredo para se tornar um grande desenvolvedor!",
                   12, color=CORES["texto_sub"]).pack(anchor="w", padx=16, pady=(0, 14))

        self._atualizar_perfil()

    def _mostrar_conteudos(self):
        self._limpar_area()
        self._nav("Conteúdos", lambda: None)
        scroll = self._scroll_area()

        criar_label(scroll, "📚  Conteúdos", 20, "bold").grid(
            row=0, column=0, sticky="w", padx=24, pady=(20, 4))
        criar_label(scroll, "Selecione um conteúdo para estudar",
                   13, color=CORES["texto_sub"]).grid(row=1, column=0, sticky="w", padx=24, pady=(0, 12))

        for i, c in enumerate(CONTEUDOS):
            pct = self.dados.progresso_conteudo(c["id"])
            card = criar_card(scroll)
            card.grid(row=i + 2, column=0, sticky="ew", padx=24, pady=5)
            card.grid_columnconfigure(1, weight=1)

            ctk.CTkLabel(card, text=c["icone"], font=("Segoe UI", 28)).grid(
                row=0, column=0, rowspan=2, padx=(16, 8), pady=12)
            
            info = ctk.CTkFrame(card, fg_color="transparent")
            info.grid(row=0, column=1, sticky="ew", padx=0, pady=(12, 0))
            info.grid_columnconfigure(0, weight=1)
            criar_label(info, c["titulo"], 14, "bold").grid(row=0, column=0, sticky="w")
            criar_label(info, c["descricao"], 11, color=CORES["texto_sub"]).grid(
                row=1, column=0, sticky="w", pady=(2, 0))

            bar = ctk.CTkProgressBar(card, height=6, corner_radius=3,
                                    fg_color=CORES["bg_card2"], progress_color=CORES["verde"])
            bar.set(pct / 100)
            bar.grid(row=1, column=1, sticky="ew", padx=0, pady=(4, 10))

            cor_btn = CORES["verde_escuro"] if pct == 100 else CORES["azul"]
            txt_btn = "✓ Concluído" if pct == 100 else ("Continuar" if pct > 0 else "Estudar")
            criar_botao(card, txt_btn, 36, cor_btn, width=110,
                       command=lambda c=c: self._abrir_conteudo(c)).grid(row=0, column=2, rowspan=2, padx=16, pady=12)

    def _abrir_conteudo(self, conteudo):
        self._limpar_area()
        self._nav("Conteúdos", lambda: None)
        self.dados.marcar_conteudo(conteudo["id"])
        scroll = self._scroll_area()

        h = ctk.CTkFrame(scroll, fg_color="transparent")
        h.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 4))
        criar_botao(h, "← Voltar", 30, CORES["bg_card"], width=90,
                   command=self._mostrar_conteudos).pack(side="left")
        criar_label(h, f"{conteudo['icone']}  {conteudo['titulo']}", 18, "bold").pack(side="left", padx=16)

        card_exp = criar_card(scroll)
        card_exp.grid(row=1, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_exp, "📖 Explicação", 13, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        criar_label(card_exp, conteudo["explicacao"], 12, color=CORES["texto_sub"],
                   justify="left", wraplength=700).pack(anchor="w", padx=16, pady=(0, 14))

        card_cod = criar_card(scroll)
        card_cod.grid(row=2, column=0, sticky="ew", padx=24, pady=8)
        hdr = ctk.CTkFrame(card_cod, fg_color="transparent")
        hdr.pack(fill="x", padx=16, pady=(14, 0))
        criar_label(hdr, "💻 Exemplo de código", 13, "bold").pack(side="left")

        cod_bg = ctk.CTkFrame(card_cod, fg_color="#0d1117", corner_radius=8)
        cod_bg.pack(fill="x", padx=16, pady=(8, 14))
        ctk.CTkLabel(cod_bg, text=conteudo["codigo"],
                    font=("Courier New", 12), text_color="#79c0ff",
                    justify="left", wraplength=700).pack(anchor="w", padx=12, pady=10)

        exs = [e for e in EXERCICIOS if e["conteudo_id"] == conteudo["id"]]
        if exs:
            criar_botao(scroll, "✏️  Praticar exercícios deste conteúdo", 44,
                       command=lambda: self._iniciar_exercicios(exs)).grid(row=3, column=0, sticky="ew", padx=24, pady=(4, 20))

    def _mostrar_exercicios_menu(self):
        self._limpar_area()
        self._nav("Exercícios", lambda: None)
        scroll = self._scroll_area()

        criar_label(scroll, "✏️  Exercícios", 20, "bold").grid(
            row=0, column=0, sticky="w", padx=24, pady=(20, 4))
        criar_label(scroll, "Escolha um tipo de exercício",
                   13, color=CORES["texto_sub"]).grid(row=1, column=0, sticky="w", padx=24, pady=(0, 12))

        # Exercícios de Digitação
        
        categorias = {}
        for ex in EXERCICIOS_DIGITACAO:
            cat = ex.get("categoria", "Outros")
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(ex)

        row_atual = 2

        for categoria, exercicios in categorias.items():
            card_cat = criar_card(scroll)
            card_cat.grid(row=row_atual, column=0, sticky="ew", padx=24, pady=5)
            r = ctk.CTkFrame(card_cat, fg_color="transparent")
            r.pack(fill="x", padx=16, pady=14)
            criar_label(r, f"⌨️  {categoria}", 14, "bold").pack(side="left")
            feitos = sum(1 for e in exercicios if e["id"] in self.dados.exercicios_feitos)
            criar_label(r, f"{feitos}/{len(exercicios)}", 12, color=CORES["texto_sub"]).pack(side="right")
            criar_botao(card_cat, "Praticar", 38, CORES["roxo"],
                       command=lambda ex=exercicios: self._iniciar_digitacao(ex)).pack(fill="x", padx=16, pady=(0, 14))
            row_atual += 1

    # Todos os exercícios (interface)
    
        card_all = criar_card(scroll)
        card_all.grid(row=row_atual, column=0, sticky="ew", padx=24, pady=5)
        r = ctk.CTkFrame(card_all, fg_color="transparent")
        r.pack(fill="x", padx=16, pady=14)
        criar_label(r, "🎯  Todos os exercícios", 14, "bold").pack(side="left")
        criar_label(r, f"{len(self.dados.exercicios_feitos)}/{len(EXERCICIOS)}", 12,
                   color=CORES["texto_sub"]).pack(side="right")
        criar_botao(card_all, "Iniciar todos", 38,
                   command=lambda: self._iniciar_exercicios(EXERCICIOS)).pack(fill="x", padx=16, pady=(0, 14))

        row_atual += 1

        for i, c in enumerate(CONTEUDOS):
            exs = [e for e in EXERCICIOS if e["conteudo_id"] == c["id"]]
            feitos = sum(1 for e in exs if e["id"] in self.dados.exercicios_feitos)
            pct = int(feitos / len(exs) * 100) if exs else 0

            card = criar_card(scroll)
            card.grid(row=row_atual + i, column=0, sticky="ew", padx=24, pady=5)
            rr = ctk.CTkFrame(card, fg_color="transparent")
            rr.pack(fill="x", padx=16, pady=(12, 6))
            criar_label(rr, f"{c['icone']}  {c['titulo']}", 13, "bold").pack(side="left")
            criar_label(rr, f"{feitos}/{len(exs)}  {pct}%", 11, color=CORES["texto_sub"]).pack(side="right")
            bar = ctk.CTkProgressBar(card, height=6, corner_radius=3,
                                    fg_color=CORES["bg_card2"], progress_color=CORES["verde"])
            bar.set(pct / 100)
            bar.pack(fill="x", padx=16, pady=(0, 6))
            criar_botao(card, "Praticar", 36,
                       state="disabled" if not exs else "normal",
                       command=lambda ex=exs: self._iniciar_exercicios(ex)).pack(fill="x", padx=16, pady=(0, 12))

    def _mostrar_desafios(self):
        self._limpar_area()
        self._nav("Desafios", lambda: None)
        scroll = self._scroll_area()

        criar_label(scroll, "⚔️  Desafios", 20, "bold").grid(
            row=0, column=0, sticky="w", padx=24, pady=(20, 4))
        criar_label(scroll, "Complete desafios para ganhar mais XP e praticar!",
                   13, color=CORES["texto_sub"]).grid(row=1, column=0, sticky="w", padx=24, pady=(0, 12))

        for i, d in enumerate(DESAFIOS):
            feito = d["id"] in self.dados.desafios_feitos
            card = criar_card(scroll)
            card.grid(row=i + 2, column=0, sticky="ew", padx=24, pady=5)
            card.grid_columnconfigure(1, weight=1)

            cor_dific = {"Fácil": CORES["verde"], "Médio": CORES["amarelo"], "Difícil": CORES["laranja"]}
            cor = cor_dific.get(d["dificuldade"], CORES["texto"])

            ctk.CTkLabel(card, text=d["icone"], font=("Segoe UI", 28)).grid(
                row=0, column=0, rowspan=2, padx=(16, 8), pady=12)
            
            info = ctk.CTkFrame(card, fg_color="transparent")
            info.grid(row=0, column=1, sticky="ew", padx=0, pady=(12, 0))
            info.grid_columnconfigure(0, weight=1)
            
            titulo_row = ctk.CTkFrame(info, fg_color="transparent")
            titulo_row.grid(row=0, column=0, sticky="w")
            criar_label(titulo_row, d["titulo"], 14, "bold").pack(side="left")
            criar_label(titulo_row, f"  {d['dificuldade']}", 10, color=cor).pack(side="left", padx=(8, 0))
            
            criar_label(info, d["descricao"], 11, color=CORES["texto_sub"]).grid(
                row=1, column=0, sticky="w", pady=(2, 0))

            criar_label(card, f"✨ +{d['xp']} XP", 12, "bold", color=CORES["amarelo"]).grid(
                row=0, column=1, sticky="e", padx=16, pady=12)

            if feito:
                criar_label(card, "✓ Concluído", 11, "bold", color=CORES["verde"]).grid(
                    row=1, column=1, sticky="e", padx=16, pady=(0, 12))
            else:
                criar_botao(card, "Começar", 36, CORES["laranja"], width=100,
                           command=lambda des=d: self._abrir_desafio(des)).grid(row=0, column=2, rowspan=2, padx=16, pady=12)

    def _abrir_desafio(self, desafio):
        self._limpar_area()
        self._nav("Desafios", lambda: None)
        scroll = self._scroll_area()

        h = ctk.CTkFrame(scroll, fg_color="transparent")
        h.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 4))
        criar_botao(h, "← Voltar", 30, CORES["bg_card"], width=90,
                   command=self._mostrar_desafios).pack(side="left")
        criar_label(h, f"{desafio['icone']}  {desafio['titulo']}", 18, "bold").pack(side="left", padx=16)

        card_desc = criar_card(scroll)
        card_desc.grid(row=1, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_desc, desafio["descricao"], 14, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        criar_label(card_desc, f"Dificuldade: {desafio['dificuldade']}", 12, color=CORES["texto_sub"]).pack(anchor="w", padx=16, pady=(0, 14))

        card_obj = criar_card(scroll)
        card_obj.grid(row=2, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_obj, "📌 Objetivo", 13, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        criar_label(card_obj, desafio["objetivo"], 12, color=CORES["texto_sub"], wraplength=700).pack(anchor="w", padx=16, pady=(0, 14))

        card_dica = criar_card(scroll)
        card_dica.grid(row=3, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_dica, f"💡 Dica: {desafio['dica']}", 12, color=CORES["amarelo"]).pack(anchor="w", padx=16, pady=14)

        card_resposta = criar_card(scroll)
        card_resposta.grid(row=4, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_resposta, "💻 Sua solução", 13, "bold").pack(anchor="w", padx=16, pady=(14, 8))
        
        self.entry_desafio = ctk.CTkTextbox(card_resposta, height=150, corner_radius=8,
                                            text_color=CORES["texto"],
                                            fg_color=CORES["bg_card2"],
                                            border_color=CORES["borda"],
                                            border_width=1)
        self.entry_desafio.pack(fill="both", padx=16, pady=(0, 14), expand=True)

        card_recompensa = criar_card(scroll)
        card_recompensa.grid(row=5, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_recompensa, "🎁 Recompensa", 13, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        criar_label(card_recompensa, f"✨ +{desafio['xp']} XP", 14, "bold", color=CORES["amarelo"]).pack(anchor="w", padx=16, pady=(0, 14))

        btn_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        btn_frame.grid(row=6, column=0, sticky="ew", padx=24, pady=20)
        btn_frame.grid_columnconfigure((0, 1), weight=1)

        criar_botao(btn_frame, "Verificar resposta", 44, CORES["verde_escuro"],
                   command=lambda d=desafio: self._verificar_desafio(d)).grid(row=0, column=0, sticky="ew", padx=(0, 8))
        criar_botao(btn_frame, "Voltar", 44, CORES["bg_card2"],
                   command=self._mostrar_desafios).grid(row=0, column=1, sticky="ew", padx=(8, 0))

    def _verificar_desafio(self, desafio):
        resposta_user = self.entry_desafio.get("1.0", "end-1c").strip()
        
        if not resposta_user:
            self._limpar_area()
            scroll = self._scroll_area()
            card = criar_card(scroll)
            card.grid(row=0, column=0, sticky="ew", padx=24, pady=20)
            criar_label(card, "⚠️", 52).pack(pady=(20, 8))
            criar_label(card, "Campo vazio!", 20, "bold", color=CORES["laranja"]).pack(pady=4)
            criar_label(card, "Por favor, digite sua solução antes de verificar.",
                       14, color=CORES["texto_sub"]).pack(pady=12)
            criar_botao(scroll, "Voltar", 44,
                       command=lambda d=desafio: self._abrir_desafio(d)).grid(row=1, column=0, sticky="ew", padx=24, pady=8)
            return
        
        self._tela_feedback_desafio(desafio, True, resposta_user)

    def _tela_feedback_desafio(self, desafio, enviado, resposta_user):
        self._limpar_area()
        scroll = self._scroll_area()

        card = criar_card(scroll)
        card.grid(row=0, column=0, sticky="ew", padx=24, pady=20)

        criar_label(card, "✅", 52).pack(pady=(20, 8))
        criar_label(card, "Desafio Verificado! 🎉", 20, "bold", color=CORES["verde"]).pack(pady=4)
        
        criar_label(card, "Sua solução foi enviada para análise.", 14, 
                   color=CORES["texto_sub"]).pack(pady=12)
        
        criar_label(card, "Verifique se seu código:", 12, "bold").pack(pady=(12, 6))
        
        checklist = ctk.CTkFrame(card, fg_color="transparent")
        checklist.pack(anchor="w", padx=16, pady=(0, 12))
        
        itens = [
            "✓ Resolve o problema proposto",
            "✓ Usa os conceitos ensinados",
            "✓ Está bem estruturado e limpo",
            "✓ Funciona sem erros"
        ]
        
        for item in itens:
            criar_label(checklist, item, 11, color=CORES["verde"]).pack(anchor="w", pady=2)
        
        criar_label(card, f"+{desafio['xp']} XP ganhos! ⚡", 13, "bold",
                   color=CORES["amarelo"]).pack(pady=(12, 0))

        btn_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        btn_frame.grid(row=1, column=0, sticky="ew", padx=24, pady=8)
        btn_frame.grid_columnconfigure((0, 1), weight=1)

        criar_botao(btn_frame, "Marcar como completo", 44, CORES["verde_escuro"],
                   command=lambda d=desafio: self._completar_desafio(d)).grid(row=0, column=0, sticky="ew", padx=(0, 8))
        criar_botao(btn_frame, "Voltar aos desafios", 44, CORES["bg_card2"],
                   command=self._mostrar_desafios).grid(row=0, column=1, sticky="ew", padx=(8, 0))

        self._atualizar_perfil()

    def _completar_desafio(self, desafio):
        self.dados.marcar_desafio(desafio["id"], desafio["xp"])
        self._atualizar_perfil()
        
        self._limpar_area()
        scroll = self._scroll_area()
        card = criar_card(scroll)
        card.grid(row=0, column=0, sticky="ew", padx=24, pady=20)
        
        criar_label(card, "✅", 52).pack(pady=(20, 8))
        criar_label(card, "Desafio Concluído! 🎉", 20, "bold", color=CORES["verde"]).pack(pady=4)
        criar_label(card, f"+{desafio['xp']} XP ganhos! ⚡", 16, "bold", color=CORES["amarelo"]).pack(pady=12)
        
        criar_botao(scroll, "Voltar aos Desafios", 44,
                   command=self._mostrar_desafios).grid(row=1, column=0, sticky="ew", padx=24, pady=8)

    def _iniciar_exercicios(self, lista):
        self.exercicios_sessao = lista[:]
        self.exercicio_index = 0
        self._mostrar_exercicio()

    def _mostrar_exercicio(self):
        self._limpar_area()
        d = self.dados
        exs = self.exercicios_sessao

        if self.exercicio_index >= len(exs):
            self._tela_fim_exercicios()
            return

        ex = exs[self.exercicio_index]
        scroll = self._scroll_area()

        hdr = ctk.CTkFrame(scroll, fg_color="transparent")
        hdr.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 4))
        criar_botao(hdr, "← Sair", 30, CORES["bg_card"], width=80,
                   command=self._mostrar_exercicios_menu).pack(side="left")
        criar_label(hdr, f"Exercício {self.exercicio_index + 1} de {len(exs)}",
                   13, "bold").pack(side="left", padx=16)

        bar = ctk.CTkProgressBar(scroll, height=8, corner_radius=4,
                               fg_color=CORES["bg_card2"], progress_color=CORES["azul"])
        bar.set((self.exercicio_index + 1) / len(exs))
        bar.grid(row=1, column=0, sticky="ew", padx=24, pady=8)

        card_q = criar_card(scroll)
        card_q.grid(row=2, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_q, ex["pergunta"], 15, "bold", wraplength=650).pack(
            anchor="w", padx=20, pady=(18, 14))

        card_dica = criar_card(scroll)
        card_dica.grid(row=3, column=0, sticky="ew", padx=24, pady=4)
        criar_label(card_dica, f"💡 Dica: {ex['dica']}", 12,
                   color=CORES["amarelo"]).pack(anchor="w", padx=16, pady=10)

        card_alt = criar_card(scroll)
        card_alt.grid(row=4, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_alt, "Escolha a resposta correta:", 12,
                   color=CORES["texto_sub"]).pack(anchor="w", padx=16, pady=(12, 6))

        self.resp_var = ctk.IntVar(value=-1)
        self.btns_alt = []
        for idx, alt in enumerate(ex["alternativas"]):
            btn = ctk.CTkButton(
                card_alt, text=f"  {alt}", anchor="w",
                height=46, corner_radius=8,
                fg_color=CORES["bg_card2"], hover_color=CORES["azul"],
                text_color=CORES["texto"], font=("Segoe UI", 13),
                command=lambda i=idx: self._selecionar_alt(i, ex, card_alt)
            )
            btn.pack(fill="x", padx=16, pady=4)
            self.btns_alt.append(btn)

        self.btn_enviar = criar_botao(scroll, "Enviar resposta", 44,
                                     state="disabled",
                                     command=lambda: self._verificar_resposta(ex))
        self.btn_enviar.grid(row=5, column=0, sticky="ew", padx=24, pady=(4, 20))

        if ex["id"] in d.exercicios_feitos:
            criar_label(scroll, "✓ Você já concluiu este exercício! Pode responder novamente.",
                       11, color=CORES["verde"]).grid(row=6, column=0, padx=24, pady=4)

        self.card_alt_ref = card_alt
        self.resp_selecionada = -1

    def _selecionar_alt(self, idx, ex, card):
        self.resp_selecionada = idx
        for i, btn in enumerate(self.btns_alt):
            btn.configure(fg_color=CORES["azul"] if i == idx else CORES["bg_card2"])
        self.btn_enviar.configure(state="normal")

    def _verificar_resposta(self, ex):
        correta = ex["correta"]
        acertou = self.resp_selecionada == correta

        for i, btn in enumerate(self.btns_alt):
            if i == correta:
                btn.configure(fg_color=CORES["verde_escuro"])
            elif i == self.resp_selecionada and not acertou:
                btn.configure(fg_color=CORES["erro"])

        self.btn_enviar.configure(state="disabled")

        if acertou and ex["id"] not in self.dados.exercicios_feitos:
            self.dados.marcar_exercicio(ex["id"], ex["xp"])

        self._tela_feedback(ex, acertou)

    def _tela_feedback(self, ex, acertou):
        self._limpar_area()
        scroll = self._scroll_area()

        card = criar_card(scroll)
        card.grid(row=0, column=0, sticky="ew", padx=24, pady=20)

        icone = "✅" if acertou else "❌"
        cor = CORES["verde"] if acertou else "#ef4444"
        msg = "Resposta correta! 🎉" if acertou else "Resposta incorreta..."

        criar_label(card, icone, 52).pack(pady=(20, 8))
        criar_label(card, msg, 20, "bold", color=cor).pack(pady=4)
        criar_label(card, f"A alternativa correta é:\n{ex['alternativas'][ex['correta']]}",
                   14, color=CORES["texto_sub"]).pack(pady=(4, 8))
        criar_label(card, ex["explicacao"], 12, color=CORES["texto_sub"],
                   wraplength=600).pack(padx=24, pady=(0, 16))

        if acertou:
            criar_label(card, f"+{ex['xp']} XP ganhos! ⚡", 13, "bold",
                       color=CORES["amarelo"]).pack(pady=(0, 12))

        prox_idx = self.exercicio_index + 1
        tem_prox = prox_idx < len(self.exercicios_sessao)

        if tem_prox:
            criar_botao(scroll, "Próximo exercício →", 44,
                       command=self._proximo_exercicio).grid(row=1, column=0, sticky="ew", padx=24, pady=8)
        else:
            criar_botao(scroll, "🏁 Ver resultados", 44, CORES["verde_escuro"],
                       command=self._proximo_exercicio).grid(row=1, column=0, sticky="ew", padx=24, pady=8)

        self._atualizar_perfil()

    def _proximo_exercicio(self):
        self.exercicio_index += 1
        self._mostrar_exercicio()

    def _tela_fim_exercicios(self):
        self._limpar_area()
        scroll = self._scroll_area()
        d = self.dados
        total = len(self.exercicios_sessao)
        feitos_sessao = sum(1 for e in self.exercicios_sessao
                           if e["id"] in d.exercicios_feitos)

        card = criar_card(scroll)
        card.grid(row=0, column=0, sticky="ew", padx=24, pady=20)
        criar_label(card, "🏁", 52).pack(pady=(20, 8))
        criar_label(card, "Sessão concluída!", 22, "bold").pack(pady=4)
        criar_label(card, f"Você acertou {feitos_sessao} de {total} exercícios",
                   14, color=CORES["texto_sub"]).pack(pady=8)

        pct = int(feitos_sessao / total * 100) if total > 0 else 0
        bar = ctk.CTkProgressBar(card, height=12, corner_radius=6,
                               fg_color=CORES["bg_card2"], progress_color=CORES["verde"])
        bar.set(pct / 100)
        bar.pack(fill="x", padx=40, pady=12)
        criar_label(card, f"{pct}% de aproveitamento", 13, color=CORES["amarelo"]).pack(pady=(0, 16))

        criar_botao(scroll, "🏠 Voltar ao início", 44,
                   command=self._mostrar_inicio).grid(row=1, column=0, sticky="ew", padx=24, pady=8)
# EXERCÍCIOS DE DIGITAÇÃO 
    def _iniciar_digitacao(self, lista):
        self.exercicios_sessao = lista[:]
        self.exercicio_index = 0
        self._mostrar_digitacao()

    def _mostrar_digitacao(self):
        self._limpar_area()
        d = self.dados
        exs = self.exercicios_sessao

        if self.exercicio_index >= len(exs):
            self._tela_fim_digitacao()
            return

        ex = exs[self.exercicio_index]
        scroll = self._scroll_area()

        hdr = ctk.CTkFrame(scroll, fg_color="transparent")
        hdr.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 4))
        criar_botao(hdr, "← Sair", 30, CORES["bg_card"], width=80,
                   command=self._mostrar_exercicios_menu).pack(side="left")
        criar_label(hdr, f"Exercício {self.exercicio_index + 1} de {len(exs)}",
                   13, "bold").pack(side="left", padx=16)

        bar = ctk.CTkProgressBar(scroll, height=8, corner_radius=4,
                               fg_color=CORES["bg_card2"], progress_color=CORES["roxo"])
        bar.set((self.exercicio_index + 1) / len(exs))
        bar.grid(row=1, column=0, sticky="ew", padx=24, pady=8)

        card_t = criar_card(scroll)
        card_t.grid(row=2, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_t, f"⌨️  {ex['titulo']}", 16, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        criar_label(card_t, ex["descricao"], 12, color=CORES["texto_sub"]).pack(anchor="w", padx=16, pady=(0, 14))

        card_cod = criar_card(scroll)
        card_cod.grid(row=3, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_cod, "Código que você deve digitar:", 12, "bold").pack(anchor="w", padx=16, pady=(14, 8))
        
        cod_bg = ctk.CTkFrame(card_cod, fg_color="#0d1117", corner_radius=8)
        cod_bg.pack(fill="x", padx=16, pady=(0, 14))
        ctk.CTkLabel(cod_bg, text=ex["codigo"],
                    font=("Courier New", 13), text_color="#79c0ff",
                    justify="left", wraplength=700).pack(anchor="w", padx=12, pady=10)

        card_inp = criar_card(scroll)
        card_inp.grid(row=4, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_inp, "Digite sua resposta aqui:", 12, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        
        self.entry_digitacao = ctk.CTkTextbox(card_inp, height=120, corner_radius=8,
                                              text_color=CORES["texto"],
                                              fg_color=CORES["bg_card2"])
        self.entry_digitacao.pack(fill="both", padx=16, pady=(0, 14), expand=True)

        card_dica = criar_card(scroll)
        card_dica.grid(row=5, column=0, sticky="ew", padx=24, pady=4)
        criar_label(card_dica, f"💡 Dica: {ex['dica']}", 12,
                   color=CORES["amarelo"]).pack(anchor="w", padx=16, pady=10)

        btn_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        btn_frame.grid(row=6, column=0, sticky="ew", padx=24, pady=(8, 20))
        btn_frame.grid_columnconfigure((0, 1), weight=1)

        criar_botao(btn_frame, "Verificar", 44, CORES["verde_escuro"],
                   command=lambda: self._verificar_digitacao(ex)).grid(row=0, column=0, sticky="ew", padx=(0, 8))

        criar_botao(btn_frame, "Pular", 44, CORES["bg_card2"],
                   command=self._proximo_digitacao).grid(row=0, column=1, sticky="ew", padx=(8, 0))

    def _verificar_digitacao(self, ex):
        resposta_user = self.entry_digitacao.get("1.0", "end-1c").strip()
        resposta_correta = ex["codigo"].strip()
        acertou = resposta_user == resposta_correta
        self._tela_feedback_digitacao(ex, acertou, resposta_user, resposta_correta)

    def _tela_feedback_digitacao(self, ex, acertou, resposta_user, resposta_correta):
        self._limpar_area()
        scroll = self._scroll_area()

        card = criar_card(scroll)
        card.grid(row=0, column=0, sticky="ew", padx=24, pady=20)

        icone = "✅" if acertou else "❌"
        cor = CORES["verde"] if acertou else "#ef4444"
        msg = "Resposta correta! 🎉" if acertou else "Resposta incorreta..."

        criar_label(card, icone, 52).pack(pady=(20, 8))
        criar_label(card, msg, 20, "bold", color=cor).pack(pady=4)

        if not acertou:
            criar_label(card, "Sua resposta:", 12, "bold").pack(pady=(12, 4))
            cod_sua = ctk.CTkFrame(card, fg_color="#0d1117", corner_radius=8)
            cod_sua.pack(fill="x", padx=16, pady=(0, 8))
            ctk.CTkLabel(cod_sua, text=resposta_user, font=("Courier New", 11),
                        text_color="#ff6b6b", justify="left").pack(anchor="w", padx=8, pady=6)

            criar_label(card, "Resposta correta:", 12, "bold").pack(pady=(12, 4))
            cod_certa = ctk.CTkFrame(card, fg_color="#0d1117", corner_radius=8)
            cod_certa.pack(fill="x", padx=16, pady=(0, 8))
            ctk.CTkLabel(cod_certa, text=resposta_correta, font=("Courier New", 11),
                        text_color="#79c0ff", justify="left").pack(anchor="w", padx=8, pady=6)

        if acertou:
            criar_label(card, f"+{ex['xp']} XP ganhos! ⚡", 13, "bold",
                       color=CORES["amarelo"]).pack(pady=(16, 0))
            if ex["id"] not in self.dados.exercicios_feitos:
                self.dados.marcar_digitacao(ex["id"], ex["xp"])

        prox_idx = self.exercicio_index + 1
        tem_prox = prox_idx < len(self.exercicios_sessao)

        if tem_prox:
            criar_botao(scroll, "Próximo →", 44,
                       command=self._proximo_digitacao).grid(row=1, column=0, sticky="ew", padx=24, pady=8)
        else:
            criar_botao(scroll, "🏁 Ver resultados", 44, CORES["verde_escuro"],
                       command=self._proximo_digitacao).grid(row=1, column=0, sticky="ew", padx=24, pady=8)

        self._atualizar_perfil()

    def _proximo_digitacao(self):
        self.exercicio_index += 1
        self._mostrar_digitacao()

    def _tela_fim_digitacao(self):
        self._limpar_area()
        scroll = self._scroll_area()
        d = self.dados
        total = len(self.exercicios_sessao)
        feitos_sessao = sum(1 for e in self.exercicios_sessao
                           if e["id"] in d.exercicios_feitos)

        card = criar_card(scroll)
        card.grid(row=0, column=0, sticky="ew", padx=24, pady=20)
        criar_label(card, "🏁", 52).pack(pady=(20, 8))
        criar_label(card, "Sessão de digitação concluída!", 22, "bold").pack(pady=4)
        criar_label(card, f"Você acertou {feitos_sessao} de {total} exercícios",
                   14, color=CORES["texto_sub"]).pack(pady=8)

        pct = int(feitos_sessao / total * 100) if total > 0 else 0
        bar = ctk.CTkProgressBar(card, height=12, corner_radius=6,
                               fg_color=CORES["bg_card2"], progress_color=CORES["roxo"])
        bar.set(pct / 100)
        bar.pack(fill="x", padx=40, pady=12)
        criar_label(card, f"{pct}% de aproveitamento", 13, color=CORES["amarelo"]).pack(pady=(0, 16))

        criar_botao(scroll, "🏠 Voltar ao início", 44,
                   command=self._mostrar_inicio).grid(row=1, column=0, sticky="ew", padx=24, pady=8)

    def _mostrar_progresso(self):
        self._limpar_area()
        self._nav("Progresso", lambda: None)
        d = self.dados
        scroll = self._scroll_area()

        criar_label(scroll, "📊  Seu Progresso", 20, "bold").grid(
            row=0, column=0, sticky="w", padx=24, pady=(20, 12))

        stats_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        stats_frame.grid(row=1, column=0, sticky="ew", padx=24, pady=4)
        stats_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        stats = [
            ("Nível atual", str(d.nivel), d.nivel_nome, CORES["azul"]),
            ("XP total", str(d.xp), "XP", CORES["amarelo"]),
            ("Exercícios feitos", str(len(d.exercicios_feitos)), "exercícios", CORES["verde"]),
            ("Desafios completos", str(len(d.desafios_feitos)), "desafios", CORES["laranja"]),
        ]
        for i, (titulo, valor, sub, cor) in enumerate(stats):
            c = criar_card(stats_frame)
            c.grid(row=0, column=i, sticky="ew", padx=4, pady=0)
            criar_label(c, titulo, 11, color=CORES["texto_sub"]).pack(pady=(12, 2))
            criar_label(c, valor, 28, "bold", color=cor).pack()
            criar_label(c, sub, 10, color=CORES["texto_sub"]).pack(pady=(2, 12))

        card_prog = criar_card(scroll)
        card_prog.grid(row=2, column=0, sticky="ew", padx=24, pady=10)
        card_prog.grid_columnconfigure((0, 1), weight=1)

        left = ctk.CTkFrame(card_prog, fg_color="transparent")
        left.grid(row=0, column=0, sticky="nsew", padx=20, pady=16)
        criar_label(left, "Progresso geral", 14, "bold").pack(anchor="w", pady=(0, 8))
        pct_g = d.progresso_geral()
        bar_g = ctk.CTkProgressBar(left, height=10, corner_radius=5,
                                  fg_color=CORES["bg_card2"], progress_color=CORES["verde"])
        bar_g.set(pct_g / 100)
        bar_g.pack(fill="x")
        criar_label(left, f"{pct_g}%  •  {len(d.exercicios_feitos)}/{len(EXERCICIOS) + len(EXERCICIOS_DIGITACAO)} exercícios",
                   12, color=CORES["texto_sub"]).pack(anchor="w", pady=(6, 0))

        right = ctk.CTkFrame(card_prog, fg_color="transparent")
        right.grid(row=0, column=1, sticky="nsew", padx=20, pady=16)
        criar_label(right, "Trilha de aprendizado", 14, "bold").pack(anchor="w", pady=(0, 6))
        for c in CONTEUDOS:
            pct_c = d.progresso_conteudo(c["id"])
            row_c = ctk.CTkFrame(right, fg_color="transparent")
            row_c.pack(fill="x", pady=2)
            criar_label(row_c, f"{c['id']}. {c['titulo']}", 11).pack(side="left")
            criar_label(row_c, f"{pct_c}%", 11, color=CORES["texto_sub"]).pack(side="right")
            bar_c = ctk.CTkProgressBar(right, height=5, corner_radius=3,
                                      fg_color=CORES["bg_card2"], progress_color=CORES["verde"])
            bar_c.set(pct_c / 100)
            bar_c.pack(fill="x", pady=(0, 2))

        card_at = criar_card(scroll)
        card_at.grid(row=3, column=0, sticky="ew", padx=24, pady=(4, 20))
        criar_label(card_at, "Atividade recente", 14, "bold").pack(anchor="w", padx=16, pady=(14, 6))

        if not d.atividade_recente:
            criar_label(card_at, "Nenhuma atividade ainda. Comece a estudar!",
                       12, color=CORES["texto_sub"]).pack(padx=16, pady=(0, 14))
        else:
            for at in d.atividade_recente[:8]:
                row_at = ctk.CTkFrame(card_at, fg_color="transparent")
                row_at.pack(fill="x", padx=16, pady=3)
                criar_label(row_at, f"✓  {at['descricao']}", 11).pack(side="left")
                criar_label(row_at, f"+{at['xp']} XP  •  {at['data']}", 10,
                           color=CORES["verde"]).pack(side="right")
            ctk.CTkFrame(card_at, fg_color="transparent", height=8).pack()

    def _mostrar_conquistas(self):
        self._limpar_area()
        self._nav("Conquistas", lambda: None)
        d = self.dados
        scroll = self._scroll_area()

        criar_label(scroll, "🏆  Suas Conquistas", 20, "bold").grid(
            row=0, column=0, sticky="w", padx=24, pady=(20, 4))

        conquistas = d.conquistas_desbloqueadas()
        desbloqueadas = sum(1 for _, _, ok in conquistas if ok)
        criar_label(scroll, f"{desbloqueadas} de {len(conquistas)} conquistas desbloqueadas",
                   13, color=CORES["texto_sub"]).grid(row=1, column=0, sticky="w", padx=24, pady=(0, 12))

        grid = ctk.CTkFrame(scroll, fg_color="transparent")
        grid.grid(row=2, column=0, sticky="ew", padx=24, pady=4)
        grid.grid_columnconfigure((0, 1, 2, 3), weight=1)

        for i, (c, prog, ok) in enumerate(conquistas):
            row_i = i // 4
            col_i = i % 4
            card = criar_card(grid)
            card.grid(row=row_i, column=col_i, sticky="nsew", padx=5, pady=5)
            card.configure(fg_color=CORES["bg_card"] if ok else CORES["bg_card2"])

            criar_label(card, c["icone"] if ok else "🔒", 32).pack(pady=(14, 4))
            criar_label(card, c["nome"], 12, "bold",
                       color=c["cor"] if ok else CORES["texto_sub"]).pack()
            criar_label(card, c["descricao"], 10, color=CORES["texto_sub"],
                       wraplength=140).pack(padx=8, pady=(4, 4))

            meta = c["meta"]
            pct_c = min(int(prog / meta * 100), 100) if meta > 0 else 100
            bar_c = ctk.CTkProgressBar(card, height=6, corner_radius=3,
                                      fg_color=CORES["borda"],
                                      progress_color=c["cor"] if ok else CORES["texto_sub"])
            bar_c.set(pct_c / 100)
            bar_c.pack(fill="x", padx=12, pady=(2, 4))
            criar_label(card, f"{prog}/{meta}", 9, color=CORES["texto_sub"]).pack(pady=(0, 12))

            if ok:
                criar_label(card, "✓ Desbloqueada", 10, "bold", color=c["cor"]).pack(pady=(0, 8))

    def _mostrar_config(self):
        self._limpar_area()
        self._nav("Configurações", lambda: None)
        scroll = self._scroll_area()

        criar_label(scroll, "⚙️  Configurações", 20, "bold").grid(
            row=0, column=0, sticky="w", padx=24, pady=(20, 12))

        card_nome = criar_card(scroll)
        card_nome.grid(row=1, column=0, sticky="ew", padx=24, pady=8)
        criar_label(card_nome, "Nome do usuário", 13, "bold").pack(anchor="w", padx=16, pady=(14, 6))
        self.entry_nome = ctk.CTkEntry(card_nome, placeholder_text="Seu nome",
                                      height=40, font=("Segoe UI", 13))
        self.entry_nome.insert(0, self.dados.nome)
        self.entry_nome.pack(fill="x", padx=16, pady=(0, 4))
        criar_botao(card_nome, "Salvar nome", 38,
                   command=self._salvar_nome).pack(fill="x", padx=16, pady=(4, 14))

        card_reset = criar_card(scroll)
        card_reset.grid(row=2, column=0, sticky="ew", padx=24, pady=(4, 20))
        criar_label(card_reset, "Resetar progresso", 13, "bold").pack(anchor="w", padx=16, pady=(14, 4))
        criar_label(card_reset, "Apaga todo o progresso, XP e conquistas. Irreversível!",
                   11, color="#ef4444").pack(anchor="w", padx=16, pady=(0, 8))
        criar_botao(card_reset, "Resetar tudo", 38, "#7f1d1d",
                   command=self._confirmar_reset).pack(fill="x", padx=16, pady=(0, 14))

    # progresso (sistema de xp)

        card_sobre = criar_card(scroll)
        card_sobre.grid(row=3, column=0, sticky="ew", padx=24, pady=(0, 20))
        criar_label(card_sobre, "Sobre o PyTutor", 13, "bold").pack(anchor="w", padx=16, pady=(14, 4))
        criar_label(card_sobre,
                   "PyTutor v2.0  •  Plataforma Inteligente para Aprendizagem de Python\n"
                   "Projeto acadêmico  •  Heitor, João Lucas, João Viana, Yan",
                   12, color=CORES["texto_sub"]).pack(anchor="w", padx=16, pady=(0, 14))

    def _salvar_nome(self):
        nome = self.entry_nome.get().strip()
        if nome:
            self.dados.nome = nome
            self.dados.salvar()
            self._atualizar_perfil()

    def _confirmar_reset(self):
        win = ctk.CTkToplevel(self)
        win.title("Confirmar reset")
        win.geometry("360x180")
        win.configure(fg_color=CORES["bg_card"])
        win.grab_set()
        criar_label(win, "⚠️ Tem certeza?", 16, "bold").pack(pady=(20, 8))
        criar_label(win, "Todo o progresso será apagado permanentemente.",
                   12, color=CORES["texto_sub"]).pack(pady=(0, 16))
        row = ctk.CTkFrame(win, fg_color="transparent")
        row.pack()
        criar_botao(row, "Cancelar", 120, CORES["bg_card2"],
                   command=win.destroy).pack(side="left", padx=8)
        criar_botao(row, "Confirmar", 120, "#7f1d1d",
                   command=lambda: self._fazer_reset(win)).pack(side="left", padx=8)
# abrir a interface 
    def _fazer_reset(self, win):
        win.destroy()
        embaralhar_exercicios()
        self.dados.xp = 0
        self.dados.nivel = 1
        self.dados.exercicios_feitos = []
        self.dados.conteudos_vistos = []
        self.dados.desafios_feitos = []
        self.dados.atividade_recente = []
        self.dados.salvar()
        self._atualizar_perfil()
        self._mostrar_inicio()


if __name__ == "__main__":
    app = PyTutor()
    app.mainloop()
