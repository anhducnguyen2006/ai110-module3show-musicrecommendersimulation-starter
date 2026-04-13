"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, recommendations: list) -> None:
    """Print a clean recommendation block for one profile."""
    print("\n" + "=" * 72)
    print(f"Profile: {profile_name}")
    print("=" * 72)
    print(
        "Prefs: "
        f"genre={user_prefs['favorite_genre']}, "
        f"mood={user_prefs['favorite_mood']}, "
        f"energy={user_prefs['target_energy']:.2f}, "
        f"tempo={user_prefs['target_tempo_bpm']:.0f}, "
        f"valence={user_prefs['target_valence']:.2f}"
    )
    print("-" * 72)

    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reason_items = [part.strip() for part in explanation.split(";") if part.strip()]

        print(f"{idx}. {song['title']} — {song['artist']}")
        print(f"   Final score: {score:.2f}")
        print("   Reasons:")
        for reason in reason_items:
            print(f"   - {reason}")
        print("-" * 72)


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        (
            "High-Energy Pop",
            {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.85,
                "target_tempo_bpm": 126,
                "target_valence": 0.84,
                "target_danceability": 0.82,
                "target_acousticness": 0.18,
                "likes_acoustic": False,
            },
        ),
        (
            "Chill Lofi",
            {
                "favorite_genre": "lofi",
                "favorite_mood": "chill",
                "target_energy": 0.38,
                "target_tempo_bpm": 76,
                "target_valence": 0.60,
                "target_danceability": 0.58,
                "target_acousticness": 0.82,
                "likes_acoustic": True,
            },
        ),
        (
            "Deep Intense Rock",
            {
                "favorite_genre": "rock",
                "favorite_mood": "intense",
                "target_energy": 0.92,
                "target_tempo_bpm": 150,
                "target_valence": 0.45,
                "target_danceability": 0.63,
                "target_acousticness": 0.12,
                "likes_acoustic": False,
            },
        ),
        (
            "Edge Case: High Energy + Moody",
            {
                "favorite_genre": "ambient",
                "favorite_mood": "moody",
                "target_energy": 0.92,
                "target_tempo_bpm": 68,
                "target_valence": 0.30,
                "target_danceability": 0.35,
                "target_acousticness": 0.88,
                "likes_acoustic": True,
            },
        ),
        (
            "Edge Case: Contradictory Dance vs Acoustic",
            {
                "favorite_genre": "classical",
                "favorite_mood": "aggressive",
                "target_energy": 0.55,
                "target_tempo_bpm": 140,
                "target_valence": 0.40,
                "target_danceability": 0.92,
                "target_acousticness": 0.92,
                "likes_acoustic": True,
            },
        ),
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(profile_name, user_prefs, recommendations)


if __name__ == "__main__":
    main()
