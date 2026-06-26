from logic_utils import check_guess

# NOTE: check_guess returns a TUPLE -> (outcome, message)
#   outcome:  "Win" | "Too High" | "Too Low"
#   message:  the hint text shown to the player (e.g. "📈 Go HIGHER!")
# So we unpack both parts and test each one separately.


def test_winning_guess():
    # If the secret is 50 and the guess is 50, the outcome should be "Win".
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_outcome():
    # Guess (60) is greater than the secret (50) -> outcome should be "Too High".
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low_outcome():
    # Guess (40) is less than the secret (50) -> outcome should be "Too Low".
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# Bug fix: the hint MESSAGES were swapped.
#   - "Too High" used to say "Go HIGHER!" (wrong) -> should tell you to go LOWER.
#   - "Too Low"  used to say "Go LOWER!"  (wrong) -> should tell you to go HIGHER.
# These tests lock in the corrected direction so the bug can't come back.
# ---------------------------------------------------------------------------


def test_too_high_message_says_go_lower():
    # When the guess is too high, the player must go DOWN to reach the secret.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_message_says_go_higher():
    # When the guess is too low, the player must go UP to reach the secret.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_specific_case_85_vs_87():
    # The exact case reported: guess 85, secret 87.
    # 85 is lower than 87, so the hint must say "Go HIGHER!", not "Go LOWER!".
    outcome, message = check_guess(85, 87)
    assert outcome == "Too Low"
    assert "HIGHER" in message
