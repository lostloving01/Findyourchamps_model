import Crawler
import time
import PlayerRecord
import shelve


def get_recent_win_lost_info_by_account(api, name, num=100):
    account_id = Crawler.get_summonerid_by_name(api, name)

    start = 0
    ob = PlayerRecord.PlayerRcd(name, account_id)
    j = Crawler.get_match_list_by_account(api, account_id, begin_index=start)
    while j['matches']:
        for l in j['matches']:
            time.sleep(0.95)
            game_id = l['gameId']
            k = Crawler.get_match_by_matchid(api, game_id)
            champ_use = l['champion']
            win_100 = k['teams'][0]['win']
            for s in k['participants']:
                if s['championId'] == champ_use:
                    result = not ((win_100 == 'Win') ^ (s['teamId'] == 100))
                    break
            ob.add_a_match(game_id, result, champ_use)
            if (ob.count % 10) == 0:
                print '\n', ob.count, ' matches have been crawled.'
        start += 100
        if start >= num:
            break
        j = Crawler.get_match_list_by_account(api, account_id, begin_index=start)
    s = shelve.open('GameInfo', writeback=True)
    s[name] = ob
    s.close()
    print '\n', 'Info of ', name, ' has benn stored.'
    print '\n', ob.count, ' matches record have been added.'





