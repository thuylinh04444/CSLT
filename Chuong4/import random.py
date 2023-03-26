import random

# Hàm này để hỏi người chơi lựa chọn búa, bao hay kéo.
def player_choice():
    choice = input("Bạn chọn gì? (búa, bao, kéo): ")
    while choice not in ['búa', 'bao', 'kéo']:
        choice = input("Bạn chọn gì? (búa, bao, kéo): ")
    return choice

# Hàm này để chọn lựa trường hợp của máy.
def computer_choice():
    choice = random.choice(['búa', 'bao', 'kéo'])
    return choice

# Hàm này để xác định người chiến thắng.
def determine_winner(player, computer):
    if player == computer:
        return "Hòa!"
    elif player == 'búa' and computer == 'kéo':
        return "Bạn thắng!"
    elif player == 'bao' and computer == 'búa':
        return "Bạn thắng!"
    elif player == 'kéo' and computer == 'bao':
        return "Bạn thắng!"
    else:
        return "Máy thắng!"

# Hàm chính để chơi trò chơi kéo búa bao.
def play_game():
    print("Chào mừng đến với trò chơi kéo búa bao!")
    print("Bạn và máy tính sẽ lần lượt chọn một trong ba lựa chọn.")
    print("Búa đánh bại kéo, kéo đánh bại bao, bao đánh bại búa.")
    print("Chúc may mắn!")
    
    play_again = 'có'
    while play_again.lower() in ['có', 'yes', 'y']:
        player = player_choice()
        computer = computer_choice()
        print("Bạn chọn: ", player)
        print("Máy tính chọn: ", computer)
        print(determine_winner(player, computer))
        play_again = input("Bạn muốn chơi lại không? (có/không): ")

# Chạy hàm chính để chơi trò chơi.
play_game()