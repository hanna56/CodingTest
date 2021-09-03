def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        try:
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False   
        except:
            return True
