from datetime import datetime
from dataclasses import dataclass, field # 3.10 - DataClass
from typing import Optional

@dataclass() #init, repr, eq

class Category: # Constructor

    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
    ) # Create the instance without reapeat datetime
