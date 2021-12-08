from BobPyKit import AnimeApp

anime = AnimeApp.Anime()

name, _id, links = anime.anime_search("Platinum End")

print(f"{name[0]}, {_id[0]}, {links[0]}")