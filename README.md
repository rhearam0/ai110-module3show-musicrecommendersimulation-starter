# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real-world recommendation systems use different types of data to figure out what users might want to listen to next. For example, Spotify looks at things like a user's listening history, liked songs, playlists, and the characteristics of the songs they listen to. In this project, I am building a **content-based recommender**, which means the system recommends songs by comparing a user's preferences to the features of each song instead of comparing them to other users.

For example, if a user mostly listens to pop music, the recommender can recognize that they prefer the **pop** genre and suggest other pop songs. It can also compare features like **energy** to recommend songs with a similar intensity and **tempo** to find songs with a similar pace. **Mood** is another important feature because it helps match the overall vibe of the music. Although the dataset includes other features like **acousticness**, my recommender will mainly use **genre, mood, energy, and tempo** because I think those features best describe the kind of music someone is looking for.

Here is the scoring model:

Start each song with a score of 0.

If the song genre matches the user's favorite genre:
add 2.0 points

If the song mood matches the user's favorite mood:
add 1.0 point

Add energy similarity:
1 - abs(song energy - target energy)

Add tempo similarity:
1 - abs(song tempo - target tempo) / 100

After scoring every song:
sort songs from highest score to lowest score
recommend the top songs

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



