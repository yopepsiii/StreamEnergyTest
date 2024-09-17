from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

    notes: Mapped[list['Note']] = relationship()


class Note(Base):
    __tablename__ = 'Notes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column(nullable=True)

    creator_id: Mapped[int] = mapped_column(ForeignKey('Users.id', ondelete='CASCADE'))

    tags: Mapped[list['Tag']] = relationship()

    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(nullable=True)


class Tag(Base):
    __tablename__ = 'Tags'

    note_id: Mapped[int] = mapped_column(ForeignKey('Notes.id', ondelete='CASCADE'), primary_key=True)
    name: Mapped[str] = mapped_column()
