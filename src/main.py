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


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Default demo profile for verification in this module.
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo_bpm": 122,
        "target_valence": 0.82,
        "target_danceability": 0.80,
        "target_acousticness": 0.22,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 72)
    print("Top Recommendations")
    print("=" * 72)
    print(
        "Profile: "
        f"genre={user_prefs['favorite_genre']}, "
        f"mood={user_prefs['favorite_mood']}, "
        f"target_energy={user_prefs['target_energy']:.2f}"
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


if __name__ == "__main__":
    main()
