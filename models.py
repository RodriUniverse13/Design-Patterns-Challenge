# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, server_default=text("nextval('departments_id_seq'::regclass)"))
    name = Column(String(50), nullable=False)


class EvaluationType(Base):
    __tablename__ = 'evaluation_types'

    id = Column(Integer, primary_key=True, server_default=text("nextval('evaluation_types_id_seq'::regclass)"))
    name = Column(String(1), nullable=False)
    bias1st_percentage = Column(Float, nullable=False)
    bias2nd_percentage = Column(Float, nullable=False)
    bias3st_percentage = Column(Float, nullable=False)


class Specialty(Base):
    __tablename__ = 'specialties'

    id = Column(Integer, primary_key=True, server_default=text("nextval('specialties_id_seq'::regclass)"))
    name = Column(String(50), nullable=False)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, server_default=text("nextval('students_id_seq'::regclass)"))
    register = Column(String(8), nullable=False, unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(10), nullable=False)
    email = Column(String(100))
    status = Column(String(20), nullable=False)


class Professor(Base):
    __tablename__ = 'professors'

    id = Column(Integer, primary_key=True, server_default=text("nextval('professors_id_seq'::regclass)"))
    department_id = Column(ForeignKey('departments.id'), nullable=False)
    specialty_id = Column(ForeignKey('specialties.id'), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    department = relationship('Department')
    specialty = relationship('Specialty')


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, server_default=text("nextval('subjects_id_seq'::regclass)"))
    evaluation_type_id = Column(ForeignKey('evaluation_types.id'), nullable=False)
    department_id = Column(ForeignKey('departments.id'), nullable=False)
    name = Column(String(50), nullable=False)
    credits = Column(Integer, nullable=False)

    department = relationship('Department')
    evaluation_type = relationship('EvaluationType')


class ProfessorHasSubject(Base):
    __tablename__ = 'professor_has_subjects'

    id = Column(Integer, primary_key=True, server_default=text("nextval('professor_has_subjects_id_seq'::regclass)"))
    subject_id = Column(ForeignKey('subjects.id'), nullable=False)
    professor_id = Column(ForeignKey('professors.id'), nullable=False)
    period = Column(String(9), nullable=False)

    professor = relationship('Professor')
    subject = relationship('Subject')


class ScheduledSubject(Base):
    __tablename__ = 'scheduled_subjects'

    id = Column(Integer, primary_key=True, server_default=text("nextval('scheduled_subjects_id_seq'::regclass)"))
    professor_subject_id = Column(ForeignKey('professor_has_subjects.id'), nullable=False)
    day = Column(String(10), nullable=False)
    start_hour = Column(Time, nullable=False)
    end_hour = Column(Time, nullable=False)

    professor_subject = relationship('ProfessorHasSubject')


class StudentHasSubject(Base):
    __tablename__ = 'student_has_subjects'

    id = Column(Integer, primary_key=True, server_default=text("nextval('student_has_subjects_id_seq'::regclass)"))
    student_id = Column(ForeignKey('students.id'), nullable=False)
    subject_id = Column(ForeignKey('professor_has_subjects.id'), nullable=False)
    bias1_grading = Column(Float)
    bias2_grading = Column(Float)
    bias3_gradind = Column(Float)

    student = relationship('Student')
    subject = relationship('ProfessorHasSubject')
