import socket
import threading

HOST = '127.0.0.1'
PORT = 5060
room_counter = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

players = []
available_rooms = {}
active_rooms = {}


def handle_before_game(player):
    global room_counter
    while True:
        try:
            operation_type, data = player.recv(1024).decode('utf-8').split('_')
            if operation_type == 'create':
                available_rooms[room_counter] = {'word': data, 'riddler': player, 'room_id': room_counter}
                player.send(f"{room_counter}".encode('utf-8'))
                room_counter += 1
            elif operation_type == 'join':
                room_id = int(data)
                if room_id in available_rooms:
                    active_rooms[room_id] = {'guesser': player,
                                             'riddler': available_rooms[room_id]['riddler']}
                    player.send(f"success_{room_id}_{available_rooms[room_id]['word']}".encode('utf-8'))
                    available_rooms.pop(room_id)
                    thread = threading.Thread(target=handle_curr_game, args=(room_id, player))
                    thread.start()
                    break
                else:
                    player.send('error_none_none'.encode('utf-8'))
        except Exception as exc:
            print(f"{player} leave (with Exception{exc})")
            players.remove(player) if player in players else None
            break


def handle_curr_game(room_id, guesser_player):
    room_id = int(room_id)
    while True:
        try:
            message = guesser_player.recv(1024).decode('utf-8')
            if message == 'leave':
                players.remove(active_rooms[room_id]['guesser'])
                players.remove(active_rooms[room_id]['riddler'])
                active_rooms.pop(room_id)

                print(players)
                break
            active_rooms[room_id]['riddler'].send(message.encode('utf-8'))
        except Exception as exc:
            print(f"{guesser_player} leave (with Exception: {exc})")
            players.remove(active_rooms[room_id]['guesser'])
            players.remove(active_rooms[room_id]['riddler'])
            active_rooms.pop(room_id)
            break


def receive():
    while True:
        player, address = server.accept()
        players.append(player)
        print("New player connect")
        print(player)
        thread = threading.Thread(target=handle_before_game, args=(player,))
        thread.start()


if __name__ == "__main__":
    receive()
