from random import choice as rc
import pandas as pd
from itertools import combinations
def group_game(df,group,i,j,l,subs):
    print("             GROUP-",subs)
    data=list(group["NAME"])
    fix=list(combinations(data,2))
    rc1=[1,2,0,1,0,0,0]
    rc2=[1,0,1,0,1,0,0]
    rc3=[0,1,0,1,0,0,0]
    rc4=[0,0,1,0,0,0,0]
    arr=[i,j]
    for slot in arr:
        slice=[fix[slot]]
        for p,q in slice:
            print("************************")
            print("{0} - {1}".format(p,q))
            sp=0
            sq=0
            if group.loc[p,"RATE"]==4:
                for k in range(5):
                    sp+=rc(rc1)
            elif group.loc[p,"RATE"]==3:
                for k in range(5):
                    sp+=rc(rc2)
            elif group.loc[p,"RATE"]==2:
                for k in range(5):
                    sp+=rc(rc3)
            else:
                for k in range(5):
                    sp+=rc(rc4)
            if group.loc[q,"RATE"]==4:
                for k in range(5):
                    sq+=rc(rc1)
            elif group.loc[q,"RATE"]==3:
                for k in range(5):
                    sq+=rc(rc2)
            elif group.loc[q,"RATE"]==2:
                for k in range(5):
                    sq+=rc(rc3)
            else:
                for k in range(5):
                    sq+=rc(rc4)
            print("      {0}-{1}".format(sp,sq))
            print("*************************\n")
            df.loc[p,"GAMES"]+=1
            df.loc[q,"GAMES"]+=1
            if sp>sq:
                df.loc[p,"POINTS"]+=3
                df.loc[p,"WON"]+=1
                df.loc[q,"LOST"]+=1
                df.loc[p,"GD"]+=sp-sq
                df.loc[q,"GD"]-=sp-sq
            elif sp<sq:
                df.loc[q,"POINTS"]+=3
                df.loc[q,"WON"]+=1
                df.loc[p,"LOST"]+=1
                df.loc[q,"GD"]+=sq-sp
                df.loc[p,"GD"]-=sq-sp
            else:
                df.loc[p,"POINTS"]+=1
                df.loc[q,"POINTS"]+=1
                df.loc[q,"DRAW"]+=1
                df.loc[p,"DRAW"]+=1
    chart=df.loc[data[0]:data[3]].sort_values(["WON","POINTS","GD","RATE"],ascending=False)
    order=list(chart["NAME"])
    for t in range(4):
        l[t]=order[t]
    print("****************************************************")
    print(chart[["GAMES","WON","LOST","DRAW","GD","POINTS"]])
    print("****************************************************")
def roundof16_game(df,s,l):
    rc1=[1,2,0,0,1,0,1,0,0]
    rc2=[1,0,1,0,1,0,0,0,0]
    rc3=[0,0,1,0,0,1,0,0,0]
    rc4=[0,0,0,1,0,0,0,0,0]
    for p,q in s:
        print("{0} - {1}".format(p,q))
        sp=0
        sq=0
        if df.loc[p,"RATE"]==4:
            for k in range(5):
                sp+=rc(rc1)
        elif df.loc[p,"RATE"]==3:
            for k in range(5):
                sp+=rc(rc2)
        elif df.loc[p,"RATE"]==2:
            for k in range(5):
                sp+=rc(rc3)
        else:
            for k in range(5):
                sp+=rc(rc4)
        if df.loc[q,"RATE"]==4:
            for k in range(5):
                sq+=rc(rc1)
        elif df.loc[q,"RATE"]==3:
            for k in range(5):
                sq+=rc(rc2)
        elif df.loc[q,"RATE"]==2:
            for k in range(5):
                sq+=rc(rc3)
        else:
            for k in range(5):
                sq+=rc(rc4)
        print("      {0}-{1}".format(sp,sq))
        df.loc[p,"GAMES"]+=1
        df.loc[q,"GAMES"]+=1
        if sp>sq:
            df.loc[p,"POINTS"]+=3
            df.loc[p,"WON"]+=1
            df.loc[q,"LOST"]+=1
            df.loc[p,"GD"]+=sp-sq
            df.loc[q,"GD"]-=sp-sq
            l.append(p)
            print(p,"ADVANCED TO QUARTER-FINAL")
            df.loc[q,"LEVEL"]=2
        elif sp<sq:
            df.loc[q,"POINTS"]+=3
            df.loc[q,"WON"]+=1
            df.loc[p,"LOST"]+=1
            df.loc[q,"GD"]+=sq-sp
            df.loc[p,"GD"]-=sq-sp
            l.append(q)
            print(q,"ADVANCED TO QUARTER-FINAL")
            df.loc[p,"LEVEL"]=2
        else:
            while sp==sq:
                if df.loc[p,"RATE"]==4:
                    for k in range(3):
                        sp+=rc(rc1)
                elif df.loc[p,"RATE"]==3:
                    for k in range(3):
                        sp+=rc(rc2)
                elif df.loc[p,"RATE"]==2:
                    for k in range(3):
                        sp+=rc(rc3)
                else:
                    for k in range(3):
                        sp+=rc(rc4)
                if df.loc[q,"RATE"]==4:
                    for k in range(3):
                        sq+=rc(rc1)
                elif df.loc[q,"RATE"]==3:
                    for k in range(3):
                        sq+=rc(rc2)
                elif df.loc[q,"RATE"]==2:
                    for k in range(3):
                        sq+=rc(rc3)
                else:
                    for k in range(3):
                        sq+=rc(rc4)
            print("({0},{1})".format(sp,sq))
            if sp>sq:
                df.loc[p,"POINTS"]+=3
                df.loc[p,"WON"]+=1
                df.loc[q,"LOST"]+=1
                df.loc[p,"GD"]+=sp-sq
                df.loc[q,"GD"]-=sp-sq
                l.append(p)
                print(p,"ADVANCED TO QUARTER-FINAL")
                df.loc[q,"LEVEL"]=2
            else:
                df.loc[q,"POINTS"]+=3
                df.loc[q,"WON"]+=1
                df.loc[p,"LOST"]+=1
                df.loc[q,"GD"]+=sq-sp
                df.loc[p,"GD"]-=sq-sp
                l.append(q)
                print(q,"ADVANCED TO QUARTER-FINAL")
                df.loc[p,"LEVEL"]=2
        print("*************************")
        print("*************************\n")
def quarter_game(df,s,l):
    rc1=[1,2,0,0,1,0,1,0,0]
    rc2=[1,0,1,0,1,0,0,0,0]
    rc3=[0,0,1,0,0,1,0,0,0]
    rc4=[0,0,0,1,0,0,0,0,0]
    for p,q in s:
        print("{0} - {1}".format(p,q))
        sp=0
        sq=0
        if df.loc[p,"RATE"]==4:
            for k in range(5):
                sp+=rc(rc1)
        elif df.loc[p,"RATE"]==3:
            for k in range(5):
                sp+=rc(rc2)
        elif df.loc[p,"RATE"]==2:
            for k in range(5):
                sp+=rc(rc3)
        else:
            for k in range(5):
                sp+=rc(rc4)
        if df.loc[q,"RATE"]==4:
            for k in range(5):
                sq+=rc(rc1)
        elif df.loc[q,"RATE"]==3:
            for k in range(5):
                sq+=rc(rc2)
        elif df.loc[q,"RATE"]==2:
            for k in range(5):
                sq+=rc(rc3)
        else:
            for k in range(5):
                sq+=rc(rc4)
        print("      {0}-{1}".format(sp,sq))
        df.loc[p,"GAMES"]+=1
        df.loc[q,"GAMES"]+=1
        if sp>sq:
            df.loc[p,"POINTS"]+=3
            df.loc[p,"WON"]+=1
            df.loc[q,"LOST"]+=1
            df.loc[p,"GD"]+=sp-sq
            df.loc[q,"GD"]-=sp-sq
            l.append(p)
            print(p,"ADVANCED TO SEMI-FINAL")
            df.loc[q,"LEVEL"]=3
        elif sp<sq:
            df.loc[q,"POINTS"]+=3
            df.loc[q,"WON"]+=1
            df.loc[p,"LOST"]+=1
            df.loc[q,"GD"]+=sq-sp
            df.loc[p,"GD"]-=sq-sp
            l.append(q)
            print(q,"ADVANCED TO SEMI-FINAL")
            df.loc[p,"LEVEL"]=3
        else:
            while sp==sq:
                if df.loc[p,"RATE"]==4:
                    for k in range(3):
                        sp+=rc(rc1)
                elif df.loc[p,"RATE"]==3:
                    for k in range(3):
                        sp+=rc(rc2)
                elif df.loc[p,"RATE"]==2:
                    for k in range(3):
                        sp+=rc(rc3)
                else:
                    for k in range(3):
                        sp+=rc(rc4)
                if df.loc[q,"RATE"]==4:
                    for k in range(3):
                        sq+=rc(rc1)
                elif df.loc[q,"RATE"]==3:
                    for k in range(3):
                        sq+=rc(rc2)
                elif df.loc[q,"RATE"]==2:
                    for k in range(3):
                        sq+=rc(rc3)
                else:
                    for k in range(3):
                        sq+=rc(rc4)
            print("({0},{1})".format(sp,sq))
            if sp>sq:
                df.loc[p,"POINTS"]+=3
                df.loc[p,"WON"]+=1
                df.loc[q,"LOST"]+=1
                df.loc[p,"GD"]+=sp-sq
                df.loc[q,"GD"]-=sp-sq
                l.append(p)
                print(p,"ADVANCED TO SEMI-FINAL")
                df.loc[q,"LEVEL"]=3
            else:
                df.loc[q,"POINTS"]+=3
                df.loc[q,"WON"]+=1
                df.loc[p,"LOST"]+=1
                df.loc[q,"GD"]+=sq-sp
                df.loc[p,"GD"]-=sq-sp
                l.append(q)
                print(q,"ADVANCED TO SEMI-FINAL")
                df.loc[p,"LEVEL"]=3
        print("*************************")
        print("*************************")
        print("*************************\n")
def semis_game(df,s,l,m):
    rc1=[1,2,0,0,1,0,1,0,0]
    rc2=[1,0,1,0,1,0,0,0,0]
    rc3=[0,0,1,0,0,1,0,0,0]
    rc4=[0,0,0,1,0,0,0,0,0]
    for p,q in s:
        print("{0} - {1}".format(p,q))
        sp=0
        sq=0
        if df.loc[p,"RATE"]==4:
            for k in range(5):
                sp+=rc(rc1)
        elif df.loc[p,"RATE"]==3:
            for k in range(5):
                sp+=rc(rc2)
        elif df.loc[p,"RATE"]==2:
            for k in range(5):
                sp+=rc(rc3)
        else:
            for k in range(5):
                sp+=rc(rc4)
        if df.loc[q,"RATE"]==4:
            for k in range(5):
                sq+=rc(rc1)
        elif df.loc[q,"RATE"]==3:
            for k in range(5):
                sq+=rc(rc2)
        elif df.loc[q,"RATE"]==2:
            for k in range(5):
                sq+=rc(rc3)
        else:
            for k in range(5):
                sq+=rc(rc4)
        print("      {0}-{1}".format(sp,sq))
        df.loc[p,"GAMES"]+=1
        df.loc[q,"GAMES"]+=1
        if sp>sq:
            df.loc[p,"POINTS"]+=3
            df.loc[p,"WON"]+=1
            df.loc[q,"LOST"]+=1
            df.loc[p,"GD"]+=sp-sq
            df.loc[q,"GD"]-=sp-sq
            l.append(p)
            m.append(q)
            print(p,"ADVANCED TO FINAL")
        elif sp<sq:
            df.loc[q,"POINTS"]+=3
            df.loc[q,"WON"]+=1
            df.loc[p,"LOST"]+=1
            df.loc[q,"GD"]+=sq-sp
            df.loc[p,"GD"]-=sq-sp
            l.append(q)
            m.append(p)
            print(q,"ADVANCED TO FINAL")
        else:
            while sp==sq:
                if df.loc[p,"RATE"]==4:
                    for k in range(3):
                        sp+=rc(rc1)
                elif df.loc[p,"RATE"]==3:
                    for k in range(3):
                        sp+=rc(rc2)
                elif df.loc[p,"RATE"]==2:
                    for k in range(3):
                        sp+=rc(rc3)
                else:
                    for k in range(3):
                        sp+=rc(rc4)
                if df.loc[q,"RATE"]==4:
                    for k in range(3):
                        sq+=rc(rc1)
                elif df.loc[q,"RATE"]==3:
                    for k in range(3):
                        sq+=rc(rc2)
                elif df.loc[q,"RATE"]==2:
                    for k in range(3):
                        sq+=rc(rc3)
                else:
                    for k in range(3):
                        sq+=rc(rc4)
            print("({0},{1})".format(sp,sq))
            if sp>sq:
                df.loc[p,"POINTS"]+=3
                df.loc[p,"WON"]+=1
                df.loc[q,"LOST"]+=1
                df.loc[p,"GD"]+=sp-sq
                df.loc[q,"GD"]-=sp-sq
                l.append(p)
                m.append(q)
                print(p,"ADVANCED TO FINAL")
            else:
                df.loc[q,"POINTS"]+=3
                df.loc[q,"WON"]+=1
                df.loc[p,"LOST"]+=1
                df.loc[q,"GD"]+=sq-sp
                df.loc[p,"GD"]-=sq-sp
                l.append(q)
                m.append(p)
                print(q,"ADVANCED TO FINAL")
        print("*************************")
        print("*************************")
        print("*************************")
        print("*************************\n")
def thirdplace_playoff(df,s):
    rc1=[1,2,0,0,1,0,1,0,0]
    rc2=[1,0,1,0,1,0,0,0,0]
    rc3=[0,0,1,0,0,1,0,0,0]
    rc4=[0,0,0,1,0,0,0,0,0]
    for p,q in s:
        print("{0} - {1}".format(p,q))
        sp=0
        sq=0
        if df.loc[p,"RATE"]==4:
            for k in range(5):
                sp+=rc(rc1)
        elif df.loc[p,"RATE"]==3:
            for k in range(5):
                sp+=rc(rc2)
        elif df.loc[p,"RATE"]==2:
            for k in range(5):
                sp+=rc(rc3)
        else:
            for k in range(5):
                sp+=rc(rc4)
        if df.loc[q,"RATE"]==4:
            for k in range(5):
                sq+=rc(rc1)
        elif df.loc[q,"RATE"]==3:
            for k in range(5):
                sq+=rc(rc2)
        elif df.loc[q,"RATE"]==2:
            for k in range(5):
                sq+=rc(rc3)
        else:
            for k in range(5):
                sq+=rc(rc4)
        print("      {0}-{1}".format(sp,sq))
        df.loc[p,"GAMES"]+=1
        df.loc[q,"GAMES"]+=1
        if sp>sq:
            df.loc[p,"POINTS"]+=3
            df.loc[p,"WON"]+=1
            df.loc[q,"LOST"]+=1
            df.loc[p,"GD"]+=sp-sq
            df.loc[q,"GD"]-=sp-sq
            print(p,"ATTAINED THIRD POSITION")
            df.loc[q,"LEVEL"]=4
            df.loc[p,"LEVEL"]=5
        elif sp<sq:
            df.loc[q,"POINTS"]+=3
            df.loc[q,"WON"]+=1
            df.loc[p,"LOST"]+=1
            df.loc[q,"GD"]+=sq-sp
            df.loc[p,"GD"]-=sq-sp
            print(q,"ATTAINED THIRD POSITION")
            df.loc[p,"LEVEL"]=4
            df.loc[q,"LEVEL"]=5
        else:
            while sp==sq:
                if df.loc[p,"RATE"]==4:
                    for k in range(3):
                        sp+=rc(rc1)
                elif df.loc[p,"RATE"]==3:
                    for k in range(3):
                        sp+=rc(rc2)
                elif df.loc[p,"RATE"]==2:
                    for k in range(3):
                        sp+=rc(rc3)
                else:
                    for k in range(3):
                        sp+=rc(rc4)
                if df.loc[q,"RATE"]==4:
                    for k in range(3):
                        sq+=rc(rc1)
                elif df.loc[q,"RATE"]==3:
                    for k in range(3):
                        sq+=rc(rc2)
                elif df.loc[q,"RATE"]==2:
                    for k in range(3):
                        sq+=rc(rc3)
                else:
                    for k in range(3):
                        sq+=rc(rc4)
            print("({0},{1})".format(sp,sq))
            if sp>sq:
                df.loc[p,"POINTS"]+=3
                df.loc[p,"WON"]+=1
                df.loc[q,"LOST"]+=1
                df.loc[p,"GD"]+=sp-sq
                df.loc[q,"GD"]-=sp-sq
                print(p,"ATTAINED THIRD POSITION")
                df.loc[q,"LEVEL"]=4
                df.loc[p,"LEVEL"]=5
            else:
                df.loc[q,"POINTS"]+=3
                df.loc[q,"WON"]+=1
                df.loc[p,"LOST"]+=1
                df.loc[q,"GD"]+=sq-sp
                df.loc[p,"GD"]-=sq-sp
                print(q,"ATTAINED THIRD POSITION")
                df.loc[p,"LEVEL"]=4
                df.loc[q,"LEVEL"]=5
        print("*************************")
        print("*************************\n")
def final_game(df,s):
    rc1=[1,2,0,0,1,0,1,0,0]
    rc2=[1,0,1,0,1,0,0,0,0]
    rc3=[0,0,1,0,0,1,0,0,0]
    rc4=[0,0,0,1,0,0,0,0,0]
    for p,q in s:
        print("                                    {0} - {1}".format(p,q))
        sp=0
        sq=0
        if df.loc[p,"RATE"]==4:
            for k in range(5):
                sp+=rc(rc1)
        elif df.loc[p,"RATE"]==3:
            for k in range(5):
                sp+=rc(rc2)
        elif df.loc[p,"RATE"]==2:
            for k in range(5):
                sp+=rc(rc3)
        else:
            for k in range(5):
                sp+=rc(rc4)
        if df.loc[q,"RATE"]==4:
            for k in range(5):
                sq+=rc(rc1)
        elif df.loc[q,"RATE"]==3:
            for k in range(5):
                sq+=rc(rc2)
        elif df.loc[q,"RATE"]==2:
            for k in range(5):
                sq+=rc(rc3)
        else:
            for k in range(5):
                sq+=rc(rc4)
        print("                                           {0}-{1}".format(sp,sq))
        df.loc[p,"GAMES"]+=1
        df.loc[q,"GAMES"]+=1
        if sp>sq:
            df.loc[p,"POINTS"]+=3
            df.loc[p,"WON"]+=1
            df.loc[q,"LOST"]+=1
            df.loc[p,"GD"]+=sp-sq
            df.loc[q,"GD"]-=sp-sq
            df.loc[q,"LEVEL"]=6
            df.loc[p,"LEVEL"]=7
            print("============================================================================================================================================================================")
            print("============================================================================================================================================================================")
            print("*****                                    CHAMPIONS:::-----",p,"                                      *****")
            print("===========================================================================================================================================================================\n")
        elif sp<sq:
            df.loc[q,"POINTS"]+=3
            df.loc[q,"WON"]+=1
            df.loc[p,"LOST"]+=1
            df.loc[q,"GD"]+=sq-sp
            df.loc[p,"GD"]-=sq-sp
            df.loc[p,"LEVEL"]=6
            df.loc[q,"LEVEL"]=7
            print("============================================================================================================================================================================")
            print("============================================================================================================================================================================")
            print("*****                                    CHAMPIONS:::-----",q,"                                      *****")
            print("===========================================================================================================================================================================\n")
        else:
            while sp==sq:
                if df.loc[p,"RATE"]==4:
                    for k in range(3):
                        sp+=rc(rc1)
                elif df.loc[p,"RATE"]==3:
                    for k in range(3):
                        sp+=rc(rc2)
                elif df.loc[p,"RATE"]==2:
                    for k in range(3):
                        sp+=rc(rc3)
                else:
                    for k in range(3):
                        sp+=rc(rc4)
                if df.loc[q,"RATE"]==4:
                    for k in range(3):
                        sq+=rc(rc1)
                elif df.loc[q,"RATE"]==3:
                    for k in range(3):
                        sq+=rc(rc2)
                elif df.loc[q,"RATE"]==2:
                    for k in range(3):
                        sq+=rc(rc3)
                else:
                    for k in range(3):
                        sq+=rc(rc4)
            print("({0},{1})".format(sp,sq))
            if sp>sq:
                df.loc[p,"POINTS"]+=3
                df.loc[p,"WON"]+=1
                df.loc[q,"LOST"]+=1
                df.loc[p,"GD"]+=sp-sq
                df.loc[q,"GD"]-=sp-sq
                df.loc[q,"LEVEL"]=6
                df.loc[p,"LEVEL"]=7
                print("============================================================================================================================================================================")
                print("============================================================================================================================================================================")
                print("*****                                    CHAMPIONS:::-----",p,"                                      *****")
                print("============================================================================================================================================================================")
            else:
                df.loc[q,"POINTS"]+=3
                df.loc[q,"WON"]+=1
                df.loc[p,"LOST"]+=1
                df.loc[q,"GD"]+=sq-sp
                df.loc[p,"GD"]-=sq-sp
                df.loc[p,"LEVEL"]=6
                df.loc[q,"LEVEL"]=7
                print("============================================================================================================================================================================")
                print("============================================================================================================================================================================")
                print("*****                                    CHAMPIONS:::-----",q,"                                      *****")
                print("============================================================================================================================================================================")
