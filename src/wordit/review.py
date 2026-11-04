"""let the Operator approve or reject a candidate in the terminal"""

from wordit.candidate import Candidate


def review_candidate(candidate: Candidate, ask=input) -> None:
    """Asks the operator to either approve or reject the candidate"""
    print(f"Suggestion: {candidate.reference}")
    print(f'Heard: "{candidate.heard_text}"')
    answer = ask("Approve(a) or reject(r)?").lower()
    if answer == "a":
        candidate.approve()
    elif answer == "r":
        candidate.reject()
    else:
        print("Enter either a for approve or r for reject")
