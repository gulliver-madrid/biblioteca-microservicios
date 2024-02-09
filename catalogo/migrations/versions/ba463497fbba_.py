"""empty message

Revision ID: ba463497fbba
Revises: 806a0d8b2792
Create Date: 2024-02-09 12:59:42.930415

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ba463497fbba'
down_revision = '806a0d8b2792'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('autores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('libros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('autores_libros',
    sa.Column('autor_id', sa.Integer(), nullable=False),
    sa.Column('libro_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['autor_id'], ['autores.id'], ),
    sa.ForeignKeyConstraint(['libro_id'], ['libros.id'], ),
    sa.PrimaryKeyConstraint('autor_id', 'libro_id')
    )
    with op.batch_alter_table('libro', schema=None) as batch_op:
        batch_op.drop_index('title')

    op.drop_table('libro')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('libro',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('date_added', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('libro', schema=None) as batch_op:
        batch_op.create_index('title', ['title'], unique=True)

    op.drop_table('autores_libros')
    op.drop_table('libros')
    op.drop_table('autores')
    # ### end Alembic commands ###
