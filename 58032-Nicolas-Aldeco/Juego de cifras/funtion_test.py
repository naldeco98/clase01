
def ComputerVsMachine(self):
    guest = ''
    guest_list_all_digits = ['0000','1111','2222','3333','4444','5555','6666','7777','8888','9999']
    ct = 0
    guest = guest_list_all_digits[ct]
    ct += 1
    return 'Is your number '+guest+'?'

def main():
    while True:
        clue = input('>>')
        ans = ComputerVsMachine(clue)
        print (ans)

main()