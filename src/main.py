"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.
"""

from pathlib import Path
import sys

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from recommender import load_songs, recommend_songs
else:
    from .recommender import load_songs, recommend_songs


def print_profile_results(songs, profile_name: str, user_prefs: dict, k: int = 5) -> None:
    print(f"\n=== {profile_name} ===")
    print(f"User preferences: {user_prefs}")
    recommendations = recommend_songs(user_prefs, songs, k=k)

    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{index}. {song['title']}")
        print(f"   Score: {score:.2f}")
        print(f"   Why: {explanation}")
        print("-" * 40)


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    songs = load_songs(str(project_root / "data" / "songs.csv"))

    profiles = [
        ("Starter example", {"genre": "pop", "mood": "happy", "energy": 0.8}),
        (
            "Conflicting mood and energy",
            {"genre": "pop", "mood": "sad", "energy": 0.9, "likes_acoustic": False},
        ),
        (
            "Genre-mood mismatch",
            {"genre": "rock", "mood": "happy", "energy": 0.2, "likes_acoustic": True},
        ),
        (
            "Extreme boundary profile",
            {"genre": "jazz", "mood": "chill", "energy": 1.0, "likes_acoustic": True},
        ),
        (
            "Empty or weak preferences",
            {"genre": "", "mood": "", "energy": 0.5, "likes_acoustic": False},
        ),
        (
            "Trap profile",
            {"genre": "hip-hop", "mood": "sad", "energy": 0.1, "likes_acoustic": True},
        ),
    ]

    for profile_name, user_prefs in profiles:
        print_profile_results(songs, profile_name, user_prefs)


if __name__ == "__main__":
    main()
