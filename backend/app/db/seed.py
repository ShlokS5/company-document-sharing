from sqlalchemy import select
from app.db.session import SessionLocal
from app.models import Department, Role


DEFAULT_ROLES = [
    ("admin", "Platform administrator"),
    ("hr", "Human Resources"),
    ("engineering", "Engineering team"),
    ("employee", "General employee"),
]

DEFAULT_DEPARTMENTS = [
    ("Human Resources", "hr"),
    ("Engineering", "engineering"),
    ("Finance", "finance"),
    ("Operations", "operations"),
]


def seed_database():
    with SessionLocal() as db:

        for name, description in DEFAULT_ROLES:
            existing = db.scalar(
                select(Role).where(Role.name == name)
            )

            if not existing:
                db.add(Role(
                    name=name,
                    description=description
                ))

        for name, slug in DEFAULT_DEPARTMENTS:
            existing = db.scalar(
                select(Department).where(
                    Department.slug == slug
                )
            )

            if not existing:
                db.add(Department(
                    name=name,
                    slug=slug
                ))

        db.commit()


if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully!")