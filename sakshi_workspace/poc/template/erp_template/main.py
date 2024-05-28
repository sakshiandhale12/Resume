from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import *

from app.models import Base  # Importing Base to ensure models are created
from app.routes import role_router  # Importing the router object

app = FastAPI()

# Load environment variables
load_dotenv()

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv("ERPLIB_PRIMARY_DB_URI")
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base.metadata.create_all(bind=engine)

# Dependency to get a session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# Include your routes here
app.include_router(role_router)


















































# Include your routes here, e.g., from . import routes




# # app/main.py

# from sqlalchemy import text

# from mylibrary import hello_world
# #from dblib import some_db_function
# from fastapi import FastAPI, Depends
# from sqlalchemy import text
# # from dblib.db_connection import get_db,engine
# from sqlalchemy.orm import Session
# # from dblib.db_connection import create_db_connection
# from dblib.config import settings
# # import sqlalchemy.pool as pool

# app = FastAPI()

# # @app.on_event("startup")
# # async def startup_event():
# #     try:
# #         connection = await create_db_connection(settings.ERPLIB_PRIMARY_DB_URI)
# #         async with connection.acquire() as conn:
# #             await conn.fetchval('SELECT 1')
# #         print("Database connection successful")
# #     except Exception as e:
# #         print(f"Failed to connect to the database: {e}")

# @app.get("/")
# def read_root():
#     return {"message": hello_world()}

# @app.get("/postgres")
# def read_root(db: Session = Depends(get_db)):
#     result = db.execute(text("SELECT version();")).fetchone()
#     return {"PostgreSQL version": result[0]}


# @app.get("/pool_status")
# def pool_status():
#     try:
#         # Execute a query to get the currently active connections
#         query = """
#         SELECT
#             pid,
#             usename,
#             datname,
#             application_name,
#             client_addr,
#             client_hostname,
#             client_port,
#             backend_start,
#             state,
#             query
#         FROM
#             pg_stat_activity
#         WHERE
#             state <> 'idle';
#         """
#         with engine.connect() as conn:
#             result = conn.execute(text(query)).fetchall()
        
#         # Format the result into a list of dictionaries
#         connection_info = []
#         for row in result:
#             connection_info.append({
#                 "pid": row[0],
#                 "usename": row[1],
#                 "datname": row[2],
#                 "application_name": row[3],
#                 "client_addr": row[4],
#                 "client_hostname": row[5],
#                 "client_port": row[6],
#                 "backend_start": row[7],
#                 "state": row[8],
#                 "query": row[9]
#             })
        
#         # Include ERPLIB_POOL_MAX_OVERFLOW in the response
#         return {
#             "connections": len(connection_info),
#             "connection_info": connection_info,
#             "pool_max_overflow": settings.ERPLIB_POOL_MAX_OVERFLOW,
#             "pool_size":settings.ERPLIB_POOL_MIN_SIZE,
#             "pool_timeout":settings.ERPLIB_POOL_IDLE_TIMEOUT
#         }
#     except Exception as e:
#         return {"error": str(e)}


# # @app.get("/pool_status")
# # def pool_status():
# #     return {
# #         "checked_out": engine.pool.checkedout(),
# #         "pool_max_overflow": engine.pool._max_overflow,
# #         "checkedin": engine.pool.checkedin(),
# #         "connections": engine.pool.size(),
# #         "pool_size": engine.pool.size(),
# #         "pool_timeout": engine.pool.timeout(),
# #     }