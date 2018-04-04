import shelve

s = shelve.open('Static_Champion_Data', writeback=False)
for key in s:
    print (s[key]['title'])
s.close()
