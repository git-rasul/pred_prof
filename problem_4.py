
def main():
    "Точка входа программы"
    with open('songs.txt', encoding='utf8') as file:
        lines = [line for line in file.read().strip().split('\n')]
        lines = lines[1:]

        songs = []
        artists = {}
        for line in lines:
            streams, artist, track, date = line.split('?')
            if artist not in artists: artists[artist] = []
            artists[artist].append(int(streams))

            day, month, year = [int(i) for i in date.split('.')]
            if year < 1990: songs.append(track)

        print(songs)

        averages = {}
        for a in artists:
            averages[a] = sum(artists[a])//len(artists[a])


        sorted_averages = sorted(averages, key=lambda x: averages[x])
        for a in reversed(sorted_averages):
            print(f'{a}: {averages[a]}')




main()
