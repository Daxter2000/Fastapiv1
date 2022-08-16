from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return (
        db.query(models.Mock_Data)
        .filter(models.Mock_Data.id == user_id)
        .first()
        .__dict__
    )

def get_user_by_id(db: Session, user_id: int):
    return (
        db.query(models.Mock_Data)
        .filter(models.Mock_Data.id == user_id)
        .first()
    )

def get_all_users(db: Session):
    return db.query(models.Mock_Data).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Mock_Data(
        id =user.id ,
        email=user.email, 
        first_name= user.first_name,
        last_name= user.last_name,
        company_name= user.company_name,
        city_name= user.city_name
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.__dict__