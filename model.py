from passlib.apps import custom_app_context as pwd_security
class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   username = Column(String)
   password = Column(String)
   
   def hash_password(self, password):
	  self.password_hash = pwd_security.encrypt(password)
   def verify_password(self, password):
      return pwd_security.verify(password,self.password_hash)
   