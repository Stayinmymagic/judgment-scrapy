from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from webscraper.models import Judge, Lender
import subprocess
import pandas as pd
import os
import datetime
import json
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.db.models import Sum, Avg
import time 
import numpy as np
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
load_dotenv()
# @csrf_exempt
import joblib
import os
import datetime
import sqlite3

def connect_db(url):
    Base = declarative_base()
    engine = create_engine(os.getenv(url), echo=True)
    connection = engine.connect()
    return connection

def fetch_loan(id, conn_loan, conn_tfe):
    
    script = """select lender_name as name, lender_birthday as birth, lender_residence_addr as residence_addr, lender_current_addr as current_addr, 
                lender_company_addr as company_addr from installment_lender where lender_id_no = '%s';"""%id
    
    df_lender = pd.read_sql(script,conn_loan)
    age = datetime.date.today().year - pd.to_datetime(df_lender['birth']).dt.year
    df_lender['age'] =  np.where(np.isnan(age) == True, 20, age)
    
    return df_lender

def fetch_tfe(id,conn_tfe):
    script = {'lender':"""SELECT ChineseName as name, birthdate as birth, CONCAT(city, area, Address)  as current_addr 
                from Account where Identification = '%s';"""%id,
                'parent': """SELECT FATHER, MOTHER, CONCAT(COUNTYNAME, TOWNNAME, ADDRESS) as residence_addr from household_admin where PID = '%s';"""%id}
    df_lender = pd.read_sql(script['lender'], conn_tfe)
    df_lender['birth'] = pd.to_datetime(df_lender['birth'], format="%Y%m%d").dt.date
    df_lender['age'] =  datetime.date.today().year - pd.to_datetime(df_lender['birth']).dt.year
    df_p = pd.read_sql(script['parent'],conn_tfe)  
    df = pd.concat([df_lender, df_p], axis=1)
    df['company_addr'] = None
    return df

    
@csrf_exempt
def search(request):
    global tfe, loan, household_table,  black_table
    # parse post data
    # Lender.objects.all().delete()
    id = request.POST['identification']
    # Lender.objects.all().filter(id=id).delete()
    # fetch data by ID 
    conn_tfe = connect_db(url="DATABASE_TFE_URL")
    conn_loan = connect_db(url="DATABASE_LOAN_URL")

    _source = '' 
    if 'TFE' in request.POST:
        df = fetch_tfe(id, conn_tfe)
        _source = 'TFE'
    else:
        df = fetch_loan(id, conn_loan, conn_tfe)
        _source = 'loan'

    lender_data = df.to_dict("records")[0]
    print(lender_data)
    # tfe, loan, household_table,  black_table = output_tables(id, conn_tfe,conn_loan)

    
    # create a record and save in model
    lender = Lender()
    lender.id = id
    lender.name = lender_data['name']
    lender.age = lender_data['age']
    lender.fatherName = household_table['FATHER']
    lender.motherName = household_table['MOTHER']
    lender.residenceAddress = lender_data['residence_addr']
    lender.currentAdddress = lender_data['current_addr']
    lender.companyAddress = lender_data['company_addr']
    lender.source = _source
    lender.save()

    conn_da = connect_db(url="DATABASE_DA_URL")
    df_note = pd.read_sql("""SELECT distinct Identification from Note""",conn_da)

    Judge.objects.all().filter(pid=id).delete()
    process = subprocess.Popen("scrapy crawl judge -a id=%s"%id, shell=True)
    process.communicate()
    results = Judge.objects.filter(pid=id).order_by('event_time')
    shacom_case = Judge.objects.filter(pid=id,company__startswith="喬美")
    if len(shacom_case) > 0:    
        if id not in df_note['Identification'].values:
            Judge.objects.filter(pid=id,company__startswith="喬美").delete()

    return render(request, 'result.html', locals())

def reject(request):
    return HttpResponse('R代碼存入memo且拒絕此申貸案件') 

def main(request):
    return render(request, 'main.html')

