import Crawler
import time
import PlayerRecord


def get_recent_win_lost_info_by_account(api, name, num):
    account_id = Crawler.get_summonerid_by_name(api, name)

    start = 0
    ob = PlayerRecord.PlayerRcd(name, account_id)
    j = Crawler.get_match_list_by_account(api, account_id, begin_index=start)
    while j['matches']:
        for l in j['matches']:
            time.sleep(1.25)
            game_id = l['gameId']
            k = Crawler.get_match_by_matchid(api, game_id)
            champ_use = l['champion']
            win_100 = k['teams'][0]['win']
            for s in k['participants']:
                if s['championId'] == champ_use:
                    result = not ((win_100 == 'Win') ^ (s['teamId'] == 100))
                    break
            ob.add_a_match(game_id, result, champ_use)
        start += 100
        if start >= num:
            break
        j = Crawler.get_match_list_by_account(api, account_id, start)
    return ob






