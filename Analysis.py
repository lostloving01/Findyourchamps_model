import shelve
import operator
import PlayerRecord


def analyze_champion_win_rate_by_name(name):
    ss = shelve.open('GameInfo')
    if name in ss:
        print '\n',name,'\'s statsitical information:'
        l = {}
        r = {}
        g = {}
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
        print '\n',"Win Rate: ", sum(r.values()), '/', sum(l.values()), '=', float(sum(r.values())) / float(sum(l.values()))
        for key in l.keys():
            g[key] = float(r[key]) / float(l[key])
        sorted_g = sorted(g.items(), key=operator.itemgetter(1), reverse=True)
        sss = shelve.open('Static_Champion_Data')
        for key in sorted_g:
            print '\n', sss[str(key[0])]['name'], ' ', key[1], ' ', r[key[0]], '/', l[key[0]]
        sss.close()
    else:
        ss.close()
        print '\n', 'Info of this summoner has not been crawled'
