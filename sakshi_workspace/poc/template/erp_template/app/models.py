from sqlalchemy import Column, String, Integer, SmallInteger, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ErpRoleMst(Base):
    __tablename__ = 'role_mst'
    __table_args__ = {'schema': 'erp_admin'}
    
    companyCode = Column('comp_cd', SmallInteger, primary_key=True, nullable=False)
    divisionCode = Column('div_cd', SmallInteger, primary_key=True, nullable=False)
    roleCode = Column('role_cd', SmallInteger, primary_key=True, nullable=False)
    roleDisplayName = Column('role_disp_name', String(50), nullable=True)
    roleLongName = Column('role_long_name', String(50), nullable=True)
    roleParentRole = Column('role_parent_role', SmallInteger, nullable=True)
    roleType = Column('role_type', String(50), nullable=True)
    roleDispSeqNo = Column('role_disp_seq_no', SmallInteger, nullable=True)
    sysAdminFlag = Column('sys_admin_flag', String(1), nullable=True)
    roleId = Column('role_id', String(50), nullable=True)
    perItemLimit = Column('per_item_limit', Numeric(21, 2), nullable=True)
    perTransactionLimit = Column('per_transaction_limit', Numeric(21, 2), nullable=True)
    createdBy = Column('created_by', String(10), nullable=False)
    createdDt = Column('created_dt', DateTime, nullable=False)
    updatedBy = Column('updated_by', String(10), nullable=True)
    updatedDt = Column('updated_dt', DateTime, nullable=True)
    terminalId = Column('terminal_id', String(100), nullable=True)
    activeYn = Column('active_yn', Integer, nullable=True)
    creatorRoleCode = Column('creator_role_cd', SmallInteger, nullable=True)
    updatorRoleCode = Column('updator_role_cd', SmallInteger, nullable=True)
    roleExpAppFlag = Column('role_exp_app_flag', String(1), nullable=False)
    refRoleId = Column('ref_role_id', String(10), nullable=True)
    hrAdminFlag = Column('hr_admin_flag', SmallInteger, nullable=True)
    defaultYn = Column('default_yn', SmallInteger, nullable=True)
