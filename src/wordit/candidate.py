"""Suggestions waiting for operator's decision."""

from dataclasses import dataclass
from enum import Enum

from wordit.reference import Reference


class Status(Enum):
    """candidate status depending on operator's decision"""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class Candidate:
    """A Detected reference waiting for operator's approval or rejection"""

    reference: Reference
    heard_text: str
    status: Status = Status.PENDING

    def approve(self) -> None:
        """Mark the candidate as approved for display"""
        self.status = Status.APPROVED

    def reject(self) -> None:
        """Mark the candidate as rejected and is never displayed"""
        self.status = Status.REJECTED
