import re
import pandas as pd
from datetime import datetime

def preprocessor(data):
    pattern = r"\[[^\]]*\]\s"
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    
    for i in range(len(dates)):
        dates[i] = dates[i].strip("[]\xa0\u202f ").replace("\u202f", " ")

    df = pd.DataFrame({'user_messages': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M:%S %p', errors='coerce')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users_list = []
    messages_list = []
    for message in df['user_messages']:
        entry = message.split(':', 1)
        if len(entry) > 1:
            users_list.append(entry[0].strip())
            messages_list.append(entry[1].strip())
        else:
            users_list.append('Group Notification')
            messages_list.append(entry[0].strip())
            
    df['user'] = users_list
    df['message'] = messages_list
    df.drop(columns=['user_messages'], inplace=True)
    
    
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year.astype('Int64')
    df['month_num'] = df['date'].dt.month.astype('Int64')
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day.astype('Int64')
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour.astype('Int64') 
    df['minute'] = df['date'].dt.minute.astype('Int64')


    period_list = []
    for hour in df['hour']:
        if pd.isna(hour):
            period_list.append(None)
        elif hour == 23:
            period_list.append("23-00")
        elif hour == 0:
            period_list.append("00-01")
        else:
            period_list.append(f"{hour:02d}-{(hour + 1):02d}")
            
    df['period'] = period_list
    
    return df





