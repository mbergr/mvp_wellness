"""Add user profile fields

Revision ID: 265ba7e38f2c
Revises: 2bd7578e8b2a
Create Date: 2024-12-06 21:47:09.730400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '265ba7e38f2c'
down_revision = '2bd7578e8b2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mood_entry', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.drop_column('updated_at')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('date_of_birth', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('gender', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('occupation', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('bio', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('joined_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('notification_enabled', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('daily_reminder_time', sa.Time(), nullable=True))
        batch_op.add_column(sa.Column('timezone', sa.String(length=50), nullable=True))
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), nullable=True))
        batch_op.drop_column('timezone')
        batch_op.drop_column('daily_reminder_time')
        batch_op.drop_column('notification_enabled')
        batch_op.drop_column('joined_at')
        batch_op.drop_column('bio')
        batch_op.drop_column('occupation')
        batch_op.drop_column('gender')
        batch_op.drop_column('date_of_birth')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    with op.batch_alter_table('mood_entry', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DATETIME(), nullable=True))
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###
