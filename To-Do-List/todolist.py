#############  2  ##################
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())


#    def __repr__(self):
#       return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def display():
    print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit")


def today_task():
    today = datetime.today()
    rows = session.query(Task).filter(Task.deadline == datetime.today().date()).all()
    print(f"Today {today.day} {today.strftime('%b')}:")
    if rows == []:
        print('Nothing to do!\n')
    else:
        for i in rows:
            print(f'{i.id}. {i.task}')


def add_task():
    new_task = input('Enter task')
    new_deadline = input('Enter deadline')
    new_tasks = Task(task=new_task, deadline=datetime.strptime(new_deadline, '%Y-%m-%d').date())
    session.add(new_tasks)
    session.commit()
    print('The task has been added!\n')


def week_task():
    day_of_week = 0
    today = datetime.today().date()
    while day_of_week < 7:
        week_day = today + timedelta(days=day_of_week)
        print(week_day.strftime('%A %d %b:'))
        rows = session.query(Task).filter(Task.deadline == week_day).all()
        if len(rows) == 0:
            print('Nothing to do!')
        for i in rows:
            print(f'{str(i.id)}. {i.task}')
        day_of_week += 1
        print()


def all_task():
    print('All tasks:')
    rows = session.query(Task).order_by(Task.deadline).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for i in rows:
            print(f'{i.id}. {i.task}. {i.deadline.strftime("%#d %b")}')

def missed_task():
    print('\nMissed tasks:')
    rows = session.query(Task).filter(Task.deadline < datetime.today().date()).order_by(Task.deadline).all()
    if rows == []:
        print('Nothing is missed!')
    else:
        for i in rows:
            print(f'{i.id}. {i.task}. {i.deadline.strftime("%#d %b")}')
    print()

def delete_task():
    print('\nChoose the number of the tasks you want to delete:')
    rows = session.query(Task).order_by(Task.deadline).all()
    if rows == []:
        print('Nothing to delete')
    else:
        for i in rows:
            print(f'{i.id}. {i.task}. {i.deadline.strftime("%#d %b")}')
        deleted = int(input())
        session.query(Task).filter(Task.id == deleted).delete()
        session.commit()
        print('The task has been deleted!')


while True:
    display()
    x = int(input('\n'))

    if x == 1:
        today_task()

    elif x == 2:
        week_task()

    elif x == 3:
        all_task()

    elif x == 4:
        missed_task()

    elif x == 5:
        add_task()

    elif x == 6:
        delete_task()

    elif x == 0:
        print('Bye!')
        break

