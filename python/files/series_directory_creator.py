import os

root_path = (
    r"D:\Downloads\Torchwood (2006)  (1080p BluRay x265 HEVC AAC 5.1 ByteShare) [UTR]"
)
series = "\\Torchwood"
seasons = 4
suffix = "1080p BluRay x265 HEVC AAC 5.1 ByteShare-UTR".replace(
    " ", "."
)  # no dot in front
dirs = []


def create_seasons():
    for season in range(1, seasons + 1):
        dirs.append(
            root_path + series.replace(" ", ".") + ".S0" + str(season) + "." + suffix
        )
    return dirs


create_seasons()


def create_dirs():
    for directory in dirs:
        os.mkdir(directory)


create_dirs()
