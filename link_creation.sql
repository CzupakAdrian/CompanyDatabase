CREATE DATABASE LINK "tokyo_link" -- <nazwa linka>
CONNECT TO Master IDENTIFIED BY Master -- <user> i <haslo>
USING 'host.docker.internal:1521/ORCLCDB.localdomain'; -- '<adres hosta>:<port>/<nazwa usługi>'