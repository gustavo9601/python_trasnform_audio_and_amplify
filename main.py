from pydub import AudioSegment
import logging
import glob

"""
Init Settings
"""
AudioSegment.converter = "C:\\audio\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\audio\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\audio\\ffmpeg\\bin\\ffprobe.exe"

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: | mensaje: [%(message)s] | fecha_ejecucion: [%(asctime)s]',
    datefmt='%d/%m/%y - %H:%M:%S',
    filename='./logs/log.txt'
)


# song = AudioSegment.from_file('audio.m4a')


def get_files_folder(path: str = 'files/in/', pattern: str = '*.m4a'):
    logging.info('Getting files from folder')
    return glob.glob(path + pattern)


def create_song_file(filename: str):
    logging.info(f'Creating file song [{filename}]')
    return AudioSegment.from_file(filename)


def add_loud_song_file(file, loud: int = 15, filename='audio.mp3'):
    logging.info(f'Add loud song [{filename}]')
    return file + loud

def export_file_song(file, path: str = 'files/out/', filename: str = 'audio.mp3', format='mp3', bitrate='312k'):
    logging.info(f'Exporting song [{filename}]')
    file.export(path + filename, format=format, bitrate=bitrate)

if __name__ == '__main__':
    songs = get_files_folder()

    for song in songs:
        new_song = create_song_file(song)
        louder_song = add_loud_song_file(new_song, filename=song[9:])
        export_file_song(louder_song, path= 'files/out/', filename=song[9:])

# louder_song = song + 15
# louder_song.export('audio_full.mp3', format='mp3', bitrate='312k')
