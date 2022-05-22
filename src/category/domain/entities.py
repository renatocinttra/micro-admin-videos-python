# sourcery skip: avoid-builtin-shadow

from datetime import datetime
from dataclasses import dataclass, field  # 3.10 - DataClass
from typing import Optional
from __seedwork.domain.entities import Entity


@dataclass(kw_only=True, frozen=True)  # init, repr, eq
class Category(Entity):  # Constructor
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        # Create the instance without reapeat datetime
        default_factory=lambda: datetime.now()
    )
