from music import Music

if __name__ == "__main__":
    
    song = Music('Us', 'Gracie Abrams', 'The Secret of Us', 3.2)
    print(song.listen())
 
    another_song = Music('Blinding lights', 'The Weekend', 'After Hours', 3.5)
    print(another_song.listen())
