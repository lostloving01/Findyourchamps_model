import shelve
import operator
import Crawler
import DataProc
import PlayerRecord
import DataProc


api = "RGAPI-fed3e1c9-b57d-4636-b055-74913c3dfefd"
# account_id = 241797390
# match_id = 2741877692
name = 'WaterLittleGod'

#Crawler.get_static_champion_data("RGAPI-1c96089d-2579-46fc-a068-d9805f896f3b")

# s = shelve.open('Static_Champion_Data', writeback=False)
# for key in s:
#     print (s[key]['name'])
# s.close()

#j = Crawler.get_match_by_matchid(api, match_id)
#j = Crawler.get_summonerid_by_name (api, "WaterLittleGod")


# ob = PlayerRecord.PlayerRcd()
# ob = DataProc.get_recent_win_lost_info_by_account(api, name, 100)
# s = shelve.open('GameInfo')
# #Test = s[name]
# s[name] = ob
# #Test = s[name]
# s.close()
l = {}
r = {}
g = {}
ss = shelve.open('GameInfo')
try:
    for i in range(ss[name].count):
        if ss[name].champ_use[i] in l:
            l[ss[name].champ_use[i]] += 1
        else:
            l[ss[name].champ_use[i]] = 1
            r[ss[name].champ_use[i]] = 0
        if ss[name].res[i]:
            r[ss[name].champ_use[i]] += 1
finally:
    ss.close()
print float(sum(r.values()))/float(sum(l.values()))
for key in l.keys():
    g[key] = float(r[key])/float(l[key])
sorted_g = sorted(g.items(), key=operator.itemgetter(1), reverse=True)
sss = shelve.open('Static_Champion_Data')
for key in sorted_g:
     print sss[str(key[0])]['name'], ' ', key[1], '\n'
sss.close()

