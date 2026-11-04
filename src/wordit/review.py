"""let the Operator approve or reject a candidate in the terminal"""

from wordit.candidate import Candidate

QUESTION = "Approve(a) or reject(r)?"


def review_candidate(candidate: Candidate, ask=input) -> None:
    """Asks the operator to either approve or reject the candidate"""
    print(f"Suggestion: {candidate.reference}")
    print(f'Heard: "{candidate.heard_text}"')
    answer = ask(QUESTION).lower()
    while answer not in ("a", "r"):
        print("Enter either a for approve or r for reject")
        answer = ask(QUESTION).lower()
    if answer == "a":
        candidate.approve()
    else:
        candidate.reject()
