from fundamentusfii import get_data_fii
import pandas as pd
import waitingbar
import os, time, stat, datetime


def data_to_csv_fii(VALUE):
    setor = VALUE
    print('data_to_csv_fiIs',setor)
    data = get_data_fii(1,setor=setor)
    #data = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in data.items()}
    df_data = pd.DataFrame.from_dict(data).transpose().reset_index() #transposing
    df_data = df_data.rename(columns={'index':'Ticker'}) #rename 'index' columns to 'ticker'
    df_data.to_csv(r'fundamentusfii.csv', sep=';', index=False, mode='w') #save csv

def analise_fii(NUMBER):
    df_fii = pd.read_csv('fundamentusfii.csv',sep=';')
    df_fii = df_fii[
        (df_fii['DY'] <= 1) & (df_fii['DY'] >= 0.06 ) & 
        (df_fii['FFOYield'] <= 1) & (df_fii['FFOYield'] >= 0.01 ) &
        (df_fii['P/VP'] <= 4) & (df_fii['P/VP'] >= 0.01 ) &
        (df_fii['LIQUIDEZ'] > 5000 )].sort_values(
            by=["DY","P/VP","FFOYield","LIQUIDEZ"],ascending=False)
    return df_fii.head(NUMBER)

def check_file_fii(VALUE):
    setor = VALUE
    print('check_file_fiis',setor)    
    filePath = 'fundamentusfii.csv'
    try:
        fileStatsObj = os.stat(filePath)
        if os.path.exists(filePath):
            today = datetime.datetime.today()
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filePath))
            duration = today - modified_date
            if duration.days > 2 or setor == 0 or 'setor' in locals():
                print('Your file is old and may have modifications ...')
                start_msg = waitingbar.WaitingBar('Starting download new data...')
                data_to_csv_fii(setor)
                start_msg.stop()
        modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
        c_time = os.path.getctime(filePath)
        dt_c = datetime.datetime.fromtimestamp(c_time)
        print('Created on:', dt_c)
        m_time = os.path.getmtime(filePath)
        dt_m = datetime.datetime.fromtimestamp(m_time)
        print('Modified on:', dt_m)
        return modificationTime
    except OSError:
        start_msg = waitingbar.WaitingBar('Starting download data...')
        data_to_csv_fii(setor)
        start_msg.stop()

if __name__ == '__main__':
    print('Check data at "funamentusfii.csv" file.')
    print("Last Modified Time : ", check_file_fii(5))
    print(analise_fii(10))
