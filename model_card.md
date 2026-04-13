# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This model suggests songs from a small catalog based on a user's taste profile.
It is built for classroom exploration, not for real users.
It assumes the user wants songs that match mood, genre, and vibe.

---

## 3. How the Model Works

The model looks at genre, mood, energy, tempo, valence, danceability, and acousticness.
It compares each song to the user's target preferences.
It gives points for exact genre and mood matches.
It also gives points when the numeric features are close to the user's target.
Songs with the highest total score are ranked first.
I changed the starter logic by making the score more detailed and by adding explanations for each result.

---

## 4. Data

The catalog has 18 songs.
The dataset includes pop, lofi, rock, ambient, jazz, synthwave, hip hop, rnb, country, reggaeton, classical, metal, deep house, and dream pop.
The moods include happy, chill, intense, relaxed, moody, focused, confident, romantic, nostalgic, playful, peaceful, aggressive, euphoric, and dreamy.
I added extra songs to make the catalog more diverse.
The dataset is still small, so it does not cover every style of music.

---

## 5. Strengths

The model works well when the user wants a clear vibe match.
It gives good results for profiles like Happy Pop, Chill Lofi, and Deep Intense Rock.
It is easy to understand because the score is based on simple rules.
It also explains why each song was chosen.

---

## 6. Limitations and Bias

The model can create a small filter bubble.
It may keep returning songs that match the same mood or energy level.
It ignores the `likes_acoustic` field in the current scoring logic.
That means one user preference is stored but not really used.
The small catalog can also make the same songs appear too often.

---

## 7. Evaluation

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and two edge cases.
I checked whether the top songs matched the user vibe.
I compared the outputs before and after changing the weights.
I was surprised that Gym Hero still ranked high for Happy Pop because it is upbeat and energetic.
The edge cases helped show how the model handles conflicting preferences.

---

## 8. Future Work

I would add the `likes_acoustic` preference to the score.
I would also add more songs so the results are less repetitive.
I would try a diversity rule so the top results are not too similar.

---

## 9. Personal Reflection

I learned that recommenders are often simple rule systems with weights behind them.
I also learned that small changes in weights can change the ranking a lot.
It was interesting to see how a song can look "wrong" by genre but still feel right by energy and mood.
This made me think more about how music apps balance accuracy, variety, and user taste.