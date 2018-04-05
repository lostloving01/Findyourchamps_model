import shelve
import Crawler
import DataProc


api = "RGAPI-1c96089d-2579-46fc-a068-d9805f896f3b"
account_id = 241797390
match_id = 2741877692
name = 'WaterLittleGod'

#Crawler.get_static_champion_data("RGAPI-1c96089d-2579-46fc-a068-d9805f896f3b")

# s = shelve.open('Static_Champion_Data', writeback=False)
# for key in s:
#     print (s[key]['name'])
# s.close()

#j = Crawler.get_match_by_matchid(api, match_id)
#j = Crawler.get_summonerid_by_name (api, "WaterLittleGod")
print DataProc.get_recent_win_lost_info_by_account(api, name)
