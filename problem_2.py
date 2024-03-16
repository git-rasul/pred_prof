def main():
    "Точкка входа программы"
    with open('songs.txt', encoding='utf8') as file:
        lines = [line for line in file.read().strip().split('\n')]
        lines = lines[1:]
        for i, line in enumerate(lines): lines[i] = line.split('?')

        sorted = selection_sort(lines, lambda x: x[1].upper())
        for i in range(5):
            streams, artist, track, date = sorted[i]
            print(f'{track},{artist},{date}')

def selection_sort(lines, key):
    """Данная функция осуществляет сортировку сложностью O(N^2)
    поданного на вход массиво по значениям функции ключа

    Описание аргументов:
    lines - массив с данными о аристах
    key - функция-ключ
    """
    keys = [key(x) for x in lines]
    ids = [i for i in range(len(lines))]

    for i in range(len(ids)):
        min_id = i
        for j in range(i, len(ids)):
            if keys[j] < keys[min_id]: min_id = j

        keys[i], keys[min_id] = keys[min_id], keys[i]
        ids[i], ids[min_id] = ids[min_id], ids[i]

    res = []
    for i in ids: res.append(lines[i])

    return res

main()