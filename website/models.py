from . import db
from sqlalchemy.sql import func

# ---------------- USERS TABLE ----------------
class User(db.Model):
    _tablename_ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer)
    username = db.Column(db.String(64))
    email = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    external_id = db.Column(db.String(32))
    is_active = db.Column(db.Boolean, default=True)
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

# ---------------- STUDENT TABLE ----------------
class Student(db.Model):
    _tablename_ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    usn = db.Column(db.String(64))
    name = db.Column(db.String(255))
    dob = db.Column(db.Date)
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    program_id = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    admission_year = db.Column(db.Integer)
    semester_id = db.Column(db.Integer)
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

# ---------------- FACULTY TABLE ----------------
class Faculty(db.Model):
    _tablename_ = "faculty"
    faculty_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    faculty_code = db.Column(db.String(32))
    name = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(255))
    employment_type = db.Column(db.String(50))
    join_date = db.Column(db.Date)
    designation = db.Column(db.String(100))
    is_hod = db.Column(db.Boolean, default=False)
    department = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

# ---------------- SECTION TABLE ----------------
class Section(db.Model):
    _tablename_ = "section"
    section_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    program_id = db.Column(db.Integer)
    year_of_study = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())