Trabalho de Redes de Computadores para Automação

Natan Kanitz e Guilherme Batista

Programação socket usando TCP ou UDP

Conceitos:

API Socket - Biblioteca feita para comunicação com a internet (TCP), Objetos com várias funções para Servidor ou Cliente.

    Procedimento exemplo:
      1) Servidor cria um socket e espera um request para responder;
      2) Cliente cria um socket e se conecta ao servidor através da função connect(IP, porta);
      3) Servidor cria um socket específico para atender cada cliente (permite a conexão com vários clientes ao mesmo tempo);
      4) Há vários métodos de comunicação entre sockets. O abordado no trabalho será com send() e recv(). O socket do cliente envia a mensagem com a função send() enquanto o servidor aguarda a mensagem com a função recv(). Quando o servidor estiver pronto para responder, as funções se invertem;
