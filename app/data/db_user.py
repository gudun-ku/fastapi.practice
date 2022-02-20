import email
import imp
from sqlalchemy.orm.session import Session
from schemas import UserBase
from data.models import DbUser
from data.hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, id: int):
    # TODO: handle exceptions
    return db.query(DbUser).filter(DbUser.id == id).first()

# TODO: return user model


def update_user(db: Session, id: int, request: UserBase):
    # TODO: handle exceptions
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
                DbUser.username: request.username,
                DbUser.email: request.email,
                DbUser.password: Hash.bcrypt(request.password)
                })
    db.commit()
    return "ok"


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
# TODO: handle exceptions
    db.delete(user)
    db.commit()
    return "ok"
