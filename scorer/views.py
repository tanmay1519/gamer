import random
from django.http import HttpResponse
from django.shortcuts import render

opponents = []
khiladi={}
decision = False
bat = ''
def index (request):

     return render(request,'index.html')
#team=(request.GET.get('teamname','default'))
def gamer (request):
  team=[]

  team=(request.GET.get('teamname','default'))
  team = team.split("   ")
  opponents.clear()
  opponents.append(team[0])
  opponents.append(team[1])
  params = {'match':f'{team[0]} v {team[1]}'}
  return render (request,'output.html',params)

def player_entry(request) :
    #team = (request.GET.get('teamname', 'default'))
    #team = team.split("\n")
    team = []

    print (opponents)
    team=opponents

    H =(request.GET.get('head','off'))
    T =(request.GET.get('tail','off'))
    choice = ['Batting','Bowling']

    toss = ['heads','tails']
    global decision
    decision = False

    actual_choice =random.choice(toss)
    if (actual_choice == 'heads' and H == 'on') or (actual_choice == 'tails' and T == 'on') :
        toss_winner = team[0]
        decision = False
        pass_dict ={'winner':f'{toss_winner} has Won The Toss','choice':"SELECT BATTING OR BOWLING"}
        return render(request, 'history.html', pass_dict)

    else :
        toss_winner =team [1]
        field_choice = random.choice (choice)
        global bat1
        global bat2
        bat1 = ''
        bat2 = ''
        if field_choice == 'Batting'  :
            bat1=''
            bat2=''
            bat1 = team[1]
            bat2 = team[0]
        else :
            bat1 = team[0]
            bat2 = team[1]

        decision = True
        pass_dict = {'winner':f'{toss_winner} has Won The Toss','choice':f"{toss_winner} has Won The Toss And Selected  {field_choice}"}
        return render(request, 'history.html', pass_dict)
if decision == False :

    def TOSSED (request):
        if decision == False:
         return render (request,'batting.html')
        else :
            return render(request, 'tosslost.html')



def entry (request):
    global bat1
    global bat2
    global khiladi
    team = opponents
    khiladi = {}

    if decision == False :
        batter = (request.GET.get('batt','off'))
        print(batter)
        bat1 = ''
        bat2 = ''
        #bowler = (request.GET.get('bowl','off'))
        if batter == 'on':
            bat1= team[0]
            bat2=team[1]
        else :
            bat1 = team[1]
            bat2 = team[0]
    ballebaaz = bat1
    nextbat =bat2
    khiladi['bat1']=bat1
    khiladi['bat2']=bat2
    return render (request,'batsman.html',khiladi)
def data (request):
    battseq = (request.GET.get('battingorder','default'))
    A = (request.GET.get('agg','off'))
    B = (request.GET.get('defe','off'))
    C = (request.GET.get('mod','off'))
    if A == 'on':
        runs = [0, 0, 0, 0, 1, 1, 1, 1, 4, 2, 4, 0, 6, 1, 1, 1, 1, -1, 1, 1, 4, 0,-1,4,2,4,2,6,4,6,-1]
    elif B == 'on':
        runs = [0, 0, 0, 0, 1, 1, 1, 1,1,1,0,1,0,1,0,1, 2, 4, 0, 6, 1, 1, 1, 1, -1, 1, 1, 4, 0,1,0,1,1,1,1,4,1,0,1,1,1]
    else :
        runs = [0, 0, 0, 0, 1, 1, 1, 1, 4, 2, 4, 0, 6, 1, 1, 1, 1, -1, 1, 1, 4, 0,1,1,1,1,2]

    battseq=battseq.split(" ")
    bat=[]
    gang1={}
    bat = battseq
    player_data = []
    a = bat[0]
    b = bat[1]
    aa = 0
    bb = 0
    over = 0
    strike = a
    #runs = [0, 0, 0, 0, 1, 1, 1, 1, 4, 2, 4, 0, 6, 1, 1, 1, 1, -1, 1, 1, 4, 0]
    i = 2
    score = 0
    out = 0
    boo = True
    u = True


    while over < 20:
        ball = 0
        o = []
        while ball < 6:
            x = random.choice(runs)
            o.append(x)
            if (x == (-1)):
                if out == 9:
                    gang1[a] = aa
                    gang1[b] = bb
                    boo = False
                    break
                if (strike == a):
                    player_data.append(f" {a} is out at {aa} ")
                    gang1[a] = aa
                    aa = 0
                    a = bat[i]
                else:
                    player_data.append(f" {b} is out at {bb} ")
                    gang1[b] = bb
                    bb = 0
                    b = bat[i]
                strike = bat[i]

                i = i + 1
                out += 1

            else:
                score += x
                if x % 2 == 0:
                    if strike == a:
                        aa += x
                    else:
                        bb += x
                else:
                    if strike == a:
                        aa += x
                        strike = b
                    else:
                        bb += x
                        strike = a
            ball += 1

        over += 1
        string =(f' over : {over}{o}  {a}={aa} {b}={bb} {bat1}={score}/{out} ')

        player_data.append(string)
        if strike == a:
            strike = b
        else:
            strike = a
        if boo == False:
            break
        if over == 6:
            runs.append(2)
            runs.append(2)
            runs.append(2)
            runs.append(3)
            runs.append(1)
            runs.append(1)
            runs.append(1)
        if over == 15:
            runs.append(-1)
            runs.append(-1)
            runs.append(2)
            runs.append(4)
            runs.append(6)
            runs.append(6)
        if out == 7 and u == True:
            u = False
            runs.remove(6)
            runs.remove(4)
            runs.remove(4)
            runs.append(0)
            runs.append(1)
            runs.append(1)
            runs.append(1)
            runs.append(0)
    gang1[a] = aa
    gang1[b] = bb
    player_data.append(f" score of {bat1}={score}-->{out}")
    print (type(player_data))
    print (player_data)

    player_data='\r'.join(player_data)
    global khiladi
    khiladi['gang1']=gang1
    khiladi['jeet']=score
    covid = {'data_player_1':player_data,'batting_team':bat1,'next_batting':bat2}
    return render (request,'scorecard1.html',covid)
def MATCH (request):
    A = (request.GET.get('Agg', 'off'))
    B = (request.GET.get('Defe', 'off'))
    C = (request.GET.get('Mod', 'off'))
    if A == 'on':
        runs = [0, 0, 0, 0, 1, 1, 1, 1, 4, 2, 4, 0, 6, 1, 1, 1, 1, -1, 1, 1, 4, 0,-1,4,2,4,2,6,4,6,-1]
    elif B == 'on':
        runs = [0, 0, 0, 0, 1, 1, 1, 1,1,1,0,1,0,1,0,1, 2, 4, 0, 6, 1, 1, 1, 1, -1, 1, 1, 4, 0,1,0,1,1,1,1,4,1,0,1,1,1]
    else :
        runs = [0, 0, 0, 0, 1, 1, 1, 1, 4, 2, 4, 0, 6, 1, 1, 1, 1, -1, 1, 1, 4, 0,1,1,1,1,2]

    #global khiladi
    player_info = []
    gang2={}
    sang = (request.GET.get('naam','default'))
    bat =sang.split(" ")
    score = khiladi['jeet']
    a = bat[0]
    b = bat[1]
    aa = 0
    bb = 0
    over = 0
    strike = a
    #runs = [0, 0, 0, 0, 1, 1, 1, 1, 4, 2, 4, 0, 6, 1, 1, 1, 1, -1, 1, 1, 4, 0]
    i = 2
    score1 = 0
    out1 = 0
    v = True
    boo = True
    while over < 20:
        ball = 0
        o = []
        while ball < 6:
            x = random.choice(runs)
            o.append(x)
            if (x == (-1)):
                if out1 == 9:
                    gang2[a] = aa
                    gang2[b] = bb
                    boo = False
                    break
                if (strike == a):
                    player_info.append(f" {a} is out at {aa} ")

                    gang2[a] = aa
                    aa = 0
                    a = bat[i]
                else:
                    player_info.append(f" {b} is out at {bb} ")
                    gang2[b] = bb
                    bb = 0
                    b = bat[i]
                strike = bat[i]
                i = i + 1
                out1 += 1
            else:
                score1 += x
                if score1 > score:
                    gang2[a] = aa
                    gang2[b] = bb
                    boo = False
                    break
                if x % 2 == 0:
                    if strike == a:
                        aa += x
                    else:
                        bb += x
                else:
                    if strike == a:
                        aa += x
                        strike = b
                    else:
                        bb += x
                        strike = a
            ball += 1
        over += 1
        player_info.append(f" over : {over} {o}  {a}={aa} {b}={bb}  {bat2}={score1}/{out1}")

        if strike == a:
            strike = b
        else:
            strike = a
        if boo == False:
            break
        if over == 6:
            runs.append(2)
            runs.append(2)
            runs.append(3)
            runs.append(1)
            runs.append(1)
            runs.append(1)
            runs.append(1)
        if over == 15:
            runs.append(-1)
            runs.append(-1)
            runs.append(2)
            runs.append(4)
            runs.append(6)
            runs.append(6)
        if out1 == 7 and v == True:
            v = False
            runs.remove(6)
            runs.remove(4)
            runs.remove(4)
            runs.append(0)
            runs.append(1)
            runs.append(1)
            runs.append(1)
            runs.append(0)
    player_info.append(f" score of {bat2}={score1}-->{out1}")
    player_info = '\r'.join(player_info)
    khiladi['ballebazi']=player_info
    khiladi['scorer']= score1
    score1=khiladi['scorer']
    score = khiladi['jeet']
    pehle =khiladi['bat1']
    dusra=khiladi['bat2']
    if score >score1 :
        gang2[a] = aa
        gang2[b] = bb

    khiladi ['gang2']=gang2
    if score > score1 :
       khiladi ['jinkla'] = f'   {pehle} beats {dusra} '
    if score < score1 :
       khiladi ['jinkla'] =f"    {dusra} beats {pehle}"

    if score == score1 :
        khiladi ['jinkla'] = "Its A Tie "
    return render(request, 'scoreboard2.html', khiladi)












