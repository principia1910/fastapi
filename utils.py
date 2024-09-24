from passlib.context import CryptContext
import boto3
import datetime
s3=boto3.client('s3')



password_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password,hashed_pass)

def s3wt(fobj,bkt,key):
    s3.upload_fileobj(fobj,bkt,key)

def utcnow():
    return datetime.datetime.now(datetime.timezone.utc)