# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

   The Game's Purpose is to propmt the user to find the secret number, providing hints of "lower" or "higher" after each input, keeping track of all user inputs. Until the user enters the correct secret number.

- [x] Detail which bugs you found.

   1. I noticed when I first loaded in, for some reason, one of my attempts was already used up even before entering a guess.

   2. I also noticed hints provided were incorrect and misleading the user to the wrong direction of the secret number.

   3. I also noticed Attempts not being tracked after each submission.

- [x] Explain what fixes you applied.

   1. Had to remove a line and move it else where, as it was not tracking attempts properly. And using an attempt on load.

   2. Had AI move game logic functions to the correct location and had it suggest a fix for the "Higher" "Lower" Gltich. Was able to fix it by swapping the way it returned "Too Low" and "Go Higher".


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User Loads in with a correct initial amount of attempts
2. User enter 12 (secret is 15)
3. Game returns "Go Higher"
4. Attempts is updated (-1)
5. User enters 17 (secret is 15)
6. Game returns "Go Lower"
7. Attemps is updated (-1)
8. User enters 15 (secret is 15)
9. Game returns "Winner"

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/

===================================================================================== test session starts =====================================================================================
platform win32 -- Python 3.13.12, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\ariel\OneDrive\Documents\CodePath\AI110\Project-GameGlitchInvestigator\ai110-Project1-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 6 items                                                                                                                                                                              

tests\test_game_logic.py ......                                                                                                                                                          [100%]

====================================================================================== 6 passed in 0.08s ======================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
