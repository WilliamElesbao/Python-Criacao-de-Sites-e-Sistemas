$(document).ready(function() {

    var socket = io("192.168.0.104:5000") // IP da sua rede local + porta
    
    socket.on("connect", function() {
        console.log("estamos on!");
    });

    socket.on("message", function(data) {
        console.log("enviou mensagem");
        $("#lista_mensagens").append($('<p>').text(data));
        // Scroll to the bottom of the "lista_mensagens"
        $("#lista_mensagens").scrollTop($("#lista_mensagens")[0].scrollHeight);
    });

    $("#botao_enviar").on('click', function() {
        console.log("clicou no botao_enviar");
        socket.send($('#usuario').val() + ": " + $('#mensagem').val());
        $('#mensagem').val('');
    });
    
    $("#mensagem").on('keypress', function() {
        if (event.key === "Enter") {
            console.log("deu enter");
            socket.send($('#usuario').val() + ": " + $('#mensagem').val());
            $('#mensagem').val('');
        }
    });
});