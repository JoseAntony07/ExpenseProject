from datetime import datetime, timedelta

from fastapi import FastAPI

from models import Expense
from mongo_conn import expense_collection
from bson import json_util
import json

app = FastAPI()


@app.get('/expenses/')
async def get_expense():
    all_expenses = list(expense_collection.find())
    response = json.loads(json_util.dumps(all_expenses))
    return {'all_expenses': response}


@app.post('/expenses/')
async def create_expense(expense: Expense):
    create_expenses = expense_collection.insert_one({'name': expense.name, 'amount': expense.amount, 'category': expense.category, 'created_on': expense.created_on})
    print(create_expenses)
    return {'message': 'successfully created the expense'}


@app.get('/totals/')
async def create_expense():
    total_expenses = expense_collection.aggregate([{
        '$group': {
            '_id': None,
            'total': {'$sum': {"$toInt": "$amount"}}}}])

    total_expenses = list(total_expenses)[0].get('total')
    return {'total_expenses': total_expenses}


@app.get('/expenses/{year}/{month}')
async def get_expense(year: int, month: int):
    start_date = datetime(year, month, 1)
    end_date = start_date + timedelta(days=32)

    filter_date = list(expense_collection.find({'created_on': {'$gte': start_date, '$lt': end_date}}))
    response = json.loads(json_util.dumps(filter_date))

    return {'all_expenses': response}
