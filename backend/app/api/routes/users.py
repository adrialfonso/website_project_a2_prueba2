""" User management routes """
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, delete, func, select

from app import crud
from app.api.deps import (
    CurrentUser,
    SessionDep,
    get_current_active_superuser,
)
from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.models import (
    Message,
    UpdatePassword,
    User,
    UserCreate,
    UserCreateOpen,
    UserOut,
    UserBase,
    UsersOut,
    UserUpdate,
    UserUpdateMe,
)
from app.utils import generate_new_account_email, send_email
#!pip install mysql-connector-python
import mysql.connector
import bcrypt
#
router = APIRouter()

host = settings.HOST
user = settings.USER
password = settings.PASSWORD
database = settings.DATABASE

@router.get("/")
def read_users(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve users.
    """
    try:
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3306
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")

            cursor = conexion.cursor()

            # Update query to fetch users
            query_users = "SELECT id_user, name, surname, username, email FROM users LIMIT %s OFFSET %s"
            cursor.execute(query_users, (limit, skip))
            filas = cursor.fetchall()

            # Count the total number of users
            query_count = "SELECT COUNT(1) FROM users"
            cursor.execute(query_count)
            count = cursor.fetchone()[0]

            # Transform tuples to a list of UserOut
            users_data = [
                UserOut(
                    id_user=row[0],
                    name=row[1],
                    surname=row[2],
                    username=row[3],
                    email=row[4]
                ) for row in filas
            ]

            return UsersOut(data=users_data, count=count)

    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")


@router.post(
    "/",
    response_model=UserOut
)
def create_user(*, session: SessionDep, user_in: UserCreate) -> Any:
    """
    Create new user.
    """
    try:
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3306
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")

            cursor = conexion.cursor()

            # Verificar si el usuario ya existe por email
            query_check_user = "SELECT id_user FROM users WHERE email = %s"
            cursor.execute(query_check_user, (user_in.email,))
            existing_user = cursor.fetchone()

            if existing_user:
                print("El usuario ya existe")
                raise HTTPException(
                    status_code=400,
                    detail="The user with this email already exists in the system.",
                )

            # Insertar el nuevo usuario en la base de datos
            query_create_user = """
                INSERT INTO users (name, surname, username, email, password)
                VALUES (%s, %s, %s, %s, %s)
            """
            hashed_password = bcrypt.hashpw(user_in.password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute(query_create_user, (
                user_in.name,
                user_in.surname,
                user_in.username,
                user_in.email,
                hashed_password
            ))

            # Confirmar la transacción
            conexion.commit()

            # Obtener el ID del usuario recién creado
            new_user_id = cursor.lastrowid

            # Crear el objeto de salida
            user_out = UserOut(
                id_user=new_user_id,
                name=user_in.name,
                surname=user_in.surname,
                username=user_in.username,
                email=user_in.email
            )
            '''
            # Enviar correo si está habilitado
            if settings.emails_enabled and user_in.email:
                email_data = generate_new_account_email(
                    email_to=user_in.email, username=user_in.email, password=user_in.password
                )
                send_email(
                    email_to=user_in.email,
                    subject=email_data.subject,
                    html_content=email_data.html_content,
                )
            '''
            return user_out

    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to the database.")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")




@router.post("/open", response_model=UserOut)
def create_user_open(session: SessionDep, user_in: UserCreateOpen) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    user_create = UserCreate.from_orm(user_in)
    user = crud.user.create_user(session=session, user_create=user_create)
    return user

@router.get("/by-email", response_model=UserOut)
def read_user_by_email(*, email: str) -> Any:
    """
    Get a user by email.
    """
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3306
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = conexion.cursor()

            # Consulta para obtener el usuario por email
            query_user = "SELECT id_user, name, surname, username, email, password FROM users WHERE email = %s"
            cursor.execute(query_user, (email,))
            user_row = cursor.fetchone()

            if not user_row:
                raise HTTPException(
                    status_code=404,
                    detail="User not found with the provided email",
                )

            # Crear el objeto UserOut basado en los datos obtenidos
            user_out = UserOut(
                id_user=user_row[0],
                name=user_row[1],
                surname=user_row[2],
                username=user_row[3],
                email=user_row[4],
            )

            return user_out

    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to the database.")
    except Exception as ex:
        print(f"Error al obtener el usuario: {ex}")
        raise HTTPException(status_code=400, detail=str(ex))

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")


@router.get("/by-id", response_model=UserOut)
def read_user_by_id(user_id: int, session: SessionDep) -> Any:
    """
    Get a specific user by id.
    """
    user = session.get(User, user_id)

    '''
    if user == current_user:
        return user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="The user doesn't have enough privileges",
        )
    '''

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found with the provided id",
        )

    return user

'''
@router.patch(
    "/{user_id}",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=UserOut,
)
def update_user(
    *,
    session: SessionDep,
    user_id: int,
    user_in: UserUpdate,
) -> Any:
    """
    Update a user.
    """

    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    if user_in.email:
        existing_user = crud.user.get_user_by_email(session=session, email=user_in.email)
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=409, detail="User with this email already exists"
            )

    db_user = crud.user.update_user(session=session, db_user=db_user, user_in=user_in)
    return db_user


@router.delete("/{user_id}")
def delete_user(
    session: SessionDep, current_user: CurrentUser, user_id: int
) -> Message:
    """
    Delete a user.
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    elif user != current_user and not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    elif user == current_user and current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="Super users are not allowed to delete themselves"
        )

    session.delete(user)
    session.commit()
    return Message(message="User deleted successfully")
'''