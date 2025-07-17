
from sqlalchemy import TIMESTAMP, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, MappedColumn
from typing import Optional
from datetime import datetime

from src.shared.enums.constant import StatusEnum
from src.shared.timestemp import get_timestamp


class TimestampMixin:
  status: Mapped[StatusEnum]= mapped_column(SqlEnum(StatusEnum, name='status_enum', native_enum = False), default= StatusEnum.ACTIVE)

  created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=get_timestamp)
  updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=get_timestamp, onupdate=get_timestamp)
  delete_at: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP(timezone=True), default=None)


  def set_deleted(self) -> None:
    self.delete_at = get_timestamp()
    self.status = StatusEnum.DELETE

  def set_status(self, status: StatusEnum):
    self.status = status



class IsVerifyMixin:
  is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
  verified_at: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP(timezone=True), default=None)

  def set_verified(self) -> None:
    self.is_verified = True
    self.verified_at = get_timestamp()
