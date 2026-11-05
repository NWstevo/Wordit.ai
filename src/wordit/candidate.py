"""Suggestions waiting for operator's decision."""

from dataclasses import dataclass
from enum import Enum

from wordit.reference import Reference


class Status(Enum):
    """candidate status depending on the operator's decision."""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class Candidate:
    """A detected reference waiting for the operator's approval or rejection."""

    reference: Reference
    heard_text: str
    verse_text: str
    status: Status = Status.PENDING

    def approve(self) -> None:
        """Mark the candidate as approved for display."""
        self.status = Status.APPROVED

    def reject(self) -> None:
        """Mark the candidate as rejected so it is never displayed."""
        self.status = Status.REJECTED
