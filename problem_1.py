import csv
import sys

def main():
    "Точка входа программы"
    name = sys.stdin.read().strip()
    rows = [["track_name", "streams", "date"]]
    with open('songs.txt', encoding='utf8') as file:
        lines = [line for line in file.read().strip().split('\n')]
        for line in lines:
            streams, artist_name, track, date = line.split('?')
            if artist_name == name:
                print(track, streams, date)
                rows.append([track, streams, date])

    with open('songs_artst.csv', 'w') as file:
        w = csv.writer(file)
        w.writerows(rows)

main()