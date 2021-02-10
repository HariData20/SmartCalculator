def tracklist(**tracks1):
    for artist, albums in tracks1.items():
        print(artist)
        for album, song in albums.items():
            print(f'ALBUM: {album} TRACK: {song} ')

