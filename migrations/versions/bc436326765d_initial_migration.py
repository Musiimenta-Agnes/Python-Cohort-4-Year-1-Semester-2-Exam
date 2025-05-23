"""initial migration

Revision ID: bc436326765d
Revises: 
Create Date: 2025-05-23 12:57:57.363902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc436326765d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Courses',
    sa.Column('course_id', sa.String(length=255), nullable=False),
    sa.Column('course_name', sa.String(length=255), nullable=False),
    sa.Column('course_instructor', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('course_id'),
    sa.UniqueConstraint('course_id')
    )
    op.create_table('Programs',
    sa.Column('program_id', sa.String(length=255), nullable=False),
    sa.Column('program_name', sa.String(length=255), nullable=False),
    sa.Column('program_address', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('program_id'),
    sa.UniqueConstraint('program_id')
    )
    op.create_table('Students',
    sa.Column('student_id', sa.String(length=255), nullable=False),
    sa.Column('student_contact', sa.String(length=255), nullable=False),
    sa.Column('student_name', sa.String(length=255), nullable=False),
    sa.Column('student_email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('student_id'),
    sa.UniqueConstraint('student_email'),
    sa.UniqueConstraint('student_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Students')
    op.drop_table('Programs')
    op.drop_table('Courses')
    # ### end Alembic commands ###
