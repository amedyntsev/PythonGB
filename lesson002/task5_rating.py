# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating = []
while True:
    ratingValue = input("Введите элемент рейтинга (или exit для выхода): ")
    if ratingValue == "exit":
        break
    if not ratingValue.isdigit() or ratingValue == '':
        continue

    ratingValue = int(ratingValue)
    pointer = 0
    while True:
        if len(rating) < 1:
            rating.append(ratingValue)
            break
        else:
            if ratingValue > rating[pointer]:
                rating.insert(pointer,ratingValue)
                break
            else:
                if (pointer + 1) == len(rating):
                    rating.append(ratingValue)
                    break
                else:
                    pointer += 1
                    continue
    print(f"Рейтинг: {rating}")
print(f"Итоговый рейтинг: {rating}")
            