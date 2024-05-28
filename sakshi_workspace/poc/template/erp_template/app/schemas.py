from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import List, Optional

class ErpRoleMstCreateSchema(BaseModel):
    companyCode: int
    divisionCode: int
    roleCode: int
    createdBy: str = Field(..., max_length=25)
    createdDt: datetime
    roleExpAppFlag: str = Field('N', max_length=1)

class ErpRoleMstResponse(BaseModel):
    companyCode: int
    divisionCode: int
    roleCode: int
    roleDisplayName: Optional[str] = None
    roleLongName: Optional[str] = None
    roleParentRole: Optional[int] = None
    roleType: Optional[str] = None
    roleDispSeqNo: Optional[int] = None
    sysAdminFlag: Optional[str] = None
    roleId: Optional[str] = None
    perItemLimit: Optional[float] = None
    perTransactionLimit: Optional[float] = None
    createdBy: Optional[str] = None
    createdDt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    updatedDt: Optional[datetime] = None
    terminalId: Optional[str] = None
    activeYn: Optional[int] = None  # Ensure this is set to Optional[str]
    creatorRoleCode: Optional[int] = None
    updatorRoleCode: Optional[int] = None
    roleExpAppFlag: Optional[str] = None
    refRoleId: Optional[str] = None
    hrAdminFlag: Optional[int] = None
    defaultYn: Optional[int] = None

    # @validator('activeYn', pre=True, always=True)
    # def set_activeYn(cls, v):
    #     return str(v) if v is not None else v

    def to_dict(self) -> dict:
        return self.dict()

    class Config:
        orm_mode = True
        from_attributes = True

class PaginationMeta(BaseModel):
    page: int
    perPage: int
    totalItems: int

class ErpRoleMstResponsePaginated(BaseModel):
    meta: PaginationMeta
    items: List[ErpRoleMstResponse]
