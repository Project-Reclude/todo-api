from app.db import db


class Point(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    body = db.Column(db.String(120), nullable=False)
    completed = db.Column(db.String(12), nullable=False)
    due = db.Column(db.String(12), nullable=True)

    def __repr__(self) -> str:
        return f"""Point(
            {self.num=},
            {self.date=}, 
            {self.category=}, 
            {self.body=}, 
            {self.completed=}, 
            {self.due=}
        )"""

    def __iter__(self):
        yield "num", self.num
        yield "date", self.date
        yield "category", self.category
        yield "body", self.body
        yield "completed", self.completed
        yield "due", self.due
