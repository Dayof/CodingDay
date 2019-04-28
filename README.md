# Coding Day

## Problema: "Mídia Social"

[Baseado neste problema de @sandromancuso][1].

Implemente uma rede social (similar ao Twitter) que satisfaça os cenários abaixo:

### Cenários

**Posting**: Usuário pode publicar mensagens em sua timeline pessoal

> \> Alice -> I love the weather today    
> \> Bob -> Damn! We lost!     
> \> Bob -> Good game though.    

**Reading**: Usuário pode ver timeline de outro usuário

> \> Alice    
> \> I love the weather today (5 minutes ago)    
> \> Bob    
> \> Good game though. (1 minute ago)     
> \> Damn! We lost! (2 minutes ago)    

**Following**: Usuário pode se inscrever para acompanhar timelines de outros usuários, e também visualizar uma lista agregada de todas as timelines a que ele está inscrito

> \> Charlie -> I'm in New York today! Anyone wants to have a coffee?     
> \> Charlie follows Alice    
> \> Charlie wall    
> \> Charlie - I'm in New York today! Anyone wants to have a coffee? (2 seconds ago)    
> \> Alice - I love the weather today (5 minutes ago)    

> \> Charlie follows Bob    
> \> Charlie wall    
> \> Charlie - I'm in New York today! Anyone wants to have a coffee? (15 seconds ago)     
> \> Bob - Good game though. (1 minute ago)     
> \> Bob - Damn! We lost! (2 minutes ago)     
> \> Alice - I love the weather today (5 minutes ago)    

### Requisitos gerais

- A aplicação precisa usar o "console" para entrada e saída;
- Usuários submetem comandos à aplicação:
    - posting: \<user name> -> \<mensagem> 
    - reading: \<user name> 
    - following: \<user name> follows \<outro user> 
    - wall: \<user name> wall 
- **NOTE:** "posting:", "reading:", "following:" and "wall:" não são parte do comando. Todos os comandos são iniciados pelo nome do usuário.


### Entregas ###

- Primeira Entrega: **Posting**
- Segunda Entrega: **Reading**
- Terceira Entrega: **Following**
- Quarta Entrega: **Reading** ordenado por tempo
- Quinta Entrega: **Following** ordenado por tempo


## Sobre o Python

### Ambiente virtual ###

```bash
python3 -m venv venv
$ source venv/bin/activate
```

### Como executar ###

```bash
$ cd dojo
$ pytest
```

## Retrospectiva

### Sessão 1

The good :smiley::
- Apanhar junto
- TDD é top
- Local tranquilo
- Balinha daora 

The Bad :worried::
- pouco tempo por sessao


### Sessão 2

The good :smiley::
- Guide daora
- Problema adequado
- Balinha top
- Social antes do pair programming
- mestre mais ou menos
- ar condicionado
- evento 11/10

The Bad :worried::
- pouco tempo por sessao

[1]: https://github.com/sandromancuso/social_networking_kata