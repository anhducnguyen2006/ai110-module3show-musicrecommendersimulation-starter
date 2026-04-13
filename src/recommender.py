from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into typed song dictionaries."""
    print(f"Loading songs from {csv_path}...")
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a weighted relevance score and explanation reasons for one song."""
    score = 0.0
    reasons: List[str] = []

    # Finalized categorical weights from the algorithm recipe.
    genre_points = 1.5
    mood_points = 2.0

    favorite_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    favorite_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))

    if favorite_genre and song.get("genre") == favorite_genre:
        score += genre_points
        reasons.append(f"genre match (+{genre_points:.1f})")

    if favorite_mood and song.get("mood") == favorite_mood:
        score += mood_points
        reasons.append(f"mood match (+{mood_points:.1f})")

    def similarity_points(
        feature_name: str,
        target: Optional[float],
        song_value: Optional[float],
        weight: float,
        range_width: float = 1.0,
    ) -> float:
        if target is None or song_value is None:
            return 0.0

        distance = abs(song_value - target) / range_width
        similarity = max(0.0, 1.0 - distance)
        points = weight * similarity
        reasons.append(
            f"{feature_name} closeness {similarity:.2f} (+{points:.2f})"
        )
        return points

    # Weighted numeric similarity points from the algorithm recipe.
    score += similarity_points(
        "energy",
        user_prefs.get("target_energy", user_prefs.get("energy")),
        song.get("energy"),
        weight=1.2,
    )
    score += similarity_points(
        "valence",
        user_prefs.get("target_valence", user_prefs.get("valence")),
        song.get("valence"),
        weight=0.9,
    )
    score += similarity_points(
        "danceability",
        user_prefs.get("target_danceability", user_prefs.get("danceability")),
        song.get("danceability"),
        weight=0.7,
    )
    score += similarity_points(
        "acousticness",
        user_prefs.get("target_acousticness", user_prefs.get("acousticness")),
        song.get("acousticness"),
        weight=0.7,
    )
    score += similarity_points(
        "tempo",
        user_prefs.get("target_tempo_bpm", user_prefs.get("tempo_bpm")),
        song.get("tempo_bpm"),
        weight=0.5,
        range_width=120.0,
    )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score, rank, and return the top-k song recommendations."""
    scored: List[Tuple[Dict, float, str]] = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return ranked[:k]
