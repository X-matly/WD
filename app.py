from flask import Flask, render_template, make_response, json, jsonify
import config
from database import db
import models
from flask import request
from form import jumpForm
import datetime

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
event = models.event

NotExist = 1
AppendSucceed = 2
InvalidDate = 3
ModifySucceed = 4
DeleteSucceed = 5
Invalid_Start_And_End_Date = 6


def valid_date(Year, Month, Day):  # 判断时间是否合法
    if (int(Month) == 2 and int(Day) == 30) or (int(Month) == 2 and int(Day) == 31) or (
            int(Month) == 4 and int(Day) == 31) or (
            int(Month) == 6 and int(Day) == 31) or (
            int(Month) == 9 and int(Day) == 31) or (
            int(Month) == 11 and int(Day) == 31):
        return False
    if ((int(Year) % 4 == 0 and int(Year) % 100 == 0) or (int(Year) % 4 != 0)) and int(
            Month) == 2 and int(
        Day) == 29:
        return False
    return True


def AppendID(allData, NewEventID):  # 新加一个ID
    if allData:  # 如果已经有数据，令新ID为laoID中最大的加1
        NewEventID = 1
        for i in allData:
            if i.ID > NewEventID:
                NewEventID = i.ID + 1
            elif i.ID == NewEventID:
                NewEventID = i.ID + 1
            else:
                NewEventID = NewEventID
    else:
        NewEventID = 1
    return NewEventID


@app.route('/')
def homepage():
    return render_template('homepage.html', flag=-1)


@app.route('/return', methods=['GET', 'POST'])  # 返回主页
def return_to_homepage():
    return render_template('homepage.html', flag=-1)


@app.route('/delete', methods=['GET', 'POST'])  # 删除事项
def delete_event():
    nID = request.form.get('ID')
    models.event.query.filter(models.event.ID == nID).delete()
    db.session.commit()
    return render_template('homepage.html', flag=DeleteSucceed)


@app.route('/tempdata.json', methods=['GET', 'POST'])  # 读取全部事项
def send_all_data():
    allData = models.event.query.all()
    List = []
    for i in allData:
        dic = {'headline': i.headline, 'start_time': i.start_time, 'end_time': i.end_time,
               'significance': i.significance,
               'ID': i.ID, "complete": i.complete}
        List.append(dic)  # 将每一个数据存入List
    return jsonify(List)  # 以json类型返回数据


@app.route('/get_single_data', methods=['POST'])  # 读取单个事项
def send_single_data():
    temp = json.loads(request.form.get('data'))
    targetID = temp['sID']  # 读取事项ID
    allData = models.event.query.all()
    List = []
    for i in allData:
        if i.ID == targetID:
            dic = {'headline': i.headline, 'start_time': i.start_time, 'end_time': i.end_time,
                   'significance': i.significance,
                   'ID': i.ID, "complete": i.complete,
                   'note': i.note}
            List.append(dic)  # 只将目标数据传输给前端
            break
    return jsonify(List)


@app.route('/jump', methods=['GET', 'POST'])  # 按ID跳转
def jump():
    if request.method == 'POST':
        form = jumpForm(request.form)
        if form.validate():
            ID = form.user_ID.data
            u = event.query.filter_by(ID=ID).first()
            if u:
                return render_template('information-page.html', get_ID=ID)
            else:
                return render_template('homepage.html', flag=NotExist)
    else:
        return render_template('homepage.html', flag=-1)


@app.route('/modify', methods=['GET', 'POST'])  # 修改事项
def modify():
    if request.method == 'POST':
        newid = request.form.get('ID')
        newHeadline = request.form.get('headline')
        newStartYear = request.form.get('start_year')
        newStartMonth = request.form.get('start_month')
        newStartDay = request.form.get('start_day')
        newEndYear = request.form.get('end_year')
        newEndMonth = request.form.get('end_month')
        newEndDay = request.form.get('end_day')
        newNote = request.form.get('note')
        newSignificance = request.form.get('significance')
        newComplete = request.form.get('complete')
        if not valid_date(newStartYear, newStartMonth, newStartDay) or not valid_date(newEndYear, newEndMonth, newEndDay):
            return render_template('homepage.html', flag=InvalidDate)  # 如果时间不合法
        newStartDate = datetime.datetime(int(newStartYear), int(newStartMonth), int(newStartDay))
        newEndDate = datetime.datetime(int(newEndYear), int(newEndMonth), int(newEndDay))
        if newStartDate > newEndDate:  # 如果开始时间晚于结束时间
            return render_template('homepage.html', flag=Invalid_Start_And_End_Date)
        models.event.query.filter(models.event.ID == newid).update(
            {"headline": newHeadline, "start_time": newStartDate, "end_time": newEndDate,
             "significance": newSignificance,
             "note": newNote, "complete": newComplete})
        db.session.commit()
        return render_template('homepage.html', flag=ModifySucceed)


@app.route('/register', methods=['GET', 'POST'])  # 添加事项
def register():
    if request.method == 'POST':  # 添加行为
        newid = request.form.get('ID')
        newHeadline = request.form.get('headline')
        '''
        newStartYear = request.form.get('start_year')
        newStartMonth = request.form.get('start_month')
        newStartDay = request.form.get('start_day')
        newEndYear = request.form.get('end_year')
        newEndMonth = request.form.get('end_month')
        newEndDay = request.form.get('end_day')
        '''
        newStartDate=request.form.get('start_time')
        newEndDate=request.form.get('end_time')
        newNote = request.form.get('note')
        newSignificance = request.form.get('significance')
        newComplete = request.form.get('complete')
        '''
        if not valid_date(newStartYear, newStartMonth, newStartDay) or not valid_date(newEndYear, newEndMonth, newEndDay):
            return render_template('homepage.html', flag=InvalidDate)  # 如果时间不合法
        newStartDate = datetime.datetime(int(newStartYear), int(newStartMonth), int(newStartDay))
        newEndDate = datetime.datetime(int(newEndYear), int(newEndMonth), int(newEndDay))
        '''
        if newStartDate > newEndDate:  # 如果开始时间晚于结束时间
            return render_template('homepage.html', flag=Invalid_Start_And_End_Date)


        allData = models.event.query.all()
        IDOfNewEvent = 1
        IDOfNewEvent = AppendID(allData, IDOfNewEvent)
        new_event = models.event(headline=newHeadline, start_time=newStartDate, end_time=newEndDate,
                                 significance=int(newSignificance),
                                 note=newNote, ID=IDOfNewEvent, complete=int(newComplete))
        db.session.add(new_event)  # 添加到数据库中
        db.session.commit()
        return render_template('homepage.html', flag=AppendSucceed)


if __name__ == '__main__':
    app.run()
