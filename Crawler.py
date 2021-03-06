import requests
import shelve
import time


def get_static_champion_data(api_key):
    url = "https://na1.api.riotgames.com/lol/static-data/v3/champions"
    para = {"api_key": api_key}
    response = requests.get(url, params=para)
    if response.status_code == 200:
        data = response.json()

        # store the data on local path
        s = shelve.open('Static_Champion_Data', writeback=True)
        try:
            for key in data['data']:
                ID = data['data'][key]['id']
                s[str(ID)] = data['data'][key]
        finally:
            s.close()
    else:
        print 'error occurs, status_code:', response.status_code


def get_recent_match_list_by_account(api_key, account_id):
    url = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/"
    url += str(account_id)+"/recent"
    para = {"api_key": api_key}
    response = requests.get(url, params=para)
    if response.status_code == 200:
        return response.json()
    else:
        print 'error occurs, status_code:', response.status_code, ', re-try after 5 sec'
        time.sleep(5)
        return get_recent_match_list_by_account(api_key, account_id)


def get_match_list_by_account(api_key, account_id, queue=450, begin_index=0, season=11, end_index=0):
    url = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/"
    url += str(account_id)
    para = {"queue": queue, "api_key": api_key, "beginIndex": begin_index, "season": season}
    if end_index!=0:
        para["endIndex"]=end_index
    response = requests.get(url, params=para)
    if response.status_code == 200:
        return response.json()
    else:
        print 'error occurs, status_code:', response.status_code, ', re-try after 5 sec'
        time.sleep(5)
        return get_match_list_by_account(api_key, account_id, queue, begin_index, season)


def get_match_by_matchid(api_key, match_id):
    url = "https://na1.api.riotgames.com/lol/match/v3/matches/"
    url += str(match_id)
    para = {"api_key": api_key}
    response = requests.get(url, params=para)
    if response.status_code == 200:
        return response.json()
    else:
        print 'error occurs, status_code:', response.status_code, ', re-try after 5 sec'
        time.sleep(5)
        return get_match_by_matchid(api_key, match_id)


def get_summonerid_by_name(api_key, name):
    url = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"
    url += name
    para = {"api_key": api_key}
    response = requests.get(url, params=para)
    if response.status_code == 200:
        return response.json()['accountId']
    else:
        print 'error occurs, status_code:', response.status_code, ', re-try after 5 sec'
        time.sleep(5)
        return get_match_by_matchid(api_key, name)

