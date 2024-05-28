from typing import *
from sqlalchemy.orm import Session
from .models import *
from .schemas import *

def transform_data(data: Tuple[List[ErpRoleMstResponse], int], db: Session) -> Tuple[List[dict], int]:
    roles, total_records = data

    # Transform roles using the ErpRoleMstResponse schema
    transformed_roles = [ErpRoleMstResponse.from_orm(role).to_dict() for role in roles]

    return transformed_roles, total_records

















# from typing import *
# from sqlalchemy.orm import Session
# from .models import *
# from .stored_procedures import *

# def transform_data(data: Tuple[List[ErpRoleMst], int], db: Session) -> Tuple[List[dict], int]:
#     roles, total_records = data

#     # Call the stored procedure
#     # procedure_result = call_my_stored_procedure(db)

#     # Example transformation: Convert roles to a list of dictionaries
#     transformed_roles = [
#         {
#             "companyCode": role.companyCode,
#             "divisionCode": role.divisionCode,
#             "roleCode": role.roleCode,
#             "roleDisplayName": role.roleDisplayName,
#             "roleLongName": role.roleLongName,
#             "roleParentRole" : role.roleParentRole,
#             "roleType" : role.roleType,
#             "roleDispSeqNo"  : role.roleDispSeqNo,
#             "sysAdminFlag"  : role.sysAdminFlag,
#             "roleId"  : role.roleId,
#             "perItemLimit"  : role.perItemLimit,
#             "perTransactionLimit"  : role.perTransactionLimit,
#             "createdBy"  : role.createdBy,
#             "createdDt"  : role.createdDt,
#             "updatedBy" : role.updatedBy,
#             "updatedDt" : role.updatedDt,
#             "terminalId"  : role.terminalId,
#             "activeYn"  : str(role.activeYn), 
#             "creatorRoleCode" : role.creatorRoleCode,
#             "updatorRoleCode" : role.updatorRoleCode,
#             "roleExpAppFlag" : role.roleExpAppFlag,
#             "refRoleId" : role.refRoleId,
#             "hrAdminFlag" : role.hrAdminFlag,
#             "defaultYn" : role.defaultYn,
#         }
#         for role in roles
#     ]

#     return transformed_roles, total_records




# def transform_data(data: Tuple[List[ErpRoleMst], int], db: Session) -> Tuple[List[dict], int]:
#     roles, total_records = data

#     # Convert each role object to a dictionary representation
#     transformed_roles = [role.__dict__ for role in roles]

#     return transformed_roles, total_records