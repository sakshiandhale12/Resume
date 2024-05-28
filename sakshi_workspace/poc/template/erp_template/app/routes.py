from fastapi import APIRouter, HTTPException
from .schemas import *
from .service import *

role_router = APIRouter()

@role_router.get("/v1/roles", response_model=ErpRoleMstResponsePaginated)
async def get_all_roles_handler(
    companyCode: int = None,
    division_code: int = None,
    role_code: int = None,
    role_display_name: str = None,
    role_long_name: str = None,
    page: int = 1,
    per_page: int = 10
):
    offset = (page - 1) * per_page
    roles, total_records = get_all_roles_transformed(
        companyCode=companyCode,
        division_code=division_code,
        role_code=role_code,
        role_display_name=role_display_name,
        role_long_name=role_long_name,
        limit=per_page,
        offset=offset
    )
    
    response = ErpRoleMstResponsePaginated(
        meta=PaginationMeta(
            page=page,
            perPage=per_page,
            totalItems=total_records
        ),
        items=roles
    )
    
    return response

@role_router.post("/v1/roles")
async def create_new_role(role: ErpRoleMstCreateSchema):
    try:
        new_role = create_role(role)
        return new_role
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create role: " + str(e))

@role_router.delete("/v1/roles/{role_code}")
async def delete_role_endpoint(role_code: int):
    try:
        deleted_role = delete_role(role_code)
        if not deleted_role:
            raise HTTPException(status_code=404, detail="Role not found")
        return {"message": "Role deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete role: " + str(e))

@role_router.put("/v1/roles/{role_code}")
async def update_role_endpoint(role_code: int, role_data: ErpRoleMstCreateSchema):
    try:
        updated_role = update_role(role_code, role_data)
        if not updated_role:
            raise HTTPException(status_code=404, detail="Role not found")
        return updated_role
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update role: " + str(e))













# from fastapi import *
# from sqlalchemy.orm import Session
# from typing import *
# from .schemas import *
# from dblib import *
# from .service import perform_transaction, get_all_roles_transformed, create_role, delete_role, update_role

# role_router = APIRouter()

# # Dependency for getting the database session
# def get_session(db: Session = Depends(get_db)) -> Session:
#     return db

# @role_router.get("/v1/roles", response_model=ErpRoleMstResponsePaginated)
# async def get_all_roles_handler(
#     companyCode: int = Query(None, alias="companyCode"),
#     division_code: int = Query(None, alias="division_code"),
#     role_code: int = Query(None, alias="role_code"),
#     role_display_name: str = Query(None, alias="role_display_name"),
#     role_long_name: str = Query(None, alias="role_long_name"),
#     page: int = Query(1, alias="page", ge=1),
#     per_page: int = Query(10, alias="per_page", ge=1),
#     db: Session = Depends(get_session)
# ):
#     """
#     Endpoint to retrieve all roles from the database.
#     """
#     offset = (page - 1) * per_page

#     roles, total_records = get_all_roles_transformed(
#         session=db,
#         companyCode=companyCode,
#         division_code=division_code,
#         role_code=role_code,
#         role_display_name=role_display_name,
#         role_long_name=role_long_name,
#         limit=per_page,
#         offset=offset
#     )
    
#     response = ErpRoleMstResponsePaginated(
#         meta=PaginationMeta(
#             page=page,
#             perPage=per_page,
#             totalItems=total_records
#         ),
#         items=roles
#     )
    
#     return response

# @role_router.post("/v1/roles")
# async def create_new_role(role: ErpRoleMstCreateSchema, db: Session = Depends(get_session)):
#     try:
#         new_role = create_role(db, role)  # Perform database operation
#         return new_role
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to create role: " + str(e))

# @role_router.delete("/v1/roles/{role_code}")
# async def delete_role_endpoint(role_code: int, db: Session = Depends(get_session)):
#     try:
#         deleted_role = delete_role(db, role_code)  # Perform database operation
#         if not deleted_role:
#             raise HTTPException(status_code=404, detail="Role not found")
#         return {"message": "Role deleted successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to delete role: " + str(e))

# @role_router.put("/v1/roles/{role_code}")
# async def update_role_endpoint(role_code: int, role_data: ErpRoleMstCreateSchema, db: Session = Depends(get_session)):
#     try:
#         updated_role = update_role(db, role_code, role_data)  # Perform database operation
#         if not updated_role:
#             raise HTTPException(status_code=404, detail="Role not found")
#         return updated_role
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to update role: " + str(e))

