# Othello
   Trabalho 2 sobre poda alfa-beta do curso de Inteligência Artificial. Nele, é implementado agente capaz de jogar Othello (também conhecido como Reversi).
## Função de avaliação
A forma final do projeto usa como função de avaliação a condição de vitória, contando a quantidade de peças no tabuleiro da cor que está sendo jogada.
## Estratégia de parada
   A estratégia de parada adotada é baseada no limite de tempo para realização da jogada (considerando que ele seja de 5s). Para cada execução das funções min ou max do algoritmo de mini-max, o nó é considerado um nó folha (sendo portanto avaliado pela função de avaliação para que em seguida o melhor movimento seja escolhido) caso não haja estados sucessores, ou caso já tenham se passado 4 segundos ou mais desde o início da execução da função de realizar movimento. 
   
   O valor 4 segundos foi decidido experimentalmente, pois observou-se que o intervalo de tempo de aproximadamente 1 segundo para avaliar os nós e retornar o melhor movimento é um intervalo de tempo seguro para que o agente não perca a vez. Essa estratégia se comprovou mais eficaz do que outras estratégias implementadas, discutidas nas próximas seções.
## Decisões de projeto
   Algoritmo de minimax com poda alfa-beta. Estratégia de parada baseada em tempo e detalhada na seção acima.
## Dificuldades encontradas
   A versão inicial do bot com poda alfa-beta não era capaz de vencer o agente que apenas faz movimentos randômicos, uma vez que ele constantemente excedia o tempo limite de cada jogada. A estratégia de parada por profundidade foi facilmente implementada, porém para valores altos o bot consistentemente também perdia a vez por exceder o limite de tempo. Em testes realizados, foi observado que a profundidade 3 costumava conseguir efetuar todos os lances, mas o nível de jogo ainda não parecia alto.
   
   Um outro ponto em que houve dificuldade foi em atualizações de código seguintes implementar a estratégia de parada por tempo. A ideia inicial foi de dividir recursivamente tempo para cada chamada da função, de acordo com o tempo máximo. Contudo, o código implementado não foi capaz de vencer a versão com parada por profundidade, então por limites de tempo uma estratégia por tempo diferente foi utilizada. 
## Melhorias eventuais
   O método escolhido para condição de parada por tempo encerra computação sequencial imediatamente quando o tempo é esgotado, o que garante que o agente não perca a sua jogada, porém faz com que a exploração da árvore de possibilidades seja assimétrica. Assim, uma possível melhoria futura seria permitir cálculos de tempo uniformes para cada ramo.
### Integrantes
- Anderson Souza de Oliveira - Turma A - Matrícula 233042
- Ernesto Vaz de Oliveira - Turma A - Matrícula 302470
- Ricco Soares - Turma A - Matricula 307968

