# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

#NAME: VIBECHECK 6.7

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

VibeCheck 6.7 is designed to suggest songs that match a user’s mood, genre taste, energy level, and acoustic preferences. It is meant for people who want quick, simple music recommendations for personal listening or classroom exploration.

---

## 3. How the Model Works  

VibeCheck 6.7 looks at a few simple features for each song, like genre, mood, energy level, and how acoustic it sounds. It also looks at the user’s favorite genre, preferred mood, target energy, and whether they like acoustic songs. The system gives points when a song matches those preferences, and songs with more matching points rise to the top. I changed the original setup by making energy matter more, so songs that feel more energetic or less energetic depending on the user’s taste now have a bigger effect on the final recommendation.

---

## 4. Data  

The model uses a small catalog of 17 songs with a mix of genres and moods, including pop, lofi, rock, jazz, electronic, ambient, and indie pop. The dataset includes both upbeat and calm songs, so it is useful for testing how the recommender reacts to different energy levels and moods. I did not add or remove any songs, so the results are shaped by the size and variety of this catalog. One limitation is that the dataset does not cover every kind of musical taste, especially more specific genres or cultural styles.

---

## 5. Strengths  

This system works best for simple, clear taste profiles, like someone who wants happy, high-energy pop or someone who wants calm, low-energy music. It does a good job picking up obvious matches between a user’s mood and the mood of a song, and it also responds well when the user prefers more acoustic or less acoustic music. The recommendations often feel reasonable when the user profile is straightforward and the song choices are easy to compare.

---

## 6. Limitations and Bias 

The system struggles with having a lack of diversity when it comes to reccomending music. For example, it is seen how the top results can feel very similar to one another which makes the system feel repetive rather than exploratory. Also the scoring is narrow meaning it only uses a few attrbutes and ignores other useful signals like artist familiarity or tempo which are factors that can affect the reccomemdations. 
Prompts:  

---

## 7. Evaluation  

I tested a few different user profiles to see whether the recommender was behaving in a way that actually made sense. First, I tried a user who liked pop, happy, high-energy songs, since that felt like the most obvious match for the scoring logic. I also tested a more chill user who preferred lower-energy music, and one who liked acoustic songs, just to see if the system could shift its recommendations in a more noticeable way.  

What surprised me most was how much the energy weighting changed the results. Once I increased its importance, songs with the right energy level started ranking really strongly, even when they did not match the genre as closely. That made the recommendations feel a little less intuitive than I expected, because the system seemed to care a lot about one feature at the expense of others. I also noticed that some of the top results still felt pretty similar, even when the user profile changed, which made me realize the recommender is good at matching obvious preferences but still a bit limited when it comes to variety.

- Happy Pop profile vs. Chill Low-Energy profile: the happy pop profile leaned toward upbeat songs, while the chill profile moved toward softer, slower picks. That makes sense because the system is responding to the energy level and mood, not just the genre label.
- Happy Pop profile vs. Acoustic profile: the happy pop profile still preferred brighter, more energetic songs, while the acoustic profile shifted toward songs with lower energy and more acoustic texture. This felt like a fair result because the acoustic preference is pushing the model in a more mellow direction.
- Chill Low-Energy profile vs. Acoustic profile: both of these profiles pulled toward calmer songs, but the acoustic profile was even more focused on songs that sounded more natural and less punchy. That makes sense because the acoustic setting is acting like an extra signal for softness and warmth.

One thing that stood out to me was why the “Gym Hero” song kept showing up for people who just wanted “Happy Pop.” It has the pop label and very high energy, so it gets boosted strongly even if the user is really only asking for a cheerful, upbeat vibe. In other words, the system is not just picking songs that are “happy pop” in the most obvious sense — it is also being pulled by the energy score, which can make some surprising songs rise to the top.

---

## 8. Future Work  

I would improve the model by giving it more features to understand what a person really likes. For example, it could look at whether someone prefers songs with more danceability, whether they like covers, or whether they enjoy different styles like classical music. I think this would make the recommendations feel more personal and less limited. I would also want the system to explain its choices better and to include more variety in the top results so it does not feel repetitive.

---

## 9. Personal Reflection  

I learned a lot about how music recommendations actually work. Since I listen to music all the time, it was really interesting to see how songs get chosen and why certain ones appear in playlists. One thing that stood out to me was how many different features are used to figure out whether someone might like a song, even when the system is using simple scoring. This definitely changed the way I think about apps like Spotify, because it made me realize how much work goes on behind the scenes to create a smooth and personalized experience.