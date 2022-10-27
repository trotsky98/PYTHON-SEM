from telegram.ext import ConversationHandler

wins = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
field = list(range(1, 10))
x = chr(10060)
o = chr(11093)
cells = 9
NEXT = 0
PLAY = 1

def printField(field):
    row = ''
    for i in range(len(field)):
        if not i % 3:
            row += f'\n\n'
        row += f'{field[i]:^10}'
    return row

def isWin(feild):
    for i in wins:
        if feild[i[0]] == feild[i[1]] == feild[i[2]]:
            return True
    return False

def help(update, _):
     update.message.reply_text("/start - для начала игры\n/cancel - для отмены игры\n Можешь выбрать, кто ходит пермым лат.буквами 'x' и 'o'\nцифрами от 1 до 9 указывай куда хочешь ходить. ")


def start(update, _):
    update.message.reply_text(f'Привет, {update.effective_user.first_name}, это игра в крестики-нолики\nКто будет ходить первый?\n (лат.бук.)x - крестик, o - нолик:')
    return NEXT

def turn(update, _):
    global xo
    next = update.message.text
    update.message.reply_text(printField(field))
    if next not in 'o x':
        update.message.reply_text(f"Некорректный ввод{chr(9940)}")
    else:
        if next=='x':
            xo=x
            update.message.reply_text(f'Первыми ходят {chr(10060)}')
            return PLAY
        if next=='o':
            xo=o
            update.message.reply_text(f'Первыми ходят {chr(11093)}')
            return PLAY

def game(update, _):
    global xo, cells
    next = update.message.text
    next = int(next)
    if next not in field:
        update.message.reply_text(f"Некорректный ввод{chr(9940)}")
    else:
        field.insert(field.index(next), xo)
        field.remove(next)
        update.message.reply_text(printField(field))
        if isWin(field):
            update.message.reply_text(f"{xo} - Победитель {chr(127942)}")
            return ConversationHandler.END
        xo = o if xo == x else x
        cells -= 1
    if cells == 0:
        update.message.reply_text(f"Ничья {chr(129309)}")
        return ConversationHandler.END

def cancel(update, _):
    update.message.reply_text('Пока')
    return ConversationHandler.END