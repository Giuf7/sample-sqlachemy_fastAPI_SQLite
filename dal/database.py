import sys
import os
from contextlib import contextmanager
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Check your .env file.")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite only
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def init_db(delete=False):
    if delete:
        Base.metadata.drop_all(bind=engine)
        print("❌ - Toutes les tables on été supprimées.")
    Base.metadata.create_all(bind=engine)
    print("✅ - Tables créées / mise à jour.")


def test_connexion():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ Connexion établie à SQL Server 😊")
            return True
    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")
        return False


@contextmanager
def get_db():
    db = session_local()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def get_db_dependency():
    """FastAPI Depends-compatible wrapper around get_db."""
    with get_db() as db:
        yield db
