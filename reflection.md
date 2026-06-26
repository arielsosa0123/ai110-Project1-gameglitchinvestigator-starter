# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  First time running the game an attempt ws used up. When pressing new game, it reset the attemps to normal.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. The hints were not displaying at all.
  2. Attempts are not being Tracked.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior         | Actual Behavior                     | Console Output / Error |
|-------|---------------------------|-------------------------------------|------------------------|
|   43  | HINTS shown                   Not shown                              None
|   69  | Attemps tracked               Not Tracked                            None
|   19  | (Easy) Range 1 to 20          (Easy) Range 1 to 100                  None
|   21  | Indication of Correct Guess   No indication of Correct Guess         None
|   12  | Input Box remains White       Input box remains red when clicked     None
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used Cluade AI for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  Claude suggested the fix for the glitch I first encountered which was the attempt counter. I carefully looked through the code to make sure if the issue was within this area.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I asked claude to assist me with fixing the check_guess function and move into the logic_utils.py file. But as it did that it simplified the code by removing the try except feature it originally had. I did not like that, and asked to fix it while maintaining it's orginal layout.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  Well, I ran the tests AI made for me which all passed, then I opened the game and tested it myself to make sure all was well.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I tested the Attempt tracking manually on all modes to make sure there were no extra issues. After using pytest.

- Did AI help you design or understand any tests? How?

  Yes AI helped me do both, designing a structure of the test and providing a deeper understanding of what is being tested and why. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
