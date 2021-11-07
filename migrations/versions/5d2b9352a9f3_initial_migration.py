"""Initial Migration

Revision ID: 5d2b9352a9f3
Revises: 
Create Date: 2021-11-07 18:28:49.417976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d2b9352a9f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usertable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('pass_hash', sa.String(), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.Column('post_user', sa.DateTime(), nullable=True),
    sa.Column('site', sa.String(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usertable_email'), 'usertable', ['email'], unique=True)
    op.create_index(op.f('ix_usertable_username'), 'usertable', ['username'], unique=False)
    op.create_table('pitchtable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('p_title', sa.String(), nullable=True),
    sa.Column('pitch_it', sa.String(), nullable=True),
    sa.Column('post', sa.DateTime(), nullable=True),
    sa.Column('posted_by', sa.String(), nullable=True),
    sa.Column('upvote', sa.Integer(), nullable=True),
    sa.Column('downvote', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['usertable.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commenttable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('p_comment', sa.String(length=255), nullable=True),
    sa.Column('post_com', sa.DateTime(), nullable=True),
    sa.Column('comment_by', sa.String(length=255), nullable=True),
    sa.Column('pitch_id', sa.String(length=255), nullable=True),
    sa.Column('pitchID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitchID'], ['pitchtable.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('commenttable')
    op.drop_table('pitchtable')
    op.drop_index(op.f('ix_usertable_username'), table_name='usertable')
    op.drop_index(op.f('ix_usertable_email'), table_name='usertable')
    op.drop_table('usertable')
    op.drop_table('roles')
    # ### end Alembic commands ###
