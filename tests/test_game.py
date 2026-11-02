"""RPS-001 outcomes and a submitted round using the real rules."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
def test_rock_against_rock():
    """Matching Rock moves tie."""
    assert determine_winner("rock", "rock") == "tie"


@pytest.mark.unit
def test_rock_against_paper():
    """The player's Rock loses to the computer's Paper."""
    assert determine_winner("rock", "paper") == "lose"


@pytest.mark.unit
def test_rock_against_scissors():
    """Rock beats Scissors."""
    assert determine_winner("rock", "scissors") == "win"


@pytest.mark.unit
def test_paper_against_rock():
    """Paper beats Rock."""
    assert determine_winner("paper", "rock") == "win"


@pytest.mark.unit
def test_paper_against_paper():
    """Matching Paper moves tie."""
    assert determine_winner("paper", "paper") == "tie"


@pytest.mark.unit
def test_paper_against_scissors():
    """Paper loses to Scissors."""
    assert determine_winner("paper", "scissors") == "lose"


@pytest.mark.unit
def test_scissors_against_rock():
    """Scissors loses to Rock."""
    assert determine_winner("scissors", "rock") == "lose"


@pytest.mark.unit
def test_scissors_against_paper():
    """Scissors beats Paper."""
    assert determine_winner("scissors", "paper") == "win"


@pytest.mark.unit
def test_scissors_against_scissors():
    """Matching Scissors moves tie."""
    assert determine_winner("scissors", "scissors") == "tie"


@pytest.mark.integration
def test_submitted_rock_loses_to_paper(monkeypatch):
    """A real request displays the predicted loss and both actual choices."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})
    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert '<p class="choice-label">You chose</p><p class="choice-value">Rock ' in page
    assert (
        '<p class="choice-label">Computer chose</p><p class="choice-value">Paper '
        in page
    )
    assert 'data-outcome="lose"' in page
    assert '<h2 id="game-heading">Computer wins</h2>' in page
    assert "game rules not built yet" not in page
