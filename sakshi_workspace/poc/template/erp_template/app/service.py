from sqlalchemy.orm import Session
from typing import Tuple, List
from fastapi import HTTPException
from .models import ErpRoleMst
from .schemas import ErpRoleMstCreateSchema
from .transformer import transform_data
from dblib import get_db

def perform_transaction(func):
    def wrapper(*args, **kwargs):
        db = next(get_db())  # Get the database session
        try:
            with db.begin():
                result = func(db, *args, **kwargs)
            return result
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail="Database operation failed: " + str(e))
        finally:
            db.close()  # Close the session
    return wrapper

@perform_transaction
def get_all_roles_transformed(
    db: Session,
    limit: int = 10,
    offset: int = 0,
    companyCode: int = None,
    division_code: int = None,
    role_code: int = None,
    role_display_name: str = None,
    role_long_name: str = None,
) -> Tuple[List[dict], int]:
    query = db.query(ErpRoleMst)

    if companyCode is not None:
        query = query.filter(ErpRoleMst.companyCode == companyCode)
    if division_code is not None:
        query = query.filter(ErpRoleMst.divisionCode == division_code)
    if role_code is not None:
        query = query.filter(ErpRoleMst.roleCode == role_code)
    if role_display_name is not None:
        query = query.filter(ErpRoleMst.roleDisplayName == role_display_name)
    if role_long_name is not None:
        query = query.filter(ErpRoleMst.roleLongName == role_long_name)

    total_records = query.count()
    roles = query.offset(offset).limit(limit).all()

    transformed_roles, total_records = transform_data((roles, total_records), db)
    return transformed_roles, total_records

@perform_transaction
def create_role(db: Session, role: ErpRoleMstCreateSchema) -> ErpRoleMst:
    db_role = ErpRoleMst(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@perform_transaction
def delete_role(db: Session, role_code: int):
    role = db.query(ErpRoleMst).filter(ErpRoleMst.roleCode == role_code).first()
    if not role:
        return None
    db.delete(role)
    db.commit()
    return role

@perform_transaction
def update_role(db: Session, role_code: int, role_data: ErpRoleMstCreateSchema):
    role = db.query(ErpRoleMst).filter(ErpRoleMst.roleCode == role_code).first()
    if not role:
        return None
    for key, value in role_data.dict().items():
        setattr(role, key, value)
    db.commit()
    db.refresh(role)
    return role








# from fastapi import APIRouter, Depends, Query, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .schemas import *
# from dblib import get_db
# from .service import *

# role_router = APIRouter()

# # Dependency for getting the database session
# def get_session(db: Session = Depends(get_db)) -> Session:
#     return db

# @role_router.get("/v1/roles", response_model=ErpRoleMstResponsePaginated)
# async def get_roles_handler(
#     companyCode: int = Query(None, alias="companyCode"),
#     division_code: int = Query(None, alias="division_code"),
#     role_code: int = Query(None, alias="role_code"),
#     role_display_name: str = Query(None, alias="role_display_name"),
#     role_long_name: str = Query(None, alias="role_long_name"),
#     page: int = Query(1, alias="page", ge=1),
#     per_page: int = Query(10, alias="per_page", ge=1),
#     db: Session = Depends(get_session) # Use the dependency to get the session
# ):
#     offset = (page - 1) * per_page

#     roles, total_records = get_roles_transformed(
#         session=db,
#         comp_cd=companyCode,
#         div_cd=division_code,
#         role_cd=role_code,
#         role_disp_name=role_display_name,
#         role_long_name=role_long_name,
#         limit=per_page,
#         offset=offset
#     )
    
#     roles_pydantic = [ErpRoleMstResponse.from_orm(role) for role in roles]
    
#     response = ErpRoleMstResponsePaginated(
#         meta=PaginationMeta(
#             page=page,
#             perPage=per_page,
#             totalItems=total_records
#         ),
#         items=roles_pydantic
#     )
    
#     return response

# @role_router.post("/v1/roles")
# async def create_new_role(role: ErpRoleMstCreateSchema, db: Session = Depends(get_session)):
#     try:
#         # Start a transaction
#         with db.begin():
#             new_role = create_role(db, role)  # Perform database operation

#         return new_role

#     except Exception as e:
#         # Rollback the transaction in case of an error
#         db.rollback()
#         raise HTTPException(status_code=500, detail="Failed to create role: " + str(e))

# @role_router.delete("/v1/roles/{role_code}")
# async def delete_role_endpoint(role_code: int, db: Session = Depends(get_session)):
#     try:
#         # Start a transaction
#         with db.begin():
#             deleted_role = delete_role(db, role_code)  # Perform database operation
        
#         if not deleted_role:
#             raise HTTPException(status_code=404, detail="Role not found")

#         return {"message": "Role deleted successfully"}

#     except Exception as e:
#         # Rollback the transaction in case of an error
#         db.rollback()
#         raise HTTPException(status_code=500, detail="Failed to delete role: " + str(e))

# @role_router.put("/v1/roles/{role_code}")
# async def update_role_endpoint(role_code: int, role_data: ErpRoleMstCreateSchema, db: Session = Depends(get_session)):
#     try:
#         # Start a transaction
#         with db.begin():
#             updated_role = update_role(db, role_code, role_data)  # Perform database operation
        
#         if not updated_role:
#             raise HTTPException(status_code=404, detail="Role not found")

#         return updated_role

#     except Exception as e:
#         # Rollback the transaction in case of an error
#         db.rollback()
#         raise HTTPException(status_code=500, detail="Failed to update role: " + str(e))







