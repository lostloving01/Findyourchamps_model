import Crawler
import time
import PlayerRecord
import shelve


def get_recent_win_fail_info_by_account(api, name, num=100):
    account_id = Crawler.get_summonerid_by_name(api, name)
    start = 0
    ob = PlayerRecord.PlayerRcd(name, account_id)
    j = Crawler.get_match_list_by_account(api, account_id, begin_index=start)
    while j['matches']:
        for l in j['matches']:
            time.sleep(0.85)
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


def get_recent_general_win_fail_info(api, seed_name, num=1000):
    seed_id = Crawler.get_summonerid_by_name(api, seed_name)
    ob = PlayerRecord.GeneralRcd()
    player_list = [seed_id]
    ob.add_a_player(seed_id)
    player_open = 0
    player_close = 0

    while player_open <= player_close:
        player_now = player_list[player_open]
        j = Crawler.get_match_list_by_account(api, player_now, end_index=20)
        if j['matches']:
            for l in j['matches']:
                game_id = l['gameId']
                if game_id in ob.game_id_set:
                    continue

                ob.add_a_game(game_id)
                time.sleep(0.85)
                k = Crawler.get_match_by_matchid(api, game_id)
                win_100 = k['teams'][0]['win']
                for s in k['participants']:
                    result = not ((win_100 == 'Win') ^ (s['teamId'] == 100))
                    ob.add_a_match(s['championId'], result)
                for s in k['participantIdentities']:
                    if not(s['player']['accountId'] in ob.player_set):
                        ob.add_a_player(s['player']['accountId'])
                        player_list.append(s['player']['accountId'])
                        player_close += 1

                if (ob.game_count % 10) == 0:
                    print '\n', ob.game_count, ' matches have been crawled.'

                if ob.game_count == num:
                    s = shelve.open('Gen_GameInfo', writeback=True)
                    s[seed_name+' '+str(num)] = ob
                    s.close()
                    print '\n', 'Recent general win/fail info has benn stored.'
                    print '\n', ob.game_count, ' matches record have been added.'
                    return
        player_open += 1

    s = shelve.open('Gen_GameInfo', writeback=True)
    s[seed_name + ' ' + str(num)] = ob
    s.close()
    print '\n', 'Recent general win/fail info has benn stored.'
    print '\n', ob.game_count, ' matches record have been added.'
    return








