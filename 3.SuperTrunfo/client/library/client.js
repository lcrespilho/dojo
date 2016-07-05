var RaccoonSuperTrunfo = function(){
    var host = 'localhost';
    var port = '8890'
    var path = ''
    var socket
    var player_id

    waitForConnection = function (callback, interval) {
        if (socket.readyState === 1) {
            console.log("Ready!");
            callback();
        } else {
            console.log("Not ready yet");
            var that = this;
            setTimeout(function () {
                that.waitForConnection(callback, interval);
            }, interval);
        }
    };

    var send = function(message){
        waitForConnection(function () {socket.send(JSON.stringify(message));}, 200);
    };

    var init = function(session_id, player_id_in){
        player_id = player_id_in

        socket = new WebSocket('ws://'+host+':'+port+path);

        socket.onopen = function(){
            console.log("On open")
        }

        send({"session_id": "session_id", "player_id": player_id})
        send({"action": "player_joined", "player_id": player_id})
        console.log("Trying to connect to game server.")

        socket.onmessage = function (event){
            var received_msg = event.data;
            console.log("Received: " + received_msg)
        };
    };

    var public_stuff = {
        'init': function(user_id, session_id){init(user_id, session_id);},
        'send': function(message){send(message);}
    };

    return public_stuff;
}();