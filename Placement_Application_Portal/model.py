from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'student' or 'admin' or 'company'
    status = db.Column(db.String(20), nullable=False, default='pending')  # 'pending', 'approved', 'rejected'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

   


class CompanyProfile(db.Model):
    __tablename__ = 'company_profiles'
    company_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    company_name = db.Column(db.String(120), nullable=False)
    hr_contact = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(120), nullable=True)
    approval_status = db.Column(db.String(20), nullable=False, default='pending')
    placement_drive = db.relationship('Placement_drives', backref='company', lazy=True)
    
class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    resume = db.Column(db.String(120), nullable=True)
    department = db.Column(db.String(120), nullable=False)
    graduation_year = db.Column(db.Integer, nullable=False)

class Placement_drives(db.Model):
    __tablename__ = 'placement_drives'
    drive_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company_profiles.company_id'), nullable=False)
    job_title = db.Column(db.String(120), nullable=False)
    job_description = db.Column(db.String(500), nullable=False)
    eligibility_criteria = db.Column(db.String(500), nullable=False)
    Salary = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    application_deadline = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'closed'

class Application(db.Model):
    __tablename__ = 'applications'
    application_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    drive_id = db.Column(db.Integer, db.ForeignKey('placement_drives.drive_id'), nullable=False)
    application_status = db.Column(db.String(20), nullable=False, default='pending')
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)