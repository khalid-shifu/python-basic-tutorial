from dataclasses import dataclass

@dataclass
class AnimeData:
    id : str
    title : str
    genre : str
    rating : float = 0.0
    episodes : int = 0
    is_completed : bool = False


    def __str__(self):
        return f"id: {self.id}, title: {self.title}, genre: {self.genre}, rating: {self.rating}, episodes: {self.episodes}, is_completed: {self.is_completed}"