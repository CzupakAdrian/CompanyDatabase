CREATE PROFILE c##enduser LIMIT
    FAILED_LOGIN_ATTEMPTS UNLIMITED
    PASSWORD_LOCK_TIME UNLIMITED;
    
ALTER USER Master
PROFILE c##enduser;

ALTER USER Master IDENTIFIED BY Master ACCOUNT UNLOCK;
