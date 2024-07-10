songs = input().split()
num_commands = int(input())

for _ in range(num_commands):
    command = input().split(" * ")
    action = command[0]

    if action == "Add Song":
        song = command[1]
        if song not in songs:
            songs.append(song)
            print(f"{song} successfully added")

    elif action == "Delete Song":
        num_songs_to_delete = int(command[1])
        if num_songs_to_delete <= len(songs):
            deleted_songs = songs[:num_songs_to_delete]
            songs = songs[num_songs_to_delete:]
            print(f"{', '.join(deleted_songs)} deleted")

    elif action == "Shuffle Songs":
        index1 = int(command[1])
        index2 = int(command[2])
        if 0 <= index1 < len(songs) and 0 <= index2 < len(songs):
            songs[index1], songs[index2] = songs[index2], songs[index1]
            print(f"{songs[index1]} is swapped with {songs[index2]}")

    elif action == "Insert":
        song = command[1]
        index = int(command[2])
        if 0 <= index <= len(songs):
            if song not in songs:
                songs.insert(index, song)
                print(f"{song} successfully inserted")
            else:
                print("Song is already in the playlist")
        else:
            print("Index out of range")

    elif action == "Sort":
        songs.sort(reverse=True)

    elif action == "Play":
        print("Songs to Play:")
        for song in songs:
            print(song)