# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

- Implement one independent round in `determine_winner(player, computer)`, returning `win`, `lose`, or `tie` from the player's perspective. Keep the supplied interface and server; add no score or saved history.
- Prediction: the player chooses Rock and the computer chooses Paper. The player loses because Paper beats Rock. Return `lose` and display both choices with **Computer wins**. This valid losing round is a positive case.
- Add nine explicit unit outcomes from the expected-results table in `tests/test_game.py`, using literal expected answers.
- Add a real request/result integration test for Rock versus Paper, checking both choices and **Computer wins**. Fix only the computer's random choice; use the real winner rules.
- Reuse the supplied negative integration checks for an unsupported choice such as `Lizard` and a missing choice: return HTTP 400 with a helpful explanation without calling the rules.
- Add a real Chromium round and replay in `tests/e2e/test_round.py` using the supplied fixtures. Fix only the computer's choice; do not duplicate all nine cases in the browser.
- Mark tests `unit`, `integration`, or `e2e`. Run the full `.venv/bin/python check.py`, review the diff against this spec, discuss an actual test for Rock versus Paper, then review the game in the browser.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [RPS-001: Play a round](https://github.com/jasdeepn24/is218_rps_game/issues/1).
- Pull request / CI: add actual URLs when they exist.
- Implementation: [Winner rules](game.py) for one independent round, with the supplied interface and server unchanged.
- Checks (2026-11-02): full `.venv/bin/python check.py` passed Black, Pylint, 23 non-browser tests, and 6 Chromium tests. [Rule and request tests](tests/test_game.py) cover all nine literal outcomes and a real Rock-versus-Paper request. [Browser test](tests/e2e/test_round.py) covers that loss and replay as Scissors versus Paper. Positive tests fix only randomness. Reviewed the diff and new test files against this spec; supplied checks and settings are unchanged.
- Student browser review (2026-11-02): Scissors versus the computer's Paper displayed **You win!**; the student explained that Scissors beats Paper and reported selecting another move to play another round.
- Test explanation: the student explained that the Rock-versus-Paper unit test catches an incorrect `win` or `tie` return; Paper beats Rock, so any return other than `lose` fails the assertion.
- Keyboard review: the student used Tab to focus a move, saw the focused button, and pressed Enter to play successfully. Repeating Tab and Enter played another round successfully.
