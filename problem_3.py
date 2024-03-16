def main():
    "Точка входа программы"
    while True:
        track_name = input("Введите название песни: ")
        if track_name == '0': break

        with open('songs.txt', encoding='utf8') as file:
            lines = [line for line in file.read().strip().split('\n')]
            lines = lines[1:]
            got = False
            for line in lines:
                streams, artist, track, date = line.split('?')
                if track == track_name:
                    got = True
                    print(artist)
                    break

            if got == False: print('К сожалению, ничего не удалось найти')


main()