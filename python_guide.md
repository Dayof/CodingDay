# Python Guide

## Introdução básica da linguagem Python 3.6:

### Variáveis

``` python
any_var = 3 # números
any_var = 'something' # strings
```

### Variáveis globais

``` python
CTE = 3

def func():
  global CTE
  CTE = 4
```

### Manipulação de strings

``` python
string_input = input('Enter some string')
print('Pair programming is %s', % ('awesome'))
f'Pair programming is {awesome}'
'{1} is {0}'.format('awesome!', 'Dojo')
'Coding ' + 'Dojo'
len('ODD')
string.count('-') # Conta quantos - existem na string
string.split('->') # Cria lista com strings antes e depois da ocorrência de ->
```

### Estruturas de dados

- Listas

``` python
list_ex = [0, 3] # define lista

list_ex + other_list # concatena

list_ex.append(3) # adiciona valor no final da lista
list_ex.insert(1, 3) # adiciona valor 3 no índice 1 da lista
list_ex.extend([1, 3]) # adiciona os valores 1 e 3 à lista
list_ex.remove(3) # retira o primeiro item com valor 3 encontrado na lista, c.c. gera exception de ValueError
list_ex.pop() # retira o último item da lista
list_ex.sort() # ordena de forma crescente a lista
list_ex.sort(reverse=True) # ordena de forma decrescente a lista

3 in list_ex # confere se o valor 3 existe na lista
list_ex.index(3) # coleta o índice do primeiro valor encontrado           
              # na lista ou lança excessão
list_ex[1] # Procura o valor no índice 1 da lista
list_ex[-1] # Procura o valor no último índice da lista
list_ex[1:] # Omite o primeiro valor da lista
list_ex[::2] # Gera cópia da lista com valores dos índices pares
```

- Dicionários

``` python
dict_ex = {'one' : 2, 'two': 1, 'four': 5} # define um dicionário

dict_ex['one'] # Procura o valor da chave 'one'
dict_ex.keys() # coleta todas as chaves do dicionário
dict_ex.values() # coleta todas as valores da chaves do dicionário
dict_ex.items() # coleta o dicionário em formato de lista de tuplas dos valores

dict_ex.setdefault('olar', []).append('eita') # adiciona [] à chave olar se ela ainda não estiver presente no dicionário, ou, adiciona o valor eita ao final da lista da chave olar se ela já existir no dicionário
```

- Tuplas

``` python
tuple_ex = (1, 3) # Define a tupla
a, b, c = (1, 2, 3) # Coleta valores da tupla em variáveis separadas

tuple_ex + other_tuple # concatena tuplas

3 in tuple_ex # confere se o valor 3 existe na tupla

tuple_ex[1] # Procura o valor no índice 1 da tupla
tuple_ex[2:] # Omite até o segundo valor da tupla (retorna uma tupla)
```

### Funções/métodos

``` python
def best_function_ever(var, var2): # Declara função com 2 parâmetros
  return var + var2 # Retorno da função

best_function_ever(3, 4) # Chama função com 2 parâmetros

# declara função anônima
func = lambda name: 'Some anonymous function called ' + name
func('anonymous') # chama função anônima
```

### Classes

``` python
class WorseClassEver: # Declara classe
  def __init__(self): # Método base de setup da classe
    return False # Retorno do método base de setup da classe
```

### Controle de Fluxo

- If's

``` python
if var > 2: # if padrão
  print('hmmm')
elif var < 2:
  print('yes')
else:
  print('ue')

'yeih!' if 3 > 2 else 'aff' # condicional ternário
```

- For

``` python
for number in [1, 2, 3]: # for sobre listas
  print(number)

for key, value in some_dict.items(): # for sobre dicionários
  print(key, value)

for i in range(4): # itera de 0 a 3
  print(i)

for i in range(2, 4): # itera de 2 a 3
  print(i)    

[i for i in range(2, 4) if i < 3] # List comprehensions: Retorna [2]
```

- While

``` python
dojo = 0
while dojo < 10:
  print('dojo is awesome')
  dojo += 1
```

- Exceções

``` python
try:
  var = list_not_declare[1]
  raise IndexError('Another index erro') # Levanta erro de acesso de índice
except IndexError as error:
  pass # Se encontrar este erro faça alguma ação para recuperar o fluxo
except (TypeError, NameError):
  pass # Exceções múltiplas
else:
  print('Good!') # Se não lançar nenhuma exceção
finally:
  print('All clean') # Executa sob qualquer circunstância
```

## Introdução básica do framework de teste `pytest`:

Importando a biblioteca:

``` python
import pytest
```

### Assertivas

``` python
assert 'DOJO' == dojo.upper()
assert 'Dojo' != dojo.upper()
assert 1 < 2
assert 1 > 2
```

### Exemplo de teste

``` python
def teste_exemplo():
    assert 5 == 5 
```

### Setup e Teardown com fixture

``` python
import pytest


@pytest.fixture
def resource():
    print('setup')
    yield
    print('teardown')


def teste_exemplo(resource):
    assert 5 == 5 
```

``` python
import pytest


@pytest.fixture
def resource():
    print('setup')
    item = 1
    yield item
    print('teardown')


def teste_exemplo(resource):
    assert 5 != resource
```

### Executar

``` sh
pytest
```
